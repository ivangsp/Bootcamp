class Validation():
    def check_room_type(self, room_type):
        #check if arg person_type is not empty
        if room_type is not None:
            if isinstance(room_type, str):
                room_type = room_type.lower()
                if room_type == "office" or room_type == "livingroom":
                    return room_type
                else:
                    raise ValueError('Invalid values, room type should either be an office or liviningspace')
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
                    raise ValueError('invalid person type, should either be a fellow or staff')
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
        return False

    #check if person name entered is a string and not empty
    def check_person_name(self, person_name):
        #check if room name  is not empty
        if person_name is not None:
            #check if its a string
            if isinstance(person_name, str):
                return person_name
            else:
                raise TypeError()
        else:
            raise TypeError()

