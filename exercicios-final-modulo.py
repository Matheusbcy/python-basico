# EXERCICIO UM

numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    if numero_int % 2 == 1:
        print('Número é impar')
    if numero_int % 2 == 0:
        print('Número é par')
else:
    print('Você não digitou um número inteiro.')

# EXERCICIO DOIS

horas = input('Digite as horas nesse momento: ')

try:
    horas_int = int(horas)
    if horas_int >= 0 and horas_int <= 5:
        print('Boa Madrugada!')
    elif horas_int >= 6 and horas_int < 12:
        print('Bom dia!')
    elif horas_int >= 12 and horas_int <= 18:
        print('Boa tarde!')
    elif horas_int > 18 and horas_int < 23:
        print('Boa Noite')
except:
    print('Por favor digite um número!')

# EXERCICIO TRES

primeiro_nome = input('Digite seu primeiro nome: ')

if len(primeiro_nome) > 1:
    if len(primeiro_nome) <= 4:
        print('Seu nome é curto')
    elif len(primeiro_nome) >= 5 and len(primeiro_nome) <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é grandão')
else:
    print('Digite mais de uma letras!')