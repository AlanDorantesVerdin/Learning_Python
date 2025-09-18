""" Practica 13: Tuplas en Python """
# Autor: Alan
# Fecha: 2025-09-18

# 1. Sintaxis de tupla
print("\n1. SINTAXIS DE TUPLA")

# Una tupla es una colección (como una lista) ordenada e inmutable de elementos.
# Se define normalmente usando paréntesis ().
tupla_colores = ("rojo", "verde", "azul")
print("Tupla de colores:", tupla_colores)  
print() 

# 2. Acceder a elementos por índice
print("2. ACCEDER A ELEMENTOS POR ÍNDICE")

# Igual que en listas, los índices comienzan en 0
# Aquí accedemos al tercer elemento (índice 2)
print("Elemento en índice 2:", tupla_colores[2])
print()

# 3. Métodos de lectura: index()
print("3. MÉTODO index()")

# index(valor) devuelve la posición de la primera aparición de 'valor'
pos_rojo = tupla_colores.index("rojo")
print("Posición de 'rojo':", pos_rojo)
print() 

# 4. Método count()
print("4. MÉTODO count()")

# count(valor) indica cuántas veces aparece 'valor' dentro de la tupla
tupla_multiples = ("rojo", "verde", "azul", "rojo", "amarillo")
cuenta_rojo = tupla_multiples.count("rojo")
print("En tupla_multiples:", tupla_multiples)
print("Número de veces que 'rojo' aparece:", cuenta_rojo)
print() 

# 5. Intentos de métodos mutadores (errores)
print("5. MÉTODOS MUTADORES NO DISPONIBLES (pop, append, remove)")

# Las tuplas son inmutables, por eso no poseen métodos que modifiquen su contenido
# (como pop, append o remove). Intentar usarlos provoca AttributeError.
try:
    tupla_colores.pop()  # No existe en tuplas → AttributeError
except AttributeError as e:
    print("Error capturado:", type(e).__name__, "-", e)

try:
    tupla_colores.append("amarillo")  # No existe en tuplas → AttributeError
except AttributeError as e:
    print("Error capturado:", type(e).__name__, "-", e)

try:
    tupla_colores.remove("rojo")  # No existe en tuplas → AttributeError
except AttributeError as e:
    print("Error capturado:", type(e).__name__, "-", e)
print()  

# 6. Desempaquetado básico de tupla
print("6. DESEMPAQUETADO BÁSICO")

# El desempaquetado permite asignar cada elemento de la tupla a una variable
numeros = (10, 20, 30, 40)
numero_1, numero_2, numero_3, numero_4 = numeros  # Cantidades deben coincidir
print("numero_1:", numero_1) # Imprime el primer dato de la tupla
print("numero_2:", numero_2) # Imprime el segundo dato de la tupla
print("numero_3:", numero_3) # Imprime el tercer dato de la tupla
print("numero_4:", numero_4) # Imprime el cuarto dato de la tupla
print()

# 7. Desempaquetado con error por cantidad no coincidente
print("7. DESEMPAQUETADO CON ERROR (demasiados valores)")

# Si el número de variables no coincide con los elementos, se produce ValueError
try:
    numero_a, numero_b = numeros  # Aquí hay 4 valores pero solo 2 variables
except ValueError as e:
    print("Error capturado:", type(e).__name__, "-", e)
print()

# 8. Desempaquetado capturando exceso con operador * 
print("8. DESEMPAQUETADO CON EXCESO")

# Usando *nombre se capturan los elementos restantes en una lista
numero_x, numero_y, *resto = numeros
print("numero_x:", numero_x) # Imprime el primer dato de la tupla
print("numero_y:", numero_y) # Imprime el segundo dato de la tupla
print("resto (lista con valores restantes):", resto) # Imprime el resto de datos en una lista
print()

# 9. Variante: usar lista vacía explícita antes de desempaquetar
print("9. VARIANTE CON LISTA VACÍA PREDECLARADA")

# Se puede predeclarar la variable que recibirá el resto; igualmente será una lista
# Esto no es necesario pero puede mejorar la claridad del código
resto2 = []  # Inicialización explícita
numero_p, numero_q, *resto2 = numeros
print("numero_p:", numero_p) 
print("numero_q:", numero_q)
print("resto2:", resto2)
print()

# 10. Tuplas anidadas
print("10. TUPLAS ANIDADAS")

# Una tupla puede contener otras tuplas como elementos
tupla_anidada = (1, 2, (3, 4), (5, 6, 7))
print("Tupla anidada:", tupla_anidada)

# Se pueden acceder a elementos de tuplas anidadas usando múltiples índices
print("Elemento en tupla anidada:", tupla_anidada[2][1])  # Accede al 4 el índice 1 de la tupla (3,4), índice 2
print()

# 11. Conversión entre listas y tuplas
print("11. CONVERSIÓN ENTRE LISTAS Y TUPLAS")

# La lista es mutable, la tupla no. A veces es útil convertir entre ambas.
# Se puede convertir una lista en tupla usando tuple()
lista_frutas = ["manzana", "banana", "cereza"]
tupla_frutas = tuple(lista_frutas)
print("Tupla de frutas:", tupla_frutas)

# Se puede convertir una tupla en lista usando list()
tupla_verduras = ("lechuga", "tomate", "pepino")
lista_verduras = list(tupla_verduras)   
print("Lista de verduras:", lista_verduras)
print()
