from .Game import Game
from .Person import Person
class Miner(Person):
    def __init__(self, game, id, name, coins=0, room=None):
        super().__init__(game, id, name, coins, room)

    def enter_room(self, room):
        self.room = room
    def find_room(self):
        options = self.game.get_un_occ