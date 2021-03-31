from tkinter import *
from tkinter import Frame, ttk
from tkinter.font import Font

root = Tk()
"""Atualizado dia 24/02/2020"""
class Cad_prod:
    def __init__(self, master):
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

        wincad_prod = root
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
        txtqtd_prod = Entry(prod_container3).pack()

        lbuni_prod = Label(wincad_prod, text='Preço Unidade', font=self.fp)
        lbuni_prod.place(x=70, y=190)
        prod_container4 = Frame(wincad_prod)
        prod_container4.place(x=210, y=195)
        txtuni_prod = Entry(prod_container4).pack()

        lbvtot_prod = Label(wincad_prod, text='Preço Total', font=self.fp)
        lbvtot_prod.place(x=70, y=220)
        prod_container5 = Frame(wincad_prod)
        prod_container5.place(x=210, y=225)
        txtvtot_prod = Entry(prod_container5).pack()

        lbvenc_prod = Label(wincad_prod, text='Vencimento', font=self.fp)
        lbvenc_prod.place(x=70, y=250)
        prod_container6 = Frame(wincad_prod)
        prod_container6.place(x=210, y=255)
        txtvenc_prod = Entry(prod_container6).pack()

        self.img_add = PhotoImage(file="D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\check.png")
        btnsalvar_prod = Button(wincad_prod, image=self.img_add)
        btnsalvar_prod.place(x=280, y=290, width=40, height=40)


        btnapagar_prod = Button(wincad_prod, text="Limpar campos")
        btnapagar_prod.place(x=70, y=300, width=110)


Cad_prod(root)
root.mainloop()