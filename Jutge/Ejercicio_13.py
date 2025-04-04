def comparar_palabras():
    palabras = input().strip().split()
    a, b = palabras[0], palabras[1]
    if a < b:
        print(f"{a} < {b}")
    elif a > b:
        print(f"{a} > {b}")
    else:
        print(f"{a} = {b}")
comparar_palabras()