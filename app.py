""" This example uses docopt with the built in cmd module to demonstrate an

interactive command application.

Usage:

     dojo.py create_room <room_type> <room_name> ...
     dojo.py add_person <first_name> <second_name>  <FELLOW-STAFF> [<wants_accommodation>]
     dojo.py print_room <room_name>
     dojo.py print_allocations [<filename>]
     dojo.py print_unallocated [<filename>]
     dojo.py reallocate_person <first_name> <second_name> <new_room_name>
     dojo.py load_people [<filename>]
     dojo.py (-h | --help)

Options:

    -i, --interactive  Interactive Mode

    -h, --help  Show this screen and exit.



"""

import sys
import cmd
from docopt import docopt, DocoptExit
from dojo.src.main import Dojo

mydojo = Dojo()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():

    print(__doc__)


class DojoCLI(cmd.Cmd):
    intro = "Welcome to my interactive program type help for a list of commands!"
    prompt = '(dojo) '

    file = None

    #creats rooms in the dojo with the specified room names
    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>... """

        try:
            room_type = args['<room_type>']
            room_names = args['<room_name>']
            #for room in list_room_names:
            if mydojo.create_room(room_type, room_names):
                for room in room_names:
                    print("An {} called {} has been successfully created!".format(room_type, room))
            else:
                print('Oops,an error occured, check the room')

        except Exception as err:
            print(err.__str__())


     #adds a person to a random room     
    @docopt_cmd
    def do_add_person(self, args):

        """Usage: add_person <first_name> <second_name> <FELLOW-STAFF> [<wants_accommodation>]
        """
        first_name = args['<first_name>']
        second_name = args['<second_name>'] 
        person_type = args['<FELLOW-STAFF>']
        person_name = first_name +" "+second_name
        wants_accommodation = args['<wants_accommodation>']
        try:

            output = mydojo.add_person(first_name, second_name, person_type, wants_accommodation)
        except Exception as err:
            print(err.__str__())
        else:
            office_name = output['office_name']
            living_room = output['livingroom']

            if office_name != 'yes':
                print("{}, {} has been successfully added.".format(person_type, person_name))
                print("{}, has been allocated office {} ".format(person_name, office_name))

            else:
                print("sorry currently all offices are full")

            if person_type == "fellow":
                if living_room != 'yes' and  living_room is not None:
                    print("{}, has been allocated livingroom {} ".format(person_name, living_room))
                elif living_room =='yes':
                    print("sorry currently all livingrooms are full")
    
            
    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>
        """
        room_name = args["<room_name>"]
        try:
            result = mydojo.print_people_in_room(room_name)
        except Exception as err:
            print(err.__str__())
        else:

            if len(result) == 0:
                print('The room is still empty')
            else:
                print ('The following people are in {}'.format(room_name))
                print ('****************************************************')
                for row in result:
                    print (row[0])

    #prints a list of people with the rooms allocated to them
    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage: print_allocations [<filename>]
        """
        filename = args['<filename>']
        try:
            mydojo.print_allocated_rooms(filename) 
        except Exception as err:
            print(err.__str__())   

   #prints a list of people with the rooms allocated to them
    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [<filename>]
        """
        filename = args['<filename>']
        try:
            mydojo.print_unallocated_people(filename)
        except Exception as err:
            print(err.__str__())
       
    #reallocate person from one room to another   
    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <first_name> <second_name> <new_room_name> 
        """
        first_name = args['<first_name>']
        second_name = args['<second_name>']
        new_room_name = args['<new_room_name>']
        try:
            result = mydojo.reallocate_person(first_name, second_name, new_room_name)
        except Exception as err:
            print(err.__str__())
        else:
            print(result)

    #load people from a file
    @docopt_cmd
    def do_load_people(self, args):
        """Usage: load_people [<filename>]
        """
        #to be implemented
        mydojo.load_people_from_file()

    def do_quit(self, arg):

        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

DojoCLI().cmdloop()


#print(opt)
