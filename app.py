""" This example uses docopt with the built in cmd module to demonstrate an

interactive command application.

Usage:

     dojo.py create_room <room_type> <room_name> ...
     dojo.py add_person <first_name> <second_name>  <FELLOW-STAFF> [<wants_accommodation>]
     dojo.py print_room <room_name>
     dojo.py print_allocations [<filename>]
     dojo.py print_unallocated [<filename>]
     dojo.py load_people [<filename>]
     dojo.py (-h | --help)

Options:

    -i, --interactive  Interactive Mode

    -h, --help  Show this screen and exit.



"""

import sys
import cmd
from docopt import docopt, DocoptExit
from src.main import Dojo

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

        room_type = args['<room_type>']
        list_room_names = args['<room_name>']
        for room in list_room_names:
            if mydojo.create_room(room_type, room):

                print("An {} called {} has been successfully created!".format(room_type, room))
            else:
                print 'Oops,an error occured'

     #adds a person to a random room     
    @docopt_cmd
    def do_add_person(self, args):

        """Usage: add_person <first_name> <second_name> <FELLOW-STAFF> [<wants_accommodation>]
        """
        person_name = args['<first_name>']+ " "+ args['<second_name>']
        person_type = args['<FELLOW-STAFF>']
        wants_accommodation = args['<wants_accommodation>']
        output = mydojo.add_person(person_name, person_type, wants_accommodation)
        office_name = output['office_name']
        living_room = output['livingroom']
        print("{}, {} has been successfully added.".format(person_type, person_name))
        print("{}, has been allocated office {} ".format(person_name, office_name))

        if person_type == "fellow":
            if living_room is not None:
                print("{}, has been allocated livingroom {} ".format(person_name, living_room))
     
    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>
        """
        room_name = args["<room_name>"]
        result = mydojo.print_people_in_room(room_name)

        #check if room name exists
        if result is None:
            print ('sorry, No room name with the name {}'.format(room_name))

        else:
            if len(result) == 0:
                print 'The room is still empty'
            else:
                print ('The following people are in {}'.format(room_name))
                print ('****************************************************')
                for row in result:
                    print row[0]

    #prints a list of people with the rooms allocated to them
    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage: print_allocations [<filename>]
        """
        filename = args['<filename>']
        result = mydojo.print_allocated_rooms(filename)
        if filename is None:     
            for i in result:
                for k, v in i.iteritems():
                    print k
                    for j in v:
                        print j
        else:
            filename = filename+'.txt'
            saveFile = open(filename,'w')
            for i in result:
                for k, v in i.iteritems():
                    saveFile.write(k+'\n')
                    saveFile.write('-------------------------------------\n')
                    for j in v:
                       saveFile.write(j+', ')

                    saveFile.write('\n')
            

   #prints a list of people with the rooms allocated to them
    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [<filename>]
        """
        filename = args['<filename>']
        result = mydojo.print_unallocated_people(filename)

        if filename is None:
            for name in result:
                print name
        else:
            saveFile = open(filename,'w')
            saveFile.write('The following people were not allocated rooms \n')
            saveFile.write('-------------------------------------\n')
            for name in result:
                saveFile.write(name+', \n')

    @docopt_cmd
    def do_load_people(self, args):
        """Usage: load_people [<filename>]
        """
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



         

    def do_quit(self, arg):

        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

DojoCLI().cmdloop()


#print(opt)
