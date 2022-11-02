import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

#-----------

nome_adm = 'devteam4'
senha_adm = 'devteam4'

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tela de Login')
        self.geometry('1000x700')
        self.config(background='#008')
        self.bg = PhotoImage(file="TELA BEM VINDO 3.png")
        self.label = Label(self, image=self.bg, width=1000, height=700, bg='silver')
        self.label.place(x=0, y=0)

        self.lb_usuario = Label(self, text="LOGIN:", anchor=W, bg='silver')
        self.lb_usuario.place(x=150, y=190, width=100, height=20)
        self.usuario = Entry(self, bg='silver')
        self.usuario.place(x=150, y=220, width=100, height=20)

        self.lb_senha = Label(self, text="PASSWORD:", anchor=W, bg='silver')
        self.lb_senha.place(x=150, y=250, width=100, height=20)
        self.senha = Entry(self, bg='silver')
        self.senha.place(x=150, y=280, width=100, height=20)

        self.botao3 = Button(self, text="Login", bg='silver', anchor=W, command=self.abrir_jan_cf)
        self.botao3.place(x=150, y=350, width=100, height=20)

        #self.usuario = Entry(self, bg='silver')
        #self.usuario.place(x=10, y=220, width=150, height=20)
        #

        #

        #


    def abrir_jan_cf(self):
        Jan_Cf()

        #DESATIVEI PARA FAZER OS TESTES SEM PRECISAR POR LOGIN E SENHA

    # def abrir_jan_cf(self):
    #      if self.usuario.get() == 'devteam4' and self.senha.get() == 'devteam4':
    #         Jan_Cf()
    #      else:
    #          messagebox.showinfo(title='Usuario ou senha invalidos', message='Usuario ou senha invalidos')

class Jan_Cf(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title('Gerenciador de Ferramentas')
        self.geometry('900x600')

        my_note = ttk.Notebook(self)
        my_note.place(x=0, y=0, width=1000, height=600)


        tb2 = Frame(my_note, background='#008', width=250, height=150, bg='silver')
        my_note.add(tb2, text='Gerenciar Ferramentas')

        tb4 = Frame(my_note, bg='silver', width=250, height=150)
        my_note.add(tb4, text='Gerenciar Tecnicos')




        tb5 = Frame(my_note, bg='silver', width=250, height=150)
        my_note.add(tb5, text='Gerenciar Reservas')

# ------------------Adicionando Widgets a aba Gerenciar Tecnicos (botes, labels, etc)--------------------

        lbnome_tb4 = Label(tb4, text='NOME', anchor=W)
        vnome = Entry(tb4)
        lbturno_tb4 = Label(tb4, text='TURNO', anchor=W)
        vturno = Entry(tb4)
        lbequipe_tb4 = Label(tb4, text='EQUIPE', anchor=W)
        vequipe = Entry(tb4)
        lbcpf_tb4 = Label(tb4, text='CPF', anchor=W)
        vcpf = Entry(tb4)
        lbfone_tb4 = Label(tb4, text='TELEFONE', anchor=W)
        vfone = Entry(tb4)

# ------------------Adicionando Widgets a aba tb2 (botes, labels, etc)--------------------

        lbid_tb2 = Label(tb2, text='ID', anchor=W)
        vid = Entry(tb2)
        lbdesc_tb2 = Label(tb2, text='DESCRIÇÃO', anchor=W)
        vdesc = Entry(tb2)
        lbfab_tb2 = Label(tb2, text='FABRICANTES', anchor=W)
        vfab = Entry(tb2)
        lbvolt_tb2 = Label(tb2, text='VOLTAGEM', anchor=W)
        vvolt = Entry(tb2)
        lbtam_tb2 = Label(tb2, text='TAMANHO', anchor=W)
        vtam = Entry(tb2)
        lbuni_tb2 = Label(tb2, text='UNIDADE', anchor=W)
        vuni = Entry(tb2)
        lbtipo_tb2 = Label(tb2, text='TIPO', anchor=W)
        vtipo = Entry(tb2)
        lbmat_tb2 = Label(tb2, text='MATERIAL', anchor=W)
        vmat = Entry(tb2)
        lbpn_tb2 = Label(tb2, text='PART NUMBER', anchor=W)
        vpn = Entry(tb2)

 # ------------------Adicionando Widgets a aba tb5 (botes, labels, etc)--------------------

        lbidfer_tb5 = Label(tb5, text='ID Ferramenta', anchor=W)
        vidfer = Entry(tb5)
        lbdesc_tb5 = Label(tb5, text='DESCRIÇÃO da solicitação', anchor=W)
        vdescres = Entry(tb5)
        lbdtret_tb5 = Label(tb5, text='DATA RETIRADA', anchor=W)
        vdtret = Entry(tb5)
        lbhrret_tb5 = Label(tb5, text='HORA RETIRADA', anchor=W)
        vhrret = Entry(tb5)
        lbdtdev_tb5 = Label(tb5, text='DATA DEVOLUÇAO', anchor=W)
        vdtdev = Entry(tb5)
        lbhrdev_tb5 = Label(tb5, text='HORA DEVOLUÇÃO', anchor=W)
        vhrdev = Entry(tb5)
        lbnmtec_tb5 = Label(tb5, text='NOME', anchor=W)
        vnmtec = Entry(tb5)

        # -Botao para executar a funcao de adicionar dados ao treeview e ao BD pelo formulario--------------------------

        btn_adicionar_tb4 = Button(tb4, text='Adicionar')
        #                           command=add_tvbd)

        btn_adicionar_tb2 = Button(tb2, text='Adicionar')# command=add_tvbd2)

        # -----------------------------------------------------------------------------------

        # -Botao para executar a funcao de Excluir dados do treeview e do BD selecionando o item-----------------------

        btn_excluir_tb4 = Button(tb4, text='Deletar')
        #                         command=del_tvbd)

        btn_excluir_tb2 = Button(tb2, text='Deletar') #command=del_tvbd2)

        # --------------------------Download --------------------------------------------------

        btn_down_tb4 = Button(tb4, text='Fazer download') #command=download)

        btn_down_tb2 = Button(tb2, text='Fazer download') #command=download2)

        ##-----------Adicionando o treeview na aba4 e carregando dados do bd-------------------------


        #dadosColunas = [item for item in Bd.tabela_funcionarios.columns]

        colunas = ['NOME', 'TURNO', 'EQUIPE', 'CPF','TELEFONE']
        valores = ['NELSON', 'NOTURNO', 'DEV4', 4]

        dadosColunas = [item for item in colunas]


        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview', background='silver', foreground='black', rowheight=25,
                        fieldbackground='silver')
        style.map('Treeview', background=[('selected', 'red')])

        treeProdutos = ttk.Treeview(tb4,
                                    columns=dadosColunas,
                                    show='headings')

        # Adding a scrollbar to Treeview widget
        ytreeScroll2 = ttk.Scrollbar(tb4)
        ytreeScroll2.configure(command=treeProdutos.yview)

        xtreeScroll2 = ttk.Scrollbar(tb4, orient='horizontal')
        xtreeScroll2.configure(command=treeProdutos.xview)

        treeProdutos.configure(yscrollcommand=ytreeScroll2.set, xscrollcommand=xtreeScroll2.set)

        xtreeScroll2.pack(side=BOTTOM, fill='x')
        ytreeScroll2.pack(side=RIGHT, fill=BOTH)

        for i in dadosColunas:
            treeProdutos.heading(f"{i}", text=f"{i}")

        #for n in Bd.tabela_funcionarios.values:
        treeProdutos.insert('', tk.END, values=valores)

        treeProdutos.place(x=4, y=100, width=1000, height=200)

 # -------------------Posicionando os elementos na aba tb2----------------------

        lbid_tb2.place(x=10, y=10, width=80, height=20)
        vid.place(x=10, y=30, width=80, height=20)
        lbdesc_tb2.place(x=100, y=10, width=80, height=20)
        vdesc.place(x=100, y=30, width=80, height=20)
        lbfab_tb2.place(x=190, y=10, width=70, height=20)
        vfab.place(x=190, y=30, width=70, height=20)
        lbvolt_tb2.place(x=270, y=10, width=70, height=20)
        vvolt.place(x=270, y=30, width=70, height=20)
        lbtam_tb2.place(x=350, y=10, width=70, height=20)
        vtam.place(x=350, y=30, width=70, height=20)
        lbuni_tb2.place(x=430, y=10, width=70, height=20)
        vuni.place(x=430, y=30, width=70, height=20)
        lbtipo_tb2.place(x=510, y=10, width=70, height=20)
        vtipo.place(x=510, y=30, width=70, height=20)
        lbmat_tb2.place(x=590, y=10, width=70, height=20)
        vmat.place(x=590, y=30, width=70, height=20)
        lbpn_tb2.place(x=670, y=10, width=70, height=20)
        vpn.place(x=670, y=30, width=70, height=20)
        btn_adicionar_tb2.place(x=10, y=300, width=80, height=20)
        btn_excluir_tb2.place(x=100, y=300, width=80, height=20)
        btn_down_tb2.place(x=190, y=300, width=100, height=20)

# -------------------Posicionando os elementos na aba tb4----------------------

        lbnome_tb4.place(x=10, y=10, width=80, height=20)
        vnome.place(x=10, y=30, width=80, height=20)
        lbturno_tb4.place(x=100, y=10, width=80, height=20)
        vturno.place(x=100, y=30, width=80, height=20)
        lbequipe_tb4.place(x=190, y=10, width=70, height=20)
        vequipe.place(x=190, y=30, width=70, height=20)
        lbcpf_tb4.place(x=270, y=10, width=70, height=20)
        vcpf.place(x=270, y=30, width=70, height=20)
        lbfone_tb4.place(x=360, y=10, width=80, height=20)
        vfone.place(x=360, y=30, width=80, height=20)
        btn_adicionar_tb4.place(x=10, y=300, width=80, height=20)
        btn_excluir_tb4.place(x=100, y=300, width=80, height=20)
        #btn_carregar_tb4.place(x=190, y=300, width=80, height=20)
        btn_down_tb4.place(x=190, y=300, width=100, height=20)

# -------------------Posicionando os elementos na aba tb5 GERENCIADOR DE RESERVAS----------------------

        lbidfer_tb5.place(x=10, y=10, width=80, height=20)
        vidfer.place(x=10, y=30, width=80, height=20)
        lbdesc_tb5.place(x=100, y=10, width=80, height=20)
        vdescres.place(x=100, y=30, width=80, height=20)
        lbdtret_tb5.place(x=190, y=10, width=70, height=20)
        vdtret.place(x=190, y=30, width=70, height=20)
        lbhrret_tb5.place(x=270, y=10, width=70, height=20)
        vhrret.place(x=270, y=30, width=70, height=20)
        lbdtdev_tb5.place(x=350, y=10, width=70, height=20)
        vdtdev.place(x=350, y=30, width=70, height=20)
        lbhrdev_tb5.place(x=430, y=10, width=70, height=20)
        vhrdev.place(x=430, y=30, width=70, height=20)
        lbnmtec_tb5.place(x=510, y=10, width=70, height=20)
        vnmtec.place(x=510, y=30, width=70, height=20)

#------------------Adicionando Widgets as demais abas (botes, labels, etc)--------------------

        lbl_tb2 = Label(tb2, text='Gerenciar Ferramentas')
        lbl_tb2.place(x=350, y=70, width=200, height=20)

        lbl_tb4 = Label(tb4, text='Gerenciar Tecnicos')
        lbl_tb4.place(x=350, y=70, width=200, height=20)

        lbl_tb5 = Label(tb5, text='Gerenciar Reservas')
        lbl_tb5.place(x=350, y=70, width=200, height=20)

if __name__ == "__main__":
    root = App()
    root.mainloop()
