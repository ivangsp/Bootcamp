from validation_class import Validation
from classes import Office, LivingRoom


class Dojo():
    def __init__(self):
        self.all_rooms = []
        self.offices = []
        self.living_rooms = []
        self.validate = Validation()

    def create_room(self, room_type, room_name):
        output = False
        #validating the arguments
        room_name = self.validate.check_room_name(room_name)
        room_type = self.validate.check_room_type(room_type)
        if room_type == 'office':
            office = Office(room_name)
            self.all_rooms.append(office)
            self.offices.append(office)
            output = True
        else:
            livingroom = LivingRoom(room_name)
            self.all_rooms.append(livingroom)
            self.living_rooms.append(livingroom)
            output = True
        return output

    def add_person(self, person_name, person_type, wants_accomodation=None):
        person_name = self.validate.check_person_name(person_name)
        person_type = self.validate.check_person_type(person_type)

        if person_type == "Fellow":
            #check if office rooms are available,
            #Assign a random a room to fellow
            #check if a fellow wants_accomodation, if yes,then
            if wants_accomodation == 'yes':
                pass
                #check if livingRooms are available
                #Assign a random room aname to a fellow
                #check if there are still spaces in that room
                #if if there are still spaces, reduce the number o
                #return a dictionary containing the details of
