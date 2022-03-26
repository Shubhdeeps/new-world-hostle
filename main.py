from tkinter import *
from components import *
from content_body import home_frame, booking_frame
from new_booking import frame
from history import render_enteries
from residents import *


# init header bar (orignal component inside components.py file)
header()
# init menubar (orignal component inside components.py file)
menubar()



# frames are init inside content_body file
# 1. init Home frame
logo_home = PhotoImage(file='./assets/logoHome.png')
homelabel = Label(home_frame, text=" ", bg=window_secondary, image=logo_home)
homelabel.place(x=170, y=80)


# 2. init New Booking frame
frame(booking_frame, "New Booking")


# 3. init residents
r1 = Resident()
item = r1.set_details("John smith", "Estonia", "P122DHJS9", "M", "22-12-2022", "22-12-2023", "Single Room")


r1.generate_booking_id()
list_items.append(r1.get_details())


# rendering already existed enteries
render_enteries()

