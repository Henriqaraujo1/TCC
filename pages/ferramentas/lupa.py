from tkinter import *
from tkinter import ttk, Frame, PhotoImage
from tkinter.font import Font

root = Tk()
"""Atualizado 24/02/2020"""
class Lupa:
    def __init__(self, master):
        fp = Font(family='verdana', size=-18)

        self.f = Font(family='helvetica', size=-20)
        self.s = ttk.Style()
        self.s.configure('.', font=f)

        self.winlupa = root
        self.winlupa.title("Cardapio")
        self.winlupa.geometry("500x450")
        self.winlupa.resizable(0, 0)
        self.winlupa.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')
        Label(self.winlupa, text="Cardapio", font=f).pack()

        def toggle_font(event):
            if event.keysym == '0':
                self.f['size'] = -12
            elif event.keysym == 'plus':
                if self.f['size'] > -31:
                    self.f['size'] = self.f['size'] - 1
                elif event.keysym == 'minus':
                    if self.f['size'] < -6:
                        self.f['size'] = self.f['size'] + 1

        self.winlupa.bind('<Control-plus>', toggle_font)
        self.winlupa.bind('<Control-minus>', toggle_font)
        self.winlupa.bind('<Control-0>', toggle_font)

        cod = Label(self.winlupa, text="Codigo", font=fp)
        cod.place(x=50, y=50)
        container0 = Frame(self.winlupa)
        container0.place(x=120, y=58, width=50)
        txtcod = Entry(container0).pack()

        desc = Label(self.winlupa, text="Item", font=fp)
        desc.place(x=185, y=50)
        container1 = Frame(self.winlupa)
        container1.place(x=285, y=58)
        txtdesc = Entry(container1).pack()

        display_desc = ttk.Treeview(self.winlupa, columns=('Cod', 'Item', 'Descrição'))
        display_desc.place(x=50, y=100, width=400, height=300)
        scroll_y = Scrollbar(self.winlupa, orient="vertical", command=display_desc.yview)
        scroll_y.place(x=450, y=100, height=300)
        scroll_x = Scrollbar(self.winlupa, orient="horizontal", command=display_desc.xview)
        scroll_x.place(x=50, y=400, width=400)

        display_desc.config(yscrollcommand=scroll_y.set)
        display_desc.config(xscrollcommand=scroll_x.set)

        display_desc.heading('#0', text='Codigo')
        display_desc.column('#0', minwidth=0, width=70)
        display_desc.heading('#1', text='Item')
        display_desc.column('#1', minwidth=0, width=90)
        display_desc.heading('#2', text='Descrição')
        display_desc.column('#2', minwidth=40, width=250)

        self.img_check = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\check1.png")
        self.btn_search = Button(self.winlupa, image=self.img_check)
        self.btn_search.place(x=430, y=45)

        self.btn_include = Button(self.winlupa, text="Incluir").place(x=50, y=420)

f = Font(family='helvetica', size=-20)
s = ttk.Style()
s.configure('.', font=f)


"""Definindo a fonte dos campos"""
fp = Font(family='verdana',
           size=-18
           )

Lupa(root)
root.mainloop()