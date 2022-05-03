from tkinter import *
from new_booking import Booking
from components import *
from content_body import home_frame, booking_frame
from residents import *
from database import get_database_enteries



# init header bar (orignal component inside components.py file)
header()
# init menubar (orignal component inside components.py file)
menubar()



# frames are init inside content_body file
# 1. init Home frame
logo_home = PhotoImage(file='./assets/logoHome.png')
homelabel = Label(home_frame, text=" ", bg=window_secondary, image=logo_home)
homelabel.place(x=170, y=80)

#running database, to store or retireve all enteries
get_database_enteries()
# 3. init New Booking frame
Booking(booking_frame, "New Booking", False, "Save")
