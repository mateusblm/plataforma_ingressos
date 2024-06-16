import sqlite3
from customtkinter import *
from utils import setup_database, show_popup, generate_user_id


class Reports:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.reports_window = CTk()
        self.reports_window.title("Relatórios e Estatísticas")
        self.reports_window.geometry("600x450")

        self.FrameReports = CTkFrame(master=self.reports_window)
        self.FrameReports.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

        self.LabelReports = CTkLabel(master=self.FrameReports, text='Relatórios de Vendas')
        self.LabelReports.place(relx=0.05, rely=0.05)

        self.ButtonTotalIngressos = CTkButton(master=self.FrameReports, command=self.total_ingressos_vendidos, text='Total de Ingressos Vendidos')
        self.ButtonTotalIngressos.place(relx=0.05, rely=0.15)

        self.ButtonTotalReceita = CTkButton(master=self.FrameReports, command=self.total_receita_gerada, text='Total de Receita Gerada')
        self.ButtonTotalReceita.place(relx=0.05, rely=0.25)

        self.LabelResult = CTkLabel(master=self.FrameReports, text='')
        self.LabelResult.place(relx=0.05, rely=0.35)

        self.reports_window.mainloop()

    def total_ingressos_vendidos(self):
        """
        Calcula e exibe o total de ingressos vendidos.
        """
        try:
            self.cursor.execute("SELECT SUM(quantidade) FROM compras")
            total = self.cursor.fetchone()[0]
            self.LabelResult.configure(text=f'Total de Ingressos Vendidos: {total}')
        except sqlite3.Error as e:
            show_popup("Erro", f"Erro ao calcular total de ingressos vendidos: {e}")

    def total_receita_gerada(self):
        """
        Calcula e exibe a receita total gerada.
        """
        try:
            self.cursor.execute("SELECT SUM(ingressos.preco * compras.quantidade) FROM ingressos JOIN compras ON ingressos.id = compras.ingresso_id")
            total = self.cursor.fetchone()[0]
            self.LabelResult.configure(text=f'Total de Receita Gerada: R${total:.2f}')
        except sqlite3.Error as e:
            show_popup("Erro", f"Erro ao calcular receita total: {e}")