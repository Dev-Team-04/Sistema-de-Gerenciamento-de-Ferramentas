#import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, Event
from random import randint


#-----------

nome_adm = 'devteam4'
senha_adm = 'devteam4'

#tabela_ferramentas = pd.read_csv(r'lista_ferramentas.csv', sep=';', index_col=0, encoding= 'unicode_escape')
#tabela_funcionarios = pd.read_csv(r'lista_funcionarios.csv', sep=',', index_col=0)
#tabela_reservas = pd.read_csv(r'lista_reservas.csv', sep=';', index_col=0)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #TELA DE LOGIN:
        self.iconbitmap(r'C:\Users\egalv\Documents\VSCODE\Sistema-de-Gerenciamento-de-Ferramentas-main\estacio_sem_nome.ico')
        self.title('Tela de Login')
        self.geometry('1000x700')
        self.config(background='#373435')
        self.bg = PhotoImage(file="TELA BEM VINDO 3.png")
        self.label = Label(self, image=self.bg, width=980, height=690)
        self.label.place(x=0, y=0)

        #LABEL E ENTRY TELA DE LOGIN
        self.lb_usuario = Label(self, text="LOGIN", anchor=W,fg='white', bg='#444244')
        self.lb_usuario.place(x=150, y=190, width=100, height=20)
        self.usuario = Entry(self, bg='white')
        self.usuario.place(x=150, y=220, width=100, height=20)
        self.lb_senha = Label(self, text="PASSWORD", anchor=W,fg='white', bg='#444244')
        self.lb_senha.place(x=150, y=250, width=100, height=20)
        self.senha = Entry(self,show='*', bg='white')
        self.senha.place(x=150, y=280, width=100, height=20)
        #BOTA DE LOGIN
        self.botao3 = Button(self, text="Login", fg='white', bg='#444244', anchor=W, command=self.abrir_jan_cf)
        self.botao3.place(x=150, y=320, width=100, height=20)
        #BOTAO DE MOSTRAR SENHA
        self.botao4 = Button(self, text="Mostrar Senha", fg='white', bg='#444244', anchor=W, command=self.my_show)
        self.botao4.place(x=150, y=350, width=100, height=20)

    #FUNÇÃO DE MOSTRAR SENHA
    def my_show(self):
        if (len(self.senha.get())!=0):
            self.senha.config(show='')
        else:
            messagebox.showinfo(message='Digite sua senha.')

    #FUNCTION ABRIR JANELA
    def abrir_jan_cf(self):
        Jan_Cf()

    #FUNCION PARA USUARIO E SENHA
    # def abrir_jan_cf(self):
    #      if self.usuario.get() == 'devteam4' and self.senha.get() == 'devteam4':
    #         Jan_Cf()
    #      else:
    #          messagebox.showinfo(title='Usuário ou senha inválidos!', message='Usuário ou senha inválidos!')

class Jan_Cf(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title('Gerenciador de Ferramentas')
        self.geometry('1000x700')
        self.config(background='#373435')
        #self.state("zoomed")

        my_note = ttk.Notebook(self)
        my_note.place(x=0, y=0, width=1000, height=700)

#------ FUNÇÃO --- DELETAR----SOMENTE --- TB4 -------- FUNCIONARIOS

        def del_tvbd():
            if not treeProdutos.selection():
                messagebox.showinfo(title='erro', message='Selecione o elemento a ser deletado')
            else:
                index = treeProdutos.index(treeProdutos.selection()[0])
                treeProdutos.delete(treeProdutos.selection()[0])
                # print(tabela_funcionarios)
                tabela_funcionarios = pd.read_csv(r'lista_funcionarios.csv', sep=',', index_col=0)
                tabela_funcionarios = tabela_funcionarios.drop([index])
                tabela_funcionarios = tabela_funcionarios.reset_index()
                # print(tabela_funcionarios)
                tabela_funcionarios = tabela_funcionarios.drop(['index'], axis=1)
                tabela_funcionarios.to_csv(r'lista_funcionarios.csv')

# ------ FUNÇÃO --- DELETAR----SOMENTE --- TB2 -------- FUNCIONARIOS

        def del_tvbd2():
            if not treeFer.selection():
                messagebox.showinfo(title='erro', message='Selecione o elemento a ser deletado')
            else:
                index = treeFer.index(treeFer.selection()[0])
                #print(index)
                treeFer.delete(treeFer.selection()[0])
                tabela_ferramentas = pd.read_csv(r'lista_ferramentas.csv', sep=';', index_col=0)
                #print(tabela_ferramentas)
                tabela_ferramentas = tabela_ferramentas.drop([index])
                tabela_ferramentas = tabela_ferramentas.reset_index()
                # print(tabela_ferramentas)
                tabela_ferramentas = tabela_ferramentas.drop(['index'], axis=1)
                # print(tabela_ferramentas)
                tabela_ferramentas.to_csv(r'lista_ferramentas.csv', sep=';')

        def val_fer():
            descricao = vdesc.get()
            fabricante = vfab.get()
            voltagem = vvolt.get()
            pnumber = vpn.get()
            tamanho = vtam.get()
            unidade = vuni.get()
            tipofer = vtipo.get()
            matfer = vmat.get()
            if len(descricao) == 0:
                return 'descricao não pode estar vazio'
            if len(fabricante) == 0:
                return 'fabricante não pode estar vazio'
            if len(voltagem) == 0:
                return 'voltagem não pode estar vazio'
            if len(pnumber) == 0:
                return 'descricao não pode estar vazio'
            if len(tamanho) == 0:
                return 'fabricante não pode estar vazio'
            if len(unidade) == 0:
                return 'voltagem não pode estar vazio'
            if len(tipofer) == 0:
                return 'descricao não pode estar vazio'
            if len(matfer) == 0:
                return 'fabricante não pode estar vazio'
            else:
                try:
                    if len(descricao) > 60: # elif len(name) <= 5 or len(name) >40: return 'O nome deve ser entre 05 a 40 caracteres'
                        return 'descricao deve ter até 60'
                    if len(fabricante) > 30:
                        return 'fabricante deve ter até 40 caracteres'
                    if len(voltagem) > 15: # Podem ser as opções para escolher uma (manha, tarde, noite)
                        return 'voltagem deve ter até 15 caracteres'
                    if len(pnumber) > 25:
                        return 'pnumber deve ter até 25 caracteres'
                    if len(tamanho) > 20:
                        return 'tamanho deve ter até 20 caracteres'
                    if len(unidade) > 15:
                        return 'Unidade de medida deve ter até 15 caracteres'
                    if len(tipofer) >15:
                        return 'tipofer deve ter até 15 caracteres'
                    # TEM QUE INSERIR AQUI A FUNÇÃO DE VALIDAR DIGITOS VERIFICADORES DO CPF
                    if len(matfer) >15 :
                        return 'matfer deve ter até 15 caracteres'
                    else:
                        return 'Sucess!'
                except Exception as ep:
                    messagebox.showerror('Error', ep)

        def add_tvbd2():
            if val_fer() != 'Sucess!':
                #or vturno.get() =='' or vequipe.get() =='' or vcpf.get() =='' or vfone.get() =='':
                messagebox.showinfo('erro', message=val_fer())
            # if vdesc.get() =='' or vfab.get() =='' or vvolt.get() =='' \
            #         or vtam.get() =='' or vuni.get() =='' or vtipo.get() =='' or vmat.get() ==''\
            #         or vpn.get() =='':
            #     messagebox.showinfo('erro', message='Preencha todos os campos')
            else:
                treeFer.insert('', tk.END,
                values=(gerar_id(), vdesc.get(), vfab.get(), vvolt.get(), vtam.get(), vuni.get(),
                vtipo.get(),vmat.get(),vpn.get()))
                lista_add = [gerar_id(), vdesc.get(), vfab.get(), vvolt.get(), vtam.get(), vuni.get(),
                vtipo.get(),vmat.get(),vpn.get()]
                #print(Bd.tabela_ferramentas)
                tabela_ferramentas.loc[len(tabela_ferramentas)] = lista_add
                #print(Bd.tabela_ferramentas)
                tabela_ferramentas.to_csv(r'lista_ferramentas.csv', sep=';')
                #vid.delete(0, END),
                vdesc.delete(0, END),
                vfab.delete(0, END),
                vvolt.delete(0, END),
                vtam.delete(0, END),
                vuni.delete(0, END),
                vtipo.delete(0, END),
                vmat.delete(0, END),
                vpn.delete(0, END),
                vnome.focus()

        def gerar_id():
            bd_fer = pd.read_csv(r'lista_ferramentas.csv', sep=';', index_col=0)
            lista_ids_existentes = bd_fer['id']
            id = randint(1, 100000)
            while id in lista_ids_existentes:
                id = randint(1, 100000)
            else:
                return id
#-----------------------------------------------------------------------

# ----------FUNÇÃO --- DOWNLOAD ---- SOMENTE --- TB4 ---- FUNCIONARIOS

        def download2():
            tabela_ferramentas.to_excel(r'C:\Users\Public\Downloads\tabela_ferramentas.xlsx')
            messagebox.showinfo(message='Download realizado com sucesso. Documento salvo em ' + r'C:\Users\Public\Downloads')

# ----------FUNÇÃO --- DE --- VALIDAÇÃO --- DE --- CPF ---- SOMENTE --- TB4 ---- FUNCIONARIOS

        def cpf_validate():
            entrada = vcpf.get()
            #  Obtém os números do CPF e ignora outros caracteres
            cpf = [int(char) for char in entrada if char.isdigit()]

            #  Verifica se o CPF tem 11 dígitos
            # if len(cpf) != 11:
            #     return False, 'CPF invalido'

            #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
            #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
            #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
            if cpf == cpf[::-1]:
                return False, 'CPF invalido'

                #  Valida os dois dígitos verificadores
            for i in range(9, 11):
                value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
                digit = ((value * 10) % 11) % 10
                if digit != cpf[i]:
                    return False, 'Digito verificador invalido'
            entrada = entrada.replace(" ", "")
            entrada = entrada.replace("-", "")
            entrada = entrada.replace("-", "")
            entrada = entrada.replace("/", "")
            entrada = entrada.replace(".", "")
            return entrada

        def validation():
            name = vnome.get()
            turno = vturno.get()
            equipe = vequipe.get()
            cpf = cpf_validate()
            print(cpf)
            fone = vfone.get()
            radio = vradio.get()
            msg = ''

            if len(name) == 0:
                return 'Nome não pode estar vazio'
            if len(turno) == 0:
                return 'Turno vazio'
            if len(equipe) == 0:
                return 'equipe vazio'
            if cpf == (False, 'Digito verificador invalido'):
                return 'Digito verificador do CPF invalido'
            if cpf == (False, 'CPF invalido'):
                return 'CPF invalido'
            if len(cpf) == 0:
                return 'cpf vazio'
            if len(fone) == 0 and len(radio) == 0:
                return 'Celular e radios vazios'
            else:
                try:
                    if any(ch.isdigit() for ch in name):
                        return 'Nome nao pode conter numeros'
                    if any(ch.isdigit() for ch in turno):
                        return 'Turno nao pode conter numeros'
                    # if any(ch is not int for ch in cpf):
                    #     return 'CPF nao pode conter letras'
                    # if any(ch.isdigit() for ch in fone):
                    #     return 'Fone nao pode conter letras'
                    elif len(
                            name) <= 5:  # elif len(name) <= 5 or len(name) >40: return 'O nome deve ser entre 05 a 40 caracteres'
                        return 'Nome é muito curto. O nome deve ser entre 05 a 40 caracteres'
                    elif len(name) > 40:
                        return 'Nome é muito longo. O nome deve ser entre 05 a 40 caracteres'
                    elif len(turno) <= 4:  # Podem ser as opções para escolher uma (manha, tarde, noite)
                        return 'Turno deve ser manha, tarde ou noite'
                    elif len(turno) > 5:
                        return 'Turno deve ser manha, tarde ou noite'
                    elif len(equipe) <= 1:
                        return 'Equipe é muito curto. A equipe deve ser entre 02 a 30 caracteres'
                    elif len(equipe) > 30:
                        return 'Equipe é muito longo. Equipe deve ser entre 02 a 30 caracteres'
                    elif len(cpf) != 11:
                        return 'CPF deve conter 11 caracteres. Sem traço nem ponto nem barras'
                    # TEM QUE INSERIR AQUI A FUNÇÃO DE VALIDAR DIGITOS VERIFICADORES DO CPF
                    elif len(radio) == 0 and len(fone) != 9:
                        return 'Fone deve conter 9 caracteres. Sem traço nem ponto nem barras'
                    elif len(fone) == 0 and (len(radio) != 0 and len(radio) > 8):
                        return 'Radio deve conter até 8 caracteres. Sem traço nem ponto nem barras'
                    else:
                        return 'Sucess!'
                except Exception as ep:
                    messagebox.showerror('Error', ep)
            # messagebox.showinfo('message', msg)

# ----------FUNÇÃO --- DOWNLOAD ---- SOMENTE --- TB4 ---- FUNCIONARIOS

        def download():
            tabela_funcionarios.to_excel(r'C:\Users\Public\Downloads\tabela_tecnicos.xlsx')
            messagebox.showinfo(
                message='Download realizado com sucesso. Documento salvo em ' + r'C:\Users\Public\Downloads')

#----------FUNÇÃO --- ADICIONAR ---- SOMENTE --- TB4 ---- FUNCIONARIOS

        def add_tvbd():
            if validation() != 'Sucess!':
                # or vturno.get() =='' or vequipe.get() =='' or vcpf.get() =='' or vfone.get() =='':
                messagebox.showinfo('erro', message=validation())
            else:
                treeProdutos.insert('', tk.END,
                                    values=(
                                    vnome.get(), vturno.get(), vequipe.get(), vcpf.get(), vfone.get(), vradio.get()))
                lista_add = [vnome.get(), vturno.get(), vequipe.get(), vcpf.get(), str(vfone.get()),
                             str(vradio.get())]
                # print(tabela_funcionarios)
                tabela_funcionarios.loc[len(tabela_funcionarios)] = lista_add
                # print(tabela_funcionarios)
                tabela_funcionarios.to_csv(r'lista_funcionarios.csv')
                vnome.delete(0, END),
                vturno.delete(0, END),
                vequipe.delete(0, END),
                vcpf.delete(0, END),
                vfone.delete(0, END),
                vradio.delete(0, END),
                vnome.focus()

# ----------------------------------RESERVAR TB5-----------------------------------------#

        def reservar():
            lista_idfer = tabela_ferramentas['id'].tolist()
            lista_idres = tabela_reservas['Id ferramenta'].tolist()
            if int(vidfer.get()) not in lista_idfer:
                messagebox.showinfo('erro', message='Id da ferramenta não localizado. Consulte a tabela'
                                                    'de ferramentas para verificação')
            else:
                if int(vidfer.get()) in lista_idres:
                    messagebox.showinfo('erro',
                                        message='Ferramenta já reservada. Consulte a tabela de reservas para maiores informações')
                else:
                    treeRes.insert('', tk.END,
                                   values=(gerar_idres(), vidfer.get(), vdescres.get(), vdtret.get(), vhrret.get(),vdtdev.get(),vhrdev.get(), vnmtec.get(), 'PENDENTE'))
                    lista_add = [gerar_idres(), vidfer.get(), vdescres.get(), vdtret.get(), vhrret.get(), vdtdev.get(),
                                 vhrdev.get(), vnmtec.get(), 'PENDENTE']
                    # print(tabela_ferramentas)
                    tabela_reservas.loc[len(tabela_reservas)] = lista_add
                    print(tabela_reservas)
                    tabela_reservas.to_csv(r'lista_reservas.csv', sep=';')
                    vidfer.delete(0, END),
                    vdescres.delete(0, END),
                    vdtret.delete(0, END),
                    vhrret.delete(0, END),
                    vdtdev.delete(0, END),
                    vhrdev.delete(0, END),
                    vnmtec.delete(0, END),
                    vidfer.focus()

        def gerar_idres():
            lista_ids_existentes = tabela_reservas['Id ferramenta'].tolist()
            id = randint(1, 100000)
            while id in lista_ids_existentes:
                id = randint(1, 100000)
            else:
                return id

# ----------------------------------DEVOLUÇÃO TB5-----------------------------------------#
        def devolucao():
            if not treeRes.selection():
                messagebox.showinfo(title='erro', message='Selecione o elemento a ser atualizado')
            else:
                index = treeRes.index(treeRes.selection()[0])
                # print(index)

                # Grab the record number
                selected = treeRes.focus()
                # Grab record values
                values = treeRes.item(selected, 'values')
                # (selected)
                # print(treeRes.item(selected)['values'][8])

                # outpus to entry boxes
                vidres.insert(0, values[0])
                vidfer.insert(0, values[1])
                vdescres.insert(0, values[2])
                vdtret.insert(0, values[3])
                vhrret.insert(0, values[4])
                vdtdev.insert(0, values[5])
                vhrdev.insert(0, values[6])
                vnmtec.insert(0, values[7])
                vstatus.insert(0, values[8])

                # Update record
                treeRes.item(selected, text="", values=(
                vidres.get(), vidfer.get(), vdescres.get(), vdtret.get(), vhrret.get(), vdtdev.get(),
                vhrdev.get(), vnmtec.get(), 'finalizado'))
                lista_add = [vidres.get(), vidfer.get(), vdescres.get(), vdtret.get(), vhrret.get(), vdtdev.get(),
                             vhrdev.get(), vnmtec.get(), 'finalizado']
                tabela_reservas = pd.read_csv('lista_reservas.csv', sep=';', index_col=0)
                tabela_reservas = tabela_reservas.drop([index])
                tabela_reservas = tabela_reservas.reset_index()
                tabela_reservas = tabela_reservas.drop(['index'], axis=1)
                # print(tabela_ferramentas)
                tabela_reservas.loc[len(tabela_reservas)] = lista_add
                print(tabela_reservas)
                tabela_reservas.to_csv(r'lista_reservas.csv', sep=';')
                vidfer.delete(0, END),
                vdescres.delete(0, END),
                vdtret.delete(0, END),
                vhrret.delete(0, END),
                vdtdev.delete(0, END),
                vhrdev.delete(0, END),
                vnmtec.delete(0, END),
                vidfer.focus()

# ----------FUNÇÃO --- DOWNLOAD ---- SOMENTE --- TB4 ---- FUNCIONARIOS

        def download3():
            tabela_reservas.to_excel(r'C:\Users\Public\Downloads\lista_reservas.xlsx')
            messagebox.showinfo(message='Download realizado com sucesso. Documento salvo em ' + r'C:\Users\Public\Downloads')
       
# -------------------------------------------------------------------------------------------------------#

        tb2 = Frame(my_note, width=250, height=150, bg='silver')
        my_note.add(tb2, text='Gerenciar Ferramentas')

        tb4 = Frame(my_note, bg='silver', width=250, height=150)
        my_note.add(tb4, text='Gerenciar Tecnicos')

        tb5 = Frame(my_note, bg='silver', width=250, height=150)
        my_note.add(tb5, text='Gerenciar Reservas')

# ------------------TB4 GERENCIAR TECNICOS--------------------

        lbradio_tb4 = Label(tb4, text='RADIO', anchor=W)
        vradio = Entry(tb4)
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

# ------------------ TB2 GERENCIAR FERRAMENTAS -------------------- 

        # Componente Label
        lbfab = Label(tb2, text="FABRICANTE ", font=("Times New Roman", 10), anchor=W,bg='silver')

        # Componente Combobox
        # n = tk.StringVar()
        vfab = ttk.Combobox(tb2, width=27)  # , textvariable=n
        # Adição de itens no Combobox
        vfab['values'] = ("SONY",
                            "CANON",
                            "DJI")
        vfab.current()

        # Componente Label
        lbvolt = Label(tb2, text="VOLTAGEM", font=("Times New Roman", 10), anchor=W, bg='silver')

        # Componente Combobox
        # n = tk.StringVar()
        vvolt = ttk.Combobox(tb2, width=27)  # , textvariable=n
        # Adição de itens no Combobox
        vvolt['values'] = ("127V",
                          "220V")
        vvolt.current()

        vvolt.current()

        # Componente Label
        lbuni = Label(tb2, text="UNIDADE :", font=("Times New Roman", 10), anchor=W,bg='silver')

        # Componente Combobox
        # n = tk.StringVar()
        vuni = ttk.Combobox(tb2, width=27)  # , textvariable=n
        # Adição de itens no Combobox
        vuni['values'] = ("CM",
                           "POLEGADA", "METROS")
        vuni.current()

        # Componente Combobox
        # n = tk.StringVar()
        vmat = ttk.Combobox(tb2, width=27)  # , textvariable=n
        # Adição de itens no Combobox
        vmat['values'] = ("PLASTICO",
                          "AÇO", "MADEIRA","VIDRO")
        vmat.current()

        # Componente Combobox
        # n = tk.StringVar()
        vtipo = ttk.Combobox(tb2, width=27)  # , textvariable=n
        # Adição de itens no Combobox
        vtipo['values'] = ("ELTRICO",
                          "MECANICA", "SEGURANÇA")
        vtipo.current()

        #lbid_tb2 = Label(tb2, text='ID', anchor=W)
        #vid = Entry(tb2)

    # Mostrar as letras em uppercase enquanto sao digitadas
        
        #def caps(event):
            #v.set(v.get().upper())
        
        lbdesc_tb2 = Label(tb2, text='DESCRIÇÃO', anchor=W, bg='silver')
        #v = StringVar()
        vdesc = Entry(tb2) # , textvariable=v
        #vdesc.bind("<KeyRelease>", caps)
        
        #lbfab_tb2 = Label(tb2, text='FABRICANTES', anchor=W)
        #vfab = Entry(tb2)
        #lbvolt_tb2 = Label(tb2, text='VOLTAGEM', anchor=W)
        #vvolt = Entry(tb2)
        lbtam_tb2 = Label(tb2, text='TAMANHO', anchor=W, bg='silver')
        vtam = Entry(tb2)
        #lbuni = Label(tb2, text='UNIDADE', anchor=W)
        #vuni = Entry(tb2)
        lbtipo = Label(tb2, text='TIPO', anchor=W, bg='silver')
        #vtipo = Entry(tb2)
        lbmat = Label(tb2, text='MATERIAL', anchor=W, bg='silver')
        #vmat = Entry(tb2)
        lbpn_tb2 = Label(tb2, text='PART NUMBER', anchor=W, bg='silver')
        vpn = Entry(tb2)

 # ------------------Adicionando Widgets a aba tb5 (botes, labels, etc)--------------------

        lbidfer_tb5 = Label(tb5, text='ID Ferramenta', anchor=W)
        vidfer = Entry(tb5)
        vidres = Entry(tb5)
        vstatus = Entry(tb5)
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

        # -BOTÃO FUNÇÃO ADICIONAR/RESERVAR--------------------------

        btn_adicionar_tb4 = Button(tb4, text='Cadastrar', command=add_tvbd)

        btn_adicionar_tb2 = Button(tb2, text='Cadastrar', command=add_tvbd2)

        btn_adicionar_tb5 = Button(tb5, text='Reservar', command=reservar)

        # -----------------------------------------------------------------------------------

        # ------------BOTÃO FUNÇÃO DELETAR-----------------------

        btn_excluir_tb4 = Button(tb4, text='Deletar', command=del_tvbd)

        btn_excluir_tb2 = Button(tb2, text='Deletar', command=del_tvbd2)

        # --------------------------Download --------------------------------------------------

        btn_down_tb4 = Button(tb4, text='Download', command=download)

        btn_down_tb2 = Button(tb2, text='Download', command=download2)

        btn_down_tb5 = Button(tb5, text='Download', command=download3)

        #--------------------------------DEVOLUÇÃO---------------------------------------

        btn_devol_tb5 = Button(tb5, text='Devolução', command=devolucao)

        ##-----------Adicionando o treeview na aba4 e carregando dados-------------------------


        #dadosColunas = [item for item in Bd.tabela_funcionarios.columns]
        """
        colunas = [item for item in tabela_funcionarios.columns]

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview', background='silver', foreground='black', rowheight=25,
                        fieldbackground='silver')
        style.map('Treeview', background=[('selected', 'red')])

        treeProdutos = ttk.Treeview(tb4,
                                    columns=colunas,
                                    show='headings')

        # Adding a scrollbar to Treeview widget
        ytreeScroll2 = ttk.Scrollbar(tb4)
        ytreeScroll2.configure(command=treeProdutos.yview)

        xtreeScroll2 = ttk.Scrollbar(tb4, orient='horizontal')
        xtreeScroll2.configure(command=treeProdutos.xview)

        treeProdutos.configure(yscrollcommand=ytreeScroll2.set, xscrollcommand=xtreeScroll2.set)

        xtreeScroll2.pack(side=BOTTOM, fill='x')
        ytreeScroll2.pack(side=RIGHT, fill=BOTH)

        for i in colunas:
            treeProdutos.heading(f"{i}", text=f"{i}")

        for n in tabela_funcionarios.values:
            treeProdutos.insert('', tk.END, values=list(n))

        treeProdutos.place(x=4, y=100, width=1000, height=200)

        # -----------Treeview da aba de ferramentas --------------

        dadosColunas2 = [item2 for item2 in tabela_ferramentas.columns]

        treeFer = ttk.Treeview(tb2, columns=dadosColunas2, show='headings')

        # Adding a scrollbar to Treeview widget
        ytreeScroll = ttk.Scrollbar(tb2)
        ytreeScroll.configure(command=treeFer.yview)

        xtreeScroll = ttk.Scrollbar(tb2, orient='horizontal')
        xtreeScroll.configure(command=treeFer.xview)

        treeFer.configure(yscrollcommand=ytreeScroll.set, xscrollcommand=xtreeScroll.set)

        xtreeScroll.pack(side=BOTTOM, fill='x')
        ytreeScroll.pack(side=RIGHT, fill=BOTH)

        for i2 in dadosColunas2:
            treeFer.heading(f"{i2}", text=f"{i2}")

        for n2 in tabela_ferramentas.values:
            treeFer.insert('', tk.END, values=list(n2))

        treeFer.place(x=4, y=100, width=1000, height=200)

        # ----------------------------------------------------------

        # -----------Treeview da aba de Reservas --------------

        dadosColunas3 = [item3 for item3 in tabela_reservas.columns]

        treeRes = ttk.Treeview(tb5, columns=dadosColunas3, show='headings')

        # Adding a scrollbar to Treeview widget
        ytreeScroll = ttk.Scrollbar(tb5)
        ytreeScroll.configure(command=treeRes.yview)

        xtreeScroll = ttk.Scrollbar(tb5, orient='horizontal')
        xtreeScroll.configure(command=treeRes.xview)

        treeRes.configure(yscrollcommand=ytreeScroll.set, xscrollcommand=xtreeScroll.set)

        xtreeScroll.pack(side=BOTTOM, fill='x')
        ytreeScroll.pack(side=RIGHT, fill=BOTH)

        for i3 in dadosColunas3:
            treeRes.heading(f"{i3}", text=f"{i3}")

        for n3 in tabela_reservas.values:
            #print(n3[8]) #Chegando a coluna status da tabela que e igual ao item 8 da lista n3.
            if n3[8] == 'PENDENTE':
                treeRes.insert('', tk.END, values=list(n3))

        treeRes.place(x=4, y=100, width=1000, height=200)

        # ---------------------------------------------------------
        """
 # -------------------Posicionando os elementos na aba tb2----------------------


        #lbid_tb2.place(x=10, y=10, width=80, height=20)
        #vid.place(x=10, y=30, width=80, height=20)

        btn_adicionar_tb2.place(x=10, y=300, width=80, height=20)
        btn_excluir_tb2.place(x=100, y=300, width=80, height=20)
        btn_down_tb2.place(x=190, y=300, width=80, height=20)

        lbdesc_tb2.place(x=10, y=330, width=100, height=20)
        vdesc.place(x=100, y=330, width=500, height=20)

        lbfab.place(x=10, y=360, width=100, height=20)
        vfab.place(x=100, y=360, width=70, height=20)

        lbvolt.place(x=10, y=390, width=100, height=20)
        vvolt.place(x=100, y=390, width=70, height=20)

        lbtam_tb2.place(x=10, y=420, width=70, height=20)
        vtam.place(x=100, y=420, width=70, height=20)

        lbuni.place(x=10, y=450, width=70, height=20)
        vuni.place(x=100, y=450, width=70, height=20)

        lbtipo.place(x=10, y=480, width=70, height=20)
        vtipo.place(x=100, y=480, width=70, height=20)

        lbmat.place(x=10, y=510, width=70, height=20)
        vmat.place(x=100, y=510, width=70, height=20)

        lbpn_tb2.place(x=10, y=540, width=70, height=20)
        vpn.place(x=100, y=540, width=70, height=20)

# -------------------LABEL E ENTRY DA ABA TECNICOS TB4----------------------

        lbnome_tb4.place(x=10, y=10, width=80, height=20)
        vnome.place(x=10, y=30, width=80, height=20)
        lbturno_tb4.place(x=100, y=10, width=80, height=20)
        vturno.place(x=100, y=30, width=80, height=20)
        lbequipe_tb4.place(x=190, y=10, width=70, height=20)
        vequipe.place(x=190, y=30, width=70, height=20)
        lbcpf_tb4.place(x=270, y=10, width=70, height=20)
        vcpf.place(x=270, y=30, width=70, height=20)
        lbfone_tb4.place(x=360, y=10, width=80, height=20)
        lbradio_tb4.place(x=450, y=10, width=80, height=20)
        vradio.place(x=450, y=30, width=80, height=20)
        vfone.place(x=360, y=30, width=80, height=20)
        btn_adicionar_tb4.place(x=10, y=300, width=80, height=20)
        btn_excluir_tb4.place(x=100, y=300, width=80, height=20)
        #btn_carregar_tb4.place(x=190, y=300, width=80, height=20)
        btn_down_tb4.place(x=190, y=300, width=80, height=20)

# -------------------Posicionando os elementos na aba tb5 GERENCIADOR DE RESERVAS----------------------

        btn_devol_tb5.place(x=100, y=300, width=80, height=20)
        btn_adicionar_tb5.place(x=10, y=300, width=80, height=20)
        btn_down_tb5.place(x=190, y=300, width=80, height=20)
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

        #lbl_tb2 = Label(tb2, text='Gerenciar Ferramentas')
        #lbl_tb2.place(x=350, y=70, width=200, height=20)

        lbl_tb4 = Label(tb4, text='Gerenciar Tecnicos')
        lbl_tb4.place(x=350, y=70, width=200, height=20)

        lbl_tb5 = Label(tb5, text='Gerenciar Reservas')
        lbl_tb5.place(x=350, y=70, width=200, height=20)

if __name__ == "__main__":
    root = App()
    root.mainloop()
