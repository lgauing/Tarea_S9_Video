class Persona():

    def __init__(self, apePtno, apeMtno, nomb):
        self.apellidoPaterno = apePtno
        self.apellidoMaterno = apeMtno
        self.nombres = nomb

    def mostrarNombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def datos(self):
        print(self.mostrarNombreCompleto())


class Estudiante(Persona):

    def __init__(self, apePtno, apeMtno, nomb, pro):
        super().__init__(apePtno, apeMtno, nomb)
        self.profesion = pro

    def datos(self):
        super().datos()
        print("Profesión: {0}".format(self.profesion))


estu1 = Estudiante("Gauin", "Gusñay", "Lady", "Ingeniería en Sotware")
per1 = Persona("Gauin", "Gusñay", "Lady")
print(estu1.mostrarNombreCompleto())
print(estu1.profesion)
estu1.datos()
print(isinstance(per1, Estudiante))
