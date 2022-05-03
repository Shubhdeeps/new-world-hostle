from constants import male_dorms, female_dorms, single_rooms, double_rooms

class Accomodation:

    @staticmethod
    def available_list():
        global male_dorms, female_dorms, double_rooms,single_rooms
        return [len(male_dorms), len(female_dorms), len(single_rooms), len(double_rooms)]
    
    @staticmethod
    def booked_male_dorm():
        global male_dorms
        if(len(male_dorms) == 0):
                return 'Booking full'
            
        return male_dorms.pop(0)
    
    @staticmethod
    def booked_female_dorm():
        global female_dorms
        if(len(female_dorms) == 0):
                return 'Booking full'
            
        return female_dorms.pop(0)
    
    @staticmethod
    def booked_single_room():
        global single_rooms
        if(len(single_rooms) == 0):
                return 'Booking full'
            
        return single_rooms.pop(0)

    @staticmethod
    def booked_double_room():
        global double_rooms
        if(len(double_rooms) == 0):
                return 'Booking full'
            
        return double_rooms.pop(0)

    @staticmethod
    def checkout(room_number, room_type):
        global single_rooms, double_rooms, male_dorms, female_dorms
        if(room_type == "male dorm"):
            male_dorms.append(room_number)
            return
        if(room_type == "female dorm"):
            female_dorms.append(room_number)
            return
        if(room_type == "single room"):
            single_rooms.append(room_number)
            return
        if(room_type == "double room"):
            double_rooms.append(room_number)
            return