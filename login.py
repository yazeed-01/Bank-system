from pathlib import Path
from random import randint
import threading
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from db import *
import sqlite3
from tkinter import messagebox as massagebox










def open_login_page():


 


    def login():
        def go_to_user_page():
            window.destroy()
            import user
            user.user_page(username)

        username =  entry_1.get()
        password = entry_2.get()
        
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        if username != "" and password != "":
            c.execute('SELECT * FROM user WHERE username = ? AND password = ?', [username, password])
            result = c.fetchone()
            if result:
                if password == result[2]:
                    go_to_user_page()
                else:
                    massagebox.showerror(title="Error", message="invalid password")
            else:
                massagebox.showerror(title="Error", message="invalid username")
        else:
            massagebox.showerror(title="Error", message="all fields are required")


















    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"F:\vs code projects\Bank system PY\home\build\assets3\frame0")


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

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=1014.0,
        y=37.0,
        width=243.46697998046875,
        height=64.231689453125
    )

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

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: login(),
        relief="flat"
    )
    button_2.place(
        x=513.0,
        y=527.0,
        width=243.46697998046875,
        height=64.231689453125
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_to_home(),
        relief="flat"
    )
    button_3.place(
        x=1014.0,
        y=37.0,
        width=243.46697998046875,
        height=64.231689453125
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        635.5,
        297.0,
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
        x=393.0,
        y=264.0,
        width=485.0,
        height=64.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        635.5,
        460.0,
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
        x=393.0,
        y=427.0,
        width=485.0,
        height=64.0
    )

    canvas.create_text(
        400.0,
        204.0,
        anchor="nw",
        text="ID:",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 50 * -1)
    )

    canvas.create_text(
        400.0,
        367.0,
        anchor="nw",
        text="Password:",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 50 * -1)
    )
    window.resizable(False, False)
    window.mainloop()


open_login_page()