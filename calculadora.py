while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite um operador: ')
    operador = input('Digite o operador (+-/*): ')

    numero_validos = None
    nume_1_float = 0
    nume_2_float = 0

    try:
        nume_1_float = float(numero_1)
        nume_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números são invalidos!')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador digitado invalido!')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue

    print('Realizando sua conta. Confira resultado abaixo')
    if operador == '+':
        print(f'Soma de {nume_1_float} + {nume_2_float} = {nume_1_float + nume_2_float}')
    elif operador == '-':
        print(f'Substração de {nume_1_float} - {nume_2_float} = {nume_1_float - nume_2_float}')
    elif operador == '/':
        print(f'Divisão de {nume_1_float} / {nume_2_float} = {nume_1_float / nume_2_float}')
    elif operador == '*':
        print(f'Multiplicação de {nume_1_float} * {nume_2_float} = {nume_1_float * nume_2_float}')
    else:
        print('Nunca deveria chegar aqui')
        
    sair = input('Quer sair [s]im? ').lower().startswith('s')

    if sair is True:
        break


