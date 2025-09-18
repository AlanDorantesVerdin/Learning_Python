""" Practica 11: Listas """
# Autor: Alan
# Fecha: 2025-09-10

# 1. Lista con distintos tipos de datos
print("\n1. LISTA CON DISTINTOS TIPOS DE DATOS")

# Una lista puede contener distintos tipos: cadenas, enteros, etc.
camiseta = ["rojo", "L", 100, 10]

# Para imprimir la lista completa solo hay que usar:
print(camiseta)
print() 

# 2. Índices y reasignación
print("2. ÍNDICES Y REASIGNACIÓN")

# La lista tiene índices que empiezan en 0, en este caso 0 es "azul", 1 es "verde" y 2 es "rojo"
colores = ["azul", "verde", "rojo"]
print("Lista original:", colores)

# Las listas son mutables: se puede cambiar un elemento accediendo por su índice
colores[0] = "amarillo"  # Reasignación del elemento en la posición 0
print("Lista después de reasignación:", colores)
print()

# 3. Error por índice inexistente o fuera de rango
print("3. ERROR POR ÍNDICE INEXISTENTE")

# Acceder o intentar modificar un índice que no existe provoca un IndexError
colores_error = ["azul", "verde", "rojo"]
print("Lista original:", colores_error)

# Se muestra el error controladamente al intentar acceder a un índice fuera de rango
try:
    colores_error[7] = "amarillo"  # Índice 7 no existe (la lista solo tiene 3 elementos)
except IndexError as e:  # Se captura el error para mostrar un mensaje controlado
    print("Error capturado:", e)
print()

# 5. Método append()
print("5. MÉTODO APPEND()")

# append() añade un nuevo elemento al final de la lista
colores_append = ["azul", "verde", "rojo"]
colores_append.append("amarillo")  # Se agrega un cuarto color 
print("Lista después de append:", colores_append)
print()

# 6. Método insert()
print("6. MÉTODO INSERT()")

# insert(posicion, valor) inserta el valor en la posición indicada desplazando los elementos a la derecha
colores_insert = ["azul", "verde", "rojo"]
colores_insert.insert(0, "amarillo")  # Inserta al inicio (posición 0)
print("Insert en posición 0:", colores_insert)

# Si el índice indicado es mayor que la longitud, Python lo agrega al final
colores_insert2 = ["azul", "verde", "rojo"]
colores_insert2.insert(7, "amarillo")  # Índice fuera de rango, se coloca al final
print("Insert en posición 7:", colores_insert2)
print()

# 7. Método extend() y concatenación
print("7. MÉTODO EXTEND() Y CONCATENACIÓN")

# extend() añade todos los elementos de otra lista al final (modifica la lista original)
colores1 = ["azul", "verde", "rojo"]
colores2 = ["amarillo", "naranja", "marrón"]
colores1.extend(colores2)  # Se fusionan los colores en una sola lista
print("Lista extendida:", colores1)

# También se puede unir listas con el operador + (crea una nueva lista con concatenación)
colores1 = ["azul", "verde", "rojo"]
colores2 = ["amarillo", "naranja", "marrón"]
colores_concat = colores1 + colores2  # Nueva lista con la concatenación
print("Lista con concatenación:", colores_concat)
print()

# 8. Método pop() sin argumento
print("8. MÉTODO POP() SIN ARGUMENTO")

# pop() sin argumentos elimina y devuelve el último elemento
colores_pop = ["azul", "verde", "rojo"]
colores_pop.pop()  # Se elimina "rojo"
print("Lista después de pop():", colores_pop)
print()

# 9. Método pop() con índice
print("9. MÉTODO POP() CON ÍNDICE")

# pop(indice) elimina y devuelve el elemento en la posición especificada
colores_pop2 = ["azul", "verde", "rojo"]
colores_pop2.pop(0)  # Se elimina el primer elemento ("azul")
print("Lista después de pop(0):", colores_pop2)
print()

# 10. Método remove()
print("10. MÉTODO REMOVE()")

# remove(valor) elimina la primera aparición del valor indicado
colores_remove = ["azul", "verde", "rojo"]
colores_remove.remove("rojo")  # Se elimina "rojo"
print("Lista después de remove('rojo'):", colores_remove)

# remove(valor) genera error si el valor no existe
try:
    colores_remove.remove("amarillo")  # "amarillo" no está en la lista
except ValueError as e:
    print("Error capturado:", e)
print()

# 11. Remove con duplicados
print("11. REMOVE CON DUPLICADOS")

# Cuando hay valores duplicados, remove() solo elimina la primera coincidencia cada vez
colores_duplicados = ["rojo", "azul", "rojo", "verde", "rojo"]
print("Lista original:", colores_duplicados)

colores_duplicados.remove("rojo")  # Elimina el primer "rojo"
print("Después del primer remove:", colores_duplicados)

colores_duplicados.remove("rojo")  # Elimina el siguiente "rojo"
print("Después del segundo remove:", colores_duplicados)

colores_duplicados.remove("rojo")  # Elimina el último "rojo"
print("Después del tercer remove:", colores_duplicados)
print()

# 12. Método index()
print("12. MÉTODO INDEX()")

# index(valor) devuelve la posición de la primera aparición del valor indicado
numeros = [87, 10, 5, 7, 378, 10, 10, 65, 10]
busca_numero = numeros.index(10)  # Primer 10 aparece en índice 1
print("Primera posición de 10:", busca_numero)

# index(valor) genera error si el valor no existe
try:
    busca_numero_inexistente = numeros.index(1000)  # 1000 no está en la lista
except ValueError as e:
    print("Error capturado:", e)
print()

# 13. Método count()
print("13. MÉTODO COUNT()")

# count(valor) devuelve cuántas veces aparece el valor en la lista
numeros = [87, 10, 5, 7, 378, 10, 10, 65, 10]
coincidencias = numeros.count(10)  # Total de veces que aparece 10
print(f"Coincidencias de 10:", coincidencias)

# Si el valor no existe, devuelve 0 sin error
coincidencias2 = numeros.count(1000)  # No existe → 0
print(f"Coincidencias de 1000:", coincidencias2)
