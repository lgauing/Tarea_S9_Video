def raisepp (nota):
    if nota < 0:
        raise ValueError("Valor incorrecto...")
        # raise ZeroDivisionError("Este mensaje es personalizado.")
    elif nota >= 20:
        print("Excelente")
    elif nota >= 11:
        print("Aprobado")
    else:
        print("Desaprobado")


