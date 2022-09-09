def generadores2 ():
    """
    def devuelveLenguajes(*lenguajes):
        for leng in lenguajes:
            yield leng
    """

    def devuelveLenguajes(*lenguajes):
        for leng in lenguajes:
            yield from leng

    lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")

    print(next(lenguajesObtenidos))
    print(next(lenguajesObtenidos))
