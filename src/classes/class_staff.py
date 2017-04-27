from class_person import Person
import random


class Staff(Person):
    def __init__(self, person_name):
        self.person_name = person_name

    def add_staff(self, all_offices):
        output = {}
        output['person_name'] = self.person_name
        output['office_name'] = self.assign_officeroom(all_offices)
        output['livingroom'] = None
        self.add_person_to_db('staff', output['office_name'], None)

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
        