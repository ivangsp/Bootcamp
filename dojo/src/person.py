from dojo.src.db import Database
from dojo.src.office import Office
import random


class Person(object):
    def ___init__(self, person_name):
        self.person_name = person_name

    def add_person_to_db(self, person_type, office_name='', livingroom=''):
        db = Database()
        db.add_person(self.person_name, person_type, office_name, livingroom)

    #assign office 
    def assign_officeroom(self, all_officerooms):
        all_officerooms_list = all_officerooms
        room_name = ""
        #if len(all_officerooms_list) == 0:
        if all_officerooms is None:
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




