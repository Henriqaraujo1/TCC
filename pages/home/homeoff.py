from tkinter import *
from tkinter import ttk, Frame, PhotoImage, filedialog
from tkinter.font import Font
from tkcalendar import DateEntry
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import ImageTk, Image


class Home:
    def __init__(self, master):
        self.f = Font(family='helvetica', size=-12)
        self.s = ttk.Style()
        self.s.configure('.', font=self.f)

        # configurando fonte para formularios, imagens, e coisas padrões
        self.fp = Font(family='verdana',
                       size=-18
                       )

        # Deixando o notebook responsivo
        def toggle_font(event):
            if event.keysym == '0':
                self.f['size'] = -12
            elif event.keysym == 'plus':
                if self.f['size'] > -31:
                    self.f['size'] = self.f['size'] - 1
                elif event.keysym == 'minus':
                    if self.f['size'] < -6:
                        self.f['size'] = self.f['size'] + 1

        root.bind('<Control-plus>', toggle_font)
        root.bind('<Control-minus>', toggle_font)
        root.bind('<Control-0>', toggle_font)
        #
        self.nb = ttk.Notebook(root)
        self.nb.grid(row=1, column=0, columnspan=50, rowspan=43)
        self.nb.pack(padx=175, fill=BOTH, expand=1)

        self.frame = Frame(master)
        self.frame.pack()
        self.menu = Menu(master)
        self.menuPedido = Menu(self.menu)
        self.menuSacola = Menu(self.menu)
        self.menuPagamento = Menu(self.menu)
        self.menuCadastro = Menu(self.menu)
        self.menuFinanceiro = Menu(self.menu)
        self.menuEstoque = Menu(self.menu)
        self.menufunc = Menu(self.menu)

        self.menu.add_cascade(label="Atendimento", menu=self.menuPedido)
        self.menuPedido.add_command(label="Pedido", command=Pedido)
        self.menuPedido.add_command(label="Sacola", command=Sacola)
        self.menuPedido.add_command(label="Pagamento", command=Pagamento)

        self.menu.add_cascade(label="Cadastros", menu=self.menuCadastro)
        self.menuCadastro.add_command(label="Cadastro de Cliente", command=Cadastro)
        self.menuCadastro.add_command(label="Cadastro de Fornecedores", command=Cadastro.Cad_forn)
        self.menuCadastro.add_separator()
        self.menuCadastro.add_command(label="Consulta Clientes", command=Cadastro.ConsCli)
        self.menuCadastro.add_command(label="Consulta de Fornecedores", command=Cadastro.ConsForn)

        self.menu.add_cascade(label="Financeiro", menu=self.menuFinanceiro)
        self.menuFinanceiro.add_command(label="Controle Financeiro", command=Financeiro)

        self.menu.add_cascade(label="Almoxarifado", menu=self.menuEstoque)
        self.menuEstoque.add_command(label="Cadastro de Produto", command=Cadastro.Cad_prod)
        self.menuEstoque.add_command(label="Controle de Estoque", command=Estoque)

        self.menu.add_cascade(label="Empresa", menu=self.menufunc)
        self.menufunc.add_command(label="Cadastro Funcionarios", command=Funcs)
        self.menufunc.add_separator()
        self.menufunc.add_command(label="Consulta Funcionarios", command=Funcs.ConsFuncio)
        master.config(menu=self.menu)

        # criação das tabs com imagens

        self.img_pedido = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\pedido.png")
        self.btnpedido = Button(self.nb, image=self.img_pedido, command=Pedido).place(x=3, y=3, width=55, height=55)

        self.img_cesta = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cesta.png")
        self.btncesta = Button(self.nb, image=self.img_cesta, command=Sacola).place(x=60, y=3, width=55, height=55)

        self.img_pag = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\money.png")
        self.btnpagamento = Button(self.nb, image=self.img_pag, command=Pagamento).place(x=117, y=3, width=55,
                                                                                         height=55)

        self.img_cadastro = PhotoImage(
            file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\usuario.png")
        self.btncadastro = Button(self.nb, image=self.img_cadastro, command=Cadastro).place(x=174, y=3, width=55,
                                                                                            height=55)

        self.img_financeiro = PhotoImage(
            file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\controle.png")
        self.btnfinanceiro = Button(self.nb, image=self.img_financeiro, command=Financeiro).place(x=231, y=3, width=55,
                                                                                                  height=55)

        self.img_estoque = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\estoque.png")
        self.btnestoque = Button(self.nb, image=self.img_estoque, command=Estoque).place(x=288, y=3, width=55,
                                                                                         height=55)

        self.img_funcs = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\funcs.png")
        self.btnfuncs = Button(self.nb, image=self.img_funcs, command=Funcs).place(x=345, y=3, width=55, height=55)