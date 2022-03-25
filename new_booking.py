from tkinter import Frame, Label, Entry, Radiobutton, ttk
from constants import window_secondary
from frame_header import header_content

country_list = ("Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua &amp; Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia &amp; Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyz Republic","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre &amp; Miquelon","Samoa","San Marino","Satellite","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain","Sri Lanka","St Kitts &amp; Nevis","St Lucia","St Vincent","St. Lucia","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad &amp; Tobago","Tunisia","Turkey","Turkmenistan","Turks &amp; Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe")
accomodation_types = ("male dorm", "female dorm", "single room", "double room")



def frame(booking_frame):
    global booking_body_frame

    booking_body_frame = Frame(booking_frame , background=window_secondary)
    booking_body_frame.place(x=50, y=81, width=660, height=380)
    header_content("New Booking", booking_frame, " Clear ", " Save ", clear_fields, save_fields)
    _init_booking()


    #adding elements to initialized booking frame
    #All Labels only
def _init_booking():
    spacing = 55
    xspacing = 200
    name_label = Label(booking_body_frame, text="Full Name", font=("Comic Sans", 16, "bold"), fg='#fff', bg=window_secondary)
    name_label.place(x=0, y=spacing)
    name = Entry(booking_body_frame,font=("Comic Sans", 15) )
    name.place(x=xspacing, y=spacing, width=250)

    gender_label = Label(booking_body_frame, text="Gender", font=("Comic Sans", 16, "bold"), fg='#fff', bg=window_secondary)
    gender_label.place(x=0, y=spacing + 50)
    male = Radiobutton(booking_body_frame, text="Male", value=1, font=("Comic Sans", 16, "bold"), fg='#fff', bg=window_secondary, activebackground=window_secondary, activeforeground='#fff')
    female = Radiobutton(booking_body_frame, text="Female", value=2, font=("Comic Sans", 14, "bold"), fg='#fff', bg=window_secondary, activebackground=window_secondary, activeforeground='#fff')
    male.place(x=xspacing, y=spacing + 50)
    female.place(x=xspacing + 100, y=spacing + 50)

    country_label = Label(booking_body_frame, text="Country", font=("Comic Sans", 16, "bold"), fg='#fff', bg=window_secondary)
    country_label.place(x=0, y=spacing + 100)
    countrylist = ttk.Combobox(booking_body_frame, state="readonly", values = country_list,font=("Comic Sans", 12))
    countrylist.set("Select a country")
    countrylist.place(x= xspacing, y=spacing + 100)

    passport_label = Label(booking_body_frame, text="Passport", font=("Comic Sans", 16, "bold"), fg='#fff', bg=window_secondary)
    passport_label.place(x=0, y=spacing + 150)
    passport = Entry(booking_body_frame,font=("Comic Sans", 15))
    passport.place(x=xspacing, y=spacing + 150, width=250)

    duration_label = Label(booking_body_frame, text="Duration", font=("Comic Sans", 16, "bold"), fg='#fff', bg=window_secondary)
    duration_label.place(x=0, y=spacing + 200)
    durationfrom = Entry(booking_body_frame,font=("Comic Sans", 15) )
    durationfrom.place(x=xspacing, y=spacing + 200, width=150)
    to_label = Label(booking_body_frame, text="To", font=("Comic Sans", 14, "bold"), fg='#fff', bg=window_secondary)
    to_label.place(x=xspacing + 180, y=spacing + 200)
    durationto = Entry(booking_body_frame,font=("Comic Sans", 15) )
    durationto.place(x= 2*xspacing + 40, y=spacing + 200, width=150)

    accomodation_label = Label(booking_body_frame, text="Accomodation", font=("Comic Sans", 16, "bold"), fg='#fff', bg=window_secondary)
    accomodation_label.place(x=0, y=spacing + 250)
    accomodationlist = ttk.Combobox(booking_body_frame, state="readonly", values = accomodation_types ,font=("Comic Sans", 12))
    accomodationlist.set("Select accomodation type")
    accomodationlist.place(x= xspacing, y=spacing + 250)

    return[name, passport, durationfrom, durationto, countrylist, accomodationlist]


#button funtioin to clear all entry fields
def clear_fields():
    entry_fields = _init_booking()
    entry_fields[0].delete(0, 'end')
    entry_fields[1].delete(0, 'end')
    entry_fields[2].delete(0, 'end')
    entry_fields[3].delete(0, 'end')
    entry_fields[4].set("Select a country")
    entry_fields[5].set("Select accomodation type")

def save_fields():
    pass
