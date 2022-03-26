from tkinter import Frame
from constants import *

#Body where all the frames will be displayed!
body = Frame(window, background=window_primary)
body.place(x=400, y=160, width=760, height=500)

def content_frame():
    global body
    frame = Frame(body, bg=window_secondary)
    frame.place(x=0, y=0, width=760, height=500)
    return frame

def collapse(frame):
    frame.place(x=0, y=0, width=0, height=0)

def flex(frame):
    frame.place(x=0, y=0, width=760, height=500)

# three frames needed, Each frame for each section i.e Home, New Booking and History

home_frame = content_frame()
booking_frame = content_frame()
history_frame = content_frame()

collapse(home_frame)
collapse(booking_frame)
collapse(history_frame)


# Selection of frame is done based on the button click
def select_page(page):
    global home_frame, booking_frame, history_frame
    if(page == "home"):
        flex(home_frame)
        collapse(booking_frame)
        collapse(history_frame)
        
    elif(page == "book"):
        flex(booking_frame)
        collapse(home_frame)
        collapse(history_frame)
        
    elif(page == "history"):
        flex(history_frame)
        collapse(booking_frame)
        collapse(home_frame)


