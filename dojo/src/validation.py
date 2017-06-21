from dojo.src.db import Database

class Validation():

    def __init__(self):
        self.db = Database()

    def check_room_type(self, room_type):
        #check if arg person_type is not empty
        if room_type is not None:
            if isinstance(room_type, str):
                room_type = room_type.lower()
                if room_type == "office" or room_type == "livingroom":
                    return room_type
                else:
                    raise ValueError('Invalid values, room type should either be an office or liviningspace, {} given'.format(room_type))
            else:
                raise TypeError('room_type can only be a string')
        else:
            raise TypeError('room_type can not be empty')

    #check if room name entered is a string and not empty
    def check_room_name(self, room_name):
        #check if room name  is not empty
        if room_name is not None:
            if isinstance(room_name, str):
                return room_name
            else:
                raise TypeError()
        else:
            raise TypeError()

    def check_personType(self, person_type):
        if person_type is not None:
            #check if its a string
            if isinstance(person_type, str):
                person_type = person_type.lower()
                #check if Person_type is either a fellow or staff
                if person_type == "fellow" or person_type == "staff":
                    return person_type
                else:
                    raise ValueError('invalid person type, should either be a fellow or staff, {} given'.format(person_type))
            else:
                raise TypeError()
        else:
            raise ValueError()

    def check_accomdoation(self, arg):
        if arg is not None:
            if isinstance(arg, str):
                arg = arg.lower()
                if arg == 'y':
                    return True
                elif arg == 'n':
                    return False
                else:
                    raise ValueError("Enter either Y/N for accomodation")
            else:
                raise TypeError('accomodation can either be y or n but not an int or float')
        return False

    #check if person name entered is a string and not empty
    def check_person_name(self, first_name, second_name=''):
        #check if room name  is not empty
        person_name = first_name+" "+second_name
        if person_name is not None:
            #check if its a string
            if isinstance(person_name, str):
                return person_name
            else:
                raise TypeError('Your name shud be  alphabetic')
        else:
            raise TypeError()

    #check if person name already exists
    def check_if_person_does_not_exist(self, person_name):
        if person_name in self.db.get_people_in_room():
            raise ValueError('Ooops, {} already exists'.format(person_name))
        else:
            return person_name


