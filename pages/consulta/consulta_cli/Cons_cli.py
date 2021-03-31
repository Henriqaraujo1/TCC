from tkinter import *
from tkinter import ttk
from tkinter.font import Font

root = Tk()
"""Atualizado em (18-02-2020)"""
class Cons_cli:
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

        self.fp = Font(family='verdana',
                       size=-18)

        winconsulta = root
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
        txt_celular = Entry(container3).pack()

        self.btn_pesquisa = PhotoImage(file='D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\lupa.png')
        btn_cod = Button(winconsulta, image=self.btn_pesquisa)
        btn_cod.place(x=500, y=70, width=30, height=30)


Cons_cli(root)
root.mainloop()