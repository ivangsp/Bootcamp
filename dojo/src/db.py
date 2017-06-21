import sqlite3
# def dict_factory(cursor, row):
#     # d = []
    # for idx, col in enumerate(cursor.description):
    #     d.append(row[idx])
    # return d
    
conn = sqlite3.connect('database.db')
#conn.row_factory = dict_factory
cursor1 = conn.cursor()

class Database():
    def __init__(self):
       
        self.create_table_room()
        self.create_table_person()

    def create_table_room(self):
        cursor1.execute("CREATE TABLE IF NOT EXISTS rooms(room_id INTEGER PRIMARY KEY AUTOINCREMENT, room_name TEXT NOT NULL  , room_type TEXT NOT NULL) ")
        conn.commit()

    def create_table_person(self):
        cursor1.execute("CREATE TABLE IF NOT EXISTS person(person_id INTEGER PRIMARY KEY AUTOINCREMENT, person_name TEXT NOT NULL UNIQUE, person_type TEXT NOT NULL, office_name TEXT NOT NULL, livingroom_name TEXT ) ")
        conn.commit()
        # cursor.close()
        # conn.close()

    def add_room(self, room_name, room_type):
        try:
            cursor1.execute("INSERT INTO rooms (room_name, room_type) VALUES (?, ?)", (room_name, room_type))
            conn.commit()
        except  sqlite3.IntegrityError:
            #raise sqlite3.IntegrityError
            conn.rollback()
    

    def add_person(self, person_name, person_type, office_name, livingroom_name):
        try:

            cursor1.execute("INSERT INTO person (person_name, person_type, office_name, livingroom_name) VALUES(?,?,?,?) ", (person_name, person_type, office_name, livingroom_name))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.rollback()


    #get all office names or livingroom names names in the database
    def get_all_rooms_by_roomtype(self, room_type):
        try:
            output = []
            cursor1.execute("SELECT room_name FROM rooms WHERE room_type=?", (room_type,))
            data = cursor1.fetchall()
            if data is not None:
                for room in data:
                    output.append(room[0])
                return output

        except sqlite3.IntegrityError:
            conn.rollback()
            print('There was a problem with SQL')

    
    #get current number of occupants
    def get_people_in_room(self,room_name=''):

        try:
            output = []
            if len(room_name)>0:
                cursor1.execute("SELECT person_name, office_name, livingroom_name FROM person WHERE office_name=? OR livingroom_name=?", (room_name,room_name,))
            else:
                cursor1.execute("SELECT person_name, office_name, livingroom_name FROM person ")
            data = cursor1.fetchall() 
            for person in data:
                output.append(person[0])
            return output

        except sqlite3.IntegrityError:
            conn.rollback()
            print('Ooops eror in SQL')

    #get room type when room name is given
    def check_if_room_exists(self,room_name):
        try:
            cursor1.execute("SELECT room_type FROM rooms WHERE room_name=?",  (room_name,))
            data = cursor1.fetchone()
            if data is not None:
                return data[0]

        except Exception as e:
            raise e
            
    def allocated_office_rooms(self):
        try:
            cursor1.execute("SELECT person_name, office_name FROM person WHERE office_name !=? AND office_name is NOT NULL", ('yes',))
            data = cursor1.fetchall()
            output ={}
            for row in data:
                if output.has_key(row[1]): #works only in python2.7
                    output[row[1]].append(row[0])

                else:
                    output[row[1]] = [row[0]]
            return output
            

        except sqlite3.Error:
            print('There was a problem with SQL')


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
            

        except sqlite3.Error:
            print('There was a problem with SQL')

    #get names of people who did not get offices
    def get_people_who_missed_rooms(self):
        try:
            cursor1.execute("SELECT person_name from person WHERE office_name=? OR livingroom_name=?", ('yes','yes'))
            data = cursor1.fetchall()
            output = []
            for row in data:
                output.append(row[0])
            return output

        except sqlite3.Error:
            print('There was a problem with SQL')

    #reallocated person from one room ro another
    def update_person_details(self, person_name, room_name, room_type):
        #personname = '%'+person_name +'%'
        try:
            if room_type =='office':
                cursor1.execute("UPDATE person SET office_name=? WHERE person_name=? ",(room_name, person_name))
                conn.commit()
                #return(cursor1.fetchall())
            else:
                cursor1.execute("UPDATE person SET livingroom_name=? WHERE person_name=?",(room_name, person_name))
                conn.commit()

        except sqlite3.Error:
            print('There was a problem with SQL')

    #delete person
    def delete_person_from_db(self, person_name):
        try:
            cursor1.execute("DELETE  FROM person WHERE person_name=? ",(person_name,))
            conn.commit()
        except Exception as err:
            raise err

    #delete room
    #update the person table
    def delete_room_from_db(self,room_name, room_type):
        try:
            cursor1.execute("DELETE  FROM rooms WHERE room_name=? AND room_type=?",(room_name, room_type))
            data = conn.commit()
            if data is None:
                if room_type == 'office':
                    cursor1.execute("UPDATE person SET office_name=? WHERE office_name=? ",('yes',room_name))
                    conn.commit()
                else:
                    cursor1.execute("UPDATE person SET livingroom_name=? WHERE livingroom_name=? ",('yes', room_name))
                    conn.commit()

        except Exception as err:
            raise err
