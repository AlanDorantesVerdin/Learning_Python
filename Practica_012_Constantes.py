""" Practica 12: Constantes en Python """
# Autor: Alan
# Fecha: 2025-09-18

# 1. Definición de constantes con convenciones
print("\n1. DEFINICIÓN DE CONSTANTES")

PI = 3.141592653589793  # Constante: valor de PI (no debería cambiar)
VELOCIDAD_LUZ = 299_792_458  # Velocidad de la luz en metros por segundo

print("PI =", PI)
print("Velocidad de la luz =", VELOCIDAD_LUZ)
print()

# 2. Variables normales (que pueden modificarse)
print("2. VARIABLES NORMALES")

# Declaración de una variable normal
edad = 25
print("Edad inicial:", edad)

# Modificación permitida de la variable normal
edad = 30 
print("Edad después de cambiar:", edad)
print()

# 4. Tuplas para valores inmutables
print("4. USO DE TUPLAS PARA INMUTABILIDAD PARCIAL")

# Una tupla es una estructura de datos inmutable (no se puede cambiar su contenido)
coordenadas_constantes = (100, 200)  # Una tupla con valores que no deben cambiar
print("Coordenadas iniciales:", coordenadas_constantes)

# Intento de cambiar alguno de sus elementos provocaría error:
try:
    # Esto va a fallar porque las tuplas son inmutables
    coordenadas_constantes[0] = 150
except TypeError as e:
    print("Error al intentar modificar tupla:", type(e).__name__, "-", e)
print()

# 5. Uso con Pylint y buenas prácticas
print("5. BUENAS PRÁCTICAS Y CONVENCIONES")

# Esta variable parece constante y está correctamente en mayúsculas
ALTURA_MAXIMA = 2.5

# Variable normal, en minúsculas
altura_usuario = 1.70

print("Constante ALTURA_MAXIMA:", ALTURA_MAXIMA)
print("Variable altura_usuario:", altura_usuario)
print()

# 6. Combinación de constante + variable
print("6. CONSTANTE + VARIABLE EN USO")

# Supongamos un juego donde la puntuación máxima es constante pero el actual puede cambiar
PUNTUACION_MAXIMA = 100
puntaje_actual = 0

print("Puntuación máxima permitida:", PUNTUACION_MAXIMA)
print("Puntaje inicial:", puntaje_actual)

# Simulación de cambio en la puntuación actual
puntaje_actual += 10
print("Puntaje después de ganar puntos:", puntaje_actual)
puntaje_actual += 20
print("Puntaje después de ganar más puntos:", puntaje_actual)
