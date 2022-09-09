"""
¿En qué consiste la Programación Orientada a Objetos?
- En trasladar la naturaleza de los objetos de la vida real a código
de programación, disminuye los errores y promociona la reutilización del código.
Python es un lenguaje orientado a objetos

Los objetos de la realidad tienen características (atributos o propiedades)
y funcionalidades o comportamientos (funciones o métodos).

Ventajas:
- Modularización (división en pequeñas partes) de un programa completo.
- Código fuente muy reutilizable.
- Código fuente más fácil de incrementar en el futuro y mantener.
- Si existe un fallo en una pequeña parte del código el programa completo
no falla.
- Encapsulamiento: Ocultamiento del objeto.
"""


class Persona():
    # Propiedades, características o atributos:
    apellidos = ""
    nombres = ""
    edad = 0
    despierta = False

    # Funcionalidades:
    def despertar(self):
        # self: Parámetro que hace referencia a la instancia perteneciente a la clase.
        self.despierta = True
        print("Buen día.")


persona1 = Persona()
persona1.apellidos = "Gauin Gusñay"
print(persona1.apellidos)
persona1.despertar()
print(persona1.despierta)

persona2 = Persona()
persona2.apellidos = "Chicaiza Mejia"
print(persona2.apellidos)
# persona2.despertar()
print(persona2.despierta)