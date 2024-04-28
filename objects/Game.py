from .GameChangeEvent import GameChangeEvent
class Game:
    # The game holds much of the overall game variables. All objects in the game extend the game.
    def __init__(self, name, levels=[], rooms=[], gamers=[], miners=[], occ_m=[], un_occ_m=[], occ_g=[], un_occ_g=[]):
        self.levels = levels
        self.rooms = rooms
        self.gamers = gamers
        self.miners = miners
        #list of occupied and unoccupied rooms
        self.occ_m = occ_m
        self.un_occ_m = un_occ_m
        self.occ_g = occ_g
        self.un_occ_g = un_occ_g
        self.name = name
        self.won = False
        self._observers = []

    def get_occ_m(self):
        return self.occ_m
    def get_un_occ_m(self):
        return self.un_occ_m
    def get_occ_g(self):
        return self.occ_g
    def get_un_occ_g(self):
        return self.un_occ_g
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
        
    def set_occ_g(self, o):
        self.occ_g = o
        
    def set_occ_m(self, o):
        self.occ_m = o
        
    def set_un_occ_m(self, u):
        self.un_occ_m = u
        
    def set_un_occ_g(self, u):
        self.un_occ_g = u
        
    def set_levels(self, l):
        self.levels = l
        
    def set_rooms(self, r):
        self.rooms = r
        
    def set_gamers(self, g):
        if g != None:
            self.gamers = g
        else:
            self.gamers = []
        
        
    def set_miners(self, m):
        self.miners = m
        


    def add_occ_m(self, room):
        self.occ_m.append(room)
        
    def rm_occ_m(self, room):
        self.occ_m.remove(room)
        
    def add_occ_g(self, room):
        self.occ_g.append(room)
        
    def rm_occ_g(self, room):
        self.occ_g.remove(room)
        

    def add_un_occ_m(self, room):
        self.un_occ_m.append(room)
        
    def rm_un_occ_m(self, room):
        self.un_occ_m.remove(room)
        
    def add_un_occ_g(self, room):
        self.un_occ_g.append(room)
        
    def rm_un_occ_g(self, room):
        self.un_occ_g.remove(room)
        


    def check_win(self):
        return self.won
    def win(self, gamer):
        self.won = True
        print("Gamer " + str(gamer.get_id()) + ", " + str(gamer.get_name()) + ", Has Won The Game!")


    # def level_from_gamer(self, gamer):
    #     for level in self.levels:
    #         print(level)
    #         print(level.get_gamers()[0])
    #         if level.get_gamers() != None and gamer in level.get_gamers():
    #             print(gamer)
    #             return level
    #     return None

    def level_from_room(self, room):
        for level in self.levels:
            if level.get_rooms() != None and room in level.get_rooms():
                return level
        return None


    def print_coins_per_room(self):
        for level in self.get_levels():
            print("level " +  str(level.get_id()))
            for room in level.get_rooms():
                print(str(room.get_coins()))


    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.handle_event(GameChangeEvent(self.deconstruct()))


    def deconstruct(self):
        name = self.name
        levels=[]
        rooms=[]
        gamers=[]
        miners=[]
        occ_m=[]
        un_occ_m=[]
        occ_g=[]
        un_occ_g=[]
        
        for level in self.levels:
            levels.append(level.deconstruct())
        for room in self.rooms:
            rooms.append(room.deconstruct())
        for gamer in self.gamers:
            gamers.append(gamer.deconstruct())
        for miner in self.miners:
            miners.append(miner.deconstruct())
        for room in self.occ_m:
            occ_m.append(room.get_id())
        for room in self.occ_g:
            occ_g.append(room.get_id())
        for room in self.un_occ_g:
            un_occ_g.append(room.get_id())
        for room in self.un_occ_m:
            un_occ_m.append(room.get_id())
        
        return {'name':name, "levels":levels, "rooms":rooms, "gamers":gamers, "miners":miners, "occ_m":occ_m, "un_occ_m":un_occ_m, "occ_g":occ_g, "un_occ_g":un_occ_g}
        
