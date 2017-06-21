from dojo.src.room import Room 
from dojo.src.db import Database

#here the office class is inheriting from the Room class
class Office(Room):
    def __init__(self,room_name):
        super(Room,self).__init__()
        self.db = Database()
        self.room_name = room_name
        self.max_num_of_people = 6

    #check if the selected office still has space
    def has_space_office(self):
        #get current number of occupants in that room_name
        current_num__of_occupants = len(self.db.get_people_in_room(self.room_name))
        if current_num__of_occupants <self.max_num_of_people:
            return True
        return False
        

