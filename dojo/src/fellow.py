# from person import Person
# from office import Office
# from livingroom import LivingRoom
# import random
# from db import Database

from dojo.src.person import Person
from dojo.src.office import Office
from dojo.src.livingroom import LivingRoom
import random
from dojo.src.db import Database




class Fellow(Person):
    def __init__(self, person_name):
        super(Person, self).__init__()
        self.person_name = person_name
        self.db =Database()
        self.all_livingrooms = self.db.get_all_rooms_by_roomtype('livingroom')
        self.all_offices = self.db.get_all_rooms_by_roomtype('office')
       

    def add_fellow(self, all_offices, all_livingrooms, accomodation):
        self.accomodation = accomodation
        output = {}
        office_name = self.assign_officeroom(self.all_offices)

        #check if an office has been assigned
        if office_name:
            output['person_name'] = self.person_name
            output['office_name'] = office_name
            output['person_type'] = 'fellow'
            output['livingroom'] = None
        else:
            output['office_name'] = None

        #check if he wants accomodtion and assign a livingspace
        if self.accomodation:
            livingspaceroom = self.assign_livingroom(self.all_livingrooms)
            if livingspaceroom:
                output['livingroom'] = livingspaceroom       
        #check if output is not empty:
        if output:
            self.add_person_to_db('fellow', output['office_name'], output['livingroom'])
            
        return output

    def assign_livingroom(self, all_livingrooms):
        all_livingrooms_list = all_livingrooms
        room_name = " "
        if len(all_livingrooms_list) == 0 :
            room_name = 'yes'
            return room_name
        else:
            room = random.choice(all_livingrooms_list)
            livingroom = LivingRoom(room)

            #check if the room selected stil has spaces
            if livingroom.has_space_livingroom():
                room_name = room
            else:
                all_livingrooms_list = all_livingrooms_list.remove(room)
                room_name = self.assign_livingroom(all_livingrooms_list)
        return room_name

    #assign an office to either a staff or a fellow
    def assign_officeroom(self, all_officerooms):
        all_officerooms_list = all_officerooms
        room_name = " "

        #check if the list containing all offices' names is not empty
        if not all_officerooms_list:
            room_name = 'yes'
        else:
            office_room = random.choice(all_officerooms_list)
            office = Office(office_room)
            if office.has_space_office():
                room_name = office_room
            else:
                all_officerooms_list = all_officerooms_list.remove(office_room)
                room_name = self.assign_officeroom(all_officerooms_list)
                
        return room_name
    
