from .Person import Person
class Gamer(Person):
    def __init__(self, id, name, coins=0, room=None):
        super().__init__(id, name, coins, room)