class Moto:
    def __init__(self):
        per = str(input("Deseja calcular gasto da gasolina (sim / nao): "))
        if(per == 'sim'):
            gasolina = float(input("Digite o valor da gasolina: "))
            tanque = int(input("Digite o tamanho do tanque: "))
            gasto = float(tanque * gasolina)


            ant_rodado = float(input("Informe a quilometragem: "))
            dep_rodado = float(input("Informe a quilometragem rodada: "))



            consumo = dep_rodado / tanque


            print("\nA média por litro é de {0:.0f}KM/L".format(consumo))
            print("\no gasto em gasolina é de R${0:.2f}".format(gasto))







Moto()