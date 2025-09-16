""" Practica 2: Introduccion a las variables """
# Autor: Alan
# Fecha: 2024-10-05

# Declaración e impresión de una variable entera sin valor inicial
NUMERO_1 = int()
print(NUMERO_1)

# Reasignación de un valor entero a la misma variable
NUMERO_1 = 10
NUMERO_1 = 20
print(NUMERO_1)

# Reasignación de diferentes tipos de datos a la misma variable
NUMERO_1 = 10
NUMERO_1 = "Alan"
print(NUMERO_1)

# Declaración e impresión de múltiples variables en una sola línea
NUMERO_1, NUMERO_2, NUMERO_3 = 10, 12, 17
print(NUMERO_1, NUMERO_2, NUMERO_3)

# Declaración e impresión de múltiples variables con diferentes tipos de datos en una sola línea
NUMERO_1, NUMERO_2, NUMERO_3 = "Hola", 5, 3.1
print(NUMERO_1, NUMERO_2, NUMERO_3)
