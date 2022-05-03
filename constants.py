from tkinter import *

#color theme constants
window_active= "#FFC40E"
window_primary = '#333B4E'
window_secondary = '#525867'
hover_color = "#090097"

#list of items to be display inside history section
list_items = []

#available rooms
single_rooms = ["100","101","102","103,104","105","106","107","108","109","110","111","112"]
double_rooms = ["113","114","115","116","117","118","119","120","121","122","123","124","125"]
female_dorms = ["200A","200B","200C","200D","201A","201B","201C","201D","202A","202B","202C","202D","203A","203B","203C","203D","204A","204B","204C","204D","205A","205B","205C","205D"]
male_dorms = ["300A","300B","300C","300D","301A","301B","301C","301D","302A","302B","302C","302D","303A","303B","303C","303D","304A","304B","304C","304D","305A","305B","305C","305D"]

#accomodation types 
accomodation_types = ["male dorm", "female dorm", "single room", "double room"]

#Initalizing tkinter, and coloring the window
window = Tk()
window.title('New World Hostle')
window.geometry("1280x720")
window.configure(bg=window_primary)
window.resizable(False, False)