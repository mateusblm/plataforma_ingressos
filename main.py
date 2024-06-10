import sys
from customtkinter import *
class Login_Register:
    def __init__(self):
        self.top = CTk()
        self.top.geometry("600x450")
        self.top.minsize(1, 1)
        self.top.maxsize(1905, 1050)
        self.top.resizable(1, 1)
        self.top.title("Plataforma Ingresso")

        self.Frame1 = CTkEntry(master=self.top)
        self.Frame1.place(relx=0.25, rely=0.156, relheight=0.722, relwidth=0.575)

        self.Entry1 = CTkEntry(master=self.Frame1)
        self.Entry1.place(relx=0.261, rely=0.4, relwidth=0.51)

        self.Entry1_2 = CTkEntry(master=self.Frame1, show="*")
        self.Entry1_2.place(relx=0.261, rely=0.585, relwidth=0.51)

        self.Button1 = CTkButton(master=self.Frame1, command=self.LoginBackEnd, text='''Sign In''')
        self.Button1.place(relx=0.300, rely=0.708)

        self.Label1 = CTkLabel(master=self.Frame1, text='''Login''')
        self.Label1.place(relx=0.25, rely=0.20)

        self.Button1_3 = CTkButton(master=self.Frame1, command=self.register, text='''Sign Up''')
        self.Button1_3.place(relx=0.550, rely=0.852)

        self.Label2 = CTkLabel(master=self.Frame1, text='''Username''')
        self.Label2.place(relx=0.261, rely=0.30)

        self.Label2_4 = CTkLabel(master=self.Frame1, text='''Password''')
        self.Label2_4.place(relx=0.261, rely=0.50)

        self.top.mainloop()

    def register(self):

        self.root = CTk()
        self.root.geometry("467x364")
        self.root.minsize(1, 1)
        self.root.maxsize(1905, 1050)
        self.root.resizable(1, 1)
        self.root.title("Registro")
        
        self.FrameRegister = CTkEntry(master=self.root)
        self.FrameRegister.place(relx=0.236, rely=0.192, relheight=0.626
                                 , relwidth=0.525)

        self.LabelRegister = CTkLabel(master=self.FrameRegister, text='''Create Your Account''')
        self.LabelRegister.place(relx=0.122, rely=0.088)

        self.EntryRegister = CTkEntry(master=self.FrameRegister)
        self.EntryRegister.place(relx=0.240, rely=0.400, relwidth=0.473)

        self.EntryRegister_1 = CTkEntry(master=self.FrameRegister)
        self.EntryRegister_1.place(relx=1.592, rely=0.772, relwidth=0.473)

        self.EntryRegister_2 = CTkEntry(master=self.FrameRegister)
        self.EntryRegister_2.place(relx=0.270, rely=1.167, relwidth=0.473)

        self.LabelRegister2 = CTkLabel(master=self.FrameRegister, text='''Username:''')
        self.LabelRegister2.place(relx=0.240, rely=0.275)

        self.Entry_Register_Pass = CTkEntry(master=self.FrameRegister, show="*")
        self.Entry_Register_Pass.place(relx=0.240, rely=0.650,relwidth=0.473)

        self.LabelRegister2_4 = CTkLabel(master=self.FrameRegister, text='''Password:''')
        self.LabelRegister2_4.place(relx=0.240, rely=0.525)

        self.ButtonRegister = CTkButton(master=self.FrameRegister, command=self.RegisterBackEnd, text='''Sign Up''')
        self.ButtonRegister.place(relx=0.200, rely=0.800)
        self.root.mainloop()

    def userpanel(self):
        user = CTk()
        user.title("Painel do usuario")
        user.geometry("600x450")
        user.mainloop()
    def adminpanel(self):
        admin = CTk()
        admin.title("Painel do admin")
        admin.geometry("600x450")
        admin.mainloop()


    def RegisterBackEnd(self):
        try:
            with open("users.txt", "a") as archiveUser:
                archiveUser.write(self.EntryRegister.get() + '\n')

            with open("passwords.txt", "a") as archivePass:
                archivePass.write(self.Entry_Register_Pass.get() + '\n')
            self.root.destroy()
        except:
            pass

    def LoginBackEnd(self):
        with open("users.txt", "r") as archiveUser:
            users = archiveUser.readlines()
        with open("passwords.txt", "r") as archivePass:
            passws = archivePass.readlines()

        users = list(map(lambda x: x.replace('\n', ''), users))
        passws = list(map(lambda x: x.replace('\n', ''), passws))

        user = self.Entry1.get()
        passw = self.Entry1_2.get()

        sucesslogin = False

        for i in range(len(users)):
            if user == "root" and passw == "toor":
                self.top.destroy()
                self.adminpanel()
            elif user == users[i] and passw == passws[i]:
                self.top.destroy()
                self.userpanel()
            sucesslogin = True

            if not sucesslogin:
                self.top.destroy()

Login_Register()
