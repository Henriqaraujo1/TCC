from tkinter import *
from tkinter import ttk, Frame, PhotoImage, filedialog
from tkinter.font import Font

root = Tk()

"""Ultima alteração 18-02-2020 (coringa)"""
class Cons_funcio:
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
        self.fp = Font(family='verdana',size=-18)

        wincons_funcio = root
        wincons_funcio.title("Consulta de Funcionários")
        wincons_funcio.geometry("790x470")
        wincons_funcio.resizable(0, 0)
        wincons_funcio.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
        Label(wincons_funcio, text="Consulta Funcionários", font=self.fp).pack()

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

        self.btn_procura = PhotoImage(file='D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\lupa.png')
        btnsearch_funcio = Button(wincons_funcio, image=self.btn_procura)
        btnsearch_funcio.place(x=490, y=70, width=30, height=30)


Cons_funcio(root)
root.mainloop()