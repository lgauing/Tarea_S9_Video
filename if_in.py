def ifin ():
    print("-- Cursos --")
    print("Ciencias - Biologia - Lenguaje - Ingles")

    curso = input("Ingrese el curso deseado: ")

    if curso in ("Ciencias", "Biologia", "Lenguaje", "Ingles"):
        print("Curso {0} seleccionado.".format(curso))
    else:
        print("No existe ese curso...")
