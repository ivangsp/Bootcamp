from class_room import Room


class LivingRoom(Room):
    def __init__(self, room_name):
        super(Room, self).__init__()
        self.room_name = room_name
        self.max_num_of_people = 4
        self.current_num__of_occupants = 0

    def has_space_livingroom(self):
        if self.current_num__of_occupants < self.max_num_of_people:
            return True
        else:
            return False
            
