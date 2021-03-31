from tkinter import *
from tkinter import ttk, Frame
from tkinter.font import Font

root = Tk()

class Estoque:
    def __init__(self, master):
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

        winestoque = root
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

f = Font(family='helvetica', size=-12)
s = ttk.Style()
s.configure('.', font=f)

fp = Font(family='verdana', size=-18)

Estoque(root)
root.mainloop()