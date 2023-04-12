contador = 0

while contador < 100:
    contador += 1
    
    if contador >= 40 and contador <= 69:
        continue

    print(f'contador: {contador}')

print('Acabou')