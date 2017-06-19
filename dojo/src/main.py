from dojo.src.validation import Validation
from dojo.src.fellow import Fellow
from dojo.src.office import Office
from dojo.src.livingroom import LivingRoom
from dojo.src.staff import Staff
from dojo.src.db import Database

class Dojo():
    def __init__(self):
        self.db = Database()
        self.validate = Validation()

        self.all_offices = self.db.get_all_rooms_by_roomtype('office')
        self.all_living_rooms = self.db.get_all_rooms_by_roomtype('livingroom')
        self.all_rooms = self.all_living_rooms + self.all_offices  

    def create_room(self, room_type, room_name):
        #validating the arguments
        room_type = self.validate.check_room_type(room_type)
        output = False
        for room in room_name:
            room_name = self.validate.check_room_name(room)

            #if room_type is office then call the office instance
            if room_type == 'office':
                #check if room_name does not exists in list of all offices
                if room_name not in self.all_offices:
                    #add that office to the database
                    office = Office(room_name)
                    office.add_room_to_db(room_type) 
                    #check if length of list of all offices has increased by 1
                    new_list_offices = self.db.get_all_rooms_by_roomtype('office')
                    if len(new_list_offices) > len(self.all_offices):
                        #if office has been created then update the list of all offices
                        #also update the list containing all room names
                        self.all_offices = new_list_offices
                        self.all_rooms = self.all_living_rooms + self.all_offices  
                        output = True
                else:
                    raise ValueError('{} office already exists'.format(room_name))

            #if room_type is livingspace then call the livingspace instance
            else:
                #check if room name does not exist
                if room_name not in self.all_living_rooms:
                    #Add livingroom name  to the database
                    livingroom = LivingRoom(room_name)
                    livingroom.add_room_to_db(room_type)

                    #check if length of list containing livingspaces' names has increased by 1
                    new_list_livingspace = self.db.get_all_rooms_by_roomtype('livingroom')
                    if len(new_list_livingspace) > len(self.all_living_rooms):

                        #if room created sucessful then update list containing alll livingspaces
                        #Also update the list containing all rooms
                        self.all_living_rooms = new_list_livingspace
                        self.all_rooms = self.all_living_rooms + self.all_offices 
                        output = True

                else:
                    raise ValueError('{} livingspace already exists'.format(room_name))

        return output


    def add_person(self, first_name, second_name, person_type, accomodation=None):
        #validate the arguments
        person_name = self.validate.check_person_name(first_name, second_name)
        person_type = self.validate.check_personType(person_type)
        accomodation = self.validate.check_accomdoation(accomodation)

        #check if person does not exists
        person_name = self.validate.check_if_person_does_not_exist(person_name)

        #if person_type is fellow, then call the Fellow class
        if person_type == "fellow":
            person = Fellow(person_name)
            #return person.assign_livingroom(self.db.get_all_rooms_by_roomtype('livingroom'))
            output = person.add_fellow(self.all_offices, self.all_living_rooms, accomodation)
            return output

        else:
            person = Staff(person_name)
            return(person.add_staff())

    #prints names of people in aspecified room name
    def print_people_in_room(self, room_name):
        #validate room name
        room_name = self.validate.check_room_name(room_name)
        #check if room name entered exists
        room_name_exists = self.db.check_if_room_exists(room_name)
        if room_name_exists is None:
            raise ValueError('OOps.., {} {}does not exist'.format(room_name, room_name_exists))

        else:
            result = self.db.get_people_in_room(room_name)
            return result
            

    def print_allocated_rooms(self, filename=''):
        people_in_office = self.db.allocated_office_rooms()
        people_in_livingspace = self.db.allocated_livingspace_rooms()

        #combine the 2 dictinaries together
        result = {**people_in_office, **people_in_livingspace}
        #check if filname is not given, then just print d allocations on the screen
        if len(filename) == 0:     
            for k, v in result.iteritems():
                print(k)
                for j in v:
                    print(j)
        else:
            #check if filename ends with .txt
            #filename = filename+'.txt'
            if filename.lower().endswith('.txt'):
                saveFile = open(filename,'w')
                for k, v in result.iteritems():
                    saveFile.write(k+'\n')
                    saveFile.write('-------------------------------------\n')
                    for j in v:
                       saveFile.write(j+', ')
                    saveFile.write('\n')
            else:
                raise ValueError('Incorrect filename')

        
    #people who did not get either livingspaces or offices
    def print_unallocated_people(self,filename=''):
        result = self.db.get_people_who_missed_rooms()
        if len(filename) == 0:
            for name in result:
                print (name)
        else:
            #check if filename ends with .txt
            #filename = filename+'.txt'
            if filename.lower().endswith('.txt'):
                saveFile = open(filename,'w')
                saveFile.write('The following people were not allocated rooms \n')
                saveFile.write('-------------------------------------\n')
                for name in result:
                    saveFile.write(name+', \n')
            else:
                raise ValueError('Incorrect filename')

    #
    def reallocate_person(self,first_name,second_name, room_name):

        room_name = self.validate.check_room_name(room_name)
        person_name = self.validate.check_person_name(first_name, second_name)

        #check if person already exists
        all_people = self.db.get_people_in_room()
        if person_name in all_people:

            #check if room name exists
            room_type = self.db.check_if_room_exists(room_name)
            if room_type is not None:
                people_in_room = self.db.get_people_in_room(room_name)
                #check if the room is an office
                #check if its full
                if people_in_room is not None and len(people_in_room)==6 and room_type == "office":
                    return( "An Office {} is already full".format(room_name))

                #check if the room is a livingspace
                #check if its full
                elif people_in_room is not None and len(people_in_room) ==4 and room_type == "livingroom":
                    return("Livingspace {} is already full".format(room_name))
                #if the room is not full
                #then reallocate the person to that room
                return (self.db.update_person_details(person_name, room_name, room_type))
            else:
                raise ValueError('Ooops, {} does not exist'.format(room_name))

        else:
            raise ValueError('{}, does not exist'.format(person_name))

    #load_people from file
    def load_people_from_file(self):
        #check if file exists
        #to be implmented here
        readMe = open('example.txt','r').readlines()
        for person in readMe:
            result = person.split()
            wants_accommodation = None
            fname = result[0]
            sname = result[1]
            person_type =result[2]

            if len(result) >3:
                wants_accommodation =result[3]

            person_name = fname + " "+sname
            output = mydojo.add_person(person_name, person_type, wants_accommodation)
            office_name = output['office_name']
            living_room = output['livingroom']
            print("{}, {} has been successfully added.".format(person_type, person_name))
            print("{}, has been allocated office {} ".format(person_name, office_name.split()))

            if person_type == "fellow":
                if living_room is not None or living_room !='yes':
                    print("{}, has been allocated livingroom {} ".format(person_name, living_room))
                elif living_room =='yes':
                    print("There currently no livingspaces availeabe, {}, was not allocated livingspace ".format(person_name))



         

        

        
        