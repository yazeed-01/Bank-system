from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sqlite3
import tkinter
from tkinter import messagebox as massagebox
def open_settings_page(u):
    usser = u

    def change_fullname():

        name = entry_1.get()
        if name == "":
            massagebox.showerror(title="Error", message="Please enter your fullname")
            return
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        fullname = entry_1.get()
        c.execute('UPDATE user SET fullname = ? WHERE username = ?', [name , usser])
        conn.commit()
        conn.close()
        massagebox.showinfo(title="Success", message="fullname changed successful")

    def change_email():
        email = entry_2.get()
        if email == "":
            massagebox.showerror(title="Error", message="Please enter your email")
            return
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        fullname = entry_1.get()
        c.execute('UPDATE user SET email = ? WHERE username = ?', [email , usser])
        conn.commit()
        conn.close()
        massagebox.showinfo(title="Success", message="email changed successful")

    def change_username():
        username = entry_4.get()
        if username == "":
            massagebox.showerror(title="Error", message="Please enter your username")
            return
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        fullname = entry_1.get()
        c.execute('UPDATE user SET username = ? WHERE username = ?', [username , usser])
        conn.commit()
        conn.close()
        massagebox.showinfo(title="Success", message="username changed successful")

    def change_password():
        password = entry_3.get()
        if password == "":
            massagebox.showerror(title="Error", message="Please enter your password")
            return
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        fullname = entry_1.get()
        c.execute('UPDATE user SET password = ? WHERE password = ?', [password , usser])
        conn.commit()
        conn.close()
        massagebox.showinfo(title="Success", message="fullname changed successful")









    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"F:\vs code projects\Bank system PY\home\build\assets5\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("1270x720")
    window.configure(bg = "#3E3E42")


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


    def go_to_home():
        window.destroy()
        import home


    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: change_fullname(),
        relief="flat"
    )
    button_1.place(
        x=7000.0,
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
        command=lambda: change_fullname(),
        relief="flat"
    )
    button_2.place(
        x=770.0,
        y=196.0,
        width=243.46697998046875,
        height=64.231689453125
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: change_email(),
        relief="flat"
    )
    button_3.place(
        x=769.0,
        y=299.0,
        width=243.46697998046875,
        height=64.231689453125
    )

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
        506.5,
        232.0,
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
        x=264.0,
        y=199.0,
        width=485.0,
        height=64.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        506.5,
        335.0,
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
        x=264.0,
        y=302.0,
        width=485.0,
        height=64.0
    )

    canvas.create_text(
        107.0,
        185.0,
        anchor="nw",
        text="Full Name",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 50 * -1)
    )

    canvas.create_text(
        150.0,
        299.0,
        anchor="nw",
        text="Email",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 50 * -1)
    )

    canvas.create_text(
        108.0,
        397.0,
        anchor="nw",
        text="Username",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 50 * -1)
    )

    canvas.create_text(
        108.0,
        514.0,
        anchor="nw",
        text="Password",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 50 * -1)
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: change_username(),
        relief="flat"
    )
    button_5.place(
        x=769.0,
        y=400.0,
        width=243.46697998046875,
        height=64.231689453125
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: change_password(),
        relief="flat"
    )
    button_6.place(
        x=768.0,
        y=511.0,
        width=243.46697998046875,
        height=64.231689453125
    )

    def go_to_user_page():
        window.destroy()
        import user
        user.user_page(usser)

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: go_to_user_page(),
        relief="flat"
    )
    button_7.place(
        x=1014.0,
        y=644.0,
        width=243.46697998046875,
        height=64.231689453125
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        506.5,
        544.0,
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
        x=264.0,
        y=511.0,
        width=485.0,
        height=64.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        506.5,
        433.0,
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
        x=264.0,
        y=400.0,
        width=485.0,
        height=64.0
    )

    def show_exist_info():
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('select * from user where username = ?', [usser])
        amount = c.fetchone()
        message = f"The Fullname for user '{usser}' is: {amount[0]}\nThe Email for user '{usser}' is: {amount[3]}\nThe Username for user '{usser}' is: {amount[1]}\nThe Password for user '{usser}' is: {amount[2]}"
        tkinter.messagebox.showinfo(title="Amount Information", message=message)


        conn.close()



    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_exist_info(),
        relief="flat"
    )
    button_8.place(
        x=312.0,
        y=639.0,
        width=684.0,
        height=67.231689453125
    )
    window.resizable(False, False)
    window.mainloop()
