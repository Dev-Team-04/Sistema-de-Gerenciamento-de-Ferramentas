import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tela de Login')
        self.geometry('1000x700')
        self.config(background='#008')
        self.bg = PhotoImage(file="MODELO 2.png")
        self.label = Label(self, image=self.bg, width=1000, height=700, bg='silver')
        self.label.place(x=0, y=0)

        self.lb_usuario = Label(self, text="LOGIN", anchor=W, bg='silver')
        self.lb_usuario.place(x=150, y=190, width=100, height=20)
        self.usuario = Entry(self, bg='blue')
        self.usuario.place(x=150, y=220, width=100, height=20)


        #
        # self.usuario = Entry(self, bg='silver')
        # self.usuario.place(x=10, y=220, width=150, height=20)
        #
        # self.lb_senha = Label(self, text="Senha", anchor=W, bg='silver')
        # self.lb_senha.place(x=10, y=250, width=100, height=20)
        #
        # self.senha = Entry(self, bg='silver')
        # self.senha.place(x=10, y=270, width=150, height=20)
        #
        self.botao3 = Button(self, text="Login", bg='silver', anchor=W, command=self.abrir_jan_cf)
        self.botao3.place(x=150, y=280, width=100, height=20)

    def abrir_jan_cf(self):
        Jan_Cf()

class Jan_Cf(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title('Gerenciador de Ferramentas')
        self.geometry('700x600')

        my_note = ttk.Notebook(self)
        my_note.place(x=0, y=0, width=1000, height=600)


        tb2 = Frame(my_note, background='#008', width=250, height=150, bg='silver')
        my_note.add(tb2, text='Gerenciar Ferramentas')

        tb4 = Frame(my_note, bg='silver', width=250, height=150)
        my_note.add(tb4, text='Gerenciar Tecnicos')

        tb5 = Frame(my_note, bg='silver', width=250, height=150)
        my_note.add(tb5, text='Gerenciar Reservas')

if __name__ == "__main__":
    root = App()
    root.mainloop()