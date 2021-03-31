from tkinter import *
from tkinter import ttk, Frame, PhotoImage
from tkinter.font import Font
from tkcalendar import DateEntry

root = Tk()

class Pedido:
    def __init__(self):
        """Definindo tamanho da tela, titulo da janela, icone e o titulo dentro da janela"""
        self.winpedido = root
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
        self.txtatend = Entry(self.container5).pack()

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
        self.txtcomanda = Entry(container00).pack()

        # Número do Pedido
        self.lbpedido = Label(self.winpedido, text="Nº Pedido", font=fp)
        self.lbpedido.place(x=100, y=150)
        self.container0 = Frame(self.winpedido)
        self.container0.place(x=280, y=150)
        self.txtpedido = Entry(self.container0).pack()

        # imagem de pesquisa
        self.img_pesq = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\pesquisa.png")

        # Cliente
        self.lbcliente = Label(self.winpedido, text="Cliente", font=fp)
        self.lbcliente.place(x=100, y=180)
        self.btncliente = Button(self.winpedido, image=self.img_pesq, command=Cadastro.ConsCli)
        self.btncliente.place(x=410, y=175)
        self.container1 = Frame(self.winpedido)
        self.container1.place(x=280, y=180)
        self.txtcliente = Entry(self.container1).pack()

        # Sabor da Pizza
        self.lbsabor1 = Label(self.winpedido, text="Primeiro Sabor", font=fp)
        self.lbsabor1.place(x=100, y=210)
        self.container2 = Frame(self.winpedido)
        self.container2.place(x=280, y=210)
        self.btnsabor1 = Button(self.winpedido, image=self.img_pesq, command=Lupa)
        self.btnsabor1.place(x=410, y=205)
        self.txtsabor1 = Entry(self.container2).pack()

        # segundo Sabor da pizza
        self.lbsabor2 = Label(self.winpedido, text="Segundo Sabor", font=fp)
        self.lbsabor2.place(x=100, y=240)

        self.container3 = Frame(self.winpedido)
        self.container3.place(x=280, y=240)
        self.btnsabor2 = Button(self.winpedido, image=self.img_pesq, command=Lupa)
        self.btnsabor2.place(x=410, y=235)
        self.txtsabor2 = Entry(self.container3).pack()

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



f = Font(family='helvetica', size=-20)
s = ttk.Style()
s.configure('.', font=f)


"""Definindo a fonte dos campos"""
fp = Font(family='verdana',
               size=-18
               )

Pedido(root)
root.mainloop()
