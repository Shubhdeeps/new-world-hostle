from pkgutil import iter_modules
from tkinter import FLAT, Frame, Label, Entry, Radiobutton, ttk, StringVar
from constants import window_secondary, window, list_items
from frame_header import header_content
from residents import *
from display_message import *
from history import render_enteries

country_list = ("Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua &amp; Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia &amp; Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyz Republic","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre &amp; Miquelon","Samoa","San Marino","Satellite","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain","Sri Lanka","St Kitts &amp; Nevis","St Lucia","St Vincent","St. Lucia","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad &amp; Tobago","Tunisia","Turkey","Turkmenistan","Turks &amp; Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe")
accomodation_types = ("male dorm", "female dorm", "single room", "double room")
line_color = '#7C7C7C'
data_fetched = {
    "name": "",
    "country": "",
    "passport": "",
    "gender": "",
    "date_from": "",
    "date_to": "",
    "room_type":""
}
class Booking:
    def __init__(self, booking_frame,  header_text, item, btn_name):
        self.btn_name = btn_name
        self.booking_body_frame = Frame(booking_frame , background=window_secondary)
        self.booking_body_frame.place(x=50, y=81, width=660, height=380)
        header_content(header_text, booking_frame, " Clear ", self.btn_name, self.clear_fields, self.save_fields)
        self._init_booking()

        if(not item == False):
            self.update_item(item)

        #adding elements to initialized booking frame
        #All Labels only
    def _init_booking(self):
        global data_fetched
        spacing = 55
        xspacing = 200
        name_label = Label(self.booking_body_frame, text="Full Name", font=("Comic Sans", 16, "bold"), fg='#fff', bg=window_secondary)
        name_label.place(x=0, y=spacing)
        name_sv = StringVar()
        name_sv.trace("w", lambda name, index, mode, sv=name_sv: self.text_update(name_sv, "name"))

        self.name = Entry(self.booking_body_frame,font=("Comic Sans", 15), textvariable=name_sv, background=line_color, relief=FLAT)
        self.name.place(x=xspacing, y=spacing, width=250)

        gender_label = Label(self.booking_body_frame, text="Gender", font=("Comic Sans", 16, "bold"), fg='#fff', bg=window_secondary)
        gender_label.place(x=0, y=spacing + 50)
        self.gender_sv = StringVar()
        self.gender_sv.trace("w", lambda name, index, mode, sv=self.gender_sv: self.text_update(self.gender_sv, "gender"))
        self.male = Radiobutton(self.booking_body_frame, text="Male", value="M", font=("Comic Sans", 14, "bold"), fg=window_active, bg=window_secondary, activebackground=window_secondary, activeforeground=window_active, padx=20, variable=self.gender_sv, indicatoron=0, relief=FLAT)
        self.female = Radiobutton(self.booking_body_frame, text="Female", value="F", font=("Comic Sans", 14, "bold"), fg=window_active, bg=window_secondary, activebackground=window_secondary, activeforeground=window_active, padx=20, variable=self.gender_sv, indicatoron=0)
        self.male.place(x=xspacing, y=spacing + 50)
        self.female.place(x=xspacing + 100, y=spacing + 50)

        country_label = Label(self.booking_body_frame, text="Country", font=("Comic Sans", 16, "bold"), fg='#fff', bg=window_secondary)
        country_label.place(x=0, y=spacing + 100)
        country_sv = StringVar()
        country_sv.trace("w", lambda name, index, mode, sv=country_sv: self.text_update(country_sv, "country"))
        self.countrylist = ttk.Combobox(self.booking_body_frame, state="readonly", values = country_list,font=("Comic Sans", 12), textvariable=country_sv, background=window_secondary)
        self.countrylist.set("Select a country")
        self.countrylist.place(x= xspacing, y=spacing + 100)

        passport_label = Label(self.booking_body_frame, text="Passport", font=("Comic Sans", 16, "bold"), fg='#fff', bg=window_secondary)
        passport_label.place(x=0, y=spacing + 150)
        passport_sv = StringVar()
        passport_sv.trace("w", lambda name, index, mode, sv=passport_sv: self.text_update(passport_sv, "passport"))
        self.passport = Entry(self.booking_body_frame,font=("Comic Sans", 15), textvariable=passport_sv, background=line_color, relief=FLAT)
        self.passport.place(x=xspacing, y=spacing + 150, width=250)

        duration_label = Label(self.booking_body_frame, text="Duration", font=("Comic Sans", 16, "bold"), fg='#fff', bg=window_secondary)
        duration_label.place(x=0, y=spacing + 200)
        duration_from_sv = StringVar()
        duration_from_sv.trace("w", lambda name, index, mode, sv=duration_from_sv: self.text_update(duration_from_sv, "date_from"))
        self.durationfrom = Entry(self.booking_body_frame,font=("Comic Sans", 15) , textvariable=duration_from_sv, background=line_color, relief=FLAT)
        self.durationfrom.place(x=xspacing, y=spacing + 200, width=150)

        to_label = Label(self.booking_body_frame, text="To", font=("Comic Sans", 14, "bold"), fg='#fff', bg=window_secondary)
        to_label.place(x=xspacing + 180, y=spacing + 200)
        duration_to_sv = StringVar()
        duration_to_sv.trace("w", lambda name, index, mode, sv=duration_to_sv: self.text_update(duration_to_sv, "date_to"))
        self.durationto = Entry(self.booking_body_frame,font=("Comic Sans", 15) , textvariable=duration_to_sv, background=line_color, relief=FLAT)
        self.durationto.place(x= 2*xspacing + 40, y=spacing + 200, width=150)

        accomodation_label = Label(self.booking_body_frame, text="Accomodation", font=("Comic Sans", 16, "bold"), fg='#fff', bg=window_secondary)
        accomodation_label.place(x=0, y=spacing + 250)
        accomodation_sv = StringVar()
        accomodation_sv.trace("w", lambda name, index, mode, sv=accomodation_sv: self.text_update(accomodation_sv, "room_type"))
        self.accomodationlist = ttk.Combobox(self.booking_body_frame, state="readonly", values = accomodation_types ,font=("Comic Sans", 12), textvariable=accomodation_sv)
        self.accomodationlist.set("Select accomodation type")
        self.accomodationlist.place(x= xspacing, y=spacing + 250)


    def update_item(self, item):
        self.name.insert(0, item["name"])
        self.passport.insert(0, item["passport"])
        self.durationto.insert(0, item["date_to"])
        self.durationfrom.insert(0, item["date_from"])
        self.countrylist.current(country_list.index(item["country"]))
        self.accomodationlist.current(accomodation_types.index(item["room_type"]))
        self.gender_sv.set(item["gender"])
        

    def text_update(self, sv, text):
        global data_fetched
        data_fetched[text] = sv.get()
        
    #button funtioin to clear all entry fields
    def clear_fields(self):
        self.name.delete(0, "end")
        self.passport.delete(0, "end")
        self.durationto.delete(0, "end")
        self.durationfrom.delete(0, "end")
        self.countrylist.set("Select a country")
        self.accomodationlist.set("Select accomodation type")
        self.gender_sv.set(None)

    def save_fields(self):
        global data_fetched
        resident = Resident()
        response = resident.set_details(data_fetched["name"], data_fetched["country"], data_fetched["passport"], data_fetched["gender"], data_fetched["date_from"], data_fetched["date_to"], data_fetched["room_type"])
        if(response == True):
            new_id = resident.generate_booking_id()
            data_fetched["booking_id"] = new_id
           
            list_items.insert(0, resident.get_details())
            self.clear_fields()
            render_enteries()
            if(self.btn_name == "Update"):
                from history import frame_init
                self.booking_body_frame.destroy()
                frame_init()
                messagebox1 = Popup(window, "Updated", "Entry was successfully updated")
                messagebox1.flex_box()
                return 

            messagebox1 = Popup(window, "Added", "Entry was successfully added, with booking id: " + str(new_id))
            messagebox1.flex_box()
            return
        
        messagebox1 = Popup(window, "Error", response)
        messagebox1.flex_box()
