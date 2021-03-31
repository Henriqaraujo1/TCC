from tkinter import *
from tkinter import ttk, Frame, PhotoImage, filedialog
from tkinter.font import Font

root = Tk()


class Pagamento:
    def __init__(self, master):
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

        self.winpagamento = root
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
        self.btnsacola_pg = Button(self.winpagamento, text="Abrir pedido") #, command=Sacola)
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
        txtdinheiro_pg = Entry(pg_container_6, width=8, bg='blue', fg='#FF0000', font=fp1).pack()


Pagamento(root)
root.mainloop()