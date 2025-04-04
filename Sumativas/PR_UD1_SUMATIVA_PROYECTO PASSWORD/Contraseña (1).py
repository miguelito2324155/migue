#passoword Reto


# Que debes de poner
print("El password debe cumplir estos requisitos:")
print("- Tener entre 6 y 8 caracteres.")
print("- Empezar con un número.")
print("- El segundo carácter debe ser una letra minúscula.")
print("- El tercero una letra mayúscula.")
print("- El cuarto debe ser uno de estos símbolos: * # / % &.")
print("- El quinto debe ser una letra minúscula.")
print("- El resto deben ser números.")

# Pon la contraseña
password = input("Introduce tu password: ")



# Comprobaciones básicas
if len(password) < 6 or len(password) > 8:
    print(f"Error: el password tiene una longitud de {len(password)} caracteres.")
else:
    if not password[0].isdigit():
        print("Error en el carácter 1: debe ser un número.")
    if not password[1].islower():
        print("Error en el carácter 2: debe ser una letra minúscula.")
    if not password[2].isupper():
        print("Error en el carácter 3: debe ser una letra mayúscula.")
    if password[3] not in '*#/%&':
        print("Error en el carácter 4: debe ser uno de estos símbolos: * # / % &.")
    if not password[4].islower():
        print("Error en el carácter 5: debe ser una letra minúscula.")
    if not password[5:].isdigit():
        print("Error en los caracteres restantes: deben ser números.")
    else:
        print("El formato del PASSWORD es correcto.")
