import sqlite3
import uuid
from customtkinter import *
from tkinter import Listbox, END

class Login_Register:
    def __init__(self):
        self.setup_database()
        self.top = CTk()
        self.top.geometry("600x450")
        self.top.minsize(1, 1)
        self.top.maxsize(1905, 1050)
        self.top.resizable(1, 1)
        self.top.title("Plataforma Ingresso")

        self.Frame1 = CTkFrame(master=self.top)
        self.Frame1.place(relx=0.25, rely=0.156, relheight=0.722, relwidth=0.575)

        self.Entry1 = CTkEntry(master=self.Frame1, placeholder_text="Username")
        self.Entry1.place(relx=0.261, rely=0.4, relwidth=0.51)

        self.Entry1_2 = CTkEntry(master=self.Frame1, show="*", placeholder_text="Password")
        self.Entry1_2.place(relx=0.261, rely=0.585, relwidth=0.51)

        self.Button1 = CTkButton(master=self.Frame1, command=self.LoginBackEnd, text='Sign In')
        self.Button1.place(relx=0.300, rely=0.708)

        self.Label1 = CTkLabel(master=self.Frame1, text='Login')
        self.Label1.place(relx=0.25, rely=0.20)

        self.Button1_3 = CTkButton(master=self.Frame1, command=self.register, text='Sign Up')
        self.Button1_3.place(relx=0.550, rely=0.852)

        self.Label2 = CTkLabel(master=self.Frame1, text='Username')
        self.Label2.place(relx=0.261, rely=0.30)

        self.Label2_4 = CTkLabel(master=self.Frame1, text='Password')
        self.Label2_4.place(relx=0.261, rely=0.50)

        self.top.mainloop()

    def setup_database(self):
        self.conn = sqlite3.connect('ingressos.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ingressos (
                                id INTEGER PRIMARY KEY,
                                time_casa TEXT,
                                time_visitante TEXT,
                                data TEXT,
                                preco REAL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id TEXT PRIMARY KEY,
                                username TEXT,
                                password TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS compras (
                                user_id TEXT,
                                ingresso_id INTEGER,
                                quantidade INTEGER,
                                FOREIGN KEY (user_id) REFERENCES users(id),
                                FOREIGN KEY (ingresso_id) REFERENCES ingressos(id))''')
        self.conn.commit()

    def register(self):
        self.root = CTk()
        self.root.geometry("467x364")
        self.root.minsize(1, 1)
        self.root.maxsize(1905, 1050)
        self.root.resizable(1, 1)
        self.root.title("Registro")
        
        self.FrameRegister = CTkFrame(master=self.root)
        self.FrameRegister.place(relx=0.236, rely=0.192, relheight=0.626, relwidth=0.525)

        self.LabelRegister = CTkLabel(master=self.FrameRegister, text='Create Your Account')
        self.LabelRegister.place(relx=0.122, rely=0.088)

        self.EntryRegister = CTkEntry(master=self.FrameRegister, placeholder_text="Username")
        self.EntryRegister.place(relx=0.240, rely=0.400, relwidth=0.473)

        self.Entry_Register_Pass = CTkEntry(master=self.FrameRegister, show="*", placeholder_text="Password")
        self.Entry_Register_Pass.place(relx=0.240, rely=0.650, relwidth=0.473)

        self.LabelRegister2 = CTkLabel(master=self.FrameRegister, text='Username:')
        self.LabelRegister2.place(relx=0.240, rely=0.275)

        self.LabelRegister2_4 = CTkLabel(master=self.FrameRegister, text='Password:')
        self.LabelRegister2_4.place(relx=0.240, rely=0.525)

        self.ButtonRegister = CTkButton(master=self.FrameRegister, command=self.RegisterBackEnd, text='Sign Up')
        self.ButtonRegister.place(relx=0.200, rely=0.800)

        self.root.mainloop()

    def userpanel(self):
        self.user = CTk()
        self.user.title("Painel do usuario")
        self.user.geometry("600x450")

        self.FrameUser = CTkFrame(master=self.user)
        self.FrameUser.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

        self.LabelUser = CTkLabel(master=self.FrameUser, text='Ingressos Disponíveis')
        self.LabelUser.place(relx=0.05, rely=0.05)

        self.listbox_ingressos = Listbox(master=self.FrameUser, selectmode=MULTIPLE)
        self.listbox_ingressos.place(relx=0.05, rely=0.15, relheight=0.3, relwidth=0.9)

        self.load_ingressos()

        self.LabelComprados = CTkLabel(master=self.FrameUser, text='Ingressos Comprados')
        self.LabelComprados.place(relx=0.05, rely=0.55)

        self.listbox_comprados = Listbox(master=self.FrameUser)
        self.listbox_comprados.place(relx=0.05, rely=0.65, relheight=0.2, relwidth=0.9)

        self.ButtonBuy = CTkButton(master=self.FrameUser, command=self.buy_ticket, text='Comprar Ingresso')
        self.ButtonBuy.place(relx=0.40, rely=0.88)

        self.load_user_tickets()

        self.user.mainloop()

    def load_ingressos(self):
        self.cursor.execute("SELECT * FROM ingressos")
        ingressos = self.cursor.fetchall()
        self.ingressos = ingressos  # Armazena ingressos para uso posterior

        for ingresso in ingressos:
            self.listbox_ingressos.insert(END, f"ID: {ingresso[0]}, {ingresso[1]} vs {ingresso[2]}, Data: {ingresso[3]}, Preço: R${ingresso[4]:.2f}")

    def buy_ticket(self):
        selected_indices = self.listbox_ingressos.curselection()
        selected_ids = [self.ingressos[i][0] for i in selected_indices]
        selected_prices = [self.ingressos[i][4] for i in selected_indices]

        if selected_ids:
            self.payment = CTk()
            self.payment.title("Pagamento")
            self.payment.geometry("400x500")

            self.FramePayment = CTkFrame(master=self.payment)
            self.FramePayment.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

            self.LabelPayment = CTkLabel(master=self.FramePayment, text='Informações do Cartão')
            self.LabelPayment.place(relx=0.05, rely=0.05)

            self.EntryCardNumber = CTkEntry(master=self.FramePayment, placeholder_text="Número do Cartão")
            self.EntryCardNumber.place(relx=0.05, rely=0.20, relwidth=0.9)

            self.EntryCardName = CTkEntry(master=self.FramePayment, placeholder_text="Nome no Cartão")
            self.EntryCardName.place(relx=0.05, rely=0.35, relwidth=0.9)

            self.EntryCardExpiry = CTkEntry(master=self.FramePayment, placeholder_text="Data de Validade (MMAA)")
            self.EntryCardExpiry.place(relx=0.05, rely=0.50, relwidth=0.9)

            self.EntryCardCVV = CTkEntry(master=self.FramePayment, placeholder_text="CVV")
            self.EntryCardCVV.place(relx=0.05, rely=0.65, relwidth=0.9)

            self.LabelQuantity = CTkLabel(master=self.FramePayment, text='Quantidade de Ingressos:')
            self.LabelQuantity.place(relx=0.05, rely=0.75)

            self.EntryQuantity = CTkEntry(master=self.FramePayment, placeholder_text="Quantidade")
            self.EntryQuantity.place(relx=0.05, rely=0.80, relwidth=0.9)

            self.ButtonConfirmPayment = CTkButton(master=self.FramePayment, command=lambda: self.confirm_payment(selected_ids, selected_prices), text='Confirmar Pagamento')
            self.ButtonConfirmPayment.place(relx=0.35, rely=0.90)

            self.payment.mainloop()

    def confirm_payment(self, ingresso_ids, ingresso_prices):
        card_number = self.EntryCardNumber.get()
        card_name = self.EntryCardName.get()
        card_expiry = self.EntryCardExpiry.get()
        card_cvv = self.EntryCardCVV.get()
        quantidade = self.EntryQuantity.get()

        if not card_number.isdigit() or len(card_number) != 16:
            self.show_popup("Erro", "Número do cartão inválido. Deve conter 16 dígitos.")
            return
        if not card_name.replace(" ", "").isalpha():
            self.show_popup("Erro", "Nome no cartão inválido. Deve conter apenas letras.")
            return
        if not card_expiry.isdigit() or len(card_expiry) != 4:
            self.show_popup("Erro", "Data de validade inválida. Deve estar no formato MMAA. Sem /")
            return
        if not card_cvv.isdigit() or len(card_cvv) != 3:
            self.show_popup("Erro", "CVV inválido. Deve conter 3 dígitos.")
            return
        if not quantidade.isdigit() or int(quantidade) <= 0:
            self.show_popup("Erro", "Quantidade inválida. Deve ser um número positivo.")
            return

        quantidade = int(quantidade)
        total_price = sum(ingresso_prices) * quantidade

        # Simula a confirmação do pagamento
        for ingresso_id in ingresso_ids:
            self.cursor.execute("INSERT INTO compras (user_id, ingresso_id, quantidade) VALUES (?, ?, ?)", (self.current_user_id, ingresso_id, quantidade))
        self.conn.commit()
        self.payment.destroy()
        self.load_user_tickets()

        self.show_popup("Sucesso", f"Compra realizada com sucesso!\nTotal: R${total_price:.2f}")

    def load_user_tickets(self):
        self.cursor.execute("SELECT ingressos.time_casa, ingressos.time_visitante, ingressos.data, ingressos.preco, SUM(compras.quantidade) FROM ingressos JOIN compras ON ingressos.id = compras.ingresso_id WHERE compras.user_id = ? GROUP BY ingressos.id", (self.current_user_id,))
        user_tickets = self.cursor.fetchall()
        self.listbox_comprados.delete(0, END)
        for ticket in user_tickets:
            self.listbox_comprados.insert(END, f"{ticket[0]} vs {ticket[1]}, Data: {ticket[2]}, Preço: R${ticket[3]:.2f}, Quantidade: {ticket[4]}")

    def adminpanel(self):
        self.admin = CTk()
        self.admin.title("Painel do admin")
        self.admin.geometry("600x450")

        self.FrameAdmin = CTkFrame(master=self.admin)
        self.FrameAdmin.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

        self.LabelAdmin = CTkLabel(master=self.FrameAdmin, text='Adicionar Ingresso')
        self.LabelAdmin.place(relx=0.05, rely=0.05)

        self.EntryTimeCasa = CTkEntry(master=self.FrameAdmin, placeholder_text="Time da Casa")
        self.EntryTimeCasa.place(relx=0.05, rely=0.15, relwidth=0.9)

        self.EntryTimeVisitante = CTkEntry(master=self.FrameAdmin, placeholder_text="Time Visitante")
        self.EntryTimeVisitante.place(relx=0.05, rely=0.25, relwidth=0.9)

        self.EntryData = CTkEntry(master=self.FrameAdmin, placeholder_text="Data do Jogo (DD/MM/AAAA)")
        self.EntryData.place(relx=0.05, rely=0.35, relwidth=0.9)

        self.EntryPreco = CTkEntry(master=self.FrameAdmin, placeholder_text="Preço do Ingresso")
        self.EntryPreco.place(relx=0.05, rely=0.45, relwidth=0.9)

        self.ButtonAddIngresso = CTkButton(master=self.FrameAdmin, command=self.add_ingresso, text='Adicionar Ingresso')
        self.ButtonAddIngresso.place(relx=0.35, rely=0.55)

        self.admin.mainloop()

    def add_ingresso(self):
        time_casa = self.EntryTimeCasa.get()
        time_visitante = self.EntryTimeVisitante.get()
        data = self.EntryData.get()
        preco = self.EntryPreco.get()

        if not preco.replace('.', '', 1).isdigit():
            self.show_popup("Erro", "Preço inválido. Deve ser um número.")
            return

        preco = float(preco)

        self.cursor.execute("INSERT INTO ingressos (time_casa, time_visitante, data, preco) VALUES (?, ?, ?, ?)", (time_casa, time_visitante, data, preco))
        self.conn.commit()

        self.EntryTimeCasa.delete(0, END)
        self.EntryTimeVisitante.delete(0, END)
        self.EntryData.delete(0, END)
        self.EntryPreco.delete(0, END)
        self.load_ingressos()

    def RegisterBackEnd(self):
        try:
            user_id = str(uuid.uuid4())
            username = self.EntryRegister.get()
            password = self.Entry_Register_Pass.get()

            self.cursor.execute("INSERT INTO users (id, username, password) VALUES (?, ?, ?)", (user_id, username, password))
            self.conn.commit()
            self.root.destroy()
        except Exception as e:
            self.show_popup("Erro", f"Erro ao registrar: {e}")

    def LoginBackEnd(self):
        try:
            username = self.Entry1.get()
            password = self.Entry1_2.get()

            self.cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
            result = self.cursor.fetchone()

            if username == "root" and password == "toor":
                self.top.destroy()
                self.adminpanel()
            elif result:
                self.current_user_id = result[0]
                self.top.destroy()
                self.userpanel()
            else:
                self.show_popup("Erro", "Login falhou. Usuário ou senha incorretos.")
        except Exception as e:
            self.show_popup("Erro", f"Erro ao fazer login: {e}")

    def show_popup(self, title, message):
        popup = CTk()
        popup.title(title)
        popup.geometry("300x200")

        label = CTkLabel(master=popup, text=message)
        label.place(relx=0.5, rely=0.4, anchor=CENTER)

        button = CTkButton(master=popup, text="OK", command=popup.destroy)
        button.place(relx=0.5, rely=0.7, anchor=CENTER)

        popup.mainloop()

Login_Register()