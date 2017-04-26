import random


class Person(object):
    def ___init__(self, person_name):
        self.person_name = person_name


class Fellow(Person):
    def __init__(self, person_name):
        super(Person, self).__init__()
        self.person_name = person_name

    def add_fellow(self, all_offices, all_livingrooms, accomodation):
        self.accomodation = accomodation
        output = {}
        output['person_name'] = self.person_name
        output['office_name'] = self.assign_officeroom(all_offices)
        if self.accomodation:
            output['livingroom'] = self.assign_livingroom(all_livingrooms)
        return output

    def assign_livingroom(self, all_livingrooms):
        all_livingrooms_list = all_livingrooms
        room_name = " "
        if len(all_livingrooms_list) == 0:
            room_name = None
        else:
            livingroom = random.choice(all_livingrooms_list)
            if livingroom.has_space_livingroom():
                room_name = livingroom.room_name
            else:
                all_livingrooms_list = all_livingrooms_list.remove(livingroom)
                room_name = self.assign_livingroom(all_livingrooms_list)
        return room_name

    def assign_officeroom(self, all_officerooms):
        all_officerooms_list = all_officerooms
        room_name = " "
        if len(all_officerooms_list) == 0:
            room_name = None
        else:
            officeroom = random.choice(all_officerooms_list)
            if officeroom.has_space_office():
                room_name = officeroom.room_name
            else:
                all_officerooms_list = all_officerooms_list.remove(officeroom)
                room_name = self.assign_officeroom(all_officerooms_list)
                    
        return room_name


class Staff(Person):
    def __init__(self, person_name):
        self.person_name = person_name

    def add_staff(self, all_offices):
        output = {}
        output['person_name'] = self.person_name
        output['office_name'] = self.assign_officeroom(all_offices)
        return output

    def assign_officeroom(self, all_officerooms):
        all_officerooms_list = all_officerooms
        room_name = " "
        if len(all_officerooms_list) == 0:
            room_name = None
        else:
            officeroom = random.choice(all_officerooms_list)
            if officeroom.has_space_office():
                room_name = officeroom.room_name
            else:
                all_officerooms_list = all_officerooms_list.remove(officeroom)
                room_name = self.assign_officeroom(all_officerooms_list) 
        return room_name
        

class Room(object):
    def __init__(self, room_name):
        self.room_name = room_name


class Office(Room):
    def __init__(self, room_name):
        super(Room, self).__init__()
        self.room_name = room_name
        self.max_num_of_people = 6
        self.current_num__of_occupants = 0

    def has_space_office(self):
        if self.current_num__of_occupants < self.max_num_of_people:
            return True
        else:
            return False


class LivingRoom(Room):
    def __init__(self, room_name):
        super(Room, self).__init__()
        self.room_name = room_name
        self.max_num_of_people = 4
        self.current_num__of_occupants = 0

    def has_space_livingroom(self):
        if self.current_num__of_occupants < self.max_num_of_people:
            return True
        else:
            return False
