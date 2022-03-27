from tkinter import *
from new_booking import Booking
from components import *
from content_body import home_frame, booking_frame, history_frame
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
Booking(booking_frame, "New Booking", False, "Save")

# 3. init residents
r1 = Resident()
r2 = Resident()
r3 = Resident()
r4 = Resident()
r5 = Resident()
r6 = Resident()
r7 = Resident()
r1.set_details("John 1", "Estonia", "P122DHJS9", "M", "22-12-2022", "22-12-2023", "single room")
r2.set_details("Mahn 2", "Finland", "M132DHJS9", "M", "22-12-2022", "22-12-2023", "single room")
r3.set_details("Bahn 3", "India", "M122DHJS9", "M", "22-12-2022", "22-12-2023", "single room")
r4.set_details("Mohn 4", "Australia", "W122DHJS9", "M", "22-12-2022", "22-12-2023", "single room")
r5.set_details("jagggg", "Canada", "M132DHJS9", "M", "22-12-2022", "22-12-2023", "single room")
r6.set_details("manggg", "Europe", "M122DHJS9", "F", "22-12-2022", "22-12-2023", "single room")
r7.set_details("sanngggg", "Nepal", "W122DHJS9", "F", "22-12-2022", "22-12-2023", "single room")


r1.generate_booking_id()
r2.generate_booking_id()
r3.generate_booking_id()
r4.generate_booking_id()
r5.generate_booking_id()
r6.generate_booking_id()
r7.generate_booking_id()
list_items.append(r1.get_details())
list_items.append(r2.get_details())
list_items.append(r3.get_details())
list_items.append(r4.get_details())
list_items.append(r5.get_details())
list_items.append(r6.get_details())
list_items.append(r7.get_details())


# rendering already existed enteries
render_enteries()
