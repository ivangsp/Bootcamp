""" This example uses docopt with the built in cmd module to demonstrate an

interactive command application.

Usage:

     dojo.py create_room <room_type> <room_name> ...
     dojo.py add_person <person_name> <FELLOW-STAFF> [<wants_accommodation>]
     dojo.py print_room <room_name>
     dojo.py print_allocations [<filename>]
     dojo.py print_unallocated [<filename>]
     dojo.py (-h | --help)

Options:

    -i, --interactive  Interactive Mode

    -h, --help  Show this screen and exit.



"""

import sys
import cmd
from docopt import docopt, DocoptExit
from dojo import Dojo

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

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>... """

        room_type = args['<room_type>']
        list_room_names = args['<room_name>']
        for room in list_room_names:
            output = mydojo.create_room(room_type, room)
            print(output)
            # if output:
            #     print("An {} called {} has been successfully created!".format(room_type, room))
    @docopt_cmd
    def do_add_person(self, args):

        """Usage: add_person <person_name> <FELLOW-STAFF> [<wants_accommodation>]
        """
        person_name = args['<person_name>']
        person_type = args['<FELLOW-STAFF>']
        wants_accommodation = args['<wants_accommodation>']
        output = mydojo.add_person(person_name, person_type, wants_accommodation)
        print("{}, {} has been successfully added.".format(person_type, person_name))
        print(output)
        
    @docopt_cmd
    def do_print_person(self, args):
        """Usage: print_room <room_name>
        """
        room_name = args['<room_name>']
        mydojo.print_people_in_room(room_name)

    #prints a list of people with the rooms allocated to them
    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage: print_allocations [<filename>]
        """
        filename = args['<filename>']
        mydojo.print_allocations(filename)

   #prints a list of people with the rooms allocated to them
    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [<filename>]
        """
        filename = args['<filename>']
        mydojo.print_unallocated_people(filename)

    def do_quit(self, arg):

        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

DojoCLI().cmdloop()




#print(opt)
