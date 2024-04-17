import pygame
import random
import threading
import time
import math

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
ROOM_WIDTH = 80
ROOM_HEIGHT = 60
NUM_ROOMS_PER_LEVEL = 3
NUM_LEVELS = 10
GAMER_SEARCH_TIME = 10000  # in ms (10 seconds)
MINER_STAY_TIME = 10  # in ms (10 milliseconds)
MINER_START_TIME = 5000  # in ms (5 seconds)
MAX_GOLD_PER_MINER = 5
NUM_GAMERS = 10
NUM_MINERS = 20

# Function to draw a miner
def draw_miner(x, y, miner_id):
    font = pygame.font.Font(None, 20)
    text = font.render(str(miner_id), True, GREEN)
    pygame.draw.circle(screen, GREEN, (x + ROOM_WIDTH // 2, y + ROOM_HEIGHT // 2), 10)
    screen.blit(text, (x + ROOM_WIDTH // 2 - 5, y + ROOM_HEIGHT // 2 - 5))

# Function to draw a gamer
def draw_gamer(x, y, gamer_num):
    font = pygame.font.Font(None, 20)
    text = font.render(str(gamer_num), True, RED)
    pygame.draw.circle(screen, RED, (x + ROOM_WIDTH // 2, y + ROOM_HEIGHT // 2), 10)
    screen.blit(text, (x + ROOM_WIDTH // 2 - 5, y + ROOM_HEIGHT // 2 - 5))

# Function to draw a room
def draw_room(x, y, room_num):
    font = pygame.font.Font(None, 20)
    text = font.render(str(room_num), True, BLACK)
    pygame.draw.rect(screen, WHITE, (x, y, ROOM_WIDTH, ROOM_HEIGHT))
    pygame.draw.rect(screen, GREY, (x, y, ROOM_WIDTH, ROOM_HEIGHT), 2)
    screen.blit(text, (x + ROOM_WIDTH // 2 - 5, y + ROOM_HEIGHT // 2 - 5))

# Function to draw gold
def draw_gold(x, y, gold_amount):
    for _ in range(gold_amount):
        pygame.draw.polygon(screen, YELLOW, [(x + random.randint(10, ROOM_WIDTH - 10), y + random.randint(10, ROOM_HEIGHT - 10)),
                                             (x + random.randint(10, ROOM_WIDTH - 10), y + random.randint(10, ROOM_HEIGHT - 10)),
                                             (x + random.randint(10, ROOM_WIDTH - 10), y + random.randint(10, ROOM_HEIGHT - 10))])

# Class to represent a room
class Room:
    def __init__(self, x, y, room_number):
        self.x = x
        self.y = y
        self.room_number = room_number
        self.gamer = None
        self.miner = None
        self.gold = 0
        self.lock = threading.Lock()

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, ROOM_WIDTH, ROOM_HEIGHT)
        pygame.draw.rect(screen, WHITE, rect, 1)
        font = pygame.font.Font(None, 20)
        text = font.render(str(self.room_number), True, WHITE)
        screen.blit(text, (self.x + 5, self.y + 5))

# Class to represent a gamer
class Gamer(threading.Thread):
    def __init__(self, gamer_num, rooms):
        threading.Thread.__init__(self)
        self.gamer_num = gamer_num
        self.rooms = rooms

    def run(self):
        time.sleep(random.randint(0, 5000) / 1000)  # Random start time (up to 5 seconds)
        while True:
            room = random.choice(self.rooms)
            with room.lock:
                if room.gamer is None:
                    room.gamer = self.gamer_num
                    time.sleep(GAMER_SEARCH_TIME / 1000)  # Search time (10 seconds)
                    room.gold += random.randint(1, 5)  # Collect gold
                    if room.gold >= 20:
                        break
                    else:
                        room.gamer = None

# Class to represent a miner
class Miner(threading.Thread):
    def __init__(self, miner_letter, rooms):
        threading.Thread.__init__(self)
        self.miner_letter = miner_letter
        self.rooms = rooms

    def run(self):
        time.sleep(MINER_START_TIME / 1000)  # Start time (5 seconds)
        while True:
            room = random.choice(self.rooms)
            with room.lock:
                if room.miner is None:
                    room.miner = self.miner_letter
                    time.sleep(MINER_STAY_TIME)  # Stay time (10 milliseconds)
                    room.gold += random.randint(1, MAX_GOLD_PER_MINER)  # Drop gold
                    room.miner = None
            time.sleep(0.1)  # Move to next room

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Miner Game")

# Create rooms
rooms = []
room_number = 1
for level in range(NUM_LEVELS):
    for room_index in range(NUM_ROOMS_PER_LEVEL):
        x = room_index * (ROOM_WIDTH + 10) + 100
        y = level * (ROOM_HEIGHT + 10) + 50
        rooms.append(Room(x, y, room_number))
        room_number += 1

# Create gamers
gamers = []
for gamer_num in range(1, NUM_GAMERS + 1):
    gamer = Gamer(gamer_num, rooms)
    gamers.append(gamer)
    gamer.start()

# Create miners
miners = []
for miner_letter in range(1, NUM_MINERS + 1):
    miner = Miner(chr(64 + miner_letter), rooms)
    miners.append(miner)
    miner.start()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    for room in rooms:
        room.draw(screen)
        if room.gold > 0:
            draw_gold(room.x + ROOM_WIDTH // 4, room.y + ROOM_HEIGHT // 4, room.gold)
        if room.gamer is not None:
            draw_gamer(room.x, room.y, room.gamer)
        if room.miner is not None:
            draw_miner(room.x + ROOM_WIDTH // 2, room.y + ROOM_HEIGHT // 2, room.miner)
    
    pygame.display.flip()

pygame.quit()
