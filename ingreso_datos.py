def ingresodatos ():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    sueldo = float(input("Ingrese su sueldo: "))

    print("Holis, " + nombre)
    edadFutura = edad + 21
    print("Tu edad es:", edad)
    print("Tu edad (dentro de 20 años) será:", edadFutura)
    print("Tu sueldo es:", sueldo)
