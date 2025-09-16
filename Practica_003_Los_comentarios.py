"""Practica 3: Los comentarios"""
# Autor: Alan
# Fecha: 2024-10-05

# Este es un comentario de una sola línea

# Comentario para explicar una sección de código y dividir en partes 
# def funcion_larga():
    # Primera sección
    # Esta sección hace esto
    # . . .

    # Segunda sección
    # Esta sección hace esto otro
    # . . .

    # Tercera sección
    # Esta sección hace otra cosa más
    # . . . 

# Comentarios al final no afectan la ejecución del código, al inicio si afectan
print("Línea 2") # Comentario cualquiera
# Comentario cualquiera print("Línea 3.")

# Comentario que desactiva una línea de código
# print("Esta línea no se ejecutará")
print("Esta línea se ejecutará")

# Comentario para explicar solo una línea de código
print("Línea 3") # Esta línea imprime "Línea 3"

""" Este es un comentario
de múltiples líneas """

''' Este también es un comentario
de múltiples líneas '''

# Comentario para desactivar un bloque de código
""" Este código está anulado y no se ejecuta
for i in range(10, 0, -1):
    print(i) """

# Docstrings para documentar módulos, clases y funciones
""" docstring del módulo """

class Clase:
    """ docstring de la clase """
    def metodo(self):
        """ docstring del método """

    def funcion():
        """ docstring de la función """
