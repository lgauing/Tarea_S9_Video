def operador_ternario ():
    """
    String sexo;
    sexo = (11 > 30) ? "Masculino" : "Femenino";
    """

    sexos = ("Hobre", "Mujer")

    posicion = True
    sexo = sexos[posicion] # Mujer
    print(sexo)
    sexo = sexos[not posicion] # Hombre
    print(sexo)