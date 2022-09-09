def operadoreslogicos ():
    distancia = 400
    numeroHermanos = 3
    salarioPadres = 3000

    tieneBeneficio = False

    if (distancia > 1500 and numeroHermanos > 2) or salarioPadres < 3000:
        tieneBeneficio = True

    print(not tieneBeneficio)

    if (7 > 3) or (8 < 6):
        print("Verdad")
    else:
        print("Es mentira...")
