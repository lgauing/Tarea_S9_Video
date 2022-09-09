class Curso():
    """
    nombre = "Lenguaje"
    creditos = 5
    profesion = "Escritor"
    """

    # Estado inicial del objeto:
    def __init__(self, nom, cred, prof):
        self.nombre = nom
        self.creditos = cred
        self.profesion = prof
        self.__imparticion = "Online"  # Propiedad encapsulada.

    def mostrarDatos(self):
        dat = "Nombre: {0} / Créditos: {1} / Modo de impartición: {2}"
        print(dat.format(self.nombre, self.creditos, self.__imparticion))
        docenteAsignado = self.__verificarDocente()
        if docenteAsignado:
            print("Existe docente asignado.")
        else:
            print("No es necesario asignar un docente...")

    def __verificarDocente(self):
        # print("Verificando si existe docente asignado...")
        if self.__imparticion == "Online":
            return True
        else:
            return False

    # toString()
    def __str__(self):
        texto = "Nombre: {0} - Créditos: {1}"
        return texto.format(self.nombre, self.creditos)


curso1 = Curso("Lenguaje", 5, "Escritor")
print(curso1)
curso1.mostrarDatos()

# curso2 = Curso("Ciencias", 4, "Escritor")
# print(curso2.nombre)
