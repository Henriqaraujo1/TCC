from tkinter import *
from tkinter import ttk, Frame
from tkinter.font import Font

root = Tk()
"""Atualizado 03-05-2020"""
class Cad_cli:
    def __init__(self, master):
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

        wincadastro = root
        wincadastro.title("Cadastro de Cliente")
        wincadastro.geometry("400x400")
        wincadastro.resizable(0, 0)
        wincadastro.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
        Label(wincadastro, text="Cadastro de Cliente", font=fp).pack(side=TOP)

        lbcodigo_cli = Label(wincadastro, text="Celular", font=fp)
        lbcodigo_cli.place(x=80, y=90)
        container00 = Frame(wincadastro)
        container00.place(x=220, y=95)
        txtcodigo_cli = Entry(container00).pack()

        lbnome_cli = Label(wincadastro, text='Nome', font=fp)
        lbnome_cli.place(x=80, y=120)
        container0 = Frame(wincadastro)
        container0.place(x=220, y=125)
        txtnome_cli = Entry(container0).pack()

        lbsobrenome_cli = Label(wincadastro, text='Sobrenome', font=fp)
        lbsobrenome_cli.place(x=80, y=150)
        container1 = Frame(wincadastro)
        container1.place(x=220, y=155)
        txtsobrenome_cli = Entry(container1).pack()

        lbcelular_cli = Label(wincadastro, text='CEP', font=fp)
        lbcelular_cli.place(x=80, y=180)
        container2 = Frame(wincadastro)
        container2.place(x=220, y=185)
        txtcelular_cli = Entry(container2).pack()

        lbcep_cli = Label(wincadastro, text='Rua', font=fp)
        lbcep_cli.place(x=80, y=210)
        container3 = Frame(wincadastro)
        container3.place(x=220, y=215)
        txtcep_cli = Entry(container3).pack()

        lbrua_cli = Label(wincadastro, text='Nº Casa', font=fp)
        lbrua_cli.place(x=80, y=240)
        container4 = Frame(wincadastro)
        container4.place(x=220, y=245)
        txtrua_cli = Entry(container4).pack()

        lbnumero_cli = Label(wincadastro, text='Bairro', font=fp)
        lbnumero_cli.place(x=80, y=270)
        container5 = Frame(wincadastro)
        container5.place(x=220, y=275)
        txtnumero_cli = Entry(container5).pack()

        lbcomplemento_cli = Label(wincadastro, text='Referencia', font=fp)
        lbcomplemento_cli.place(x=80, y=300)
        container6 = Frame(wincadastro)
        container6.place(x=220, y=305)
        txtnumero_cli = Entry(container6).pack()

        self.img_salvar_cli = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\check1.png")
        btnsalvar_cli = Button(wincadastro, image=self.img_salvar_cli)
        btnsalvar_cli.place(x=300, y=355, width=40)

        btnapagar_cli = Button(wincadastro, text="Limpar campos")
        btnapagar_cli.place(x=150, y=360, width=110)

        self.img_consulta_cli = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\consulta.png")
        btnconsulta_cli = Button(wincadastro, image=self.img_consulta_cli, command=False)
        btnconsulta_cli.place(x=300, y=30, width=45, height=45)

fp = Font(family='verdana',
         size=-18
         )

"""Definindo a fonte de titulo da pagina"""
f = Font(family='helvetica', size=-12)
s = ttk.Style()
s.configure('.', font=f)

Cad_cli(root)
root.mainloop()