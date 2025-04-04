def tipo_de_letra():
    letra = input().strip()
    vocales = 'aeiouAEIOU'
    if letra.isupper():
        print('uppercase')
    else:
        print('lowercase')
    if letra in vocales:
        print('vowel')
    else:
        print('consonant')
tipo_de_letra()