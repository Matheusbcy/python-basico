# name = 'Matheus'

# print(name[-5])

# print('t' in name)
# print('Z' in name)
# print( 10 * '-')
# print('t' not in name)
# print('Z' not in name)

nome = input('Digite seu nome: ')
encontrar = input('Digite oque deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')