from validation import Validation
from livingroom import LivingRoom
from office import Office
from fellow import Fellow
from staff import Staff
from db import Database
from src import *

class Dojo():
    def __init__(self):
        self.db = Database()
        self.validate = Validation()

        self.all_offices = self.db.get_all_office_names()
        self.all_living_rooms = self.db.get_all_livingspace_names()
        self.all_rooms = self.all_living_rooms + self.all_offices  

    def create_room(self, room_type, room_name):
        #validating the arguments
        room_name = self.validate.check_room_name(room_name)
        room_type = self.validate.check_room_type(room_type)

        #if room_type is office then call the office instance
        if room_type == 'office':
        
            #add that office to the database
            office = Office(room_name)
            office.add_room_to_db(room_type)
            
            #check if length of list of all offices has increased by 1
            new_list_offices = self.db.get_all_office_names()
            if len(new_list_offices) > len(self.all_offices):
                return True

        #if room_type is livingspace then call the livingspace instance
        else:

            #Add livingroom name  to the database
            livingroom = LivingRoom(room_name)
            livingroom.add_room_to_db(room_type)

            #check if length of list containing livingspaces' names has increased by 1
            new_list_livingspace = self.db.get_all_livingspace_names()
            if len(new_list_livingspace) > len(self.all_living_rooms):
                return True

        return False


    def add_person(self, person_name, person_type, accomodation=None):
        #validate the arguments
        person_name = self.validate.check_person_name(person_name)
        person_type = self.validate.check_personType(person_type)
        accomodation = self.validate.check_accomdoation(accomodation)

        #if person_type is fellow, then call the Fellow class
        if person_type == "fellow":
            person = Fellow(person_name)
            output = person.add_fellow(self.all_offices, self.all_living_rooms, accomodation)
            return output

        else:
            person = Staff(person_name)
            return (person.add_staff(self.all_offices))

    #prints names of people in aspecified room name
    def print_people_in_room(self, room_name):
        #validate room name
        room_name = self.validate.check_room_name(room_name)
        #check if room name entered exists
        room_name_exists = self.db.check_if_room_exists(room_name)
        if room_name_exists is None:
            return None

        else:
            result = self.db.get_people_in_room_name(room_name)
            return result
            

    def print_allocated_rooms(self, filename=None):
        people_in_office = self.db.allocated_office_rooms()
        people_in_livingspace = self.db.allocated_livingspace_rooms()
        return (people_in_office, people_in_livingspace)
        
    #people who did not get either livingspaces or offices
    def print_unallocated_people(self,filename=None):
    	return self.db.get_people_who_missed_rooms()
        
        