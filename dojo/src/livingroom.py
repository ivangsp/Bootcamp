# from room import Room
# from db import Database

from dojo.src.room import Room
from dojo.src.db import Database


class LivingRoom(Room):
    def __init__(self, room_name):
        super(Room, self).__init__()
        self.room_name = room_name
        self.max_num_of_people = 4
        self.db = Database()

    def has_space_livingroom(self):
        #get current number of occupants in that room_name
        current_num__of_occupants = len(self.db.get_people_in_room_name(self.room_name))
        if current_num__of_occupants < self.max_num_of_people:
            return True
        return False
