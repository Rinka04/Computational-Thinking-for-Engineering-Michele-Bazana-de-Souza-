# exercicio 

""" vel = int(input (" Velocidadce do carro em km/h+ "))
if vel > 80 :
    print("Você foi multado")
    multa = (vel -80) * 5
    print (f"0 valor da milta é R${multa: .2f}")"""

#exercicio 2

num1 = float(input("Numero 1 = "))
num2 = float(input("Numero 2 = "))
num3 = float(input("Numero 3 = "))

maior = num1
if num2 >= num1 and num2 >= num3:
    maior - num2
if num3>= num1 and num3 >= num2:
    maior = num3

    print(maior)
menor = num1
if num2 <= num1 and num2 <= num3:
    menor = num2
if num3 <= num1 and num3 <= num2:
    menor = num1

    print(f"Maior = {maior}")
    print (f"Menor = {menor}")
    