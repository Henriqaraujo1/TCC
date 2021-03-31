from tkinter import *
from tkinter import ttk, PhotoImage
from tkinter.font import Font
from PIL import ImageTk, Image

root = Tk()

class Mesa:
    def __init__(self, master):
        self.fp = Font(family='verdana', size=-18)

        self.m = Font(family="verdana", size=-14)

        self.f = Font(family='helvetica', size=-20)
        self.s = ttk.Style()
        self.s.configure('.', font=self.f)


        self.winmesa = root
        self.winmesa.title("Mesas")
        self.winmesa.geometry("500x470")
        Label(self.winmesa, text='Mesas', font=self.f)

        def toggle_font(event):
            if event.keysym == '0':
                self.f['size'] = -12
            elif event.keysym == 'plus':
                if self.f['size'] > -31:
                    self.f['size'] = self.f['size'] - 1
                elif event.keysym == 'minus':
                    if self.f['size'] < -6:
                        self.f['size'] = self.f['size'] + 1

        self.winmesa.bind('<Control-plus>', toggle_font)
        self.winmesa.bind('<Control-minus>', toggle_font)
        self.winmesa.bind('<Control-0>', toggle_font)

        self.displayMesas = LabelFrame(self.winmesa, width=460, height=350)
        self.displayMesas.place(x=20, y=65)

        def change_status():
            img_verde = PhotoImage(file="d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\mesaVerde.png")
            self.displayMesas.configure(image=img_verde)
            self.displayMesas.image = img_verde


        btn_refresh = Button(self.winmesa, text="Atualizar").place(x=350, y=420)

        Button(self.winmesa, text="Livre", font=self.m, bg='#2FEBA0', fg='black', command=change_status).place(x=187, y=15)
        Button(self.winmesa, text="Ocupada", font=self.m, bg='#EB4E3D', fg='black').place(x=237, y=15)
        Button(self.winmesa, text="Limpeza", font=self.m, bg='#45D4FF', fg='black').place(x=315, y=15)
        Button(self.winmesa, text="Reserva", font=self.m, bg='#EBE93D', fg='black').place(x=390, y=15)





        self.img_mesas = "d:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\mesa.png"
        self.open_img = Image.open(self.img_mesas)

        self.img1 = ImageTk.PhotoImage(self.open_img)
        self.in_frame = Label(self.displayMesas, image=self.img1)
        self.in_frame.place(x=50)

Mesa(root)
root.mainloop()