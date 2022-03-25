import imp
from tkinter import *

#color theme constants
window_active= "#FFC40E"
window_primary = '#333B4E'
window_secondary = '#525867'
hover_color = "#090097"

#list of items to be display inside history section
list_items = []

#Initalizing tkinter, and coloring the window
window = Tk()
window.title('New World Hostle')
window.geometry("1280x720")
window.configure(bg=window_primary)
window.resizable(False, False)