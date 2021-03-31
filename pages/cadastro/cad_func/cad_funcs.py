from tkinter import *
from tkinter import Frame
from tkinter.font import Font

"""EU VOLTEI POHA, ATUALIZAÇÃO 03/05/2020"""

class Funcs:


    def __init__(self,master):
        winfuncs = root
        winfuncs.title("Funcionarios")
        winfuncs.geometry("500x400")
        winfuncs.resizable(0, 0)
        winfuncs.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\home\\img\\cliente.ico')

        fp = Font(family='verdana', size=-18)
        Label(winfuncs, text='Cadastrar Funcionarios', font=fp).pack(side=TOP)

        self.lbmatri = Label(winfuncs, text='Matricula', font=fp)
        self.lbmatri.place(x=100, y=40)
        self.container00 = Frame(winfuncs)
        self.container00.place(x=270, y=45)
        self.txtmatri = Entry(self.container00).pack()

        self.lbnome = Label(winfuncs, text='Funcionário', font=fp)
        self.lbnome.place(x=100, y=70)
        self.container0 = Frame(winfuncs)
        self.container0.place(x=270, y=75)
        self.txtnome = Entry(self.container0).pack()

        self.lbsobrenome = Label(winfuncs, text='Sobrenome', font=fp)
        self.lbsobrenome.place(x=100, y=100)
        self.container1 = Frame(winfuncs)
        self.container1.place(x=270, y=105)
        self.txtsobrenome = Entry(self.container1).pack()

        self.lbcelular = Label(winfuncs, text='Celular', font=fp)
        self.lbcelular.place(x=100, y=130)
        self.container2 = Frame(winfuncs)
        self.container2.place(x=270, y=135)
        self.txtcelular = Entry(self.container2).pack()

        self.lbcep = Label(winfuncs, text='CEP', font=fp)
        self.lbcep.place(x=100, y=160)
        self.container3 = Frame(winfuncs)
        self.container3.place(x=270, y=165)
        self.txtcep = Entry(self.container3).pack()

        self.lbrua = Label(winfuncs, text='Rua', font=fp)
        self.lbrua.place(x=100, y=190)
        self.container4 = Frame(winfuncs)
        self.container4.place(x=270, y=195)
        self.txtrua = Entry(self.container4).pack()

        self.lbnumero = Label(winfuncs, text='Número da casa', font=fp)
        self.lbnumero.place(x=100, y=220)
        self.container5 = Frame(winfuncs)
        self.container5.place(x=270, y=225)
        self.txtnumero = Entry(self.container5).pack()

        self.lbbairro = Label(winfuncs, text='Bairro', font=fp)
        self.lbbairro.place(x=100, y=250)
        self.container6 = Frame(winfuncs)
        self.container6.place(x=270, y=255)
        self.txtbairro = Entry(self.container6).pack()

        self.lbfun = Label(winfuncs, text='Função', font=fp)
        self.lbfun.place(x=100, y=280)
        self.container7 = Frame(winfuncs)
        self.container7.place(x=270, y=285)
        self.txtfun = Entry(self.container7).pack()

        self.lbsalario = Label(winfuncs, text='Salario', font=fp)
        self.lbsalario.place(x=100, y=310)
        self.container8 = Frame(winfuncs)
        self.container8.place(x=270, y=315)
        self.txtsalario = Entry(self.container8).pack()

        # img_user = LabelFrame(winfuncs, text='Foto Funcionario', font=fp)
        # img_user.place(x=450, y=120, width=170, height=170)
        #
        # def Open():
        #     same = True
        #     # n can't be zero, recommend 0.25-4
        #     n = 0.25
        #
        #     path = filedialog.askopenfilename(initialdir='',
        #                                       title='Selecione a Imagem',
        #                                       filetypes=(('png files', "*.png"), ('jpg files', "*.jpg")))
        #
        #     image = Image.open(path)
        #     [imageSizeWidth, imageSizeHeight] = image.size
        #
        #     newImageSizeWidth = int(imageSizeWidth * n)
        #     if same:
        #         newImageSizeHeight = int(imageSizeHeight * n)
        #     else:
        #         newImageSizeHeight = int(imageSizeHeight / n)
        #
        #     image = image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        #     img = ImageTk.PhotoImage(image)
        #
        #     Canvas1 = Canvas(img_user)
        #
        #     Canvas1.create_image(newImageSizeWidth / 2, newImageSizeHeight / 2, image=img)
        #     Canvas1.config(width=newImageSizeWidth, height=newImageSizeHeight)
        #     Canvas1.pack(side=TOP)
        #
        #     # Ainda está com erro, mas ate o momento o erro não para a execução e a imagem carrega
        #     canvas = FigureCanvasTkAgg(Canvas1, master=img_user)
        #     plot_widget = canvas.get_tk_widget()
        #     plot_widget.place(x=5)

        # btn = Button(winfuncs, text='Selecionar', command=Open)
        # btn.place(x=450, y=300)

        btn_salvar = Button(winfuncs, text='Salvar')
        btn_salvar.place(x=270, y=350, width=50)
root=Tk()

Funcs(root)
root.mainloop()