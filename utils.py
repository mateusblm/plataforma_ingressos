import sqlite3
import uuid
from customtkinter import CTk, CTkLabel, CTkButton
from tkinter import CENTER

def setup_database():
    """
    Configura o banco de dados SQLite, criando as tabelas necessárias se elas não existirem.
    """
    try:
        conn = sqlite3.connect('ingressos.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS ingressos (
                            id INTEGER PRIMARY KEY,
                            time_casa TEXT,
                            time_visitante TEXT,
                            data TEXT,
                            preco REAL)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id TEXT PRIMARY KEY,
                            username TEXT,
                            password TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS compras (
                            user_id TEXT,
                            ingresso_id INTEGER,
                            quantidade INTEGER,
                            FOREIGN KEY (user_id) REFERENCES users(id),
                            FOREIGN KEY (ingresso_id) REFERENCES ingressos(id))''')
        conn.commit()
        return conn, cursor
    except sqlite3.Error as e:
        show_popup("Erro", f"Erro ao configurar o banco de dados: {e}")
        return None, None

def show_popup(title, message):
    """
    Exibe uma janela popup com uma mensagem.

    Args:
        title (str): Título da janela popup.
        message (str): Mensagem a ser exibida na janela popup.
    """
    popup = CTk()
    popup.title(title)
    popup.geometry("300x200")

    label = CTkLabel(master=popup, text=message)
    label.place(relx=0.5, rely=0.4, anchor=CENTER)

    button = CTkButton(master=popup, text="OK", command=popup.destroy)
    button.place(relx=0.5, rely=0.7, anchor=CENTER)

    popup.mainloop()

def generate_user_id():
    """
    Gera um ID único para o usuário usando UUID.
    """
    return str(uuid.uuid4())