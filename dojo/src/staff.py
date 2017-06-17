#from src import *
# from person import Person
# from office import Office
# from db import Database
# import random

from dojo.src.person import Person
from dojo.src.office import Office
from dojo.src.db import Database
import random



class Staff(Person):
    def __init__(self, person_name):
        super(Person, self).__init__()
        self.person_name = person_name
        self.db = Database()
        self.all_offices = self.db.get_all_rooms_by_roomtype('office')

    #adds staff to the database and assigns him a room
    def add_staff(self):
        output = {}
        output['person_name'] = self.person_name
        output['office_name'] = self.assign_officeroom(self.all_offices)
        output['livingroom'] = None
        self.add_person_to_db('staff', output['office_name'], None)
        return output

    def assign_officeroom(self, all_officerooms):
        all_officerooms_list = all_officerooms
        room_name = " "
        if len(all_officerooms_list) == 0:
            room_name = 'yes'
        else:
            officeroom = random.choice(all_officerooms_list)
            office = Office(officeroom)
            if office.has_space_office():
                room_name = officeroom
            else:
                all_officerooms_list = all_officerooms_list.remove(officeroom)
                room_name = self.assign_officeroom(all_officerooms_list)
        return room_name

    