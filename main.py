from customtkinter import *


if __name__ == '__main__':
    root = CTk()
    root.geometry("350x400")
    root.title("Login Cliente")
    root._set_appearance_mode("light")
    font1 = CTkFont(family="bold", size=15)
    btn1 = CTkButton(master=root, text="Login", corner_radius=32, font=font1, width=100)
    btn2 = CTkButton(master=root, text="Sign up", corner_radius=32, font=font1, width=100)
    label1 = CTkLabel(master=root, font=font1, text="Usuario")
    label1.place(relx=0.25, rely=0.3, anchor="center")
    btn1.place(relx=0.65, rely=0.7, anchor="center")
    btn2.place(relx=0.3, rely=0.7, anchor="center")

    root.mainloop()

