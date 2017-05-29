#from src import *
from person import Person
from office import Office
from db import Database
import random



class Staff(Person):
    def __init__(self, person_name):
        super(Person, self).__init__()
        self.person_name = person_name
        self.db = Database()

    #adds staff to the database and assigns him a room
    def add_staff(self, all_offices):
        output = {}
        output['person_name'] = self.person_name
        output['office_name'] = self.assign_officeroom(self.db.get_all_office_names())
        output['livingroom'] = None
        self.add_person_to_db('staff', output['office_name'], None)

        return output

    def assign_officeroom(self, all_officerooms):
        all_officerooms_list = all_officerooms
        room_name = " "
        if all_officerooms_list is None:
            room_name = 'yes'
        else:
            officeroom = random.choice(all_officerooms_list)
            office = Office(officeroom[0])
            if office.has_space_office():
                room_name = officeroom[0]
            else:
                all_officerooms_list = all_officerooms_list.remove(officeroom)
                room_name = self.assign_officeroom(all_officerooms_list)
        return room_name
    