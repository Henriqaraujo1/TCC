from tkinter import *
from tkinter import ttk, Frame, PhotoImage, Tk
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
        self.menuCadastro.add_command(label="Cadastro de Cliente", command=Cadastro.CadCli)
        self.menuCadastro.add_command(label="Cadastro de Fornecedores", command=Cadastro.CadForn)
        self.menuCadastro.add_separator()
        self.menuCadastro.add_command(label="Consulta Clientes", command=Cadastro.ConsCli)
        self.menuCadastro.add_command(label="Consulta de Fornecedores", command=Cadastro.ConsForn)

        self.menu.add_cascade(label="Financeiro", menu=self.menuFinanceiro)
        self.menuFinanceiro.add_command(label="Controle Financeiro", command=Financeiro)

        self.menu.add_cascade(label="Almoxarifado", menu=self.menuEstoque)
        self.menuEstoque.add_command(label="Cadastro de Produto", command=Cadastro.CadProd)
        self.menuEstoque.add_command(label="Controle de Estoque", command=Estoque)

        self.menu.add_cascade(label="Empresa", menu=self.menufunc)
        self.menufunc.add_command(label="Cadastro Funcionarios", command=Funcs)
        self.menufunc.add_separator()
        self.menufunc.add_command(label="Consulta Funcionarios", command=Cadastro.ConsFuncio)
        master.config(menu=self.menu)

        # criação das tabs com imagens

        self.img_pedido = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\pedido.png")
        btnpedido = Button(self.nb, image=self.img_pedido, command=Pedido)
        btnpedido.place(x=3, y=3, width=55, height=55)

        self.img_cesta = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cesta.png")
        btncesta = Button(self.nb, image=self.img_cesta, command=Sacola)
        btncesta.place(x=60, y=3, width=55, height=55)

        self.img_pag = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\money.png")
        btnpagamento = Button(self.nb, image=self.img_pag, command=Pagamento)
        btnpagamento.place(x=117, y=3, width=55, height=55)

        self.img_cad_cli = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\usuario.png")
        btncad_cli = Button(self.nb, image=self.img_cad_cli, command=Cadastro.CadCli)
        btncad_cli.place(x=174, y=3, width=55, height=55)

        self.img_financeiro = PhotoImage(
            file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\controle.png")
        btnfinanceiro = Button(self.nb, image=self.img_financeiro, command=Financeiro)
        btnfinanceiro.place(x=231, y=3, width=55, height=55)

        self.img_estoque = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\estoque.png")
        btnestoque = Button(self.nb, image=self.img_estoque, command=Estoque)
        btnestoque.place(x=288, y=3, width=55, height=55)

        self.img_funcs = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\funcs.png")
        btnfuncs = Button(self.nb, image=self.img_funcs, command=Funcs)
        btnfuncs.place(x=345, y=3, width=55, height=55)


# Definiçao das paginas por classes, por enquanto é a melhor forma de organizar o codigo
class Pedido:
    def __init__(self):

        self.f = None

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

        'Definindo tamanho da tela, titulo da janela, icone e o titulo dentro da janela'
        self.winpedido = Toplevel(root)
        self.winpedido.title("Pedido")
        self.winpedido.geometry("700x500")
        self.winpedido.resizable(0, 0)
        Label(self.winpedido, text="Pedido", font=f).pack()
        self.winpedido.iconbitmap("d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico")

        # Formulario da aba Pedido

        # Nome do atendente
        self.lbatend = Label(self.winpedido, text="Atendente", font=fp)
        self.lbatend.place(x=10, y=25)
        self.container5 = Frame(self.winpedido)
        self.container5.place(x=110, y=30, width=120)
        self.txtatend = Entry(self.container5)
        self.txtatend.pack()

        # Data
        self.imgdata = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\data.png")
        self.teste = Label(self.winpedido, image=self.imgdata)
        self.teste.place(x=80, y=53)
        self.hora = DateEntry(self.winpedido, width=12, background='darkblue',
                              foreground='white', borderwidth=2)
        self.hora.place(x=110, y=57, width=120)

        lbcomanda = Label(self.winpedido, text='Comanda', font=fp)
        lbcomanda.place(x=100, y=120)
        container00 = Frame(self.winpedido)
        container00.place(x=280, y=120)
        txtcomanda = Entry(container00)
        txtcomanda.pack()

        # Número do Pedido
        self.lbpedido = Label(self.winpedido, text="Nº Pedido", font=fp)
        self.lbpedido.place(x=100, y=150)
        self.container0 = Frame(self.winpedido)
        self.container0.place(x=280, y=150)
        txtpedido = Entry(self.container0)
        txtpedido.pack()

        # imagem de pesquisa
        self.img_pesq = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\pesquisa.png")

        # Cliente
        self.lbcliente = Label(self.winpedido, text="Cliente", font=fp)
        self.lbcliente.place(x=100, y=180)
        self.btncliente = Button(self.winpedido, image=self.img_pesq, command=Cadastro.ConsCli)
        self.btncliente.place(x=410, y=175)
        container1 = Frame(self.winpedido)
        container1.place(x=280, y=180)
        txtcliente = Entry(container1)
        txtcliente.pack()

        # Sabor da Pizza
        self.lbsabor1 = Label(self.winpedido, text="Primeiro Sabor", font=fp)
        self.lbsabor1.place(x=100, y=210)
        self.container2 = Frame(self.winpedido)
        self.container2.place(x=280, y=210)
        btnsabor1 = Button(self.winpedido, image=self.img_pesq, command=Lupa)
        btnsabor1.place(x=410, y=205)
        txtsabor1 = Entry(self.container2)
        txtsabor1.pack()

        # segundo Sabor da pizza
        self.lbsabor2 = Label(self.winpedido, text="Segundo Sabor", font=fp)
        self.lbsabor2.place(x=100, y=240)

        container3 = Frame(self.winpedido)
        container3.place(x=280, y=240)
        self.btnsabor2 = Button(self.winpedido, image=self.img_pesq, command=Lupa)
        self.btnsabor2.place(x=410, y=235)
        txtsabor2 = Entry(container3)
        txtsabor2.pack()

        # Borda
        self.lbborda = Label(self.winpedido, text="Borda", font=fp)
        self.lbborda.place(x=100, y=270)

        self.OPTIONS = [
            "Sem borda Recheada",
            "Calabresa",
            "Catupiry",
            "Cheddar"
        ]  # etc

        self.variable = StringVar(root)
        self.variable.set(self.OPTIONS[0])  # default value

        self.w = OptionMenu(self.winpedido, self.variable, *self.OPTIONS)
        # self.w.config(bg="GREEN")
        self.w.place(x=280, y=265)

        # Tamanho
        self.lbtamanho = Label(self.winpedido, text="Tamanho", font=fp)
        self.lbtamanho.place(x=100, y=300)

        self.grande = "Grande"
        Checkbutton(self.winpedido, text="Grande", variable=self.grande).place(x=280, y=300)
        self.media = "Media"
        Checkbutton(self.winpedido, text="Media", variable=self.media).place(x=380, y=300)
        self.pequena = "Pequena"
        Checkbutton(self.winpedido, text="Pequena", variable=self.pequena).place(x=480, y=300)

        # Bebida
        self.lbbebida = Label(self.winpedido, text="Bebida", font=fp)
        self.lbbebida.place(x=100, y=330)

        self.container6 = Frame(self.winpedido)
        self.container6.place(x=280, y=330)
        self.btnbebida = Button(self.winpedido, image=self.img_pesq, command=Lupa)
        self.btnbebida.place(x=410, y=325)
        self.txtbebida = Entry(self.container6).pack()

        # Sobremesa
        self.lbsobremesa = Label(self.winpedido, text="Sobremesa", font=fp)
        self.lbsobremesa.place(x=100, y=360)

        self.container7 = Frame(self.winpedido)
        self.container7.place(x=280, y=360)
        self.btnsobremesa = Button(self.winpedido, image=self.img_pesq, command=Lupa)
        self.btnsobremesa.place(x=410, y=355)
        self.txtsobremesa = Entry(self.container7).pack()

        # Vericação de mesas
        self.lbmesas = Label(self.winpedido, text="Mesas", font=fp)
        self.lbmesas.place(x=100, y=390)
        self.container8 = Frame(self.winpedido)
        self.container8.place(x=280, y=393)
        self.txtmesas = Entry(self.container8).pack()
        self.winpedido.mesas = Button(self.winpedido, text='Verificar mesas', command=Mesa)
        self.winpedido.mesas.place(x=410, y=390)

        # Finalização do pedido
        Button(self.winpedido, text="Finalizar Pedido").place(x=300, y=450, height=30, width=90)
        Button(self.winpedido, text="Cancelar Pedido").place(x=395, y=450, height=30, width=90)

        # adição de pedido
        Button(self.winpedido, text="Adicionar item").place(x=180, y=450, height=30, width=90)


class Lupa:
    def __init__(self):

        self.f = Font(family='helvetica', size=-20)
        self.s = ttk.Style()
        self.s.configure('.', font=f)

        self.winlupa = Toplevel(root)
        self.winlupa.title("Cardapio")
        self.winlupa.geometry("500x450")
        self.winlupa.resizable(0, 0)
        self.winlupa.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
        Label(self.winlupa, text="Cardapio", font=f).pack()

        def toggle_font(event):
            if event.keysym == '0':
                self.f['size'] = -12
            elif event.keysym == 'plus':
                if self.f['size'] > -31:
                    self.f['size'] = self.f['size'] - 1
                elif event.keysym == 'minus':
                    if self.f['size'] < -6:
                        self.f['size'] = self.f['size'] + 1

        self.winlupa.bind('<Control-plus>', toggle_font)
        self.winlupa.bind('<Control-minus>', toggle_font)
        self.winlupa.bind('<Control-0>', toggle_font)

        cod = Label(self.winlupa, text="Codigo", font=fp)
        cod.place(x=50, y=50)
        container0 = Frame(self.winlupa)
        container0.place(x=120, y=58, width=50)
        txtcod = Entry(container0)
        txtcod.pack()

        desc = Label(self.winlupa, text="Item", font=fp)
        desc.place(x=185, y=50)
        container1 = Frame(self.winlupa)
        container1.place(x=285, y=58)
        txtdesc = Entry(container1)
        txtdesc.pack()

        display_desc = ttk.Treeview(self.winlupa, columns=('Cod', 'Item', 'Descrição'))
        display_desc.place(x=50, y=100, width=400, height=300)
        scroll_y = Scrollbar(self.winlupa, orient="vertical", command=display_desc.yview)
        scroll_y.place(x=450, y=100, height=300)
        scroll_x = Scrollbar(self.winlupa, orient="horizontal", command=display_desc.xview)
        scroll_x.place(x=50, y=400, width=400)

        display_desc.config(yscrollcommand=scroll_y.set)
        display_desc.config(xscrollcommand=scroll_x.set)

        display_desc.heading('#0', text='Codigo')
        display_desc.column('#0', minwidth=0, width=70)
        display_desc.heading('#1', text='Item')
        display_desc.column('#1', minwidth=0, width=90)
        display_desc.heading('#2', text='Descrição')
        display_desc.column('#2', minwidth=40, width=250)

        self.img_check = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\check1.png")
        self.btn_search = Button(self.winlupa, image=self.img_check)
        self.btn_search.place(x=430, y=45)

        self.btn_include = Button(self.winlupa, text="Incluir").place(x=50, y=420)


class Mesa:
    def __init__(self):
        self.fp = Font(family='verdana', size=-18)

        self.m = Font(family="verdana", size=-14)

        self.f = Font(family='helvetica', size=-20)
        self.s = ttk.Style()
        self.s.configure('.', font=self.f)

        self.winmesa = Toplevel(root)
        self.winmesa.title("Mesas")
        self.winmesa.geometry("500x470")
        Label(self.winmesa, text='Mesas', font=self.f)

        def toggle_font(event):
            if event.keysym == '0':
                self.f['size'] = -12
            elif event.keysym == 'plus':
                if self.f['size'] > -31:
                    self.f['size'] = self.f['size'] - 1
                elif event.keysym == 'minus':
                    if self.f['size'] < -6:
                        self.f['size'] = self.f['size'] + 1

        self.winmesa.bind('<Control-plus>', toggle_font)
        self.winmesa.bind('<Control-minus>', toggle_font)
        self.winmesa.bind('<Control-0>', toggle_font)

        self.displayMesas = LabelFrame(self.winmesa, width=460, height=350)
        self.displayMesas.place(x=20, y=65)

        def change_status():
            img_verde = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\mesaVerde.png")
            self.displayMesas.configure(image=img_verde)
            self.displayMesas.image = img_verde

        btn_refresh = Button(self.winmesa, text="Atualizar")
        btn_refresh.place(x=350, y=420)

        Button(self.winmesa, text="Livre", font=self.m, bg='#2FEBA0', fg='black', command=change_status).place(x=187,
                                                                                                               y=15)
        Button(self.winmesa, text="Ocupada", font=self.m, bg='#EB4E3D', fg='black').place(x=237, y=15)
        Button(self.winmesa, text="Limpeza", font=self.m, bg='#45D4FF', fg='black').place(x=315, y=15)
        Button(self.winmesa, text="Reserva", font=self.m, bg='#EBE93D', fg='black').place(x=390, y=15)

        self.img_mesas = "d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\mesa.png"
        self.open_img = Image.open(self.img_mesas)

        self.img1 = ImageTk.PhotoImage(self.open_img)
        self.in_frame = Label(self.displayMesas, image=self.img1)
        self.in_frame.place(x=50)


# Pagina da sacola
class Sacola:
    def __init__(self):

        """Definindo a fonte de titulo da pagina"""
        # f = Font(family='helvetica', size=-25)
        # s = ttk.Style()
        # s.configure('.', font=f)

        """Atualmente essa parte do codigo faz com que as imagens, botoes possam aparecer
        dentro da pagina, então usar em toda criação de pagina"""

        def toggle_font(event):
            if event.keysym == '0':
                f['size'] = -12
            elif event.keysym == 'plus':
                if f['size'] > -31:
                    f['size'] = f['size'] - 1
                elif event.keysym == 'minus':
                    if f['size'] < -6:
                        f['size'] = f['size'] + 1

        root.bind('<Control-plus>', toggle_font)
        root.bind('<Control-minus>', toggle_font)
        root.bind('<Control-0>', toggle_font)

        winsacola = Toplevel(root)
        winsacola.title("Sacola")
        winsacola.geometry("840x520")
        winsacola.resizable(0, 0)
        winsacola.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
        Label(winsacola, text="Sacola", font=f).pack(side=TOP)

        display_sacola = ttk.Treeview(winsacola, height=15, columns=('id_pedido',
                                                                     'comanda',
                                                                     'nome_pedido',
                                                                     'valor_unitario',
                                                                     'Valor_total',
                                                                     'Cliente',
                                                                     'Atendente'))

        display_sacola.place(x=20, y=150, width=800, height=350)
        scroll_y = Scrollbar(winsacola, orient="vertical", command=display_sacola.yview)
        scroll_y.place(x=820, y=150, height=350)
        scroll_x = Scrollbar(winsacola, orient="horizontal", command=display_sacola.xview)
        scroll_x.place(x=20, y=500, width=800)

        display_sacola.configure(yscrollcommand=scroll_y.set)
        display_sacola.configure(xscrollcommand=scroll_x.set)

        display_sacola.heading('#0', text='Cod Pedido')
        display_sacola.column('#0', minwidth=0, width=75)
        display_sacola.heading('#1', text='Comanda')
        display_sacola.column('#1', minwidth=0, width=60)
        display_sacola.heading('#2', text='Descrição')
        display_sacola.column('#2', minwidth=0, width=200)
        display_sacola.heading('#3', text='Preço Unitario')
        display_sacola.column('#3', minwidth=0, width=80)
        display_sacola.heading('#4', text='Preço Total')
        display_sacola.column('#4', minwidth=0, width=80)
        display_sacola.heading('#5', text='Cliente')
        display_sacola.column('#5', minwidth=0, width=90)
        display_sacola.heading('#6', text='Atendente')
        display_sacola.column('#6', minwidth=0, width=90)

        lbpedido = Label(winsacola, text='Cod Pedido', font=fp)
        lbpedido.place(x=100, y=50)
        sac_container0 = Frame(winsacola)
        sac_container0.place(x=210, y=55)
        txtpedido_sac = Entry(sac_container0)
        txtpedido_sac.pack()

        lbcomanda_ped = Label(winsacola, text='Comanda', font=fp)
        lbcomanda_ped.place(x=375, y=50)
        sac_container1 = Frame(winsacola)
        sac_container1.place(x=470, y=55)
        txtcomanda_sac = Entry(sac_container1)
        txtcomanda_sac.pack()

        btnsearch_ped = Button(winsacola, text='Procurar')
        btnsearch_ped.place(x=400, y=120)


class Pagamento:
    def __init__(self):
        self.f = Font(family='helvetica', size=-25)
        self.s = ttk.Style()
        self.s.configure('.', font=self.f)

        """Atualmente essa parte do codigo faz com que as imagens, botoes possam aparecer
        dentro da pagina, então usar em toda criação de pagina"""

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

        self.fp = Font(family='verdana',
                       size=-18
                       )

        fp1 = Font(family='verdana',
                   size=20
                   )

        self.winpagamento = Toplevel(root)
        self.winpagamento.title("Pagamento")
        self.winpagamento.geometry("600x500")
        self.winpagamento.resizable(0, 0)
        self.winpagamento.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
        Label(self.winpagamento, text="Pagamento", font=self.f).place(x=250)
        # self.winpagamento.resizable(0, 0)

        # Tela pagamentos (contairnes, texto, imagens)
        self.lbcomanda_pg = Label(self.winpagamento, text="Comanda", font=self.fp)
        self.lbcomanda_pg.place(x=70, y=70)
        self.container00 = Frame(self.winpagamento)
        self.container00.place(x=250, y=75)
        self.txtcomanda_pg = Entry(self.container00).pack()

        # Verificação do numero do pedido (Pode digitar)
        self.lbpedido_pg = Label(self.winpagamento, text="Nº do Pedido", font=self.fp)
        self.lbpedido_pg.place(x=70, y=100)
        self.container0 = Frame(self.winpagamento)
        self.container0.place(x=250, y=105)
        self.txtpedido_pg = Entry(self.container0).pack()

        # Abrir a tela da sacola para confirmar o pedido
        self.imgcesta_pg = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cesta.png")
        self.btnsacola_pg = Button(self.winpagamento, text="Abrir pedido", command=Sacola)
        self.btnsacola_pg.place(x=390, y=100)
        # Verificação nome cliente (não pode digitar)
        self.lbcliente_pg = Label(self.winpagamento, text="Cliente", font=self.fp)
        self.lbcliente_pg.place(x=70, y=135)
        self.container1 = Frame(self.winpagamento)
        self.container1.place(x=250, y=135)
        self.txtcliente_pg = Entry(self.container1).pack()

        # Verificação do Número da mesa (Pode Digitar)
        self.lbmesa_pg = Label(self.winpagamento, text="Nº Mesa", font=self.fp)
        self.lbmesa_pg.place(x=70, y=170)
        self.container2 = Frame(self.winpagamento)
        self.container2.place(x=250, y=170)
        self.txtmesa_pg = Entry(self.container2).pack()

        # opções de descontos(Pode digitar)
        self.lbdesconto_pg = Label(self.winpagamento, text="Valor do desconto", font=self.fp)
        self.lbdesconto_pg.place(x=70, y=205)
        self.container3 = Frame(self.winpagamento)
        self.container3.place(x=250, y=205)
        self.txtdesconto_pg = Entry(self.container3).pack()

        # Total do pedido
        self.lbtotal_pg = Label(self.winpagamento, text="Total do pedido", font=self.fp)
        self.lbtotal_pg.place(x=70, y=295)
        self.container4 = Frame(self.winpagamento)
        self.container4.place(x=230, y=295)

        self.txttotal_pg = Entry(self.container4, width=8, bg='blue', fg='#FF0000', font=fp1).pack()

        # opções de pagamentos Dinheiro ,Cartão de credito e debito
        self.lbdinheiro = Label(self.winpagamento, text="Forma de Pagamento", font=self.fp, anchor=W)
        self.lbdinheiro.place(x=70, y=245)

        self.dinheiro = "Dinheiro"
        self.cartaocd = "Crédito"
        self.cartaodb = "Debito"

        self.OPTIONS = [
            self.dinheiro,
            self.cartaodb,
            self.cartaodb,
        ]  # etc

        self.variable = StringVar(root)
        self.variable.set(self.OPTIONS[0])  # default value

        self.w = OptionMenu(self.winpagamento, self.variable, *self.OPTIONS)
        self.w.place(x=300, y=245)
        # Calcular troco(Pode digitar)
        self.lbtroco_pg = Label(self.winpagamento, text="Troco", font=self.fp)
        self.lbtroco_pg.place(x=345, y=455)
        self.container5 = Frame(self.winpagamento)
        self.container5.place(x=400, y=450)
        self.txttroco_pg = Entry(self.container5, width=8, bg='blue', fg='#FF0000', font=fp1).pack()

        lbpagamento = Label(self.winpagamento, text='Dinheiro', font=self.fp)
        lbpagamento.place(x=70, y=350)
        pg_container_6 = Frame(self.winpagamento)
        pg_container_6.place(x=230, y=350)
        txtdinheiro_pg = Entry(pg_container_6, width=8, bg='blue', fg='#FF0000', font=fp1)
        txtdinheiro_pg.pack()


class Cadastro:
    class CadCli:
        def __init__(self):
            """Atualmente essa parte do codigo faz com que as imagens, botoes possam aparecer
            dentro da pagina, então usar em toda criação de pagina"""

            self.f = None

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

            wincadastro = Toplevel(root)
            wincadastro.title("Cadastro de Cliente")
            wincadastro.geometry("400x400")
            wincadastro.resizable(0, 0)
            wincadastro.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
            Label(wincadastro, text="Cadastro de Cliente", font=fp).pack(side=TOP)

            lbcodigo_cli = Label(wincadastro, text="Celular", font=fp)
            lbcodigo_cli.place(x=80, y=90)
            container00 = Frame(wincadastro)
            container00.place(x=220, y=95)
            txtcodigo_cli = Entry(container00)
            txtcodigo_cli.pack()

            lbnome_cli = Label(wincadastro, text='Nome', font=fp)
            lbnome_cli.place(x=80, y=120)
            container0 = Frame(wincadastro)
            container0.place(x=220, y=125)
            txtnome_cli = Entry(container0)
            txtnome_cli.pack()

            lbsobrenome_cli = Label(wincadastro, text='Sobrenome', font=fp)
            lbsobrenome_cli.place(x=80, y=150)
            container1 = Frame(wincadastro)
            container1.place(x=220, y=155)
            txtsobrenome_cli = Entry(container1)
            txtsobrenome_cli.pack()

            lbcelular_cli = Label(wincadastro, text='CEP', font=fp)
            lbcelular_cli.place(x=80, y=180)
            container2 = Frame(wincadastro)
            container2.place(x=220, y=185)
            txtcelular_cli = Entry(container2)
            txtcelular_cli.pack()

            lbcep_cli = Label(wincadastro, text='Rua', font=fp)
            lbcep_cli.place(x=80, y=210)
            container3 = Frame(wincadastro)
            container3.place(x=220, y=215)
            txtcep_cli = Entry(container3)
            txtcep_cli.pack()

            lbrua_cli = Label(wincadastro, text='Nº Casa', font=fp)
            lbrua_cli.place(x=80, y=240)
            container4 = Frame(wincadastro)
            container4.place(x=220, y=245)
            txtrua_cli = Entry(container4)
            txtrua_cli.pack()

            lbnumero_cli = Label(wincadastro, text='Bairro', font=fp)
            lbnumero_cli.place(x=80, y=270)
            container5 = Frame(wincadastro)
            container5.place(x=220, y=275)
            txtnumero_cli = Entry(container5)
            txtnumero_cli.pack()

            lbcomplemento_cli = Label(wincadastro, text='Referencia', font=fp)
            lbcomplemento_cli.place(x=80, y=300)
            container6 = Frame(wincadastro)
            container6.place(x=220, y=305)
            txtnumero_cli = Entry(container6)
            txtnumero_cli.pack()

            self.img_salvar_cli = PhotoImage(
                file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\check1.png")
            btnsalvar_cli = Button(wincadastro, image=self.img_salvar_cli)
            btnsalvar_cli.place(x=300, y=355, width=40)

            btnapagar_cli = Button(wincadastro, text="Limpar campos")
            btnapagar_cli.place(x=150, y=360, width=110)

            self.img_consulta_cli = PhotoImage(
                file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\consulta.png")
            btnconsulta_cli = Button(wincadastro, image=self.img_consulta_cli, command=Cadastro.ConsCli)
            btnconsulta_cli.place(x=300, y=30, width=45, height=45)

    class CadForn:
        def __init__(self):
            """Definindo a fonte de titulo da pagina"""
            self.f = Font(family='helvetica', size=-20)
            self.s = ttk.Style()
            self.s.configure('.', font=self.f)

            """Atualmente essa parte do codigo faz com que as imagens, botoes possam aparecer
            dentro da pagina, então usar em toda criação de pagina"""

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

            """Definindo a fonte dos campos"""
            self.fp = Font(family='verdana',
                           size=-18)

            self.wincad_forn = Toplevel(root)
            self.wincad_forn.title("Cadastro de Fornecedores")
            self.wincad_forn.geometry("500x400")
            self.wincad_forn.resizable(0, 0)
            Label(self.wincad_forn, text="Cadastro de Fornecedores", font=self.f).pack()
            self.wincad_forn.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')

            self.lbcnpj = Label(self.wincad_forn, text="CNPJ", font=self.fp)
            self.lbcnpj.place(x=100, y=100)
            self.container00 = Frame(self.wincad_forn)
            self.container00.place(x=210, y=105)
            self.txtcnpj = Entry(self.container00).pack()

            self.lbnome_forn = Label(self.wincad_forn, text='Nome', font=self.fp)
            self.lbnome_forn.place(x=100, y=130)
            self.container0 = Frame(self.wincad_forn)
            self.container0.place(x=210, y=135)
            self.txtnome_forn = Entry(self.container0).pack()

            self.lbcelular_forn = Label(self.wincad_forn, text='Celular', font=self.fp)
            self.lbcelular_forn.place(x=100, y=160)
            self.container2 = Frame(self.wincad_forn)
            self.container2.place(x=210, y=165)
            self.txtcelular_forn = Entry(self.container2).pack()

            self.lbcep_forn = Label(self.wincad_forn, text='CEP', font=self.fp)
            self.lbcep_forn.place(x=100, y=190)
            self.container3 = Frame(self.wincad_forn)
            self.container3.place(x=210, y=195)
            self.txtcep_forn = Entry(self.container3).pack()

            self.lbrua_forn = Label(self.wincad_forn, text='Rua', font=self.fp)
            self.lbrua_forn.place(x=100, y=220)
            self.container4 = Frame(self.wincad_forn)
            self.container4.place(x=210, y=225)
            self.txtrua_forn = Entry(self.container4).pack()

            self.lbnumero_forn = Label(self.wincad_forn, text='Nº', font=self.fp)
            self.lbnumero_forn.place(x=100, y=250)
            self.container5 = Frame(self.wincad_forn)
            self.container5.place(x=210, y=255)
            self.txtnumero_forn = Entry(self.container5).pack()

            self.lbbairro_forn = Label(self.wincad_forn, text='Bairro', font=self.fp)
            self.lbbairro_forn.place(x=100, y=280)
            self.container6 = Frame(self.wincad_forn)
            self.container6.place(x=210, y=285)
            self.txtbairro_forn = Entry(self.container6).pack()

            btnsalvar_forn = Button(self.wincad_forn, text="Salvar")
            btnsalvar_forn.place(x=200, y=350, width=90)

            btnapagar_forn = Button(self.wincad_forn, text="Limpar campos")
            btnapagar_forn.place(x=300, y=350, width=110)

            self.img_consulta = PhotoImage(
                file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\consulta.png")
            btnconsulta = Button(self.wincad_forn, image=self.img_consulta, command=Cadastro.ConsForn)
            btnconsulta.place(x=390, y=50, width=50, height=50)

    class CadProd:
        def __init__(self):
            self.f = Font(family='helvetica', size=-20)
            self.s = ttk.Style()
            self.s.configure('.', font=self.f)

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

            """Definindo a fonte dos campos"""
            self.fp = Font(family='verdana', size=-18)

            wincad_prod = Toplevel(root)
            wincad_prod.title('Cadastro de Produtos')
            wincad_prod.geometry("400x350")
            wincad_prod.resizable(0, 0)
            wincad_prod.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
            Label(wincad_prod, text='Cadastro de Produto', font=self.f).pack()

            lbcod_prod = Label(wincad_prod, text="Codigo", font=self.fp)
            lbcod_prod.place(x=70, y=70)
            prod_container1 = Frame(wincad_prod)
            prod_container1.place(x=210, y=75)
            self.txtcod_prod = Entry(prod_container1).pack()

            lbnome_prod = Label(wincad_prod, text='Nome', font=self.fp)
            lbnome_prod.place(x=70, y=100)
            prod_container0 = Frame(wincad_prod)
            prod_container0.place(x=210, y=105)
            self.txtnome_prod = Entry(prod_container0).pack()

            lbpeso_prod = Label(wincad_prod, text='Peso', font=self.fp)
            lbpeso_prod.place(x=70, y=130)
            prod_container2 = Frame(wincad_prod)
            prod_container2.place(x=210, y=135)
            self.txtpeso_prod = Entry(prod_container2).pack()

            lbqtd_prod = Label(wincad_prod, text='Quantidade', font=self.fp)
            lbqtd_prod.place(x=70, y=160)
            prod_container3 = Frame(wincad_prod)
            prod_container3.place(x=210, y=165)
            txtqtd_prod = Entry(prod_container3)
            txtqtd_prod.pack()

            lbuni_prod = Label(wincad_prod, text='Preço Unidade', font=self.fp)
            lbuni_prod.place(x=70, y=190)
            prod_container4 = Frame(wincad_prod)
            prod_container4.place(x=210, y=195)
            txtuni_prod = Entry(prod_container4)
            txtuni_prod.pack()

            lbvtot_prod = Label(wincad_prod, text='Preço Total', font=self.fp)
            lbvtot_prod.place(x=70, y=220)
            prod_container5 = Frame(wincad_prod)
            prod_container5.place(x=210, y=225)
            txtvtot_prod = Entry(prod_container5)
            txtvtot_prod.pack()

            lbvenc_prod = Label(wincad_prod, text='Vencimento', font=self.fp)
            lbvenc_prod.place(x=70, y=250)
            prod_container6 = Frame(wincad_prod)
            prod_container6.place(x=210, y=255)
            txtvenc_prod = Entry(prod_container6)
            txtvenc_prod.pack()

            self.img_add = PhotoImage(file="D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\check.png")
            btnsalvar_prod = Button(wincad_prod, image=self.img_add)
            btnsalvar_prod.place(x=280, y=290, width=40, height=40)

            btnapagar_prod = Button(wincad_prod, text="Limpar campos")
            btnapagar_prod.place(x=70, y=300, width=110)

    class ConsCli:
        def __init__(self):
            self.f = Font(family='helvetica', size=-20)
            self.s = ttk.Style()
            self.s.configure('.', font=self.f)

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

            self.fp = Font(family='verdana',
                           size=-18)

            winconsulta = Toplevel(root)
            winconsulta.title("Consulta de Clientes")
            winconsulta.geometry("950x470")
            winconsulta.resizable(0, 0)
            winconsulta.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
            Label(winconsulta, text='Consulta de Clientes', font=self.fp).pack()

            display_consulta = ttk.Treeview(winconsulta, height=15, columns=('id_cliente',
                                                                             'nome_cliente',
                                                                             'sobrenome',
                                                                             'celular',
                                                                             'cep',
                                                                             'rua',
                                                                             'Nº',
                                                                             'Complemento',
                                                                             'Bairro',
                                                                             'Referencia'))

            display_consulta.place(x=30, y=120, width=900, height=300)
            scroll_v = Scrollbar(winconsulta, orient="vertical", command=display_consulta.yview)
            scroll_v.place(x=930, y=120, height=320)
            scroll_h = Scrollbar(winconsulta, orient="horizontal", command=display_consulta.xview)
            scroll_h.place(x=30, y=420, width=900)

            display_consulta.configure(yscrollcommand=scroll_v.set)
            display_consulta.configure(xscrollcommand=scroll_h.set)

            display_consulta.heading('#0', text='Cod')
            display_consulta.column('#0', minwidth=0, width=50)
            display_consulta.heading('#1', text='Nome ')
            display_consulta.column('#1', minwidth=0, width=150)
            display_consulta.heading('#2', text='Celular')
            display_consulta.column('#2', minwidth=0, width=100)
            display_consulta.heading('#3', text='CEP')
            display_consulta.column('#3', minwidth=0, width=70)
            display_consulta.heading('#4', text='Rua')
            display_consulta.column('#4', minwidth=0, width=150)
            display_consulta.heading('#5', text='Nº')
            display_consulta.column('#5', minwidth=0, width=40)
            display_consulta.heading('#6', text='Bairro')
            display_consulta.column('#6', minwidth=0, width=150)
            display_consulta.heading('#7', text='Complemento')
            display_consulta.column('#7', minwidth=0, width=150)
            display_consulta.heading('#8', text='Referencia')
            display_consulta.column('#8', minwidth=0, width=150)

            lb_celular = Label(winconsulta, text='Celular', font=self.fp)
            lb_celular.place(x=300, y=70)
            container3 = Frame(winconsulta)
            container3.place(x=370, y=75)
            txt_celular = Entry(container3)
            txt_celular.pack()

            self.btn_pesquisa = PhotoImage(
                file='D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\lupa.png')
            btn_cod = Button(winconsulta, image=self.btn_pesquisa)
            btn_cod.place(x=500, y=70, width=30, height=30)

    class ConsFuncio:
        def __init__(self):
            self.f = Font(family='helvetica', size=-20)
            self.s = ttk.Style()
            self.s.configure('.', font=self.f)

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

            """Definindo a fonte dos campos"""
            self.fp = Font(family='verdana', size=-18)

            wincons_funcio = Toplevel(root)
            wincons_funcio.title("Consulta de Funcionários")
            wincons_funcio.geometry("790x470")
            wincons_funcio.resizable(0, 0)
            wincons_funcio.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
            Label(wincons_funcio, text="Consulta Funcionário", font=self.fp).pack()

            display_consulta = ttk.Treeview(wincons_funcio, height=15, columns=('id_funcionario',
                                                                                'nome_funcionauro',
                                                                                'celular',
                                                                                'cep'
                                                                                'rua',
                                                                                'numero',
                                                                                'bairro',
                                                                                'funcao',
                                                                                'salario'))

            display_consulta.place(x=20, y=120, width=750, height=300)
            scroll_v = Scrollbar(wincons_funcio, orient="vertical", command=display_consulta.yview)
            scroll_v.place(x=760, y=120, height=320)
            scroll_h = Scrollbar(wincons_funcio, orient="horizontal", command=display_consulta.xview)
            scroll_h.place(x=20, y=420, width=730)

            display_consulta.configure(yscrollcommand=scroll_v.set)
            display_consulta.configure(xscrollcommand=scroll_h.set)

            display_consulta.heading('#0', text='Matricula')
            display_consulta.column('#0', minwidth=0, width=70)
            display_consulta.heading('#1', text='Nome')
            display_consulta.column('#1', minwidth=0, width=150)
            display_consulta.heading('#2', text='Celular')
            display_consulta.column('#2', minwidth=0, width=70)
            display_consulta.heading('#3', text='CEP')
            display_consulta.column('#3', minwidth=0, width=150)
            display_consulta.heading('#4', text='Rua')
            display_consulta.column('#4', minwidth=0, width=90)
            display_consulta.heading('#5', text='Nº')
            display_consulta.column('#5', minwidth=0, width=100)
            display_consulta.heading('#6', text='Bairro')
            display_consulta.column('#6', minwidth=0, width=100)
            display_consulta.heading('#7', text='Função')
            display_consulta.column('#7', minwidth=0, width=100)
            display_consulta.heading('#8', text='Salario')
            display_consulta.column('#8', minwidth=0, width=100)

            lbcod_funcio = Label(wincons_funcio, text='Matricula', font=self.fp)
            lbcod_funcio.place(x=270, y=70)
            funcio_container0 = Frame(wincons_funcio)
            funcio_container0.place(x=360, y=75)
            self.txtcod_funcio = Entry(funcio_container0).pack()

            self.btn_procura = PhotoImage(
                file='D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\lupa.png')
            btnsearch_funcio = Button(wincons_funcio, image=self.btn_procura)
            btnsearch_funcio.place(x=490, y=70, width=30, height=30)

    class ConsForn:
        def __init__(self):
            """Definindo a fonte de titulo da pagina"""
            self.f = Font(family='helvetica', size=-20)
            self.s = ttk.Style()
            self.s.configure('.', font=self.f)

            """Atualmente essa parte do codigo faz com que as imagens, botoes possam aparecer
            dentro da pagina, então usar em toda criação de pagina"""

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

            """Definindo a fonte dos campos"""
            self.fp = Font(family='verdana',
                           size=-18)

            wincons_forn = Toplevel(root)
            wincons_forn.title("Consulta")
            wincons_forn.geometry("800x480")
            wincons_forn.resizable(0, 0)
            wincons_forn.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
            Label(wincons_forn, text="Consulta De Fornecedores", font=self.fp).pack()

            display_consulta = ttk.Treeview(wincons_forn, height=15, columns=('id_cliente',
                                                                              'nome_cliente',
                                                                              'celular',
                                                                              'cep',
                                                                              'rua',
                                                                              'n_casa',
                                                                              'Bairro',))

            display_consulta.place(x=30, y=150, width=750, height=300)
            scroll_v = Scrollbar(wincons_forn, orient="vertical", command=display_consulta.yview)
            scroll_v.place(x=780, y=150, height=350)
            scroll_h = Scrollbar(wincons_forn, orient="horizontal", command=display_consulta.xview)
            scroll_h.place(x=30, y=450, width=750)

            display_consulta.configure(yscrollcommand=scroll_v.set)
            display_consulta.configure(xscrollcommand=scroll_h.set)

            display_consulta.heading('#0', text='CNPJ')
            display_consulta.column('#0', minwidth=0, width=100)
            display_consulta.heading('#1', text='Nome')
            display_consulta.column('#1', minwidth=0, width=150)
            display_consulta.heading('#2', text='Celular')
            display_consulta.column('#2', minwidth=0, width=100)
            display_consulta.heading('#3', text='CEP')
            display_consulta.column('#3', minwidth=0, width=70)
            display_consulta.heading('#4', text='Rua')
            display_consulta.column('#4', minwidth=0, width=150)
            display_consulta.heading('#5', text='Nº Casa')
            display_consulta.column('#5', minwidth=0, width=40)
            display_consulta.heading('#6', text='Bairro')
            display_consulta.column('#6', minwidth=0, width=150)

            lb_cnpj = Label(wincons_forn, text='CNPJ', font=self.fp)
            lb_cnpj.place(x=300, y=70)
            container0 = Frame(wincons_forn)
            container0.place(x=360, y=75)
            txt_cod = Entry(container0)
            txt_cod.pack()

            self.btn_procurar = PhotoImage(
                file="D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\lupa.png")
            btn_cod = Button(wincons_forn, image=self.btn_procurar)
            btn_cod.place(x=490, y=70, width=30, height=30)

    # #class Cons_prod:
    #     def __init__(self):
    #         fp = Font(family='verdana', size=-18)
    #
    #         wincons_prod = Toplevel(root)
    #         wincons_prod.title("Consulta")
    #         wincons_prod.geometry("790x500")
    #         wincons_prod.resizable(0,0)
    #         wincons_prod.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
    #
    #         display_consulta = ttk.Treeview(wincons_prod, height=15, columns=('id_produto',
    #                                                                           'nome_produto',
    #                                                                           'peso',
    #                                                                           'quantidade'
    #                                                                           'valor_unitario',
    #                                                                           'valor_total',
    #                                                                           'vencimento',))
    #
    #         display_consulta.place(x=20, y=150, width=750, height=300)
    #         scroll_v = Scrollbar(wincons_prod, orient="vertical", command=display_consulta.yview)
    #         scroll_v.place(x=760, y=150, height=350)
    #         scroll_h = Scrollbar(wincons_prod, orient="horizontal", command=display_consulta.xview)
    #         scroll_h.place(x=20, y=450, width=750)
    #
    #         display_consulta.configure(yscrollcommand=scroll_v.set)
    #         display_consulta.configure(xscrollcommand=scroll_h.set)
    #
    #         display_consulta.heading('#0', text='Cod_produto')
    #         display_consulta.column('#0', minwidth=0, width=70)
    #         display_consulta.heading('#1', text='Nome')
    #         display_consulta.column('#1', minwidth=0, width=150)
    #         display_consulta.heading('#2', text='Peso')
    #         display_consulta.column('#2', minwidth=0, width=100)
    #         display_consulta.heading('#3', text='Quantidade')
    #         display_consulta.column('#3', minwidth=0, width=70)
    #         display_consulta.heading('#4', text='Valor Unitario')
    #         display_consulta.column('#4', minwidth=0, width=150)
    #         display_consulta.heading('#5', text='Valor Total')
    #         display_consulta.column('#5', minwidth=0, width=90)
    #         display_consulta.heading('#6', text='Vencimento')
    #         display_consulta.column('#6', minwidth=0, width=100)
    #
    #
    #         lbcod_prod = Label(wincons_prod, text='Codigo Produto', font=fp)
    #         lbcod_prod.place(x=100, y=50)
    #         prod_container0 = Frame(wincons_prod)
    #         prod_container0.place(x=250, y=55)
    #         self.txtcod_prod = Entry(prod_container0).pack()
    #
    #         lbnome_prod = Label(wincons_prod, text='Nome', font=fp)
    #         lbnome_prod.place(x=400, y=50)
    #         prod_container1 = Frame(wincons_prod)
    #         prod_container1.place(x=470,y=55)
    #         self.txtnome_prod = Entry(prod_container1).pack()
    #
    #
    #         btnsearch_prod = Button(wincons_prod, text='Procurar')
    #         btnsearch_prod.place(x=480, y=120)


class Financeiro:
    def __init__(self):
        self.winfinanceiro = Toplevel(root)
        self.winfinanceiro.title("Controle Financeiro")
        self.winfinanceiro.geometry("%dx%d+0+0" % (width_value, height_value))
        self.winfinanceiro.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
        self.winfinanceiro.state('zoomed')

        self.f = Font(family='helvetica', size=-12)
        self.s = ttk.Style()
        self.s.configure('.', font=self.f)

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

        self.fp = Font(family='verdana',
                       size=-18
                       )
        self.nb = ttk.Notebook(self.winfinanceiro)
        self.mensal = ttk.Frame(self.nb)
        self.nb.add(self.mensal, text='Receita')
        self.nb.pack(expand=1, fill=BOTH)
        self.nb.pressed_index = None
        # canvas = Canvas(self.mensal, width=200, height=400)
        # scroll = Scrollbar(self.mensal, command=canvas.yview)
        # canvas.config(yscrollcommand=scroll.set)
        # canvas.pack(side=LEFT, fill=BOTH, expand=True)
        # scroll.pack(side=RIGHT, fill=Y)

        self.imgdata = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\data.png")
        self.lbhora = Label(self.mensal, image=self.imgdata)
        self.lbhora.place(x=80, y=16)
        self.hora = DateEntry(self.mensal, width=12, background='darkblue',
                              foreground='white', borderwidth=2)
        self.hora.place(x=110, y=20, width=120)

        self.btnhora = Button(self.mensal, text="Buscar")
        self.btnhora.place(x=240, y=16)

        self.lfreceita = LabelFrame(self.mensal, text='Receita', font=self.fp)
        self.lfreceita.place(x=100, y=60, width=375, height=280)

        # Definição das variaveis
        semana1 = "1ª"
        semana2 = "2ª"
        semana3 = "3ª"
        semana4 = "4ª"
        semana5 = "5ª"

        # Definição dos valores
        vlr_semana1 = 25
        vlr_semana2 = 10
        vlr_semana3 = 15
        vlr_semana4 = 40
        vlr_semana5 = 0

        labels = [semana1, semana2, semana3, semana4, semana5]
        values = [vlr_semana1, vlr_semana2, vlr_semana3, vlr_semana4, vlr_semana5]

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots(figsize=(3.6, 2.5), dpi=100)
        fig.set_facecolor('lightgoldenrodyellow')

        rects1 = ax.bar(x - width / 25, values, width)

        # Add some text for labels, title and custom x-axis tick labels, etc.

        ax.set_ylabel('')
        plt.title("Receita em semanas")
        ax.set_xticks(x)
        plt.yticks(np.arange(0, 100, 20))
        ax.set_xticklabels(labels)
        plt.grid('on', ls='--')

        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        autolabel(rects1)

        canvas = FigureCanvasTkAgg(fig, master=self.lfreceita)
        plot_widget = canvas.get_tk_widget()
        #
        plot_widget.place(x=5)

        self.lfdespesas = LabelFrame(self.mensal, text="Despesas", font=self.fp)
        self.lfdespesas.place(x=490, y=60, width=375, height=280)

        # Definição das variaveis
        semana1 = "1ª"
        semana2 = "2ª"
        semana3 = "3ª"
        semana4 = "4ª"
        semana5 = "5ª"

        # Definição dos valores
        vlr_semana1 = 25
        vlr_semana2 = 10
        vlr_semana3 = 15
        vlr_semana4 = 40
        vlr_semana5 = 0

        labels = [semana1, semana2, semana3, semana4, semana5]
        values = [vlr_semana1, vlr_semana2, vlr_semana3, vlr_semana4, vlr_semana5]

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots(figsize=(3.6, 2.5), dpi=100)
        fig.set_facecolor('lightgoldenrodyellow')

        rects1 = ax.bar(x - width / 25, values, width)

        # Add some text for labels, title and custom x-axis tick labels, etc.

        ax.set_ylabel('')
        plt.title("Despesas em semanas")
        ax.set_xticks(x)
        plt.yticks(np.arange(0, 100, 20))
        ax.set_xticklabels(labels)
        plt.grid('on', ls='--')

        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        autolabel(rects1)

        canvas = FigureCanvasTkAgg(fig, master=self.lfdespesas)
        plot_widget = canvas.get_tk_widget()
        #
        plot_widget.place(x=5)

        self.lflucro = LabelFrame(self.mensal, text="Lucro", font=self.fp)
        self.lflucro.place(x=880, y=60, width=375, height=140)

        self.lflucratividade = LabelFrame(self.mensal, text="Lucratividade", font=self.fp)
        self.lflucratividade.place(x=880, y=200, width=375, height=140)

        self.lfprejuizo = LabelFrame(self.mensal, text="Prejuizo", font=self.fp)
        self.lfprejuizo.place(x=100, y=350, width=375, height=280)

        # Definição das variaveis
        semana1 = "1ª"
        semana2 = "2ª"
        semana3 = "3ª"
        semana4 = "4ª"
        semana5 = "5ª"

        # Definição dos valores
        vlr_semana1 = 25
        vlr_semana2 = 10
        vlr_semana3 = 15
        vlr_semana4 = 40
        vlr_semana5 = 0

        labels = [semana1, semana2, semana3, semana4, semana5]
        values = [vlr_semana1, vlr_semana2, vlr_semana3, vlr_semana4, vlr_semana5]

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots(figsize=(3.6, 2.5), dpi=100)
        fig.set_facecolor('lightgoldenrodyellow')

        rects1 = ax.bar(x - width / 25, values, width)

        # Add some text for labels, title and custom x-axis tick labels, etc.

        ax.set_ylabel('')
        plt.title("Prejuizo em semanas")
        ax.set_xticks(x)
        plt.yticks(np.arange(0, 100, 20))
        ax.set_xticklabels(labels)
        plt.grid('on', ls='--')

        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        autolabel(rects1)

        canvas = FigureCanvasTkAgg(fig, master=self.lfprejuizo)
        plot_widget = canvas.get_tk_widget()
        #
        plot_widget.place(x=5)

        self.lfcaixames = LabelFrame(self.mensal, text="Caixa do mês", font=self.fp)
        self.lfcaixames.place(x=490, y=350, width=375, height=280)

        # Definição das variaveis
        semana1 = "1ª"
        semana2 = "2ª"
        semana3 = "3ª"
        semana4 = "4ª"
        semana5 = "5ª"

        # Definição dos valores
        vlr_semana1 = 25
        vlr_semana2 = 10
        vlr_semana3 = 15
        vlr_semana4 = 40
        vlr_semana5 = 0

        labels = [semana1, semana2, semana3, semana4, semana5]
        values = [vlr_semana1, vlr_semana2, vlr_semana3, vlr_semana4, vlr_semana5]

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots(figsize=(3.6, 2.5), dpi=100)
        fig.set_facecolor('lightgoldenrodyellow')

        rects1 = ax.bar(x - width / 25, values, width)

        # Add some text for labels, title and custom x-axis tick labels, etc.

        ax.set_ylabel('')
        plt.title("Caixa em semanas")
        ax.set_xticks(x)
        plt.yticks(np.arange(0, 100, 20))
        ax.set_xticklabels(labels)
        plt.grid('on', ls='--')

        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        autolabel(rects1)

        canvas = FigureCanvasTkAgg(fig, master=self.lfcaixames)
        plot_widget = canvas.get_tk_widget()
        #
        plot_widget.place(x=5)

        self.lfdivdespesa = LabelFrame(self.mensal, text="Divisão de Despesas", font=self.fp)
        self.lfdivdespesa.place(x=880, y=350, width=187.5, height=280)

        fig = plt.figure(figsize=(1.8, 2.5))

        # Definimos com o label, os topicos
        labels2 = ["USA", "Brasil", "Japão", "Canada"]
        # Definimos os valores com Value
        values2 = [25, 15, 40, 23]
        # usamos o explode para destacar um dos valores do outro
        # explode = [0.5, 0, 0, 0.10, 0]
        # definindo as cores
        colors = ["c", "y", "r", "g"]

        # Aqui mostramos o grafico
        plt.pie(values2,
                autopct="%.1f%%",
                colors=colors)
        plt.legend(labels=labels2,
                   loc='center',
                   bbox_to_anchor=(0.2, -0.6, 0.5, 1),
                   ncol=2)
        plt.title("Divisão de Despesas")

        canvas = FigureCanvasTkAgg(fig, master=self.lfdivdespesa)
        plot_widget = canvas.get_tk_widget()
        #
        plot_widget.place(x=3)

        self.lfdivreceita = LabelFrame(self.mensal, text="Divisão de Receitas", font=self.fp)
        self.lfdivreceita.place(x=1067, y=350, width=187.5, height=280)

        fig = plt.figure(figsize=(1.8, 2.5))

        # Definimos com o label, os topicos
        labels3 = ["USA", "Brasil", "Japão", "Canada"]
        # Definimos os valores com Value
        values3 = [25, 15, 40, 23]
        # usamos o explode para destacar um dos valores do outro
        # explode = [0.5, 0, 0, 0.10, 0]
        # definindo as cores
        colors2 = ["c", "y", "r", "g"]

        # Aqui mostramos o grafico
        plt.pie(values3,
                autopct="%.1f%%",
                colors=colors2)
        plt.legend(labels=labels3,
                   loc='center',
                   bbox_to_anchor=(0.2, -0.6, 0.5, 1),
                   ncol=2)
        plt.title("Divisão de Receita")

        canvas = FigureCanvasTkAgg(fig, master=self.lfdivreceita)
        plot_widget = canvas.get_tk_widget()
        #
        plot_widget.place(x=3)


class Estoque:
    def __init__(self):
        self.f = None

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

        winestoque = Toplevel(root)
        winestoque.title("Estoque")
        winestoque.geometry("790x500")
        winestoque.resizable(0, 0)
        winestoque.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
        Label(winestoque, text="Consulta de Estoque", font=fp).pack()

        display_consulta = ttk.Treeview(winestoque, height=15, columns=('id_produto',
                                                                        'nome_produto',
                                                                        'peso',
                                                                        'quantidade'
                                                                        'valor_unitario',
                                                                        'valor_total',
                                                                        'vencimento',))

        display_consulta.place(x=20, y=150, width=750, height=300)
        scroll_v = Scrollbar(winestoque, orient="vertical", command=display_consulta.yview)
        scroll_v.place(x=760, y=150, height=350)
        scroll_h = Scrollbar(winestoque, orient="horizontal", command=display_consulta.xview)
        scroll_h.place(x=20, y=450, width=750)

        display_consulta.configure(yscrollcommand=scroll_v.set)
        display_consulta.configure(xscrollcommand=scroll_h.set)

        display_consulta.heading('#0', text='Cod_produto')
        display_consulta.column('#0', minwidth=0, width=70)
        display_consulta.heading('#1', text='Nome')
        display_consulta.column('#1', minwidth=0, width=150)
        display_consulta.heading('#2', text='Peso')
        display_consulta.column('#2', minwidth=0, width=100)
        display_consulta.heading('#3', text='Quantidade')
        display_consulta.column('#3', minwidth=0, width=70)
        display_consulta.heading('#4', text='Valor Unitario')
        display_consulta.column('#4', minwidth=0, width=150)
        display_consulta.heading('#5', text='Valor Total')
        display_consulta.column('#5', minwidth=0, width=90)
        display_consulta.heading('#6', text='Vencimento')
        display_consulta.column('#6', minwidth=0, width=100)

        lbcod_prod = Label(winestoque, text='Codigo Produto', font=fp)
        lbcod_prod.place(x=100, y=50)
        prod_container0 = Frame(winestoque)
        prod_container0.place(x=250, y=55)
        self.txtcod_prod = Entry(prod_container0).pack()

        lbnome_prod = Label(winestoque, text='Nome', font=fp)
        lbnome_prod.place(x=400, y=50)
        prod_container1 = Frame(winestoque)
        prod_container1.place(x=470, y=55)
        self.txtnome_prod = Entry(prod_container1).pack()

        btnsearch_prod = Button(winestoque, text='Procurar')
        btnsearch_prod.place(x=480, y=120)


class Funcs:

    def __init__(self):
        winfuncs = root
        winfuncs.title("Funcionarios")
        winfuncs.geometry("500x400")
        winfuncs.resizable(0, 0)
        winfuncs.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')

        Label(winfuncs, text='Cadastrar Funcionarios', font=fp).pack(side=TOP)

        self.lbmatri = Label(winfuncs, text='Matricula', font=fp)
        self.lbmatri.place(x=100, y=40)
        self.container00 = Frame(winfuncs)
        self.container00.place(x=270, y=45)
        self.txtmatri = Entry(self.container00).pack()

        self.lbnome = Label(winfuncs, text='Funcionário', font=fp)
        self.lbnome.place(x=100, y=70)
        self.container0 = Frame(winfuncs)
        self.container0.place(x=270, y=75)
        self.txtnome = Entry(self.container0).pack()

        self.lbsobrenome = Label(winfuncs, text='Sobrenome', font=fp)
        self.lbsobrenome.place(x=100, y=100)
        self.container1 = Frame(winfuncs)
        self.container1.place(x=270, y=105)
        self.txtsobrenome = Entry(self.container1).pack()

        self.lbcelular = Label(winfuncs, text='Celular', font=fp)
        self.lbcelular.place(x=100, y=130)
        self.container2 = Frame(winfuncs)
        self.container2.place(x=270, y=135)
        self.txtcelular = Entry(self.container2).pack()

        self.lbcep = Label(winfuncs, text='CEP', font=fp)
        self.lbcep.place(x=100, y=160)
        self.container3 = Frame(winfuncs)
        self.container3.place(x=270, y=165)
        self.txtcep = Entry(self.container3).pack()

        self.lbrua = Label(winfuncs, text='Rua', font=fp)
        self.lbrua.place(x=100, y=190)
        self.container4 = Frame(winfuncs)
        self.container4.place(x=270, y=195)
        self.txtrua = Entry(self.container4).pack()

        self.lbnumero = Label(winfuncs, text='Número da casa', font=fp)
        self.lbnumero.place(x=100, y=220)
        self.container5 = Frame(winfuncs)
        self.container5.place(x=270, y=225)
        self.txtnumero = Entry(self.container5).pack()

        self.lbbairro = Label(winfuncs, text='Bairro', font=fp)
        self.lbbairro.place(x=100, y=250)
        self.container6 = Frame(winfuncs)
        self.container6.place(x=270, y=255)
        self.txtbairro = Entry(self.container6).pack()

        self.lbfun = Label(winfuncs, text='Função', font=fp)
        self.lbfun.place(x=100, y=280)
        self.container7 = Frame(winfuncs)
        self.container7.place(x=270, y=285)
        self.txtfun = Entry(self.container7).pack()

        self.lbsalario = Label(winfuncs, text='Salario', font=fp)
        self.lbsalario.place(x=100, y=310)
        self.container8 = Frame(winfuncs)
        self.container8.place(x=270, y=315)
        self.txtsalario = Entry(self.container8).pack()

        # img_user = LabelFrame(winfuncs, text='Foto Funcionario', font=fp)
        # img_user.place(x=450, y=120, width=170, height=170)
        #
        # def Open():
        #     same = True
        #     # n can't be zero, recommend 0.25-4
        #     n = 0.25
        #
        #     path = filedialog.askopenfilename(initialdir='',
        #                                       title='Selecione a Imagem',
        #                                       filetypes=(('png files', "*.png"), ('jpg files', "*.jpg")))
        #
        #     image = Image.open(path)
        #     [imageSizeWidth, imageSizeHeight] = image.size
        #
        #     newImageSizeWidth = int(imageSizeWidth * n)
        #     if same:
        #         newImageSizeHeight = int(imageSizeHeight * n)
        #     else:
        #         newImageSizeHeight = int(imageSizeHeight / n)
        #
        #     image = image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        #     img = ImageTk.PhotoImage(image)
        #
        #     Canvas1 = Canvas(img_user)
        #
        #     Canvas1.create_image(newImageSizeWidth / 2, newImageSizeHeight / 2, image=img)
        #     Canvas1.config(width=newImageSizeWidth, height=newImageSizeHeight)
        #     Canvas1.pack(side=TOP)
        #
        #     # Ainda está com erro, mas ate o momento o erro não para a execução e a imagem carrega
        #     canvas = FigureCanvasTkAgg(Canvas1, master=img_user)
        #     plot_widget = canvas.get_tk_widget()
        #     plot_widget.place(x=5)

        # btn = Button(winfuncs, text='Selecionar', command=Open)
        # btn.place(x=450, y=300)

        btn_salvar = Button(winfuncs, text='Salvar')
        btn_salvar.place(x=270, y=350, width=50)


if __name__ == "__main__":
    root = Tk()
    # titulo da janela e configuração de tela
    root.title("programa Pizzaria")
    root.config(bg="#8DFFBC")

    """Definindo a fonte de titulo da pagina"""
    f = Font(family='helvetica', size=-20)
    s = ttk.Style()
    s.configure('.', font=f)

    """Definindo a fonte dos campos"""
    fp = Font(family='verdana',
              size=-18
              )

    # Define o tamanho da janela
    root.state('zoomed')
    width_value, height_value = root.winfo_screenwidth(), root.winfo_screenheight()
    # root.geometry("%dx%d+0+0" % (w, h))

    # Definindo icone de tela e janela
    root.iconbitmap("D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico")

    # imagem do cliente
    logo = PhotoImage(file='D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.png')
    label = Label(root, image=logo)
    label.place(height=175, width=175, x=0)
    Home(root)
    root.mainloop()
