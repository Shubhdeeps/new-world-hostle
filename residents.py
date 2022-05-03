import random
from datetime import *
from accomodation import *



class Resident:
    def __init__(self):
        pass      

    def set_details(self, name, country, passport, gender, d_from, d_to, room_type):
         if(name == "" or country == 'Select a country' or country == "" or passport == "" or d_from == "" or d_to == "" or room_type == "" or room_type == 'Select accomodation type'):
             return "All fields required"
         
         if(self.varify_string(name) == False):
             return "Invalid name format"

         if(self.varify_string(country) == False):
            return "Invalid country format"
        
         if(self.varify_string(passport) == False or  self.varify_length(passport, 9) == False):
             return "Invalid passport format"
            
         if(passport.isupper() == False):
             return "Passport number must be in upper case"

         if(self.varify_string(country) == False):
             return "Invalid country format"

         if(self.varify_date(d_from) == False or self.varify_date(d_to) == False):
             return "Please use dd-mm-yyyy date format"

             
         if(room_type == "male dorm"):
             self.room_number = Accomodation().booked_male_dorm()
            
         if(room_type == "female dorm"):
             self.room_number = Accomodation().booked_female_dorm()
            
         if(room_type == "single room"):
             self.room_number = Accomodation().booked_single_room()
            
         if(room_type == "double room"):
             self.room_number = Accomodation().booked_double_room()

         if(self.room_number == 'Booking full'):
             return "Booking full for seleted room type"

         self.name = name
         self.country = country
         self.passport = passport
         self.gender = gender
         self.date_from = d_from
         self.date_to = d_to
         self.room_type = room_type
         

         return True

    def generate_booking_id(self):
        self.booking_id = round(random.random()*1000000)
        return self.booking_id

    def set_details_database(self, name, booking_id, country, passport, gender, d_from, d_to, room_type, room_number):
        self.name = name
        self.booking_id = booking_id
        self.country = country
        self.passport = passport
        self.gender = gender
        self.date_from = d_from
        self.date_to = d_to
        self.room_type = room_type
        self.room_number = room_number

        if(room_type == "male dorm"):
             male_dorms.remove(room_number)
            
        if(room_type == "female dorm"):
            female_dorms.remove(room_number)
        
        if(room_type == "single room"):
            single_rooms.remove(room_number)
        
        if(room_type == "double room"):
            double_rooms.remove(room_number)

        return

    def get_details(self):
        return {
                "name": self.name,
                "booking_id": self.booking_id,
                "country": self.country,
                "passport": self.passport,
                "gender": self.gender,
                "date_from": self.date_from,
                "date_to": self.date_to,
                "room_type": self.room_type,
                "room_number": self.room_number
        }
    def varify_string(self, string):
        return isinstance(string, str)

    def varify_date(self, date):
        try:
            datetime.strptime(date,'%d-%m-%Y')
        except:
            return False
        else:
            return True

    def varify_length(self, passport, number):
        if(len(passport) == number):
            return True
        else:
            return False
    