# from validation import Validation
# from livingroom import LivingRoom
# from office import Office
# from fellow import Fellow
# from staff import Staff
# from db import Database

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
            result = self.db.get_people_in_room_name(room_name)
            return result
            

    def print_allocated_rooms(self, filename=None):
        people_in_office = self.db.allocated_office_rooms()
        people_in_livingspace = self.db.allocated_livingspace_rooms()

        #combine the 2 dictinaries together
        result = {**people_in_office, **people_in_livingspace}
        #check if filname is not given, then just print d allocations on the screen
        if filename is None:     
            for k, v in result.iteritems():
                print(k)
                for j in v:
                    print(j)
        else:
            #check if filename ends with .txt
            #filename = filename+'.txt'
            if filename.lower.endswith('.txt'):
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
    def print_unallocated_people(self,filename=None):
        result = self.db.get_people_who_missed_rooms()
        if filename is None:
            for name in result:
                print (name)
        else:
            #check if filename ends with .txt
            #filename = filename+'.txt'
            if filename.lower.endswith('.txt'):
                saveFile = open(filename,'w')
                saveFile.write('The following people were not allocated rooms \n')
                saveFile.write('-------------------------------------\n')
                for name in result:
                    saveFile.write(name+', \n')
            else:
                raise ValueError('Incorrect filename')

    #
    def reallocate_person(self,person_name, room_name):

        room_name = self.validate.check_room_name(room_name)
        person_name = self.validate.check_person_name(person_name)

        #check fist if room name exists
        room_details = self.db.check_if_room_exists(room_name)
        if room_details is not None:
            room_type = room_details[0]

            people_in_room = self.db.get_people_in_room_name(room_name)
            #check if the room is an office
            #check if its full

            if people_in_room is not None and len(people_in_room)==6 and room_type == "office":
                return( "An Office {} is already full".format(room_name))

            #check if the room is a livingspace
            #check if its full
            elif len(self.db.get_people_in_room_name(room_name))==4 and room_type == "livingroom":
                return("Livingspace {} is already full".format(room_name))
            #if the room is not full
            #then reallocate the person to that room
            return (self.db.update_person_details(person_name, room_name, room_type))
            return output
        else:
            return ('oops, {} does not exist,'.format(room_name))

        

        
        