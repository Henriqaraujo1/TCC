from tkinter import *
from tkinter import ttk
from tkinter.font import Font


class Nota_fiscal:
    def __init__(self, master):
        win_nf = root
        win_nf.title("Nota Fiscal")
        root.geometry("900x600")
        win_nf.config(bg="#000000") #Cor da lateral
        win_nf.iconbitmap('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\imgs\\nota-fiscal.ico')

        # img_nf = PhotoImage('D:\\Onedrive World\\OneDrive\\dev\\programa\\pages\\imgs\\nota-fiscal.png')
        # img_label_nf = Label(win_nf, image=img_nf)
        # img_label_nf.place(height=180, width=180, y=300)

        #padrão formatação da fonte
        ft = Font(family='calibri',
                     size=13)
        ft1 = Font(family='calibri',
                     size=11)
        bg_font = "white"

        # estilo da tela
        w = Canvas(win_nf, width=800,height=600, bg="white")
        w.place(x=120)


        btn_incluir = Button(win_nf, text="Incluir").place(x=25, y=3, width=70, height=25)
        btn_apagar = Button(win_nf, text="Apagar").place(x=25, y=35, width=70, height=25)
        btn_confirmar = Button(win_nf, text="Confirmar").place(x=25, y=67, width=70, height=25)
        btn_cancelar = Button(win_nf, text="Cancelar").place(x=25, y=99, width=70, height=25)
        btn_atualizar = Button(win_nf, text="Atualizar").place(x=25, y=131, width=70, height=25)
        btn_finalizar = Button(win_nf, text="Finalizar").place(x=25, y=163, width=70, height=25)
        btn_imprimir = Button(win_nf, text="Imprimir").place(x=25, y=195, width=70, height=25)

        id_nf = Label(win_nf, text="#Codigo NF", font=ft ,bg=bg_font)
        id_nf.place(x=170, y=30)
        container0 = Frame(win_nf)
        container0.place(x=260, y=33, width=80)
        txt_id_nf = Entry(container0).pack()

        chave_NF = Label(win_nf, text="Chave de Acesso", font=ft , bg=bg_font)
        chave_NF.place(x=360, y=30)
        container1 = Frame(win_nf)
        container1.place(x=485, y=33)
        txt_chave_nf = Entry(container1).pack(ipadx=100)

        protc = Label(win_nf, text="Protocolo", font=ft, bg=bg_font)
        protc.place(x=170, y=60)
        container2 = Frame(win_nf)
        container2.place(x=260, y=65)
        txt_protc = Entry(container2).pack()

        autori = Label(win_nf, text="Autorização", font=ft, bg=bg_font)
        autori.place(x=392, y=60)
        container3 = Frame(win_nf)
        container3.place(x=485, y=65)
        txt_autori = Entry(container3).pack()

        forn_nf = Label(win_nf, text="Fornecedor", font=ft, bg=bg_font)
        forn_nf.place(x=170, y=90)
        container4 = Frame(win_nf)
        container4.place(x=260, y=95)
        txt_forn_nf = Entry(container4).pack()
        btn_forn = Button(win_nf, text="Fornecedor", font=ft)
        btn_forn.place(x=392, y=90, height=25)

        num_nf = Label(win_nf, text="Nº Nota Fiscal", font=ft, bg=bg_font)
        num_nf.place(x=170, y=120)
        container5 = Frame(win_nf)
        container5.place(x=280, y=125, width=105)
        txt_num_nf = Entry(container5).pack()

        model_nf = Label(win_nf, text="Modelo NF", font=ft, bg=bg_font)
        model_nf.place(x=390, y=120)
        container6 = Frame(win_nf)
        container6.place(x=485, y=125)
        txt_model_nf = Entry(container6).pack()

        serie_nf = Label(win_nf, text="Série/ Sub-Série", font=ft, bg=bg_font)
        serie_nf.place(x=170, y=150)
        container7 = Frame(win_nf)
        container7.place(x=300, y=155)
        txt_serie_nf = Entry(container7).pack()

        cif_nf = Label(win_nf, text="CIF/FOB", font=ft, bg=bg_font)
        cif_nf.place(x=170, y=180)
        container8 = Frame(win_nf)
        container8.place(x=255, y=185)
        txt_cif_nf = Entry(container8).pack()

        #colocar dois campos de data
        dt_emissao = Label(win_nf, text="Emissão, Entrada", font=ft, bg=bg_font)
        dt_emissao.place(x=170, y=210)
        container9 = Frame(win_nf)
        container9.place(x=305, y=215)
        txt_dt_emissao = Entry(container9).pack()

        cfop_nf = Label(win_nf, text="CFOP", font=ft, bg=bg_font)
        cfop_nf.place(x=170, y=240)
        container10 = Frame(win_nf)
        container10.place(x=255, y=245)
        txt_cfop_nf = Entry(container10).pack()

        display_itens_nf = ttk.Treeview(win_nf, height=15, columns=('item',
                                                                    'produto',
                                                                    'descricao',
                                                                    'unid',
                                                                    'med',
                                                                    'qtde',
                                                                    'valor Unit',
                                                                    'valor total',
                                                                    'Base icms',
                                                                    'icms',
                                                                    'valor icms',))

        display_itens_nf.place(x=170, y=280, width=640, height=150)
        scroll_v = Scrollbar(win_nf, orient="vertical", command=display_itens_nf)
        scroll_v.place(x=810, y=280, height=150)
        scroll_h = Scrollbar(win_nf, orient="horizontal", command=display_itens_nf)
        scroll_h.place(x=172, y=410, width=637)

        display_itens_nf.configure(yscrollcommand=scroll_v.set)
        display_itens_nf.configure(xscrollcommand=scroll_h.set)


        display_itens_nf.heading('#0', text='Item')
        display_itens_nf.column('#0', minwidth=0, width=35)
        display_itens_nf.heading('#1',text="Produto")
        display_itens_nf.column('#1', minwidth=0, width=100)
        display_itens_nf.heading('#2', text='Descrição')
        display_itens_nf.column('#2', minwidth=0, width=300)
        display_itens_nf.heading('#3', text='Unid.')
        display_itens_nf.column('#3', minwidth=0, width=35)
        display_itens_nf.heading('#4', text='Med.')
        display_itens_nf.column('#4', minwidth=0, width=35)
        display_itens_nf.heading('#5', text="Qtde.")
        display_itens_nf.column('#5', minwidth=0, width=35)
        display_itens_nf.heading('#6', text='Valor Unit.')
        display_itens_nf.column('#6', minwidth=0, width=60)
        display_itens_nf.heading('#7', text="Valor Total")
        display_itens_nf.column('#7', minwidth=0, width=60)
        display_itens_nf.heading('#8', text='Base ICMS')
        display_itens_nf.column('#8', minwidth=0, width=60)
        display_itens_nf.heading('#9', text="ICMS (%)")
        display_itens_nf.column('#9', minwidth=0, width=35)
        display_itens_nf.heading('#10', text="Valor ICMS")
        display_itens_nf.column('#10', minwidth=0, width=60)

        '''calcular imposto
        Valor da nota fiscal: R$ 200,00;
        PIS (1,65% sobre o total): R$ 3,30;
        COFINS (7,6% sobre o total): R$ 15,20;
        IRPJ (15% sobre o total): R$ 30,00;
        CSLL (9% sobre o total): R$ 18,00;
        Valor total dos impostos na nota fiscal: R$ 66,50.'''

        ipi_base = Label(win_nf, text="Base IPI R$", font=ft1, bg=bg_font)
        ipi_base.place(x=170, y=430)
        container11 = Frame(win_nf)
        container11.place(x=175, y=455, width=70)
        txt_ipi_base = Entry(container11).pack()

        ipi_valor = Label(win_nf, text="Valor IPI R$", font=ft1, bg=bg_font)
        ipi_valor.place(x=260, y=430)
        container12 = Frame(win_nf)
        container12.place(x=260, y=455, width=70)
        txt_ipi_valor = Entry(container12).pack()

        icms_base = Label(win_nf, text="Base ICMS R$", font=ft1, bg=bg_font)
        icms_base.place(x=365, y=430)
        container13 = Frame(win_nf)
        container13.place(x=365, y=455, width=70)
        txt_icms_base = Entry(container13).pack()

        icms_valor = Label(win_nf, text="Valor ICMS R$", font=ft1, bg=bg_font)
        icms_valor.place(x=460, y=430)
        container14 = Frame(win_nf)
        container14.place(x=460, y=455, width=70)
        txt_icms_valor = Entry(container14).pack()

        iss_base = Label(win_nf, text="Base ISS R$", font=ft1, bg=bg_font)
        iss_base.place(x=560, y=430)
        container15 = Frame(win_nf)
        container15.place(x=560, y=455, width=70)
        txt_iss_base = Entry(container15).pack()

        iss_valor = Label(win_nf, text="Valor ISS R$", font=ft1, bg=bg_font)
        iss_valor.place(x=650, y=430)
        container16 = Frame(win_nf)
        container16.place(x=650, y=455, width=70)
        txt_iss_valor = Entry(container16).pack()

        frete = Label(win_nf, text="Frete", font=ft1, bg=bg_font)
        frete.place(x=740, y=430)
        container17 = Frame(win_nf)
        container17.place(x=740, y=455, width=70)
        txt_frete = Entry(container17).pack()

        seguro = Label(win_nf, text="Seguro", font=ft1, bg=bg_font)
        seguro.place(x=170, y=470)
        container18 = Frame(win_nf)
        container18.place(x=175, y=495, width=70)
        txt_seguro = Entry(container18).pack()

        icms_bsubs = Label(win_nf, text="Base ICMS Subs.", font=ft1, bg=bg_font)
        icms_bsubs.place(x=255, y=470)
        container19 = Frame(win_nf)
        container19.place(x=260, y=495, width=70)
        txt_icms_bsubs = Entry(container19).pack()

        icms_vsubs = Label(win_nf, text="V. ICMS Subs.", font=ft1, bg=bg_font)
        icms_vsubs.place(x=365, y=470)
        container20 = Frame(win_nf)
        container20.place(x=365, y=495, width=70)
        txt_icms_vsubs = Entry(container20).pack()

        acresci_nf = Label(win_nf, text="Acréscimo", font=ft1, bg=bg_font)
        acresci_nf.place(x=460, y=470)
        container21 = Frame(win_nf)
        container21.place(x=460, y=495, width=70)
        txt_acresci_nf = Entry(container21).pack()

        outras_desp_nf = Label(win_nf, text="Outras Custos", font=ft1, bg=bg_font)
        outras_desp_nf.place(x=555, y=470)
        container22 = Frame(win_nf)
        container22.place(x=560, y=495, width=70)
        txt_outras_despnf = Entry(container22).pack()

        desconto_nf = Label(win_nf, text="Desconto", font=ft1, bg=bg_font)
        desconto_nf.place(x=650, y=470)
        container23 = Frame(win_nf)
        container23.place(x=650, y=495, width=70)
        txt_desconto_nf = Entry(container23).pack()

        total_itens_nf = Label(win_nf, text="Total dos itens", font=ft1, bg=bg_font)
        total_itens_nf.place(x=460, y=540)
        container24 = Frame(win_nf)
        container24.place(x=560, y=540, width=70)
        txt_tot_itens_nf = Entry(container24).pack()


        total_nf = Label(win_nf, text='Total da Nota', font=ft1, bg=bg_font)
        total_nf.place(x=645, y=540)
        container25 = Frame(win_nf)
        container25.place(x=740, y=540, width=70)
        txt_tot_nf = Entry(container25).pack()







if __name__ == '__main__':
    root = Tk()
    Nota_fiscal(root)
    root.mainloop()
