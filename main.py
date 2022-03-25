from tkinter import *
from components import *
from content_body import home_frame, booking_frame, history_frame, select_page
from new_booking import frame
from history import *




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
frame(booking_frame)

