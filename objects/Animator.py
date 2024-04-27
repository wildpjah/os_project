class Animator:
    #Animates our program.
    def __init__(self, game, w=800, h=1000):
        self.w = w
        self.h = h
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        BLACK = (0, 0, 0)
        YELLOW = (255, 255, 0)
        ROOM_WIDTH = 80
        ROOM_HEIGHT = 60

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Miner Game")
