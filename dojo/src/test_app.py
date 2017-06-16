import unittest
from main import Dojo

class Test_Dojo(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_create_room_successfully(self):
        initial_room_count = len(self.dojo.all_rooms)
        blue_office = self.dojo.create_room('office', 'blue2')
        self.assertTrue(blue_office)
        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)


