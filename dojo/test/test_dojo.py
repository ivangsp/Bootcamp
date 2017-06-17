import unittest
from dojo.src.main import Dojo

class Test_Dojo(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    #test if room is created sucessfull
    def test_create_room_successfully(self):
        initial_room_count = len(self.dojo.all_rooms)
        blue_office = self.dojo.create_room('office', ['blue'])
        #check if it return true when room is successfully created
        self.assertTrue(blue_office)
        #check if length of all_rooms increased by 1
        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    #test if multiple rooms are created successfully
    def test_multiple_offices_created_successfully(self):
        initial_room_count = len(self.dojo.all_rooms)
        offices = self.dojo.create_room('office', ['00','K2','K3'])
        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count- initial_room_count, 3)

    #test if multiple livingspaces rooms are created successfully
    def test_multiple_livingspaces_are_created_successfully(self):
        initial_room_count = len(self.dojo.all_rooms)
        offices = self.dojo.create_room('livingroom', ['L40','L2','L3'])
        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count- initial_room_count, 3)


    #test if throws an error when invalid room type is entered
    def test_room_type_is_office_or_livingroom(self):
        self.assertRaises(ValueError, self.dojo.create_room, 'ofice', ['red'])
        self.assertRaises(ValueError, self.dojo.create_room, 'livingspace',['L1'])
        self.assertRaises(ValueError, self.dojo.create_room, '', ['red'])

    #test if room name does already exist ie integrity error
    def test_if_room_name_exists(self):
        self.dojo.create_room('office', ['Red2'])
        self.dojo.create_room('livingroom', ['White1'])
        self.assertRaises(ValueError, self.dojo.create_room, 'office', ['Red2'])
        self.assertRaises(ValueError, self.dojo.create_room, 'livingroom', ['white1'])

    #test if person type is eithe staff or fellow
    def test_person_type_is_either_staff_or_fellow(self):
        self.assertRaises(ValueError, self.dojo.add_person, 'Allan', 'W','fella', 'y')
        self.assertRaises(ValueError, self.dojo.add_person, 'Isaac', 'A', 'staf')

    #test if person name already exists
    def test_person_name_does_not_exist(self):
        self.dojo.add_person('Davies', 'ivan', 'fellow', 'y')
        self.dojo.add_person('Allan', 'W', 'staff')
        self.assertRaises(ValueError, self.dojo.add_person, 'Allan', 'W','staff')
        self.assertRaises(ValueError, self.dojo.add_person, 'gsp', 'ivan', 'fellow','y')

    #test if accomodation is either yes or No
    def test_if_accomodation_is_either_y_or_N(self):
        self.assertRaises(ValueError, self.dojo.add_person, 'john', 'W' , 'fellow','yap')

    #test if add_person is successfull
    def test_add_person_successfull(self):
        staff  = self.dojo.add_person('Aretha', 'A', 'staff')
        fellow = self.dojo.add_person('gsp', 'ivan', 'fellow', 'y')
        self.assertNotEqual(staff, {})
        self.assertNotEqual(fellow, {})

    #test_if_person_is_assigned an office
    def test_if_person_is_assigned_office(self):
        staff = self.dojo.add_person('Okello', 'Allan','staff')
        office_name =staff['office_name']
        offices_available = self.dojo.all_offices
        self.assertIn(office_name, offices_available)

    #test_if_person_is_assigned_a livingspace
    def test_if_person_is_assigned_livingspace(self):
        self.dojo.create_room('livingroom', 'DJANGO')
        fellow = self.dojo.add_person('geofrey', 'w', 'fellow','y')
        livingroom = fellow['livingroom']
        livingspace_available = self.dojo.all_living_rooms
        self.assertIn(livingroom, livingspace_available)

    #test_if_person_is_not_assigned_office_if_offices_not_available
    # def test_if_person_is_not_assigned_office_if_offices_not_available(self):
    #     staff = self.dojo.add_person('Mitchele', 'M','staff')
    #     office_name =staff['office_name']
    #     offices_available = self.dojo.all_offices
    #     self.assertNotIn(office_name, offices_available)

    #test_if_person_is_not_assigned_livingspace_if_livingroom_not_available
    # def test_if_person_is_not_assigned_livingroom_if_livingspace_not_available(self):
    #     staff = self.dojo.add_person('Marion', 'M','fellow','y')
    #     livingroom =staff['livingroom']
    #     livingroom_available = self.dojo.all_offices
    #     self.assertNotIn(livingroom, livingroom_available)

    #test_if_person_is_not_assigned_livingspace_if he dt request for it
    def test_if_person_is_not_assigned_livingroom_if_did_not_request_for_it(self):
        staff = self.dojo.add_person('Victor', 'S','fellow')
        livingroom =staff['livingroom']
        self.assertEqual(livingroom, None)

    #test if it throws ValueError if room name does not exists in print_room method
    def test_if_room_name_exists(self):
        self.assertRaises(ValueError, self.dojo.print_people_in_room, 'redvb')

    #test if room name is still empty in print room method
    def test_if_room_name_is_still_empty_in_print_room_method(self):
        self.dojo.create_room('office', ['Java'])
        output = self.dojo.print_people_in_room('Java')
        self.assertEqual(len(output), 0)

    #test_if_filename_ends_with_txt_in_print_allocations_methods
    def test_if_filename_ends_with_txt_in_print_allocations_method(self):
        self.assertRaises(ValueError, self.dojo.print_allocated_rooms, 'example.php')

    #test_if_filename_ends_with_txt_in_print_unallocated_methods
    def test_if_filename_ends_with_txt_in_print_unallocated_method(self):
        self.assertRaises(ValueError, self.dojo.print_unallocated_people, 'file1.vat')
