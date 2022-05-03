from tkinter import Button, Frame, Label
from constants import window_active, window_primary, window_secondary

popup_color = "#FEFFF0"

class Popup:
    def __init__(self, window, title, content):
        self.title = title
        self.content = content

        self.pop_up_frame = Frame(window, bg=window_active)
        self.pop_up_frame.place(relx=1, x=-320, rely=1, y=-160, width=0, height=0)
        inner_frame = Frame(self.pop_up_frame, bg=popup_color)
        inner_frame.place(x=1, y=1, relwidth=1, relheight=1, width=-2, height=-2)
        

        # --- header content ---
        header_line = Frame(inner_frame, bg='#7C7C7C')
        header_line.place(x=12, y=0, height=40, relwidth=1, width=-24)
        header_frame = Frame(header_line, bg=popup_color)
        header_frame.place(x=0, y=0, relwidth=1, height=39)
        
        header = Label(header_frame,
                       font=("Comic Sans", 12, "bold"),
                       text=self.title,
                       background=popup_color,
                       foreground=window_primary)
        header.pack(side="left")

        #------- body content

        body_content = Label(inner_frame, 
                        font=("Comic Sans", 10), 
                        text=self.content, 
                        background= popup_color, 
                        foreground= window_primary, wraplength=276, justify="center")
        body_content.place(x=12, rely=0.4, y=-5)


        button = Button(inner_frame, 
                        font=("Comic Sans", 10, "bold"), 
                        text='Dismiss', 
                        background= popup_color, 
                        foreground= window_active, 
                        activebackground=popup_color,
                        activeforeground= window_primary,
                        bd=0, 
                        padx=20,
                        pady=5,
                        command=self._quit_box)
        button.place(relx=1, rely=1, x=-90, y=-40)
        

    def flex_box(self):
        self.pop_up_frame.place(width=300, height=140)

    def _quit_box(self):
        self.pop_up_frame.place(width=0, height=0)

