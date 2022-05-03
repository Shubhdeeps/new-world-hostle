from tkinter import Frame, Label, Button
from constants import window_active, window_primary, window_secondary


# --- Header content of Each page ---
def header_content(ttl, frame, btn_one_text, btn_two_text, f1, f2):
    head_container = Frame(frame ,background='#7C7C7C')
    head_container.place(x=50, y=0, width=660, height=80)

    head_inner = Frame(head_container,background=window_secondary)
    head_inner.place(x=0, y=0, width=760, height=79)

    title = Label(head_inner,
                    font=("Comic Sans", 20, "bold"),
                    text=ttl,
                    bg=window_secondary,
                    fg=window_active)
    title.place(x=0, y=40)

    header_button_one = Button(head_inner,
                        font=("Comic Sans", 10, "bold"),
                        text=btn_one_text,
                        bg="#D45900",
                        fg="#fff",
                        activebackground=window_primary,
                        activeforeground='#fff',
                        bd=0,
                        padx=20,
                        pady=5, 
                        command=lambda: f1())
    header_button_one.place(x=476, y=39)

    header_button_two = Button(head_inner,
                        font=("Comic Sans", 10, "bold"),
                        text=btn_two_text,
                        bg="#4AA800",
                        fg="#fff",
                        activebackground=window_primary,
                        activeforeground='#fff',
                        bd=0,
                        padx=20,
                        pady=5,        
                        command=lambda: f2())
    header_button_two.place(x=570, y=39)