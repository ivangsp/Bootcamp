from db import Database


class Person(object):
    def ___init__(self, person_name):
        self.person_name = person_name

    def add_person_to_db(self, person_type, office_name=None, livingroom=None):
        db = Database()
        db.add_person(self.person_name, person_type, office_name, livingroom)

