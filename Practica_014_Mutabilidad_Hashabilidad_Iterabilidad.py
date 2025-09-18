""" Practica 14: Mutabilidad, Iterabilidad y Hashabilidad"""
# Autor: Alan
# Fecha: 2025-09-18

# 1. Mutabilidad: objetos que permiten cambio interno
print("\n1. MUTABILIDAD")

# Las listas son mutables: permiten cambiar sus elementos sin crear un nuevo objeto
lista = [10, 10, 30, 40] 
print("Lista original:", lista)

# Mutación: se modifica el valor en el índice 1
lista[1] = 20  
print("Después de cambiar indice 1 a 20:", lista)
print()

# 2. Inmutabilidad: tipos que no permiten modificación interna
print("2. INMUTABILIDAD")

# Tupla (inmutable): no permite reasignar elementos por índice
tupla = (10, 10, 30, 40)  
print("Tupla original:", tupla)

try:
    tupla[1] = 20  # Provoca TypeError porque las tuplas no soportan asignación por índice
except TypeError as e:
    print("Error capturado:", type(e).__name__, "-", e)
print()

# 3. Cadenas como objetos inmutables
print("3. CADENAS Y ACCESO POR ÍNDICE")

# Una cadena (str) es inmutable, pero se puede acceder a sus caracteres por índice
saludo = "Hola"  
print("Caracteres de saludo:", saludo[0], saludo[1], saludo[2], saludo[3])
print()

# Intento de modificar cadena
print("3b. INTENTO DE MODIFICAR CADENA (NO PERMITIDO)")
try:
    saludo[0] = "h"  # No es posible alterar un carácter en un str; se requiere crear otro str
except TypeError as e:
    print("Error capturado:", type(e).__name__, "-", e)
print()

# Reasignación de variable a otro string, no es un cambio en la cadena, es un cambio del valor de la variable
print("3c. REASIGNACIÓN DE VARIABLE A OTRO STRING")
saludo = "Adiós"  # Se crea un nuevo str y la variable ahora referencia ese nuevo objeto
print("Nuevo saludo:", saludo)
print()

# 4. Hashabilidad: qué objetos son hashables y cuáles no
print("4. HASHABILIDAD")

# Un objeto es hashable si su valor no cambia (inmutable) y define __hash__()
# Hash es una función que devuelve un entero representando el objeto
saludo = "Hola"  
print("Hash de saludo (string):", hash(saludo))

# Aunque cambiemos la variable, el string original sigue teniendo el mismo hash
bienvenido = "Hola"
print("Hash de bienvenido (otro string con mismo contenido):", hash(bienvenido))

# Las listas no son hashables porque son mutables
numeros = [10, 20, 30]  
try:
    print("Hash de lista numeros:", hash(numeros))  # No hashable → error
except TypeError as e:
    print("Error capturado:", type(e).__name__, "-", e)
print()

# 5. Iterabilidad: objetos que se pueden recorrer por índice
print("5. ITERABILIDAD")

numeros2 = [10, 20, 30]  # Las listas son iterables y permiten acceso por índice
print("Elemento posición 0 de la lista numeros2:", numeros2[0])
print()

# Objeto no iterable via índice
print("5b. INTENTO DE ACCEDER POR ÍNDICE EN UN INT (NO ITERABLE)")
numero_simple = 10  # Los enteros no son contenedores; no soportan indexación
try:
    print(numero_simple[0])
except TypeError as e:
    print("Error capturado:", type(e).__name__, "-", e)
print()
