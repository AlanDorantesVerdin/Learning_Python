""" Practica 8: Entrada y salida de datos """
# Autor: Alan
# Fecha: 2024-10-05

# 1. Print() usando varios objetos
print("1. Print con varios objetos:")

# Se imprimen distintos tipos de datos separados por comas
print("El resultado","de sumar",10,"más",50.65,"es:",10+50.65)
print()

# El parametro sep es el separador entre los objetos (por defecto es un espacio)
print("El resultado", "de sumar", 10, "más", 50.65, "es:", 10 + 50.65, sep="-")
print()

# 2. El salto de línea
print("2. Salto de línea:")

# Por defecto print() añade un salto de línea al final pero nosotros podemos añadir más con "\n"
print("Línea 1\n" + "Línea 2\n" + "Línea 3")
print()

# 3. Funcion input() para pedir datos al usuario
print("3. Funcion input() para ingresar datos:")

# Se pide al usuario que ingrese su nombre y se almacena en la variable nombre
nombre = input("Por favor, introduce tu nombre: ")
print("Gracias, el nombre es: " + nombre + ".") # Se puede usar la variable posteriormente
print()

# 4. Variante con salto de línea en el prompt del input
print("4. Variante con salto de línea:")
nombre2 = input("Por favor, introduce tu nombre:\n")
print("El nombre almacenado es: " + nombre2 + ".")
print()

# 5. Suma de dos entradas con input()
print("5. Suma de dos entradas (como cadenas):")

# Las entradas se tratan como cadenas de texto
numero_1 = input("Introduce el primer número a sumar: ")
numero_2 = input("Introduce el segundo número a sumar: ")

# La suma de cadenas concatena las cadenas en lugar de sumar los valores numéricos
suma = numero_1 + numero_2
print("Resultado (como cadenas):", suma)
print()

# 6. Suma de dos entradas convertidas a enteros
print("6. Suma de dos entradas (convertidas a enteros):")

# Convertir las entradas a enteros usando int()
numero_1 = int(input("Introduce el primer número a sumar: "))
numero_2 = int(input("Introduce el segundo número a sumar: "))

# La suma de enteros suma los valores numéricos
suma = numero_1 + numero_2
print("Resultado (como enteros):", suma)
