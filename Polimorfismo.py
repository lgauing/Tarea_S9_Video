# Polimorfismo (poli => muchas / morfos: formas)

class Alumno():

    def describir(self):
        print("Soy un excelente alumno.")


class Docente():

    def describir(self):
        print("Me dedico a enseñar metodos nuevos de enseñanza.")


class Trabajador():

    def describir(self):
        print("Trabajo dentro de mi propia empresa.")


def describirPersona(persona):
    persona.describir()


doc1 = Trabajador()
describirPersona(doc1)
