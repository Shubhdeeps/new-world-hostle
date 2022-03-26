import random
from datetime import *

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

    def upload_booking_id(self, booking_id):
        self.booking_id = booking_id

    def get_details(self):
        return {
                "name": self.name,
                "booking_id": self.booking_id,
                "country": self.country,
                "passport": self.passport,
                "gender": self.gender,
                "date_from": self.date_from,
                "date_to": self.date_to,
                "room_type": self.room_type
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
    