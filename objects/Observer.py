from objects.Game import Game
from objects.Person import Person
from objects.Gamer import Gamer
from objects.Miner import Miner
from objects.Room import Room
from objects.Level import Level
class Observer:
    def __init__(self, managed_proxy):
        self._managed_proxy = managed_proxy

    def handle_event(self, event):
        # Update managed proxy object mg with the modified Game object
        self._managed_proxy.data = self.Reconstruct(event.game_instance)

    
    def Reconstruct(self, g_dict):
        name = g_dict['name']
        levels = g_dict['levels']
        rooms = g_dict['rooms']
        gamers = g_dict['gamers']
        miners = g_dict['miners']
        occ_m = g_dict['occ_m']
        un_occ_m = g_dict['un_occ_m']
        occ_g = g_dict['occ_g']
        un_occ_g = g_dict['un_occ_g']
        
        new_levels=[]
        new_rooms=[]
        new_gamers=[]
        new_miners=[]
        new_occ_m=[]
        new_un_occ_m=[]
        new_occ_g=[]
        new_un_occ_g=[]
        g = Game(name)

        for level_dict in levels:
            new_level = Level(g, level_dict["id"], level_dict["name"], [], [], [])
            new_levels.append(new_level)

            for room_dict in rooms:
                if room_dict["level"] == new_level.get_id():
                    new_room = Room(g, room_dict["id"], room_dict["name"], new_level, None, None, room_dict["coins"])
                    new_rooms.append(new_room)
                    new_level.add_room(new_room)
                    new_un_occ_g.append(new_room)
                    new_un_occ_m.append(new_room)
            
        for miner_dict in miners:
            room_id = miner_dict["room"]
            new_room = None
            for room in new_rooms:
                if room.get_id() == room_id:
                    new_room = room
                    break
            new_miner = Miner(g, miner_dict["id"], miner_dict["name"], miner_dict["coins"], new_room)
            new_miners.append(new_miner)
            if new_room is not None:
                new_room.set_miner(new_miner)
                new_occ_m.append(new_room)
                new_un_occ_m.remove(new_room)

        for gamer_dict in gamers:
            room_id = gamer_dict["room"]
            level_id = gamer_dict["level"]
            new_room = None
            new_level = None
            for room in new_rooms:
                if room.get_id() == room_id:
                    new_room = room
                    break
            for level in new_levels:
                if level.get_id() == level_id:
                    new_level = level
                    break
            new_gamer = Gamer(g, gamer_dict["id"], gamer_dict["name"], gamer_dict["coins"], new_level, new_room)
            new_gamers.append(new_gamer)
            new_level.add_gamer(new_gamer)
            if new_room is not None:
                new_room.set_gamer(new_gamer)
                new_occ_g.append(new_room)
                new_un_occ_g.remove(new_room)

        g.set_levels(new_levels)
        g.set_rooms(new_rooms)
        g.set_gamers(new_gamers)
        g.set_miners(new_miners)
        g.set_occ_m(new_occ_m)
        g.set_un_occ_m(new_un_occ_m)
        g.set_occ_g(new_occ_g)
        g.set_un_occ_g(new_un_occ_g)
        return g