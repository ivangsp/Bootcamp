from src import *
from person import Person
from office import Office
from livingroom import LivingRoom
import random
from db import Database

#from src import Person
# from src import Office
# from src import LivingRoom
# import random
# from src import Database
# from src.person import Person




class Fellow(Person):
    def __init__(self, person_name):
        super(Person, self).__init__()
        self.person_name = person_name
        self.db =Database()
       

    def add_fellow(self, all_offices, all_livingrooms, accomodation):
        self.accomodation = accomodation
        output = {}
        output['person_name'] = self.person_name
        output['office_name'] = self.assign_officeroom(self.db.get_all_office_names())
        output['person_type'] = 'fellow'
        if self.accomodation:
            output['livingroom'] = self.assign_livingroom(self.db.get_all_livingspace_names())
            self.add_person_to_db('fellow', output['office_name'], output['livingroom'])
        else:
            output['livingroom'] = None
        return output

    def assign_livingroom(self, all_livingrooms):
        all_livingrooms_list = all_livingrooms
        room_name = " "
        if all_livingrooms_list is None:
            room_name = 'yes'
        else:
            room = random.choice(all_livingrooms_list)
            livingroom = LivingRoom(room[0])

            #check if the room selected stil has spaces
            if livingroom.has_space_livingroom():
                room_name = room[0]
            else:
                all_livingrooms_list = all_livingrooms_list.remove(room)
                room_name = self.assign_livingroom(all_livingrooms_list)
        return room_name

    #assign an office to either a staff or a fellow
    def assign_officeroom(self, all_officerooms):
        all_officerooms_list = all_officerooms
        room_name = " "

        #check if the list containing all offices' names is not empty
        if all_officerooms_list is None :
            room_name = 'yes'
        else:
            office_room = random.choice(all_officerooms_list)
            office = Office(office_room[0])
            if office.has_space_office():
                room_name = office_room[0]
            else:
                all_officerooms_list = all_officerooms_list.remove(office_room)
                room_name = self.assign_officeroom(all_officerooms_list)
        return room_name
    
