from .Game import Game
from .Person import Person
class Gamer(Person):
    def __init__(self, game, id, name, coins=0, room=None):
        super().__init__(id, game, name, coins, room)