class Cuenta():

    def __init__(self, propi, sld, mnda):
        self.__propietario = propi
        self.__saldo = sld
        self.__moneda = mnda

    # Getters (métodos GET)
    def get_Saldo(self):
        return self.__saldo

    def get_Propietario(self):
        return self.__propietario

    def get_Moneda(self):
        return self.__moneda

    # Setters (métodos SET)
    def set_Moneda(self, moneda):
        self.__moneda = moneda


cuenta1 = Cuenta("Oscar García", 15000, "Sucres"
                                        "")
print(cuenta1.get_Saldo())
print(cuenta1.get_Moneda())
cuenta1.set_Moneda("Dólares")
print(cuenta1.get_Moneda())
