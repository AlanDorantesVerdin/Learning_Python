""" Practica 10: Valores Literales """
# Autor: Alan
# Fecha: 2024-10-05

# 1. Cadenas literales asignadas
print("\n1. CADENAS LITERALES ASIGNADAS")

frase = "Aprendiendo Python" # Literal que no va a modificarse, asignado a variable
print(frase)

frase = "La frase ha cambiado totalmente" # Reasignación de la variable a otro literal
print(frase)
print()

# 2. Cadenas no literales (con entrada de datos)
print("2. CADENAS NO LITERALES")

nombre = input("Introduzca su nombre: ") # Entrada de datos en una cadena (podra modificarse)
print("Su nombre es: " + nombre)
print()

# 3. Literales numéricos
print("3. LITERALES NUMÉRICOS")

# Asignación de literales numéricos a variables
numero1 = 10
numero2 = 586
print("Número 1 =", numero1, "y Número 2 =", numero2)
print()

# 4. Literal suelto

# La siguiente línea es un valor literal sin soporte (no asignado a variable ni usado)
"Este valor es literal y no tiene soporte, está 'suelto en el código'."

# 5. Comparaciones: literal vs no literal
print("5. COMPARACIONES: LITERAL VS NO LITERAL")

# Literal fijo
saludo_literal = "Hola Mundo"
print("Saludo literal:", saludo_literal)

# No literal
otra_entrada = input("Introduce otro saludo: ")
saludo_completo = saludo_literal + " " + otra_entrada
print("Saludo combinado:", saludo_completo)
