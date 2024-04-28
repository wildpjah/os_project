from abc import ABC, abstractmethod
from .Game import Game
from .GameChangeEvent import GameChangeEvent
class Person(ABC):
    def __init__(self, game, id, name, coins=0, level=None, room=None):
        self.id = id
        self.name = name
        self.coins = coins
        self.room = room
        self.game = game
        self.level = level

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
    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name
        ()
    def set_coins(self, coins):
        self.coins = coins
        ()
    def set_room(self, room):
        self.room = room
        ()
    def set_game(self, game):
        self.game = game
        ()
    
    def add_coins(self, coins):
        self.coins = self.coins + coins
        ()
    
    def get_level(self):
        return self.level
    def set_level(self, level):
        self.level = level
        ()


    def deconstruct(self):
        if self.room is not None:
            room_id = self.room.get_id()
        else:
            room_id = None
        if self.level is not None:
            level_id = self.level.get_id()
        else:
            level_id = None
        dict = {'id':self.get_id(), 'name':self.get_name(), 'coins':self.get_coins(), 'level':level_id, "room":room_id}
        return dict