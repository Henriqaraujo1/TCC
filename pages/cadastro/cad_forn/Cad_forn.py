from tkinter import *
from tkinter import ttk, Frame, PhotoImage, filedialog
from tkinter.font import Font

root = Tk()
"""Ultima Alteração 17-02-2020 (Coringa)"""
class Cad_forn:
    def __init__(self, master):
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

        self.wincad_forn = root
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

        self.img_consulta = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\consulta.png")
        btnconsulta = Button(self.wincad_forn, image=self.img_consulta) #command=Cadastro.ConsForn)
        btnconsulta.place(x=390, y=50, width=50, height=50)


Cad_forn(root)
root.mainloop()