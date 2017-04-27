from validation_class import Validation
from classes import Office, LivingRoom, Fellow, Staff


class Dojo():
    def __init__(self):
        self.all_rooms = []
        self.all_offices = []
        self.all_living_rooms = []
        self.validate = Validation()

    def create_room(self, room_type, room_name):
        output = False
        #validating the arguments
        room_name = self.validate.check_room_name(room_name)
        room_type = self.validate.check_room_type(room_type)

        #if room_type is office then call the office instance
        if room_type == 'office':
            #create room office
            office = Office(room_name)
            #add that office to the database
            office.add_room_to_db(room_type)
            
            self.all_offices.append(office)
            self.all_rooms.append(office)
            output = True
        else:
            #create room livingroom
            livingroom = LivingRoom(room_name)
            #Add livingroom to the database
            livingroom.add_room_to_db(room_type)

            self.all_living_rooms.append(livingroom)
            self.all_rooms.append(livingroom)
            output = True
        return output

    def add_person(self, person_name, person_type, accomodation=None):
        #validate the arguments
        person_name = self.validate.check_person_name(person_name)
        person_type = self.validate.check_personType(person_type)
        accomodation = self.validate.check_accomdoation(accomodation)

        if person_type == "fellow":
            person = Fellow(person_name)
            return(person.add_fellow(self.all_offices, self.all_living_rooms, accomodation))

        else:
            person = Staff(person_name)
            return (person.add_staff(self.all_offices))
            
            