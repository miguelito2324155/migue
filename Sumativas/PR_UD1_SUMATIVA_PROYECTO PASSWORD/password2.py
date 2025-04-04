# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:06:23 2024

@author: RomeroRamosMiguel
"""

# Versión 2 de Password

# Explicación de los requisitos
# Esto muestra las reglas que debe seguir el password
print("El password debe cumplir estos requisitos:")
print("- Contener al menos 3 números.")
print("- Contener al menos 3 letras (distinguiendo mayúsculas y minúsculas).")
print("- Contener al menos 2 símbolos (por ejemplo: * # / % &).")

# Funciones de comprobación
# Esta función revisa si un password cumple las reglas

def verificar_password(password):
    numeros = 0  # Contar los números
    letras_minusculas = 0  # Contar letras minúsculas
    letras_mayusculas = 0  # Contar letras mayúsculas
    simbolos = 0  # Contar los símbolos

    # Recorremos cada carácter del password
    # Revisamos qué tipo de carácter es
    for char in password:
        if char.isdigit():  # Si es un número
            numeros += 1
        elif char.islower():  # Si es una letra minúscula
            letras_minusculas += 1
        elif char.isupper():  # Si es una letra mayúscula
            letras_mayusculas += 1
        elif char in "*#/%&":  # Si es un símbolo
            simbolos += 1

    # Validamos los criterios
    # Revisamos si se cumplen los requisitos mínimos
    cumple_numeros = numeros >= 3
    cumple_letras = (letras_minusculas + letras_mayusculas) >= 3
    cumple_simbolos = simbolos >= 2

    return cumple_numeros and cumple_letras and cumple_simbolos

# Variables para conteo de passwords correctos e incorrectos
# Guardamos cuántos passwords son correctos e incorrectos
correctos = 0
incorrectos = 0

# Permitir al usuario introducir hasta 3 passwords
# Pedimos 3 passwords al usuario y los revisamos
for i in range(1, 4):
    password = input(f"Introduce el password {i}: ")  # Pedimos un password
    if verificar_password(password):  # Si cumple las reglas
        print("El password cumple con los requisitos.")
        correctos += 1
    else:  # Si no cumple las reglas
        print("El password NO cumple con los requisitos.")
        incorrectos += 1

# Mostrar resultados finales
# Decimos cuántos passwords fueron correctos e incorrectos
print("\nResultados finales:")
print(f"Passwords correctos: {correctos}")
print(f"Passwords incorrectos: {incorrectos}")

# Ejemplo de pruebas para testear el código
# Puedes copiar estas pruebas y pegarlas para comprobar diferentes casos
# Ejemplo 1: 123Ab* (No cumple)
# Ejemplo 2: a1B* (NO cumple)
# Ejemplo 3: 12abcDEF## (NO cumple)