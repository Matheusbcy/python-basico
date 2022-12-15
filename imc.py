nome = 'Victor'
peso = 100
altura = 1.71
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'Pesa {peso} quilos e deu IMC é:'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

if(imc <= 18.5): print("está abaixo so peso")
if(imc > 18.5 and imc <= 24.9): print("Peso normal")
if(imc > 24.9 and imc <= 29.9): print("Sobrepeso")
if(imc > 29.9 and imc <= 34.9): print("Pre-Obeso")
if(imc > 34.9 and imc <= 39.9): print("Obeso 2")
if(imc > 40): print("Obeso 3")

