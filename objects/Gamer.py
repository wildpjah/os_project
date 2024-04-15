from .Game import Game
from .Person import Person
import random
class Gamer(Person):
    def __init__(self, game, id, name, coins=0, room=None):
        super().__init__(game, id, name, coins, room)

    def enter_room(self, room):
        old_room = self.room
        if self.room != None:
            self.room.set_gamer(None)
            self.game.rm_occ_g(self.room)
        self.room = room
        room.set_gamer(self)
        self.game.add_occ_g(room)
    def find_room(self):
        un_occ = self.game.get_un_occ_g()
        rooms = (self.game.gamer_by_level(self)).get_rooms()
        options = []
        for room in rooms:
            if room in un_occ:
                options.append(room)
        if options[0] == None:
            return None
        r = random.randint(0, len(options)-1)
        return options[r]
    def collect(self):
        r = self.room
        if self.room != None:
            self.add_coins(self.room.get_coins())
            r.set_coins(0)