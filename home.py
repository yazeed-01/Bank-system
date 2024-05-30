from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sqlite3
from tkinter import messagebox as massagebox
from db import *






def open_home_page():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"F:\vs code projects\Bank system PY\home\build\assets\frame0")


    def relative_to_assets(path: str) -> Path:
                                            return ASSETS_PATH / Path(path)
    root = Tk()

    def go_to_register():
                        root.destroy()  
                        import register  
                        register.open_registration_page()

    def go_to_login():
                        root.destroy()  
                        import login  
                        login.open_login_page()


    #_______________________________________________________________

    root.geometry("1270x720")
    root.configure(bg = "#3E3E42")

    canvas = Canvas(
        root,
        bg = "#3E3E42",
        height = 720,
        width = 1270,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    #_________________________________________________________________________________



    canvas.place(x = 0, y = 0)
    canvas.create_text(
        16.0,
        44.0,
        anchor="nw",
        text="Yazeed Bank",
        fill="#F5F5F5",
        font=("JacquesFrancois Regular", 60 * -1)
    )


    #_______________________________________________________________


    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: go_to_register(),
        relief="flat"
    )
    button_1.place(
        x=320.0,
        y=497.0,
        width=566.0,
        height=126.6083984375
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0, 
        relief="flat"
        ,command=lambda: go_to_login()
    )
    button_2.place(
        x=320.0,
        y=257.0,
        width=566.0,
        height=130.359619140625
    )

    canvas.create_rectangle(
        -5.0,
        163.0,
        1440.0086669921875,
        168.0,
        fill="#FFFFFF",
        outline="")
    root.resizable(False, False)
    root.mainloop()

open_home_page()