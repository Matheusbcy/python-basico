
palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = ''
while True:
    letra_digitada = input("Digite a letra que voce acha que existe na palavra secreta: ")

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            print(letra_secreta)
        else:
            print("*")