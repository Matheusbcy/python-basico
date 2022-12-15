first_value = input('Digite um valor: ')
secondary_value = input('Digite outro valor: ')

first_int = int(first_value)
secondary_int = int(secondary_value)

if first_int > secondary_int:
    print(f'{first_int} é maior que o {secondary_int}')
else:
    print(f'{secondary_int} é maior que o {first_int}')


