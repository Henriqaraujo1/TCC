class Pizza:

    def __init__(self):
        # Definindo sabores
        self.s1 = "Mussarela"
        self.s2 = "Calabresa"
        self.s3 = "Bacon"
        self.s4 = "Baiana"
        self.s5 = "Portuguesa"
        self.s6 = "4 Queijo"
        self.s7 = "Camarão"
        self.s8 = "Modo da Casa"
        self.s9 = "Pepperoni"
        self.s10 = "Frango c/ Catupiry"

        # definindo Preço
        self.v1 = 20.00
        self.v2 = 20.00
        self.v3 = 23.90
        self.v4 = 23.90
        self.v5 = 25.90
        self.v6 = 27.90
        self.v7 = 30.00
        self.v8 = 25.90
        self.v9 = 29.90
        self.v10 = 25.60

        #definindo tamanhos
        self.b1 = "Lata 300ML"
        self.b2 = "Garrafa 500ML"
        self.b3 = "Garrafa de 1L"
        self.b4 = "Garrafa de 2L"

        #definindo os tipos
        self.b5 = "Coca-Cola"
        self.b6 = "Sprite"
        self.b7 = "Fanta"
        self.b8 = "Guarana"
        self.b9 = "Pepsi"

        #definindo preço
        self.vb1 = 3.50
        self.vb2 = 5.00
        self.vb3 = 6.00
        self.vb4 = 8.00

        self.set_pag()
        # self.set_cardipio()
        # self.set_bebida()

    def set_cardipio(self):
        card = str(input("Deseja ver o cardapio (s/n): "))
        if (card == 's'):
            print("{:-^55s}".format("Pizzaria"))
            print("{:-^55}".format("Pizzas"))
            print("| 01 - {}            -----------------| R${} |".format(self.s1, str(self.v1)))
            print("| 02 - {}            -----------------| R${} |".format(self.s2, str(self.v2)))
            print("| 03 - {}                -----------------| R${} |".format(self.s3, str(self.v3)))
            print("| 04 - {}               -----------------| R${} |".format(self.s4, str(self.v4)))
            print("| 05 - {}           -----------------| R${} |".format(self.s5, str(self.v5)))
            print("| 06 - {}             -----------------| R${} |".format(self.s6, str(self.v6)))
            print("| 07 - {}              -----------------| R${} |".format(self.s7, str(self.v7)))
            print("| 08 - {}         -----------------| R${} |".format(self.s8, str(self.v8)))
            print("| 09 - {}            -----------------| R${} |".format(self.s9, str(self.v9)))
            print("| 10 - {}   -----------------| R${} |".format(self.s10, str(self.v10)))
            print("-" * 55)

            print("{:-^55}".format("Bebibas"))
            print("|-----------------| 350ML | 500ML | 1 Litro | 2 Litro |")
            print("|01 - {}   | R${} | RS{} |  RS{}  |  RS{}  |".format(self.b5, self.vb1, self.vb2, self.vb3, self.vb4))
            print("|01 - {}      | R${} | RS{} |  RS{}  |  RS{}  |".format(self.b6, self.vb1, self.vb2, self.vb3, self.vb4))
            print("|01 - {}       | R${} | RS{} |  RS{}  |  RS{}  |".format(self.b7, self.vb1, self.vb2, self.vb3, self.vb4))
            print("|01 - {}     | R${} | RS{} |  RS{}  |  RS{}  |".format(self.b8, self.vb1, self.vb2, self.vb3, self.vb4))
            print("|01 - {}       | R${} | RS{} |  RS{}  |  RS{}  |".format(self.b9, self.vb1, self.vb2, self.vb3, self.vb4))
            print("-"*55)

            self.set_pedido()


        else:
            print("Obrigado, Volte sempre")

    # Func para fazer pedido de um sabor
    def set_pedido(self):
        #Tratando erros
        while True:
            self.prg = str(input("\nDeseja fazer um pedido (sim/nao): "))
            if (self.prg == 'sim' or self.prg == 'nao' or self.prg == 'sair'):
                break

            if(self.prg != 'sim' or self.prg != 'nao'):
                try:
                    eval(self.prg)
                except(NameError,ValueError,SyntaxError, AttributeError):
                    print("\nDigite sim ou não!! ou sair para finalizar pedido")

        if (self.prg == 'sim'):
            #Tratando erros
            while True:
                self.qtd_sabor = str(input("\nSerá 1 ou 2 sabores: "))

                if(self.qtd_sabor != '1' or self.qtd_sabor != '2'):
                    try:
                        eval(self.qtd_sabor)
                    except(NameError, ValueError, SyntaxError,TypeError):
                        print("Por favor escolha entre o 1 sabor ou 2 sabores!!!")
                if (self.qtd_sabor == '1' or self.qtd_sabor == '2'):
                    break

            if (self.qtd_sabor == '1'):
                #tratamento de erros, resolver problema de quando é pressionado enter sem nenhum valor
                #desativando a tecla de enter do teclado, so deixar enviar quando tiver valor
                while True:
                    self.sabor = int(input("\nEscolha seu sabor: "))
                    if(self.sabor > 10):
                        print("Digite entre 1 a 10 para escolher o sabor")
                        continue

                    if (self.sabor == 0):
                        print("Digite entre 1 a 10 para escolher o sabor")
                        continue

                    if (self.sabor >= 1 or self.sabor <= 10):
                        break



                #Tomada de decisão
                if (self.sabor == 1):
                    self.sabor = self.s1
                    self.preco = self.v1
                    self.set_bebida()

                elif (self.sabor == 2):
                    self.sabor = self.s2
                    self.preco = self.v2
                    self.set_bebida()

                elif (self.sabor == 3):
                    self.sabor = self.s3
                    self.preco = self.v3
                    self.set_bebida()

                elif (self.sabor == 4):
                    self.sabor = self.s4
                    self.preco = self.v4
                    self.set_bebida()

                elif (self.sabor == 5):
                    self.sabor = self.s5
                    self.preco = self.v5
                    self.set_bebida()

                elif (self.sabor == 6):
                    self.sabor = self.s6
                    self.preco = self.v6
                    self.set_bebida()

                elif (self.sabor == 7):
                    self.sabor = self.s7
                    self.preco = self.v7
                    self.set_bebida()

                elif (self.sabor == 8):
                    self.sabor = self.s8
                    self.preco = self.v8
                    self.set_bebida()

                elif (self.sabor == 9):
                    self.sabor = self.s9
                    self.preco = self.v9
                    self.set_bebida()

                elif (self.sabor == 10):
                    self.sabor = self.s10
                    self.preco = self.v10
                    self.set_bebida()
                #
                # else:
                #     self.sabor = ""
                #
                #     self.preco = 0
                #     self.total = 0

                self.total = self.preco + self.preco_b
                self.teste = "Total"
                print("\nPedido")
                print("| {:<20} | R${} |".format(self.sabor, self.preco))
                print("| {:<20} | R${} | ".format(self.tam_b, self.preco_b))
                print("| {:<20} | R${} |".format(self.teste,self.total))
            elif(self.qtd_sabor == '2'):
                self.set_pedido2()

        elif(self.prg == 'nao'):
            print("Programa fechado")
    #escolhendo dois saboores
    def set_pedido2(self):
            #Tratando erros
            while True:
                self.sabor2 = int(input("\nEscolha seu sabor: "))
                if (self.sabor2 > 10):
                    print("Digite entre 1 a 10 para escolher o sabor")
                    continue

                if (self.sabor2 == 0):
                    print("Digite entre 1 a 10 para escolher o sabor")
                    continue

                if (self.sabor2 >= 1 or self.sabor2 <= 10):
                    break
            # Escolhendo o primeiro sabor

            if (self.sabor2 == 1):
                self.sabor2 = self.s1
                self.preco_s1 = self.v1
            elif (self.sabor2 == 2):
                self.sabor2 = self.s2
                self.preco_s1 = self.v2
            elif (self.sabor2 == 3):
                self.sabor2 = self.s3
                self.preco_s1 = self.v3
            elif (self.sabor2 == 4):
                self.sabor2 = self.s4
                self.preco_s1 = self.v4
            elif (self.sabor2 == 5):
                self.sabor2 = self.s5
                self.preco_s1 = self.v5
            elif (self.sabor2 == 6):
                self.sabor2 = self.s6
                self.preco_s1 = self.v6
            elif (self.sabor2 == 7):
                self.sabor2 = self.s7
                self.preco_s1 = self.v7
            elif (self.sabor2 == 8):
                self.sabor2 = self.s8
                self.preco_s1 = self.v8
            elif (self.sabor2 == 9):
                self.sabor2 = self.s9
                self.preco_s1 = self.v9
            elif (self.sabor2 == 10):
                self.sabor2 = self.s10
                self.preco_s1 = self.v10



            # escolhendo o segundo sabor junto com a escolha de bebida
                # Tratando erros
            while True:
                self.sabor3 = int(input("\nEscolha seu sabor: "))
                if (self.sabor3 > 10):
                    print("Digite entre 1 a 10 para escolher o sabor")
                    continue

                if (self.sabor3 == 0):
                    print("Digite entre 1 a 10 para escolher o sabor")
                    continue

                if (self.sabor3 >= 1 or self.sabor <= 10):
                    break


            if (self.sabor3 == 1):
                self.sabor3 = self.s1
                self.preco_s2 = self.v1
                self.set_bebida()
            elif (self.sabor3 == 2):
                self.sabor3 = self.s2
                self.preco_s2 = self.v2
                self.set_bebida()
            elif (self.sabor3 == 3):
                self.sabor3 = self.s3
                self.preco_s2 = self.v3
                self.set_bebida()
            elif (self.sabor3 == 4):
                self.sabor3 = self.s4
                self.preco_s2 = self.v4
                self.set_bebida()
            elif (self.sabor3 == 5):
                self.sabor3 = self.s5
                self.preco_s2 = self.v5
                self.set_bebida()
            elif (self.sabor3 == 6):
                self.sabor3 = self.s6
                self.preco_s2 = self.v6
                self.set_bebida()
            elif (self.sabor3 == 7):
                self.sabor3 = self.s7
                self.preco_s2 = self.v7
                self.set_bebida()
            elif (self.sabor3 == 8):
                self.sabor3 = self.s8
                self.preco_s2 = self.v8
                self.set_bebida()
            elif (self.sabor3 == 9):
                self.sabor3 = self.s9
                self.preco_s2 = self.v9
                self.set_bebida()
            elif (self.sabor3 == 10):
                self.sabor3 = self.s10
                self.preco_s2 = self.v10
                self.set_bebida()


            self.total_s1 = (self.preco_s1)/2 + (self.preco_s2)/2 + (self.preco_b)
            self.teste_s1 = "Total"
            print("\nPedido")
            print("| 1/2 {:<20} | R${}| \n| 1/2 {:<20} | R${}|".format(self.sabor2,(self.preco_s1)/2,self.sabor3,(self.preco_s2)/2))
            print("| {:<24} | R${}|".format(self.teste_s1,self.total_s1))



    def set_bebida(self):
        #Tratando erro de escolha
        while True:
            self.perg_b = str(input("Deseja bebiba (sim | nao):"))
            if(self.perg_b == 'sim' or self.perg_b == 'nao' or self.perg_b == 'sair'):
                break

            if(self.perg_b != 'sim' or self.perg_b != 'nao'):
                try:
                    eval(self.perg_b)
                except(NameError, ValueError, SyntaxError, AttributeError):
                    print("\nDigite sim ou não!! ou sair para finalizar pedido")

        if(self.perg_b == 'sim'):
            while True:
                self.tam_b = str(input("\n1 - 350Ml\n2 - 500ML\n3 - 1L\n4 - 2L\n\nEscolha o tamanho: "))
                try:
                    eval(self.tam_b)
                except (NameError):
                    print("Digite entre 1 a 5 para escolher o sabor da bebida")

                if (self.tam_b == '1' or self.tam_b == '2' or self.tam_b == '3' or self.tam_b == '4'):
                    break

                if (self.tam_b != '1' or self.tam_b != '2' or self.tam_b != '3' or self.tam_b != '4'):
                    print("Digite entre 1 a 5 para escolher o sabor da bebida")
                    continue

            if(self.tam_b == '1'):
                while True:
                    self.sab_b = str(input("\n1 - Coca-cola\n2 - Sprite\n3 - Fanta\n4 - Guarana\n5 - Pepsi\n\nEscolha o sabor: "))
                    try:
                        eval(self.sab_b)
                    except (AttributeError):
                        print("Digite entre 1 a 5 para escolher o sabor da bebida")

                    if(self.sab_b == '1' or self.sab_b == '2' or self.sab_b == '3' or self.sab_b == '4' or self.sab_b == '5'):
                        break

                    if(self.sab_b != '1' or self.sab_b != '2' or self.sab_b != '3' or self.sab_b != '4' or self.sab_b != '5'):
                        print("Digite entre 1 a 5 para escolher o sabor da bebida")
                        continue



                if (self.sab_b == '1'):
                    self.tam_b = self.b5
                    self.preco_b = self.vb1
                elif (self.sab_b == '2'):
                    self.tam_b = self.b6
                    self.preco_b = self.vb1
                elif (self.sab_b == '3'):
                    self.tam_b = self.b7
                    self.preco_b = self.vb1
                elif (self.sab_b == '4'):
                    self.tam_b = self.b8
                    self.preco_b = self.vb1
                elif (self.sab_b == '5'):
                    self.tam_b = self.b9
                    self.preco_b = self.vb1


            elif (self.tam_b == '2'):
                while True:
                    self.sab_b = str(input("\n1 - Coca-cola\n2 - Sprite\n3 - Fanta\n4 - Guarana\n5 - Pepsi\n\nEscolha o sabor: "))
                    try:
                        eval(self.sab_b)
                    except (AttributeError):
                        print("Digite entre 1 a 5 para escolher o sabor da bebida")

                    if(self.sab_b == '1' or self.sab_b == '2' or self.sab_b == '3' or self.sab_b == '4' or self.sab_b == '5'):
                        break

                    if(self.sab_b != '1' or self.sab_b != '2' or self.sab_b != '3' or self.sab_b != '4' or self.sab_b != '5'):
                        print("Digite entre 1 a 5 para escolher o sabor da bebida")
                        continue


                if (self.sab_b == '1'):
                    self.tam_b = self.b5
                    self.preco_b = self.vb2
                elif (self.sab_b == '2'):
                    self.tam_b = self.b6
                    self.preco_b = self.vb2
                elif (self.sab_b == '3'):
                    self.tam_b = self.b7
                    self.preco_b = self.vb2
                elif (self.sab_b == '4'):
                    self.tam_b = self.b8
                    self.preco_b = self.vb2
                elif (self.sab_b == '5'):
                    self.tam_b = self.b9
                    self.preco_b = self.vb2

            elif (self.tam_b == '3'):
                while True:
                    self.sab_b = str(
                        input("\n1 - Coca-cola\n2 - Sprite\n3 - Fanta\n4 - Guarana\n5 - Pepsi\n\nEscolha o sabor: "))
                    try:
                        eval(self.sab_b)
                    except (AttributeError):
                        print("Digite entre 1 a 5 para escolher o sabor da bebida")

                    if (self.sab_b == '1' or self.sab_b == '2' or self.sab_b == '3' or self.sab_b == '4' or self.sab_b == '5'):
                        break

                    if (self.sab_b != '1' or self.sab_b != '2' or self.sab_b != '3' or self.sab_b != '4' or self.sab_b != '5'):
                        print("Digite entre 1 a 5 para escolher o sabor da bebida")
                        continue

                if(self.sab_b == '1'):
                    self.tam_b = self.b5
                    self.preco_b = self.vb3
                elif (self.sab_b == '2'):
                    self.tam_b = self.b6
                    self.preco_b = self.vb3
                elif (self.sab_b == '3'):
                    self.tam_b = self.b7
                    self.preco_b = self.vb3
                elif (self.sab_b == '4'):
                    self.tam_b = self.b8
                    self.preco_b = self.vb3
                elif (self.sab_b == '5'):
                    self.tam_b = self.b9
                    self.preco_b = self.vb3
            elif (self.tam_b == '4'):
                while True:
                    self.sab_b = str(input("\n1 - Coca-cola\n2 - Sprite\n3 - Fanta\n4 - Guarana\n5 - Pepsi\n\nEscolha o sabor: "))
                    try:
                        eval(self.sab_b)
                    except (AttributeError):
                        print("Digite entre 1 a 5 para escolher o sabor da bebida")

                    if(self.sab_b == '1' or self.sab_b == '2' or self.sab_b == '3' or self.sab_b == '4' or self.sab_b == '5'):
                        break

                    if(self.sab_b != '1' or self.sab_b != '2' or self.sab_b != '3' or self.sab_b != '4' or self.sab_b != '5'):
                        print("Digite entre 1 a 5 para escolher o sabor da bebida")
                        continue

                if(self.sab_b == '1'):
                    self.tam_b = self.b5
                    self.preco_b = self.vb4
                elif (self.sab_b == '2'):
                    self.tam_b = self.b6
                    self.preco_b = self.vb4
                elif (self.sab_b == '3'):
                    self.tam_b = self.b7
                    self.preco_b = self.vb4
                elif (self.sab_b == '4'):
                    self.tam_b = self.b8
                    self.preco_b = self.vb4
                elif (self.sab_b == '5'):
                    self.tam_b = self.b9
                    self.preco_b = self.vb4

            # print("Bebidas")
            # print("{}{}".format(self.tam_b,self.preco_b))


        else:
            self.preco_b = 0
            self.tam_b = ""
            print("Obrigado volte sempre")


    def set_pag(self):
        while True:
            self.pag1 = str(input("1 - Dinheiro\n2 - Debito\n3 - Credito\nQual a forma de pagamento?"))
            try:
                eval(self.pag1)
            except (NameError, ValueError,SyntaxError):
                print("Digite de 1 a 3 para escolher pagamento ou sair para finalizar programa")

            if(self.pag1 == '1' or self.pag1 == '2' or self.pag1 == '3' or self.pag1 == 'sair'):

                break


        if(self.pag1 == '1'):
            print(self.total)
        if (self.pag1 == '2'):
            print(self.total)
        if (self.pag1 == '3'):
            print(self.total)
        # print(self.preco_b)
        # print(self.preco_s1)
        # print(self.preco_s2)






janela = Pizza()
