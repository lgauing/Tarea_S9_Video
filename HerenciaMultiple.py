class ClaseA():

    def __init__(self, pmtro1, pmtro2):
        self.parametro1 = pmtro1
        self.parametro2 = pmtro2


class ClaseB():

    def __init__(self, parm3, parm4, parm5):
        self.parametro3 = parm3
        self.parametro4 = parm4
        self.parametro5 = parm5


class ClaseX(ClaseA, ClaseB):
    pass


cX1 = ClaseX(17, 23)
