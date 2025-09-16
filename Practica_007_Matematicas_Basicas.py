""" Practica 7: Matematicas basicas """
# Autor: Alan
# Fecha: 2024-10-05

# 1. Operador suma (+)
print("1. SUMA")

# Calcula la suma de dos o más números con + y la imprime
print("Suma de 20 y 50:", 20 + 50)
print("Suma de 30, 70, 100 y 200:", 30 + 70 + 100 + 200)

# Tambien sirve para concatenar cadenas de texto
print("Hola, " + "soy Alan")
print()

# 2. Guardar operación en variable e imprimirla
print("2. SUMA EN VARIABLE")

# Guardar el resultado en una variable sirve para usarlo posteriormente
operacion = 20 + 50
print("Suma de 20 y 50 (operacion):", operacion)

# Se puede usar la variable en otras operaciones
print("Suma de operacion y 100:", operacion + 100)
print()

# 3. Operador resta (-)
print("3. RESTA")

# Calcula la diferencia de dos números con - y la guarda en una variable
operacion = 10 - 4
print("Resta de 10 y 4:", operacion)
print()

# 4. Operador multiplicación (*)
print("4. MULTIPLICACIÓN")

# Calcula el producto de dos números con * y lo guarda en una variable
operacion = 10 * 4
print("Multiplicación de 10 y 4:", operacion)
print()

# 5. Operador división (/)
print("5. DIVISIÓN")

# Calcula el cociente de dos números con / y lo guarda en una variable
operacion = 10 / 3
print("División de 10 y 3:", f"{operacion:.2f}") # Mostrar con 2 decimales
print()

# 6. Operaciones múltiples y mixtas
print("6. OPERACIONES MIXTAS")

# Se pueden combinar varios operadores en una sola operación, se respeta la prioridad de operadores
operacion = 100 * 98 + 65 * 2 - 10 / 5
print("Resultado de la operación mixta:", operacion)
print()

# 7. Operar con nombres de variables
print("7. VARIABLES EN OPERACIONES")

# Se pueden usar variables, que contengan numeros, en las operaciones matemáticas
numero1 = 100
numero2 = 500
resultado = numero1 + numero2
print("Suma de numero1 (100) y numero2 (500):", resultado)
print()

# 8. Operador módulo (%)
print("8. MÓDULO (resto de la división)")
numero1 = 10
numero2 = 3

# La division normal (/) nos da el resultado o cociente (con decimales)
cociente = numero1 / numero2

# El operador módulo (%) nos da el resto de la división
resto = numero1 % numero2

print("Cociente:", f"{cociente:.2f}") # Mostrar con 2 decimales
print("Resto:", resto)

# El operador módulo (%) también funciona con números decimales 
numero1 = 7.5
numero2 = 3
resto = numero1 % numero2
print("Resto con decimales:", resto)
print()

# 9. División entera (//)
print("9. DIVISIÓN ENTERA (//)")
numero1 = 10
numero2 = 3

# La división normal (/) nos da el resultado o cociente (con decimales)
division = numero1 / numero2

# La división entera (//) nos da el cociente sin decimales (parte entera)
division_entera = numero1 // numero2

print("División normal:", f"{division:.2f}") # Mostrar con 2 decimales
print("División entera:", division_entera)
print()

# 10. Ejercicio de media de edades
print("10. MEDIA DE EDADES (EJERCICIO)")

edades = [15, 26, 54, 22, 17, 50, 33, 32] # Lista de edades
suma_edades = sum(edades) # Suma de todas las edades de la lista
numero_edades = len(edades) # Número de edades en la lista, elementos de la lista

# Calculo de la media (promedio) de edades con división normal
media = suma_edades / numero_edades
print("En total hay:", numero_edades, "edades en la media.")
print("La edad media (float) es:", media)

# Calculo de la media (promedio) de edades con división entera
media_entera = suma_edades // numero_edades
print("La edad media (entera) es:", media_entera)
print()

# 11. Potencias (**)
print("11. POTENCIAS")

# Calculo de la potencia 2 elevado a 10 sin usar el operador **
operacion = 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 # 2 multiplicado 10 veces
print("2 elevado a 10 (multiplicando):", operacion)

# Calculo de la potencia 2 elevado a 10 usando el operador **
operacion = 2 ** 10 # 2 elevado a la 10
print("2 elevado a 10 (**):", operacion)

# Calculo de una potencia muy grande
operacion = 2 ** 5000
print("2 elevado a 5000:", operacion)
print()

# 12. Prioridad de operaciones y paréntesis
print("12. PRIORIDAD Y PARÉNTESIS")

# La multiplicación y división tienen mayor prioridad que la suma y resta
operacion = 10 + 6 * 2
print("10 + 6 * 2:", operacion)

# En este caso, los paréntesis cambian la prioridad de las operaciones, estos tienen mayor prioridad
operacion = (10 + 6) * 2
print("((10 + 6) * 2):", operacion)

# La potencia se realiza primero al tener mayor prioridad que la multiplicación y división
operacion = 2 ** 10 / 2
print("2 ** 10 / 2 =", operacion)

# Los paréntesis cambian la prioridad, se realiza primero la división y luego la potencia
operacion = 2 ** (10 / 2)
print("2 ** (10 / 2) =", operacion)
print()

# 13. Números largos y guiones bajos
print("13. NÚMEROS LARGOS")

# Los números largos se pueden escribir con guiones bajos para mejorar la legibilidad sin afectar su valor
numero_largo = 56404357843987
print("Sin guiones bajos:", numero_largo)
numero_largo = 56_404_357_843_987
print("Con guiones bajos:", numero_largo)

# Esto también funciona con números decimales
numero_largo = 56_404_357_843.78
print("Número con decimales:", numero_largo)
numero_largo = 56_404_357_843.7_865_657
print("Número con guiones en decimales:", numero_largo)
