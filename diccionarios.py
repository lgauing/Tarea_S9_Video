def diccionarios ():

    miDiccionario = {"Ecuador": "Guayaquil", "España": "Barcelona", "Perú": "Lima"}
    print(miDiccionario["Perú"])
    print(miDiccionario)

    miDiccionario["Toronto"] = "Canada"
    print(miDiccionario)

    miDiccionario["España"] = "Valencia"
    print(miDiccionario)

    del miDiccionario["España"]
    print(miDiccionario)

    dic2 = {"Gauin": "Lady", 25: True, "Sueldo": 190.90}
    print(dic2[25])

    llaves = ("España", "Ecuador", "Perú")
    dicPaises = {llaves[0]: "Madrid", llaves[1]: "Guayaquil", llaves[2]: "Lima"}
    print(dicPaises)

    datosPersonales = {"Ape": "Gauin", "Anios": {1: 2014, 2: 2015, 3: 2016, 4: 2017, 5: 2018}}
    print(datosPersonales)
    print(datosPersonales["Anios"])

    print(datosPersonales.get('Apel', "Lady"))

    print(datosPersonales.keys())
    valores = tuple(datosPersonales.values())
    print(valores)
