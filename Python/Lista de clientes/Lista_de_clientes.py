#https://site112.com/tabela-cores-html -> Cores
#https://www.youtube.com/playlist?list=PLqx8fDb-FZDFznZcXb_u_NyiQ7Nai674- -> Tutorial (14/50)
#https://github.com/rafael-rfzorzi/Tkinter_Minhas_aulas_pt (GitHub)
#Configuração:
from tkinter import *
from tkinter import ttk
from time import sleep
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
janela = Tk()
#Relátorios(PDFs):
class Relatorios():
    def print_clientes(self):
        webbrowser.open("clientes.pdf")
    def gerar_rel(self):
        self.c = canvas.Canvas("clientes.pdf")
        self.rel_codigo = self.input_codigo.get()
        self.rel_nome = self.input_nome.get()
        self.rel_telefone = self.input_telefone.get()
        self.rel_cidade = self.input_cidade.get()
        #Tamanho e tipo de letra do título:
        self.c.setFont("Helvetica-Bold",24)
        self.c.drawString(200,790,'Ficha do Cliente')
        #Tamanho e tipo de letra do texto:
        self.c.setFont("Helvetica-Bold",18)
        self.c.drawString(50,700,'Código: ')
        self.c.drawString(50,660,'Nome: ')
        self.c.drawString(50,620,'Telefone: ')
        self.c.drawString(50,580,'Cidade: ')
        #Tamanho e tipo de letra com a informações:
        self.c.setFont("Helvetica",18)
        self.c.drawString(150,700,self.rel_codigo)
        self.c.drawString(150,660,self.rel_nome)
        self.c.drawString(150,620,self.rel_telefone)
        self.c.drawString(150,580,self.rel_cidade)
        #Criação do retangulo para espaçamento do texto:
        self.c.rect(20, 740, 550, -185, fill=False, stroke=True)
        self.c.rect(20, 530, 550, 4, fill=True, stroke=False)
        #Parte responsável por abrir a página e salvar o pdf
        self.c.showPage()
        self.c.save()
        self.print_clientes()
#BackEND
class Funcs():
    def variaveis(self):
        self.codigoF = self.input_codigo.get()
        self.nomeF = self.input_nome.get()
        self.telefoneF = self.input_telefone.get()
        self.cidadeF = self.input_cidade.get()
    #Função utilizada para o botão limpar
    def limpar_tela(self):
        self.input_codigo.delete(0, END)
        self.input_telefone.delete(0, END)
        self.input_cidade.delete(0, END)
        self.input_nome.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("Clientes.bd")
        self.cursor = self.conn.cursor()
    def desconecta_bd(self):
        self.conn.close()
    def montaTabelas(self):
        self.conecta_bd() 
        #Criação da tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conn.commit()
        self.desconecta_bd()
    def add_clientes(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO clientes (nome_cliente,telefone,cidade)
            VALUES (?, ?, ?)""", (self.nomeF,self.telefoneF,self.cidadeF))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_tela()
    def select_lista(self):
        self.lista.delete(*self.lista.get_children())
        self.conecta_bd()
        X = self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes
        ORDER BY nome_cliente ASC; """)
        for i in X:
            self.lista.insert("", END, values=i)
        self.desconecta_bd()
    def duploclick(self, event):
        self.limpar_tela()
        self.lista.selection()
        for n in self.lista.selection():
            coluna1,coluna2,coluna3,coluna4 = self.lista.item(n, "values")
            self.input_codigo.insert(END, coluna1)
            self.input_nome.insert(END, coluna2)
            self.input_telefone.insert(END, coluna3)
            self.input_cidade.insert(END, coluna4)
    #Função responsável pela utilização do botão "Apagar":
    def deletar_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM clientes WHERE cod = ? """, (self.codigoF))
        self.conn.commit()
        self.desconecta_bd()
        self.limpar_tela()
        self.select_lista()
    #Função responsável pela utilização do botão "Alterar":
    def alterar_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
        WHERE cod = ? """, (self.nomeF, self.telefoneF,self.cidadeF,self.codigoF))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_tela()
    #Função responsável pela utilização do botão "Buscar":
    def buscar_cliente(self):
        self.conecta_bd()
        self.lista.delete(*self.lista.get_children())
        self.input_nome.insert(END, '%')
        nomeB = self.input_nome.get()
        self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
        WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC """ % nomeB)
        buscanome = self.cursor.fetchall()
        for i in buscanome:
            self.lista.insert("",END, values=i)
        self.limpar_tela()
        self.desconecta_bd()
#FrontEND
class aplicativo(Funcs,Relatorios):
    #Função responsável por iniciar a janela
    def __init__(self):
        self.janela = janela
        self.config_tela()
        self.tela()
        self.coisas_Retangulo1()
        self.coisas_Retangulo2()
        self.montaTabelas()
        self.select_lista()
        self.menus()
        janela.mainloop()
    #Função responsável pela configuração da janela
    def config_tela(self):
        self.janela.title("Cadastro do usuário")
        self.janela.geometry("700x520")
        self.janela.configure(background="#4682B4")
        self.janela.resizable(False, False)
        self.janela.maxsize(width=900, height=700)
        self.janela.minsize(width=500, height=400)
    #Função responsável pelos retangulos que são exibidos na tela
    def tela(self):
        self.Retangulo_princ = Frame(
            self.janela, bd=4, bg="#D3D3D3",
            highlightbackground="Black",highlightthickness=3)
        self.Retangulo_princ.place(relx=0.16, rely=0.03,relwidth=0.7, relheight=0.46)
        self.Retangulo_sec = Frame(
            self.janela, bd=4, bg="#D3D3D3",
            highlightbackground="Black",highlightthickness=3)
        self.Retangulo_sec.place(relx=0.16, rely=0.51,relwidth=0.7, relheight=0.46)
    #Função responsável pela criação das coisas no retangulo 1
    def coisas_Retangulo1(self):
    #Botão buscar:    
        self.botao_buscar = Button(self.Retangulo_princ, text="Buscar",bd=2, bg= "#4682B4", fg="White",font=("Calibri",10,"bold"),command=self.buscar_cliente)
        self.botao_buscar.place(relx=0.28, rely=0.09, relheight=0.16, relwidth=0.12)
    #Botão novo:    
        self.botao_novo = Button(self.Retangulo_princ, text="Novo",bd=2, bg="#4682B4", fg="White",font=("Calibri",10,"bold"),command=self.add_clientes)
        self.botao_novo.place(relx=0.54, rely=0.09, relheight=0.16, relwidth=0.12)
    #Botão alterar:    
        self.botao_alterar = Button(self.Retangulo_princ, text="Alterar",bd=2, bg="#4682B4", fg="White",font=("Calibri",10,"bold"),command=self.alterar_cliente)
        self.botao_alterar.place(relx=0.67, rely=0.09, relheight=0.16, relwidth=0.12)
    #Botão apagar:    
        self.botao_apagar = Button(self.Retangulo_princ, text="Apagar",bd=2, bg="Red", fg="White",font=("Calibri",10,"bold"), command=self.deletar_cliente)
        self.botao_apagar.place(relx=0.8, rely=0.09, relheight=0.16, relwidth=0.12)
    #Botão limpar:
        self.botao_limpar = Button(self.Retangulo_princ, text="Limpar",bd=2, bg="#4682B4", fg="White",font=("Calibri",10,"bold"),command=self.limpar_tela)
        self.botao_limpar.place(relx=0.8, rely=0.77, relheight=0.16, relwidth=0.12)
    #Criação da caixa de texto e o input(Código):
        self.codigo = Label(self.Retangulo_princ, text="Código", bg="#D3D3D3", fg="#4682B4",font=("Calibri",11))
        self.codigo.place(relx=0.08, rely=0.05)
        self.input_codigo = Entry(self.Retangulo_princ,font=("Calibri",11), highlightbackground="Black", highlightthickness=1)
        self.input_codigo.place(relx=0.085, rely=0.16, relwidth=0.13)
    #Criação da caixa de texto e o input(Telefone):
        self.telefone = Label(self.Retangulo_princ, text="Telefone", bg="#D3D3D3", fg="#4682B4",font=("Calibri",11))
        self.telefone.place(relx=0.08, rely=0.27)
        self.input_telefone = Entry(self.Retangulo_princ,font=("Calibri",11), highlightbackground="Black", highlightthickness=1)
        self.input_telefone.place(relx=0.085, rely=0.38, relwidth=0.28)
    #Criação da caixa de texto e o input(Cidade):
        self.cidade = Label(self.Retangulo_princ, text="Cidade", bg="#D3D3D3", fg="#4682B4",font=("Calibri",11))
        self.cidade.place(relx=0.08, rely=0.49) 
        self.input_cidade = Entry(self.Retangulo_princ,font=("Calibri",11), highlightbackground="Black", highlightthickness=1)
        self.input_cidade.place(relx=0.085, rely=0.60, relwidth=0.42)
    #Criação da caixa de texto e o input(Nome):
        self.nome = Label(self.Retangulo_princ, text="Nome", bg="#D3D3D3", fg="#4682B4",font=("Calibri",11))
        self.nome.place(relx=0.08, rely=0.71) 
        self.input_nome = Entry(self.Retangulo_princ,font=("Calibri",11), highlightbackground="Black", highlightthickness=1)
        self.input_nome.place(relx=0.085, rely=0.82, relwidth=0.57)
    #Função responsável pela criação das coisas no retangulo 2:
    def coisas_Retangulo2(self):
        self.lista = ttk.Treeview(self.Retangulo_sec, height=3, columns=("coluna1","coluna2","coluna3","coluna4",))
    #Texto principal:
        self.lista.heading("#0", text="")
        self.lista.heading("#1", text="Código")
        self.lista.heading("#2", text="Nome")
        self.lista.heading("#3", text="Telefone")
        self.lista.heading("#4", text="Cidade")
    #Tamanho das colunas:
        self.lista.column("#0", width=1, stretch=NO)
        self.lista.column("#1", width=47)
        self.lista.column("#2", width=180)
        self.lista.column("#3", width=105)
        self.lista.column("#4", width=110)
        self.lista.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.9)
    #Barra de rolagem:
        self.Scroollista = Scrollbar(self.Retangulo_sec, orient="vertical")
        self.lista.configure(yscroll=self.Scroollista.set)
        self.Scroollista.place(relx=0.963,rely=0.10, relwidth=0.03, relheight=0.8)
    #Função duplo click:
        self.lista.bind("<Double-1>", self.duploclick)
    #Criação de menus:
    def menus(self):
        barra_menu = Menu(self.janela)
        self.janela.config(menu=barra_menu)
        menu1 = Menu(barra_menu)
        menu2 = Menu(barra_menu)
        def Quit(): janela.destroy()
        barra_menu.add_cascade(label ="Opções",menu= menu1)
        barra_menu.add_cascade(label = "Sobre",menu= menu2)
        menu1.add_command(label="Relatório",command=self.gerar_rel)
        menu1.add_command(label="Limpar Tela",command=self.limpar_tela)
        menu1.add_command(label="Sair",command=Quit)
        

print("\n------ ⌛ Conectando ao banco de dados ⌛ ------\n")
sleep(1)
print("------ ✔️  Banco de dados conectado ✔️  ------\n")
aplicativo()
print("------ 🔌 Banco de dados desconectado 🔌 ------\n")