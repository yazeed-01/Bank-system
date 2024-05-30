from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
from tkinter.ttk import Radiobutton, Style
import sqlite3
import hashlib
from tkinter import messagebox as massagebox
from db import *













def open_registration_page():
    def register():

        
        fullname = entry_1.get()
        email = entry_3.get()
        password = entry_4.get()
        n_username = entry_5.get()
        amount = entry_2.get()
        if n_username != "" and password != "" and fullname != "" and email != "" and amount != "":
                c.execute('SELECT * FROM user WHERE username = ?', [n_username])
                if c.fetchone() is not None:
                    massagebox.showerror(title="Error", message="user already exists")
                else:
                    data_insert_query = '''INSERT INTO user (fullname, username, password, email, amount) VALUES (?, ?, ?, ?, ?)'''
                    data_insert_tuple = (fullname, n_username, password, email, amount)
                    cursor = conn.cursor()
                    cursor.execute(data_insert_query, data_insert_tuple)
                    conn.commit()
                    conn.close()
                    massagebox.showinfo(title="Error", message="user created")
        else:
            massagebox.showerror(title="Error", message="all fields are required")




    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"F:\vs code projects\Bank system PY\home\build\assets2\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("1270x720")
    window.configure(bg = "#3E3E42")

    


    def switch_to_home():
        window.destroy()
        import home
        home.open_home_page()

    canvas = Canvas(
        window,
        bg = "#3E3E42",
        height = 720,
        width = 1270,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        0.0,
        30.0,
        anchor="nw",
        text="Yazeed Bank",
        fill="#F5F5F5",
        font=("JacquesFrancois Regular", 60 * -1)
    )

    canvas.create_rectangle(
        13.0,
        124.0,
        1458.0086669921875,
        129.0,
        fill="#FFFFFF",
        outline="")

#_______________________________________________________________


    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        549.5,
        201.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Arial Bold", 20)
        
    )
    entry_1.place(
        x=307.0,
        y=168.0,
        width=485.0,
        height=64.0
    )


#_______________________________________________________________


    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        578.5,
        673.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Arial Bold", 20)
    )
    entry_2.place(
        x=365.0,
        y=643.0,
        width=427.0,
        height=59.0
    )

#_______________________________________________________________


    canvas.create_text(
        9.0,
        168.0,
        anchor="nw",
        text="Full Name:",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 50 * -1)
    )

    canvas.create_text(
        46.0,
        285.0,
        anchor="nw",
        text="Email:",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 50 * -1)
    )


#_______________________________________________________________



    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        549.5,
        325.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Arial Bold", 20)
    )
    entry_3.place(
        x=307.0,
        y=293.0,
        width=485.0,
        height=63.0
    )




    #_______________________________________________________________

    canvas.create_text(
        5.0,
        411.0,
        anchor="nw",
        text="Password:",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 50 * -1)
    )

#_______________________________________________________________




    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        597.0,
        455.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Arial Bold", 20)
    )
    entry_4.place(
        x=402.0,
        y=420.0,
        width=390.0,
        height=68.0
    )


#_______________________________________________________________


    canvas.create_text(
        63.0,
        539.0,
        anchor="nw",
        text="Username:",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 50 * -1)
    )



#_______________________________________________________________


    entry_5 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Arial Bold", 20)
    )
    entry_5.place(
        x=403.0,
        y=549.0,
        width=390.0,
        height=68.0
    )

#_______________________________________________________________

    canvas.create_text(
        62.0,
        634.0,
        anchor="nw",
        text="Amount:",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 50 * -1)
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: register(),
        relief="flat"
    )
    button_3.place(
        x=1004.0,
        y=633.0,
        width=243.46697998046875,
        height=64.231689453125
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_to_home(),
        relief="flat"
    )
    button_4.place(
        x=1014.0,
        y=37.0,
        width=243.46697998046875,
        height=64.231689453125
    )
    window.resizable(False, False)
    window.mainloop()


open_registration_page()