from .Game import Game
class Level(Game):
    name = None
    rooms = []
    miners = []
    gamers = []

    def __init__(self, game, id, name="", rooms=[], miners=[], gamers=[]):
        self.id = id
        self.name = name
        self.rooms = rooms
        self.miners = miners
        self.gamers = gamers
        self.game = game

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_rooms(self):
        return self.rooms
    def getminers(self):
        return self.miners
    def get_gamers(self):
        return self.gamers
    def get_num_rooms(self):
        return len(rooms)
    def get_game(self):
        return self.game

    def set_id(self, id):
        self.id = id
    def set_name(self, name):
        self.name = name
    def add_room(self, room):
        self.rooms.append(room)
    def add_miner(self, miner):
        self.miners.append(miner)
    def add_gamer(self, gamer):
        self.gamers.append(gamer)
    
    def __str__(self):
        output = "\nGame " + self.game.getName() + ", Level " + str(self.id) + " " + str(self.name) + ": \n\n" + \
            "Miners on level: " + str(self.miners) + \
                "\nGamers on level: " + str(self.gamers) + "\n"
        for room in self.rooms:
            output += str(room) + "\n\n"
        output += "End Of Level"
        return output

    def __repr__(self):
        output = "\nGame " + self.game.get_name() + ", Level " + str(self.id) + " " + str(self.name) + ": \n\n" + \
            "Miners on level: " + str(self.miners) + \
                "\nGamers on level: " + str(self.gamers) + "\n"
        for room in self.rooms:
            output += str(room) + "\n\n"
        output += "End Of Level"
        return output