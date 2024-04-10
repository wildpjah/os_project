class Level:
    name = None
    rooms = []
    miners = []
    gamers = []

    def __init__(self, name, rooms, miners, gamers, rank):
        self.name = name
        self.rooms = rooms
        self.miners = miners
        self.gamers = gamers
        self.rank = rank

    def get_name(self):
        return self.name
    def get_rooms(self):
        return self.rooms
    def getminers(self):
        return self.miners
    def get_gamers(self):
        return self.gamers

    def set_name(self, name):
        self.name = name
    def add_room(self, room):
        self.rooms.append(room)
    def add_miner(self, miner):
        self.miners.append(miner)
    def add_gamer(self, gamer):
        self.gamers.append(gamer)
    
    def __str__(self):
        output = str(self.name) + ": \n\n"
        for room in self.rooms:
            output += str(room) + "\n\n"
        output += "End Of Level"
        return output