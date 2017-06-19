from dojo.src.person import Person
from dojo.src.db import Database

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
