from abc import ABC, abstractmethod
from .Game import Game
class Person(ABC):
    def __init__(self, game, id, name, coins=0, room=None):
        self.id = id
        self.name = name
        self.coins = coins
        self.room = room
        self.game = game

    @abstractmethod
    def find_room(self):
        pass
    @abstractmethod
    def enter_room(self, room):
        pass

    def __repr__(self):
        return type(self).__name__ + " " + str(self.id) + ", " + self.name + ": {coins:" + str(self.coins) + ", In Room: " + str(self.room) + "}"

    def __str__(self):
        return str(self.__class__) + " " + str(self.id) + ", " + self.name + ": {coins:" + str(self.coins) + ", In Room: " + str(self.room) + "}"


    def get_name(self):
        return self.name
    def get_coins(self):
        return self.coins
    def get_room(self):
        return self.room
    def get_game(self):
        return self.game

    def set_name(self, name):
        self.name = name
    def set_coins(self, coins):
        self.coins = coins
    def set_room(self, room):
        self.room = room
    def set_game(self, game):
        self.game = game
    
    def add_coins(self, coins):
        self.coins += coins