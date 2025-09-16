""" Practica 5: Las palabras reservadas """
# Autor: Alan
# Fecha: 2024-10-05

# No se puede usar una palabra reservada como nombre de variable (descomentar para ver el error) 
# global = 10
# Sin embargo, se puede usar con un prefijo o sufijo
variable_global = 10

# Imprimir la lista de palabras reservadas en Python para conocerlas
import keyword
print(keyword.kwlist)

# Tambien esta las soft keywords (palabras reservadas suaves)
# Son palabras reservadas pero que no generan error si se usan como nombres de variables
match = 5 