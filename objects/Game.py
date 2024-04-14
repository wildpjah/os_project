class Game:
    # The game holds much of the overall game variables. All objects in the game extend the game.
    def __init__(self, name, levels=[], rooms=[], gamers=[], miners=[], occ=[], un_occ=[]):
        self.levels = levels
        self.rooms = rooms
        self.gamers = gamers
        self.miners = miners
        #list of occupied and unoccupied rooms
        self.occ = occ
        self.un_occ = un_occ
        self.name = name

    def get_occ(self, occ):
        return self.occ
    def get_un_occ(self):
        return self.un_occ
    def get_levels(self):
        return self.levels
    def get_rooms(self):
        return self.rooms
    def get_gamers(self):
        return self.gamers
    def get_miners(self):
        return self.miners
    def get_name(self):
        return self.name
    
    def set_name(self, n):
        self.name = n
    def set_occ(self, o):
        self.occ = o
    def set_un_occ(self, u):
        self.un_occ = u
    def set_levels(self, l):
        self.levels = l
    def set_rooms(self, r):
        self.rooms = r
    def set_gamers(self, g):
        self.gamers = g
    def set_miners(self, m):
        self.miners = m
    def add_occ(self, room):
        self.occ.append(room)
    def rm_occ(self, room):
        self.occ.remove(room)
    def add_un_occ(self, room):
        self.occ.append(room)
    def rm_un_occ(self, room):
        self.occ.remove(room)