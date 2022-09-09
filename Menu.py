from ast import For
from math import factorial
import os
from Generadores import generadores
from Generadores2 import generadores2
from POO.Cuenta import Cuenta
from POO.Curso import Curso
from POO.Herencia import Estudiante
from POO.HerenciaMultiple import ClaseX
from POO.Persona import Persona
from POO.Polimorfismo import Trabajador, describirPersona
from POO.RelacionesClases import Ciudad, Pais, Urbanizacion
from break_continue_pass import break_continue
from cadenas import cadenas
from concatenacion import concatenar1
from diccionarios import diccionarios
from excepciones import exepciones
from for1 import for_p
from funciones import funciones
from if_else import ifelse
from if_in import ifin
from ingreso_datos import ingresodatos
from modulos.modulo import Modulos
from operador_ternario import operador_ternario
from operadores_aritmeticos import  matematicas
from operadores_logicos import operadoreslogicos
from raise1 import raisepp
from range import range1
from tuplas import tuplas
from variables import *
from conversiones import *
from holamundo import Imprimir
from Listas import ReLista
from while1 import whilee
from paquete1.funciones_cadena import contar_letras
from paquete1.funciones_numericas import *
class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo=titulo
        self.opciones= opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija la opción [1...{}]:".format(len(self.opciones)))
        return opc
opc = ""
while opc != "34":
    os.system("cls")
    men = Menu("Menu Principal",["1) Hola, Lisa", "2) Listas", "3) Variables", "4) Conversiones", "5) Operaciones Aritméticas", "6) Concatenación", "7) Cadenas", "8) Tuplas", "9) Diccionario", "10) Ingreso de Datos", "11) Condicional if-else", "12) Condicional if-in", "13) Funciones", "14) Operaciones Lógicos", "15) Operador Ternario", "16) Función Range", "17) Bucles For", "18) Factorial", "19) Bucle While", "20) Brake, Continue & Pass", "21) Generadores", "22) Generadores 2", "23) Excepciones", "24) Raise", "25) Módulos", "26) Paquetes", "27) Personas", "28) Curso", "29) Cuenta", "30) Herencia", "31) Herencia Múltiple", "32) Polimorfismo", "33) Relaciones de Clases", "34) Salir"])
    opc = men.menu()
    if opc == "1":
        opc1 = ""
        os.system("cls")
        Elementos = (input("Ingrese nombre: "))
        if Elementos  == "":
            ele=3
        else:
            ele= Elementos
        resultados = Imprimir(ele)
        while opc1 != "2":
            os.system("cls")
            men1 = Menu("Menu",["1)Mostrar", "2)Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("<---Mostrar--->")
                res=resultados.pr()
                input("Presione una tecla para continuar...")                
    if opc == "2":  

            opc1 = ""
            os.system("cls")
            resultados = ReLista()
            while opc1 != "9":
                os.system("cls")
                men1 = Menu("Menu Operaciones listas",["1)Mostrar Lista", "2)Mostrar un elemento de la lista", "3)Agregar elemento a la lista","4)Ver operacion de listas con posicion", "5)insertar en lista", "6)Indice de lista","7)Remover lista","8)Sacar de lista","9) Salir"])
                opc1 = men1.menu()
                if opc1 == "1":
                    os.system("cls")
                    print("<---Mostrar--->")
                    res=resultados.mostrarLis()
                    print(res)
                    input("Presione una tecla para continuar...")
                elif opc1 == "2":
                    os.system("cls")
                    print("<---Mostar Elemento--->")
                    res=resultados.mostrarLis()
                    print(res)
                    num=len(res)
                    print("<---De acuerdo a la lista escoja una posicion numero positivo y menor a {}--->".format(num))
                    r=int(input("Ingrese Posicion: "))
                    if r==6:
                        print("posicion no encontrada")
                    else:
                        res=resultados.Mostrar1(r)
                    input("Presione una tecla para continuar...")
                elif opc1 == "3":
                    os.system("cls")
                    print("<---Agregar Elemento--->")
                    opc1 = ""
                    while opc1 != "3":
                        os.system("cls")
                        men1 = Menu("Menu de elecion de tipo variable",["1)numero", "2)texto", "3)Salir"])
                        opc1 = men1.menu() 
                           
                        if opc1 =="1":
                            os.system("cls")
                            ele=input("ingrese elemento a agregar: ")
                            res=resultados.agregar(int(ele))
                            input("Presione una tecla para continuar...")
                            
                        elif opc1 == "2":
                            os.system("cls")
                            ele=input("ingrese elemento a agregar: ")
                            res=resultados.agregar(ele)
                            input("Presione una tecla para continuar...")
                            
                elif opc1 == "4":
                    os.system("cls")
                    print("<---View de listas Distintas maneras de ver elementos de lista--->")
                    res=resultados.mostrarLis()
                    print(res)
                    print("============================================ ")

                    resultados.viewlist()
                    input("Presione una tecla para continuar...")
                elif opc1 == "5":
                    os.system("cls")
                    print("<---Insertar en posicion especifica--->")             
                    pos=int(input("Ingrese Posicion a colocar: "))
                    nom=input("ingrese elemento a ingresar: ")
                    resultados.insertar(pos,nom)
                    print(resultados.mostrarLis())
                    input("Presione una tecla para continuar...")

                elif opc1 == "6":
                    os.system("cls")
                    print("<---Indice de elementos--->")             
                    print(resultados.indiceElem())
                    input("Presione una tecla para continuar...")


                elif opc1 == "7":
                    os.system("cls")
                    print("<---remover elementos de la lista--->") 
                    opc1 = ""
                    while opc1 != "3":
                        
                        os.system("cls")
                        print(resultados.mostrarLis())
                        men1 = Menu("Que desea remover ",["1)numero", "2)texto", "3)Salir"])
                        opc1 = men1.menu() 
                           
                        if opc1 =="1":
                            os.system("cls")
                            print(resultados.mostrarLis())
                            ele=input("ingrese elemento a remover: ")
                            res=resultados.remover(float(ele))
                            print(resultados.mostrarLis())
                            input("Presione una tecla para continuar...")
                            
                        elif opc1 == "2":
                            os.system("cls")
                            print(resultados.mostrarLis())
                            ele=input("ingrese elemento a remover: ")
                            res=resultados.remover(ele) 
                            print(resultados.mostrarLis())
                    input("Presione una tecla para continuar...")

                elif opc1 == "8":
                    os.system("cls")
                    print("<---Sacar elemento de la lista--->")             
                    resultados.sacar()
                    print(resultados.mostrarLis())
                    input("Presione una tecla para continuar...")              
    if opc == "3":  

            opc1 = ""
            os.system("cls")
            
            while opc1 != "2":
                os.system("cls")
                men1 = Menu("Menu",["1)ver variables", "2)Salir"])
                opc1 = men1.menu()
                if opc1 == "1":
                    os.system("cls")
                    print("Ver Variables")
                    ver()
                    input("Presione una tecla para continuar...")                   
    elif opc == "4":
        opc1 = ""
        os.system("cls")
        print("<---Ver Conversiones--->")
        mostrarconversiones()
        input("Presione una tecla para continuar...")
    elif opc == "5":
        opc1 = ""
        os.system("cls")
        print("<---Operaciones matematicas--->")
        matematicas()
        input("Presione una tecla para continuar...")
    elif opc == "6":
        opc1 = ""
        os.system("cls")
        print("<---Concatenar Listas--->")
        concatenar1()
        input("Presione una tecla para continuar...") 
    elif opc == "7":
        opc1 = ""
        os.system("cls")
        print("<---Cadenas--->")
        cadenas()
        input("Presione una tecla para continuar...")    
    elif opc == "8":
        opc1 = ""
        os.system("cls")
        print("<---Tuplas--->")
        tuplas()
        input("Presione una tecla para continuar...")
    elif opc == "9":
        opc1 = ""
        os.system("cls")
        print("Diccionario")
        diccionarios()
        input("Presione una tecla para continuar...")
    elif opc == "10":
        opc1 = ""
        os.system("cls")
        print("Ingreso de datos")
        ingresodatos()
        input("Presione una tecla para continuar...") 
    elif opc == "11":
        opc1 = ""
        os.system("cls")
        print("<---If Else--->")
        ifelse()
        input("Presione una tecla para continuar...")     
    elif opc == "12":
        opc1 = ""
        os.system("cls")
        print("<---If in--->")
        ifin()
        input("Presione una tecla para continuar...")    
    elif opc == "13":
        opc1 = ""
        os.system("cls")
        print("<---Funciones--->")
        funciones()
        input("Presione una tecla para continuar...")
    elif opc == "14":
        opc1 = ""
        os.system("cls")
        print("<---Operadores logicos--->")
        operadoreslogicos()
        input("Presione una tecla para continuar...")  
    elif opc == "15":
        opc1 = ""
        os.system("cls")
        print("<---Operador Ternario--->")
        operador_ternario()
        input("Presione una tecla para continuar...")   
    elif opc == "16":
        opc1 = ""
        os.system("cls")
        print("<---Funcion Range--->")
        range1()
        input("Presione una tecla para continuar...")    
    elif opc == "17":
        opc1 = ""
        os.system("cls")
        print("<---Bucles For--->")
        for_p()
        input("Presione una tecla para continuar...")     
    elif opc == "18":
        opc1 = ""
        os.system("cls")
        print("<---Factorial--->")
        factorial()
        input("Presione una tecla para continuar...")
    elif opc == "19":
        opc1 = ""
        os.system("cls")
        print("<---Bucle While--->")
        whilee()
        input("Presione una tecla para continuar...")    
    elif opc == "20":
        opc1 = ""
        os.system("cls")
        print("<---Brake_continue_pass--->")
        break_continue()
        input("Presione una tecla para continuar...")    
    elif opc == "21":
        opc1 = ""
        os.system("cls")
        print("<---Generadores--->")
        generadores()
        input("Presione una tecla para continuar...")
    elif opc == "22":
        opc1 = ""
        os.system("cls")
        print("<---Generadores2--->")
        generadores2()
        input("Presione una tecla para continuar...")     
    elif opc == "23":
        opc1 = ""
        os.system("cls")
        print("<---Exepciones--->")
        exepciones()
        input("Presione una tecla para continuar...")   
    elif opc == "24":
        opc1 = ""
        os.system("cls")
        print("<---Raise--->")
        raisepp(17)
        input("Presione una tecla para continuar...")    
    elif opc == "25":
        opc1 = ""
        os.system("cls")
        print("<---Modulos--->")
        Modulos()
        input("Presione una tecla para continuar...")   
    elif opc == "26":
        opc1 = ""
        os.system("cls")
        print("<---Paquete--->")
        print(multiplicar(5,6))
        print(contar_letras("Hola"))
        input("Presione una tecla para continuar...")    
    elif opc == "27":
        opc1 = ""
        os.system("cls")
        print("<---Persona--->")
        persona1=Persona()
        persona1.apellidos = "Byron LLanos"
        print(persona1.apellidos)
        persona1.despertar()
        print(persona1.despierta)

        persona2 = Persona()
        persona2.apellidos = "Byron Briones"
        print(persona2.apellidos)
        # persona2.despertar()
        print(persona2.despierta)
        input("Presione una tecla para continuar...")
    elif opc == "28":
        opc1 = ""
        os.system("cls")
        print("<---Curso--->")
        curso1 = Curso("Calculo", 5, "Ingeniería Sistemas")
        print(curso1)
        curso1.mostrarDatos()
        input("Presione una tecla para continuar...")    
    elif opc == "29":
        opc1 = ""
        os.system("cls")
        print("<---Cuenta--->")
        cuenta1 = Cuenta("Lady Gauin", 1500, "Dolares")
        print(cuenta1.get_Saldo())
        print(cuenta1.get_Moneda())
        cuenta1.set_Moneda("Dólares")
        print(cuenta1.get_Moneda())
        input("Presione una tecla para continuar...")  
    elif opc == "30":
        opc1 = ""
        os.system("cls")
        print("<---Herencia--->")
        estu1 = Estudiante("Gauin", "Gusñay", "Lady", "Ingeniería Sistemas")
        print(estu1.mostrarNombreCompleto())
        print(estu1.profesion)
        input("Presione una tecla para continuar...")    
    elif opc == "31":
        opc1 = ""
        os.system("cls")
        print("<---Herencia Multiple--->")
        cX1 = ClaseX(15, 21)
        input("Presione una tecla para continuar...")   
    elif opc == "32":
        opc1 = ""
        os.system("cls")
        print("<---Polimorfismo--->")
        doc1 = Trabajador()
        describirPersona(doc1)
        input("Presione una tecla para continuar...")   
    elif opc == "33":
        opc1 = ""
        os.system("cls")
        print("<---Relaciones Clases--->")
        pais1 = Pais("Ecuador", "Lady Gauin")
        print(pais1)

        ciudad1 = Ciudad("Naranjito", 1500, pais1)
        print(ciudad1)

        urba1 = Urbanizacion("San Luis", ciudad1)
        print(urba1)
        input("Presione una tecla para continuar...")
        
        
    
    print("Lo espermos en una proxima ocasión")