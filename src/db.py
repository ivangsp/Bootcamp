import sqlite3

def dict_factory(cursor, row):
    d = []
    for idx, col in enumerate(cursor.description):
        d.append(row[idx])
    return d

conn = sqlite3.connect('database5.db')
conn.row_factory = dict_factory
cursor1 = conn.cursor()

class Database():
    def __init__(self):
       
        self.create_table_room()
        self.create_table_person()

    def create_table_room(self):
        cursor1.execute("CREATE TABLE IF NOT EXISTS rooms(room_id INTEGER PRIMARY KEY AUTOINCREMENT, room_name TEXT NOT NULL UNIQUE , room_type TEXT NOT NULL) ")
        conn.commit()

    def create_table_person(self):
        cursor1.execute("CREATE TABLE IF NOT EXISTS person(person_id INTEGER PRIMARY KEY AUTOINCREMENT, person_name TEXT NOT NULL UNIQUE, person_type TEXT NOT NULL, office_name TEXT NOT NULL, livingroom_name TEXT ) ")
        conn.commit()
        # cursor.close()
        # conn.close()

    def add_room(self, room_name, room_type):
        cursor1.execute("INSERT INTO rooms (room_name, room_type) VALUES (?, ?)", (room_name, room_type))
        conn.commit()
        # cursor.close()
        # conn.close()

    def add_person(self, person_name, person_type, office_name, livingroom_name):
        try:

            cursor1.execute("INSERT INTO person (person_name, person_type, office_name, livingroom_name) VALUES(?,?,?,?) ", (person_name, person_type, office_name, livingroom_name))
            conn.commit()
        except sqlite3.IntegrityError,e:
            conn.rollback()


    #get all office names in the database
    def get_all_office_names(self):
        try:
            data = cursor1.execute("SELECT room_name FROM rooms WHERE room_type=?", ('office',)).fetchall()
            return data

        except sqlite3.Error, e:
            conn.rollback()
            print('There was a problem with SQL',e)

    #get all livingspace names in the data
    def get_all_livingspace_names(self):
        try:
            data = cursor1.execute("SELECT room_name FROM rooms WHERE room_type=?", ('livingroom',)).fetchall()
            return data

        except sqlite3.Error, e:
            conn.rollback()
            print('There was a problem with SQL',e)

    #get current number of occupants
    def get_people_in_room_name(self,room_name):

        try:
            data = cursor1.execute("SELECT person_name, office_name FROM person WHERE office_name=? OR livingroom_name=?", (room_name,room_name,)).fetchall()
            #cursor1.fetchall()
            return data

        except sqlite3.Error, e:
            conn.rollback()
            print('Ooops eror in SQL',e)

    #get room type when room name is given
    def check_if_room_exists(self,room_name):
        try:
            cursor1.execute("SELECT room_type FROM rooms WHERE room_name=?",  (room_name,))
            data = cursor1.fetchone()
            return data

        except sqlite3.Error, e:
            conn.rollback()
            print('There was a problem with SQL',e)

    def allocated_office_rooms(self):
        try:
            cursor1.execute("SELECT person_name, office_name FROM person WHERE office_name !=? AND office_name is NOT NULL", ('yes',))
            data = cursor1.fetchall()
            output ={}
            for row in data:
                if output.has_key(row[1]):
                    output[row[1]].append(row[0])

                else:
                    output[row[1]] = [row[0]]
            return output
            

        except sqlite3.Error, e:
            print('There was a problem with SQL',e)

    def allocated_livingspace_rooms(self):
        try:
            cursor1.execute("SELECT person_name, livingroom_name FROM person WHERE livingroom_name !=? AND livingroom_name is NOT NULL", ('yes',))
            data = cursor1.fetchall()
            output ={}
            for row in data:
                if output.has_key(row[1]):
                    output[row[1]].append(row[0])

                else:
                    output[row[1]] = [row[0]]
            return output
            

        except sqlite3.Error, e:
            print('There was a problem with SQL',e)

    #get names of people who did not get offices
    def get_people_who_missed_rooms(self):
        try:
            cursor1.execute("SELECT person_name from person WHERE office_name=? OR livingroom_name=?", ('yes','yes'))
            data = cursor1.fetchall()
            output = []
            for row in data:
                output.append(row[0])
            return output

        except sqlite3.Error, e:
            print('There was a problem with SQL',e)

    #get names of people who did not get livingspaces
    def get_people_who_missed_livingspaces(self):
        try:
            cursor1.execute("SELECT person_name from person WHERE livingroom_name=?",('yes',))
            return (cursor1.fetchall())

        except sqlite3.Error, e:
            print('There was a problem with SQL',e)

       

    # create_table_room()
    # add_room("james2", "office33")

    # create_table_person()

# db = Database()
# db.add_persons('ivan2', 'fellow', 'blue', 'Red')
# db.add_room("office", "gray")





