# from db import Database
from dojo.src.db import Database



class Room(object):
    def __init__(self, room_name):
        self.room_name = room_name

    #Adds a room names and room_type  to the the table room
    def add_room_to_db(self, room_type):
        db = Database()
        db.add_room(self.room_name, room_type)
        
        