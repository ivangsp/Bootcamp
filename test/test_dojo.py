import unittest
from dojo import Dojo

class TestCreateRoom(unittest.TestCase):
	def setUp(self):
		mydojo			  = Dojo()

    def test_create_room_successfully(self):
        my_class_instance = Dojo()
        initial_room_count = len(my_class_instance.all_rooms)
        blue_office = my_class_instance.create_room(“Blue”, “office”)
        self.assertTrue(blue_office)
        new_room_count = len(my_class_instance.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1

    #test if create_room method raises a integrtyError
    def test_if_create_room_method_raises_integrity_error(self):
        self.assertRaises(IntegrityError,)

    def test_add_person_sucessfully(self):
    	person1_added 	  = mydojo.add_person('gsp ivan','Fellow','yes')
    	person2_added 	  = mydojo.add_person('gsp ivan','Fellow')
    	person3_added 	  = mydojo.add_person('gsp ivan','staff')
    	self.assertDictEqual(person_added, {'name':'gsp ivan','person_type':'fellow','accomdn':'yes'})
    	self.assertDictEqual(person2_added, {'name':'gsp ivan','person_type':'fellow','accomdn':'No'})
    	self.assertDictEqual(person3_added, {'name':'gsp ivan','person_type':'Staff'})

    	
    #Test_if_person_Type Entered_is either staff or Fellow 
    def test_if_person_entered_is_either_staff_or_fellow(self):
    	person = mydojo.add_person('gsp ivan','Fellow','yes')

    #check_if_Room_Type_Entered_is_either_an_office_or_LivingRoom
    def test_if_Room_Type_Entered_is_either_an_office_or_LivingRoom(self):
    	#check_if_raises_typeError_when_a str_is not_passed_as_room_type
    	self.assertRaises(TypeError,mydojo.create_room("Red",5367)
    	#check_if_raises_valueError_when_room_type_is not office or LivingRoom
    	self.assertRaises(ValueError,mydojo.create_room("Red",'office2')
    	self.assertRaises(ValueError,mydojo.create_room("Red",'livinroom')

     #check if room name is a string and not empty
    def test_if_room_names_is_a_string(self):
        #check_if_raises_typeError_when_a str_is not_passed_as_person_type
        self.assertRaises(TypeError,mydojo.create_room(2667,'office')
        self.assertRaises(TypeError,mydojo.create_room(2667,'livingroom')

    #check if person_type entered is either a staff or a fellow
    def test_if_person_type_is_either_staff_or_fellow(self):
    	#check_if_raises_typeError_when_a str_is not_passed_as_person_type
    	self.assertRaises(TypeError,mydojo.add_person("gsp ivan",637383)
    	#check_if_raises_valueError_when_person_type_is not either a staff or felloww
    	self.assertRaises(ValueError,mydojo.add_person("gsp ivan",'fello')
    	self.assertRaises(ValueError,mydojo.add_person("gsp ivan",'stafff')

    #check if person name is a string and not empty
    def test_if_person_name_is_a_string(self):
    	#check_if_raises_typeError_when_a str_is not_passed_as_person_type
    	self.assertRaises(TypeError,mydojo.add_person(2667,'fellow')
    	self.assertRaises(TypeError,mydojo.add_person(2667,'fellow')

    def test_if_method_print_people_in_room_returns_an_error(self):
        #test if room name  entered in print_person command is a valid room name
        self.assertRaises(TypeError, mydojo.print_people_in_room(6728))
        self.assertRaises(ValueError,mydojo.print_people_in_room('blue2'))


    def test_if_method_print_allocations_returns_an_error(self):
        #test if database errors occured
        #check if filename specfied exists
        #check if filename is a afile
    def test_if_method_print_unallocated_people_returns_error(self):
        #test if file name specified is valid and exists
        #test if it returns a database error

       
