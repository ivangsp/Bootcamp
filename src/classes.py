
class Person(object):
    def ___init__(self, person_name):
        self.person_name = self.person_name


class Fellow(Person):
    def __init__(self):
        pass


class Staff(Person):
    def __init__(self):
        pass
     

class Room(object):
    def __init__(self, room_name):
        self.room_name = room_name


class Office(Room):
    def __init__(self, room_name):
        super(Room, self).__init__()
        self.max_num_of_people = 6


class LivingRoom(Room):
    def __init__(self, room_name):
        super(Room, self).__init__()
        self.max_num_of_spaces = 4
