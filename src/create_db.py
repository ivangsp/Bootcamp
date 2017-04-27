import sqlite3
conn = sqlite3.connect('dojo.db')
cursor = conn.cursor()


class Database():
    def __init__(self):
        self.create_table_room()
        self.create_table_person()

    def create_table_room(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS rooms(room_id INTEGER PRIMARY KEY AUTOINCREMENT, room_name TEXT NOT NULL, room_type TEXT NOT NULL) ")
        conn.commit()

    def create_table_person(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS person(person_id INTEGER PRIMARY KEY AUTOINCREMENT, person_name TEXT NOT NULL, person_type TEXT NOT NULL, office_name TEXT, livingroom_name TEXT ) ")
        conn.commit()
        # cursor.close()
        # conn.close()

    def add_room(self, room_name, room_type):
        cursor.execute("INSERT INTO rooms (room_name, room_type) VALUES (?, ?)", (room_name, room_type))
        conn.commit()
        # cursor.close()
        # conn.close()

    def add_person(self, person_name, person_type, office_name, livingroom_name):
        cursor.execute("INSERT INTO person (person_name, person_type, office_name, livingroom_name) VALUES(?,?,?,?) ", (person_name, person_type, office_name, livingroom_name))
        conn.commit()
        # cursor.close()
        # conn.close()

    # create_table_room()
    # add_room("james2", "office33")

    # create_table_person()

# db = Database()
# db.add_persons('ivan2', 'fellow', 'blue', 'Red')
# db.add_room("office", "gray")




