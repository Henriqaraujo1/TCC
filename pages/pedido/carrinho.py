from tkinter import *
from tkinter import ttk, Frame, Tk
from tkinter.font import Font

root = Tk()

class Sacola:
    def __init__(self,master):
        fp = Font(family='verdana',
                  size=-18
                  )

        """Definindo a fonte de titulo da pagina"""
        f = Font(family='helvetica', size=-25)
        s = ttk.Style()
        s.configure('.', font=f)

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

        winsacola = root
        winsacola.title("Sacola")
        winsacola.geometry("840x520")
        # winsacola.resizable(0, 0)
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
        txtpedido_sac = Entry(sac_container0).pack()

        lbcomanda_ped = Label(winsacola, text='Comanda', font=fp)
        lbcomanda_ped.place(x=375, y=50)
        sac_container1 = Frame(winsacola)
        sac_container1.place(x=470, y=55)
        txtcomanda_sac = Entry(sac_container1).pack()

        btnsearch_ped = Button(winsacola, text='Procurar')
        btnsearch_ped.place(x=400, y=120)

Sacola(root)
root.mainloop()