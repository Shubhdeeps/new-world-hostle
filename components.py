from tkinter import Frame, Label, PhotoImage, Button, Menu
from constants import *
from content_body import select_page



# ---------------------HEADER COMPONENT-------------------
logo = PhotoImage(file='./assets/logo.png')
def header():
    global logo
    #Creating Header, which contain title logo, and theme changing button
    header = Frame(window, bg='#505050')
    header.place(x=120, width=1040, height=105)

    innerheader = Frame(header, bg=window_primary)
    innerheader.place(width=1040, height=104)

    #Header logo
    
    logolabel = Label(innerheader, text=" ", bg=window_primary, image=logo)
    logolabel.place(x=5, y=48)

    quitbtn = Button(innerheader,
                    font=("Comic Sans", 10, "bold"),
                    text="Quit",
                    bg="#D45900",
                    fg="white",
                    activebackground="#B92C2C",
                    activeforeground='#fff',
                    bd=0,
                    width=20, height=2,
                    command=window.destroy)
    quitbtn.place(x=878, y=60)


# -------------------------MENUBAR COMPONENT---------------------------
def menubar():
    #Creating Menubar, and adding File menu, and Help menu
    menubar = Menu(window)
    window.config(menu=menubar)

    # for File menu
    filemenu = Menu(menubar, tearoff=0, activebackground = window_active)
    menubar.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label="Import")

    #Export Menu catagorized into CSV and TEXT file
    exportmenu = Menu(menubar, tearoff=0, activebackground = window_active)
    filemenu.add_cascade(label="Export as" , menu=exportmenu)
    exportmenu.add_command(label="CSV file")
    exportmenu.add_command(label="Text file")

    filemenu.add_separator()
    filemenu.add_command(label="Quit application", command= window.destroy)



    #for Help menu
    helpmenu = Menu(menubar, tearoff=0, activebackground = window_active)
    menubar.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label="About application")
    helpmenu.add_command(label="Developer info")

#-------------NAVIGATION BAR COMPONENT------------------------
#the group of button added directly to windows
buttongroup = Frame(window, bg=window_primary)
buttongroup.place(x=120, y=160, width=240, height=500)


#in order to change active button color, this function used
def _nav_buttons(text, function):
    global buttongroup
    global change_btn

    button = Button(buttongroup,
                font=("Comic Sans", 10, "bold"),
                text=text,
                bg=window_secondary,
                fg='#fff',
                activebackground=window_secondary,
                activeforeground='#fff',
                bd=0,
                command=lambda: change_btn(function)
                )
    return button


def change_btn(req):
    global _button_home, _button_new_booking, _button_history
    select_page(req)
    if(req == "home"):
        btn_set_active(_button_home, True)
        btn_set_active(_button_new_booking, False)
        btn_set_active(_button_history, False)
    elif(req == "book"):
        btn_set_active(_button_home, False)
        btn_set_active(_button_new_booking, True)
        btn_set_active(_button_history, False)
    elif(req == "history"):
        btn_set_active(_button_home, False)
        btn_set_active(_button_new_booking, False)
        btn_set_active(_button_history, True)


def btn_set_active(btn, isActive):
    if isActive == True:
        btn.config(bg=window_active, fg=window_primary)
    else:
        btn.config(bg=window_secondary, fg='#fff')


_button_home = _nav_buttons("Home", "home")
_button_new_booking  = _nav_buttons("New Booking", "book")
_button_history  = _nav_buttons("History", "history")

_button_home.place(x=0, y=0, width=240, height=60)
_button_new_booking.place(x=0, y=80, width=240, height=60)
_button_history.place(x=0, y=160, width=240, height=60)

# by default home button will be active
change_btn("home")