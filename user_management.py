import sqlite3
from customtkinter import *
from tkinter import Listbox, END
from utils import setup_database, show_popup, generate_user_id


class UserManagement:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.user_management_window = CTk()
        self.user_management_window.title("Gestão de Usuários")
        self.user_management_window.geometry("600x450")

        self.FrameUserManagement = CTkFrame(master=self.user_management_window)
        self.FrameUserManagement.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

        self.LabelUserManagement = CTkLabel(master=self.FrameUserManagement, text='Gestão de Usuários')
        self.LabelUserManagement.place(relx=0.05, rely=0.05)

        self.listbox_users = Listbox(master=self.FrameUserManagement)
        self.listbox_users.place(relx=0.05, rely=0.15, relheight=0.6, relwidth=0.9)

        self.ButtonLoadUsers = CTkButton(master=self.FrameUserManagement, command=self.load_users, text='Carregar Usuários')
        self.ButtonLoadUsers.place(relx=0.05, rely=0.80)

        self.ButtonDeleteUser = CTkButton(master=self.FrameUserManagement, command=self.delete_user, text='Excluir Usuário')
        self.ButtonDeleteUser.place(relx=0.35, rely=0.80)

        self.load_users()

        self.user_management_window.mainloop()

    def load_users(self):
        """
        Carrega e exibe a lista de usuários no listbox.
        """
        try:
            self.listbox_users.delete(0, END)
            self.cursor.execute("SELECT id, username FROM users")
            users = self.cursor.fetchall()
            for user in users:
                self.listbox_users.insert(END, f"ID: {user[0]}, Username: {user[1]}")
        except sqlite3.Error as e:
            show_popup("Erro", f"Erro ao carregar usuários: {e}")

    def delete_user(self):
        """
        Exclui o usuário selecionado do banco de dados.
        """
        selected_index = self.listbox_users.curselection()
        if selected_index:
            user_id = self.listbox_users.get(selected_index).split(",")[0].split(":")[1].strip()
            try:
                self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
                self.conn.commit()
                self.load_users()
            except sqlite3.Error as e:
                show_popup("Erro", f"Erro ao excluir usuário: {e}")