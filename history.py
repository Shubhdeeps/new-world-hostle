from tkinter import Frame, Label, Entry, PhotoImage, Button
from constants import window_secondary, window_active, window_primary, window, list_items
from display_message import Popup
from frame_header import header_content
from content_body import history_frame

from residents import *

#init history content frame
history_body_frame = Frame(history_frame,background=window_secondary)
history_body_frame.place(x=50, y=81, width=660, height=380)

class Items:
    def __init__(self, ind, person):

        global history_body_frame
        self._isActive = False
        self.person = person
        
        self._outer_frame = Frame(history_body_frame, background="#7C7C7C")
        self._outer_frame.place(x=0, y = (ind*65 + 5), width=660, height=60)
        self._inner_frame = Frame(self._outer_frame, background = window_secondary)
        self._inner_frame.place(x=1, y=1, width=658, height=58)


        self._bindAction(self._inner_frame)
        self._inner_frame.bind("<Double-Button-1>", self._double_action)
        self._outer_frame.bind("<Enter>", self._mouse_enter)
        self._outer_frame.bind("<Leave>", self._mouse_leave)

        self._booking_id = Label(self._inner_frame, font=("Comic Sans", 12, "bold"),bg=window_secondary, text=person["booking_id"], fg="#fff")
        self._booking_id.place(x=45, y=19)
        

        self._name = Label(self._inner_frame, font=("Comic Sans", 12), text=person["name"], bg=window_secondary, fg="#fff")
        self._name.place(x=270, y=19)

        self._country = Label(self._inner_frame, font=("Comic Sans", 12), text=person["country"], bg=window_secondary, fg="#fff")
        self._country.place(x=550, y=19)


    def _mouse_enter(self, event):
        if(self._isActive == False):
            self._outer_frame["background"] = window_active
            self._booking_id["foreground"] = window_active
            self._name["foreground"] = window_active
            self._country["foreground"] = window_active
    
    def _mouse_leave(self,event):
        if(self._isActive == False):
            self._outer_frame["background"] = "#7C7C7C"
            self._booking_id["foreground"] = '#fff'
            self._name["foreground"] = '#fff'
            self._country["foreground"] = '#fff'

    def _actions(self, event):
        self._isActive = not self._isActive
        self._changebg()


    def _changebg(self):
         bgcolor = window_active if self._isActive else window_secondary
         fgcolor = window_primary if self._isActive else "#fff"
        
         self._inner_frame.config(bg = bgcolor)
         self._booking_id.config(bg = bgcolor, fg=fgcolor)
         self._name.config(bg = bgcolor, fg=fgcolor)
         self._country.config(bg = bgcolor, fg=fgcolor)


    def _bindAction(self, element):
        element.bind("<Button-1>", self._actions)

    def get_selected_bookings(self):
        return [self.person["booking_id"], self._isActive]

    def set_true(self):
        self._isActive = True
        self._changebg()

    def set_false(self):
        self._isActive = False
        self._changebg()

    def delete_entry(self):
        self._outer_frame.destroy()

    def _double_action(self, event):
        messagebox1 = Popup(window, "{self.person.name} from {self.person.country}", "passport number: 122222, checkin date: 12-03-2001 to 12-04-2001, Gender: Male")
        messagebox1.flex_box()


#rendering entries
def render_enteries():
    for i in list_items:
        i.delete_entry()

    list_items.clear()
    for x in range(len(get_enteries())):
        item = Items(x, get_enteries()[x])
        list_items.append(item)

render_enteries()



#to check if an entry has been seleted or not
def check_selected():
    seletedNum = 0
    for x in list_items:
            if(x.get_selected_bookings()[1] == True):
                seletedNum += 1
                
    return seletedNum


# function to delete enteries
def delete_entry():
    deleted_enteries = []     

    if(check_selected() == 0):
        messagebox1 = Popup(window, "Nothing Selected", "Please Select a Booking")
        messagebox1.flex_box()
        return

    for x in list_items:
        if(x.get_selected_bookings()[1] == True):
            deleted = delete_resident_entry(x.get_selected_bookings()[0])
            print(deleted)
            deleted_enteries.append(str(deleted))
            
    
    strng = ""
    for m in deleted_enteries:
        strng += m + ', '

    messagebox1 = Popup(window, "Delete", "Booking id: " +  strng +  " deleted successfully")
    messagebox1.flex_box()

    render_enteries()
            
            
# update function
def update_entry():

    if(check_selected() == 0):
        messagebox1 = Popup(window, "Nothing Selected", "Please Select a Booking")
        messagebox1.flex_box()
        return

    if(check_selected() > 1):
        messagebox1 = Popup(window, "Multiple Entries Selected", "Please Select a single entry to update")
        messagebox1.flex_box()
        return

    
def select_all():
    for x in list_items:
        x.set_true()
    

def de_select_all():
    for x in list_items:
        x.set_false()


#creating header 
header_content("History", history_frame, "Delete", "Update", delete_entry, update_entry)



#search area
search_area = Entry(history_body_frame,font=("Comic Sans", 15) )
search_area.place(x=0, y=350, width=200)

searchlogo = PhotoImage(file='./assets/search.png')
searchlabel = Label(history_body_frame, text=" ", bg=window_secondary, image=searchlogo)
searchlabel.place(x=205, y=350)

# button to select all enteries
select_all_button = Button(history_body_frame,
                        font=("Comic Sans", 10, "bold"),
                        text="Select All",
                        bg=window_primary,
                        fg="#fff",
                        activebackground=window_primary,
                        activeforeground='#fff',
                        bd=0,
                        padx=20,
                        pady=5,
                        command=lambda: select_all())

deselect_all_button = Button(history_body_frame,
                        font=("Comic Sans", 10, "bold"),
                        text="Deselect All",
                        bg=window_primary,
                        fg="#fff",
                        activebackground=window_primary,
                        activeforeground='#fff',
                        bd=0,
                        padx=20,
                        pady=5,
                        command=lambda: de_select_all())

deselect_all_button.place(x=430, y=350)
select_all_button.place(x=555, y=350)