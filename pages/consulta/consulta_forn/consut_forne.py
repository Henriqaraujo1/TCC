from tkinter import *
from tkinter import ttk, Frame
from tkinter.font import Font

root = Tk()

class Cons_forn:
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

        wincons_forn = root
        wincons_forn.title("Consulta")
        wincons_forn.geometry("800x480")
        wincons_forn.resizable(0, 0)
        wincons_forn.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
        Label(wincons_forn, text="Consulta De Fornecedores",font=self.fp).pack()

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
        txt_cod = Entry(container0).pack()

        self.btn_procurar = PhotoImage(file="D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\lupa.png")
        btn_cod = Button(wincons_forn, image=self.btn_procurar)
        btn_cod.place(x=490, y=70, width=30, height=30)



Cons_forn(root)
root.mainloop()