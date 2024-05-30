from pathlib import Path
import tkinter
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sqlite3
from tkinter import messagebox as massagebox
from db import *

def user_page(u):
    usser = u
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"F:\vs code projects\Bank system PY\home\build\assets4\frame0")
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    window = Tk()
    window.geometry("1270x720")
    window.configure(bg = "#3E3E42")



    def Withdraw():
        global username
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        amount = entry_1.get()
        if amount: 
            try:
                c.execute('UPDATE user SET amount = amount - ? WHERE username = ?', [amount , usser])
                conn.commit()
                massagebox.showinfo(title="Success", message="Withdrawal successful")
            except sqlite3.Error as err:
                massagebox.showerror(title="Error", message=f"Withdrawal failed: {err}")

        conn.close()

    def deposit():
        global username
        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        amount = entry_2.get()
        if amount: 
            try:
                c.execute('UPDATE user SET amount = amount + ? WHERE username = ?', [amount , usser])
                conn.commit()
                massagebox.showinfo(title="Success", message="deposit successful")
            except sqlite3.Error as err:
                massagebox.showerror(title="Error", message=f"Withdrawal failed: {err}")

        conn.close()

    def transfer():
        global username
        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        amount = entry_3.get()
        idd = entry_4.get()
        c.execute('SELECT * FROM user WHERE username = ?', [idd])
        if c.fetchone() is  None:
                    massagebox.showerror(title="Error", message="user not found")
                    return
        if amount: 
                try:
                    c.execute('UPDATE user SET amount = amount + ? WHERE username = ?', [amount , idd])
                    conn.commit()
                    c.execute('UPDATE user SET amount = amount - ? WHERE username = ?', [amount , usser])
                    conn.commit()
                    massagebox.showinfo(title="Success", message="deposit successful")
                except sqlite3.Error as err:
                    massagebox.showerror(title="Error", message=f"Withdrawal failed: {err}")

        conn.close()

    
    def balance():
        global username
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('select amount from user where username = ?', [usser])
        amount = c.fetchone()
        message = f"The amount for user '{usser}' is: {amount}"
        tkinter.messagebox.showinfo(title="Amount Information", message=message)


        conn.close()










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
        command=lambda: Withdraw(),
        relief="flat"
    )
    button_2.place(
        x=580.0,
        y=140.0,
        width=243.46697998046875,
        height=64.231689453125
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: deposit(),
        relief="flat"
    )
    button_3.place(
        x=580.0,
        y=254.0,
        width=243.46697998046875,
        height=64.231689453125
    )
    def go_to_home():
        window.destroy()
        import home

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: go_to_home(),
        relief="flat"
    )
    button_4.place(
        x=1014.0,
        y=37.0,
        width=243.46697998046875,
        height=64.231689453125
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        410.5,
        172.0,
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
        x=269.0,
        y=139.0,
        width=283.0,
        height=64.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        407.0,
        285.0,
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
        x=269.0,
        y=252.0,
        width=276.0,
        height=64.0
    )

    canvas.create_text(
        40.0,
        136.0,
        anchor="nw",
        text="Withdraw",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 50 * -1)
    )

    canvas.create_text(
        40.0,
        248.0,
        anchor="nw",
        text="Deposit",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 50 * -1)
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transfer(),
        relief="flat"
    )
    button_5.place(
        x=1024.0,
        y=360.0,
        width=243.46697998046875,
        height=64.231689453125
    )


    def go_to_settings():
        window.destroy()
        import settings
        settings.open_settings_page(usser)




    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: go_to_settings(),
        relief="flat"
    )
    button_6.place(
        x=996.0,
        y=610.0,
        width=243.46697998046875,
        height=64.231689453125
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=20.0,
        y=625.0,
        width=501.0,
        height=64.231689453125
    )


    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: balance(),
        relief="flat"
    )
    button_8.place(
        x=15.0,
        y=530.0,
        width=540.0,
        height=64.231689453125
    )




    def on_entry_click(event):
        if entry_3.get() == "Amount":
                entry_3.delete(0, tkinter.END)
                entry_3.configure(foreground="black")

    def on_focus_out(event):
        if entry_3.get() == "":
                entry_3.insert(0, "Amount")
                entry_3.configure(foreground="gray")

    canvas.create_rectangle(
        1.0,
        533.0,
        558.0,
        597.231689453125,
        fill="#000000",
        outline="")

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        392.0,
        400.0,
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
        x=269.0,
        y=367.0,
        width=246.0,
        height=64.0
    )
    entry_3.insert(0, "Amount")
    entry_3.bind("<FocusIn>", on_entry_click)
    entry_3.bind("<FocusOut>", on_focus_out)






    def on_entry_click(event):
        if entry_4.get() == "Username":
                entry_4.delete(0, tkinter.END)
                entry_4.configure(foreground="black")

    def on_focus_out(event):
        if entry_4.get() == "":
                entry_4.insert(0, "Username")
                entry_4.configure(foreground="gray")


    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        771.5,
        397.0,
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
        x=529.0,
        y=364.0,
        width=485.0,
        height=64.0
    )
    entry_4.insert(0, "Username")
    entry_4.bind("<FocusIn>", on_entry_click)
    entry_4.bind("<FocusOut>", on_focus_out)

    canvas.create_text(
        40.0,
        360.0,
        anchor="nw",
        text="Transfer",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 50 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
