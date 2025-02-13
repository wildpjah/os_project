from objects.Game import Game
from objects.Person import Person
from objects.Gamer import Gamer
from objects.Miner import Miner
from objects.Room import Room
from objects.Level import Level
import multiprocessing
from multiprocessing.managers import SyncManager
import pygame


class MyManager(SyncManager):
    def create_managed_list(self):
        return self.list()

def GetRandomName():
    # TODO
    # Right now this does not actually do the random name thing we discussed
    return "Level"

def NewGame(num_levels, num_rooms, num_gamers, num_miners):
    MyManager.register('Game', Game)
    MyManager.register('Person', Person)
    MyManager.register('Gamer', Gamer)
    MyManager.register('Miner', Miner)
    MyManager.register('Room', Room)
    MyManager.register('Level', Level)
    manager = MyManager()
    manager.start()

    mg = manager.Namespace()
    #ug is the unmanaged class that g is a reference to that will be manipulated by the original process ONLY.
    g = Game(mg, "Bruh")
    mg.data = g
    # initialize amounts
    num_levels = num_levels
    # number of rooms is per level
    num_rooms = num_rooms
    num_gamers = num_gamers
    num_miners = num_miners
    # levels holds all levels in order of progression. order of other lists does not matter.
    levels = []
    rooms = []
    gamers = []
    miners = []
    #list of occupied and unoccupied rooms
    occ_m = []
    occ_g = []
    un_occ_m = []
    un_occ_g = []

    # initialize Levels and Rooms
    level_id = 1
    for i in range(1, num_levels + 1):
        # create a new level and append it to the array
        new_level = Level(g, i, GetRandomName(), [], [], [])
        levels.append(new_level)
        # initialize Rooms and put them in our level too
        for i in range(1, num_rooms + 1):
            new_room = Room(g, level_id, "Room", new_level, None, None, 0)
            new_level.add_room(new_room)
            rooms.append(new_room)
            un_occ_m.append(new_room)
            un_occ_g.append(new_room)
            level_id = level_id + 1
    # initialize Gamers in level 1
    for i in range(1, num_gamers + 1):
        new_gamer = Gamer(g, i, "Gamer")
        gamers.append(new_gamer)
        levels[0].add_gamer(new_gamer)
        new_gamer.set_level(levels[0])
    
    # initialize Miners
    for i in range(1, num_miners + 1):
        miners.append(Miner(g, i, "Miner"))


    g.set_levels(levels)
    g.set_rooms(rooms)
    g.set_gamers(gamers)
    g.set_miners(miners)
    g.set_occ_m(occ_m)
    g.set_un_occ_m(un_occ_m)
    g.set_occ_g(occ_g)
    g.set_un_occ_g(un_occ_g)
    mg.data = g
    return (mg, g)


def AnimateGame(game):
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 1200
    pygame.init()
    running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Miner Game")
    count = 0
    while running:
        if game is None:
            pygame.quit()
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_game(game, screen)
        pygame.display.flip()
        count += 1
    pygame.quit()
    print("count " + str(count))


def draw_game(game, screen):
    # assume we're always working within the above loop. This being a separate function just keeps that loop clean
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    ROOM_WIDTH = 120
    ROOM_HEIGHT = 60
    LEVEL_HEIGHT = 100
    LEVEL_WIDTH = 700
    SPACING = 10
    game = game.data
    
    # Top of the window will be Where the miners wait?
    screen.fill(BLACK)
    rect = pygame.Rect(5,5,LEVEL_WIDTH, LEVEL_HEIGHT)
    font = pygame.font.Font(None, 20)
    text = font.render("Miner Waiting Room", True, WHITE)
    screen.blit(text, (10, 10))
    pygame.draw.rect(screen, WHITE, rect, 1)

    line_x = (ROOM_WIDTH + 20) * (len(game.get_rooms()) / len(game.get_levels()))
    line_y2 = 5 + len(game.get_levels()) * (LEVEL_HEIGHT+10)
    pygame.draw.line(screen, WHITE, (line_x, 5), (line_x, line_y2))



    i = 1
    for level in game.get_levels():
        #Draw Level
        rect = pygame.Rect(5,5+(i*LEVEL_HEIGHT),LEVEL_WIDTH, LEVEL_HEIGHT)
        label = "Level " + str(i)
        text = font.render(label, True, WHITE)
        screen.blit(text, (10, 10+(i*LEVEL_HEIGHT)))
        pygame.draw.rect(screen, WHITE, rect, 1)
        j = 0
        for room in level.get_rooms():
            # Draw Room
            x = 15 + (j * (ROOM_WIDTH + 10))
            y = 25 + i*(LEVEL_HEIGHT)
            rect = pygame.Rect(x,y,ROOM_WIDTH, ROOM_HEIGHT)
            font = pygame.font.Font(None, 20)
            text = font.render(str(room.get_id()), True, WHITE)
            screen.blit(text, (x + 5, y + 5))
            pygame.draw.rect(screen, WHITE, rect, 1)

            # Draw coins in room
            num_c = room.get_coins()
            circle_center = (x + 100, y + 40)
            text = str(num_c)
            text_surface = font.render(text, True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = circle_center
            #Actually drawing
            if num_c > 0:
                pygame.draw.circle(screen, YELLOW, circle_center, 10)
            screen.blit(text_surface, text_rect)
            
            # advance variables
            j = j + 1
        
        waiting = []
        j=0
        for gamer in level.get_gamers():
            #Draw gamers
            if gamer.get_room() is not None:
                #Draw in a room
                room = gamer.get_room()
                x = ((3-(room.get_id()%3)) * (ROOM_WIDTH + 10)) - 80
                y = 60 + i*(LEVEL_HEIGHT)
                circle_center = (x, y)
                text = str(gamer.get_id())
                text_surface = font.render(text, True, BLACK)
                text_rect = text_surface.get_rect()
                text_rect.center = circle_center
                #Actually drawing
                pygame.draw.circle(screen, RED, circle_center, 10)
                screen.blit(text_surface, text_rect)
            else:
                #Put in waiting area
                waiting.append(gamer)
            j=j+1
        j=0
        for gamer in waiting:
            #Draw all waiting gamers
            x_min = line_x + 20
            x_max = 695
            level = gamer.get_level()
            y_min = (level.get_id() * LEVEL_HEIGHT) + 10
            circle_center = (x_min + (25*j), y_min + 15)
            text = str(gamer.get_id())
            text_surface = font.render(text, True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = circle_center
            #Actually drawing
            pygame.draw.circle(screen, RED, circle_center, 10)
            screen.blit(text_surface, text_rect)
            j = j + 1
        i = i + 1
    waiting = []
    for miner in game.get_miners():
        if miner.get_room() is not None:
            # Draw miner in room
            room = miner.get_room()
            x = ((3-(room.get_id()%3)) * (ROOM_WIDTH + 10)) - 40
            level = room.get_level().get_id()
            y = 60 + ((level)*LEVEL_HEIGHT)
            circle_center = (x, y)
            text = str(miner.get_id())
            text_surface = font.render(text, True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = circle_center
            #Actually drawing
            pygame.draw.circle(screen, GREEN, circle_center, 10)
            screen.blit(text_surface, text_rect)
        else:
            waiting.append(miner)
        #Draw miner - note: some miners may not be in a room. There needs to be a space they can wait that's not a level.
        j=0
        for miner in waiting:
            x_min = 25
            y_min = 25
            if j < 10:
                circle_center = (x_min + 25*j, y_min + 15)
            else:
                c = j-10
                circle_center = (x_min + 25*c, y_min + 50)
            text = str(miner.get_id())
            text_surface = font.render(text, True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = circle_center
            #Actually drawing
            pygame.draw.circle(screen, GREEN, circle_center, 10)
            screen.blit(text_surface, text_rect)
            j = j + 1
