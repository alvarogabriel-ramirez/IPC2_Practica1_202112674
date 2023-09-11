import xml.etree.ElementTree as ET
import os
from Lista import Lista
from Items import item

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def crear_tablero():    
    matriz = Lista()
    print("-----------------Coloréalo--------------")
    print("Ingrese el ancho del tablero. ")
    print("-----------------Guatematel--------------")
    ancho = int(input(">    "))
    print("-----------------Coloréalo--------------")
    print("Ingrese el alto del tablero. ")
    print("-----------------Guatematel--------------")
    largo = int(input(">    "))

    for fila in range(largo):
        for columna in range(ancho):
            pieza = item(fila + 1, columna + 1, "", " ")
            matriz.insertar(pieza)
    print("")
    while True:

        print("-----------------Coloréalo--------------")
        print("Por favor elija su color:")
        print("- AZUL\n- ROJO\n- VERDE\n- PURPURA\n- NARANJA")
        print("-----------------Guatematel--------------")
        color = input(">    ").strip().upper()

        print(f"{color}:\nIngrese la fila en que desea colocar la pieza.\nRango : 1 - {largo}")
        print("-----------------Guatematel--------------")
        row = int(input(">    "))

        print(f"{color}:\nIngrese la columna en que desea colocar la pieza.\nRango : 1 - {ancho}")
        print("-----------------Guatematel--------------")
        column = int(input(">    "))

        matriz.guardarEnTablero(row, column, color)

        print("-----------------Coloréalo--------------")
        print(f"{color}")
        print("Tablero Resultante : ")
        matriz.imprimir()
        print("-----------------Guatematel--------------")

        respuesta = input("¿Desea agregar otra pieza? (Si/No): ").strip().lower()
        if respuesta != "si":
            break  

    clear()
    print("-----------------Coloréalo--------------")
    print("Tablero Final : ")
    matriz.imprimir()
    print("-----------------Guatematel--------------")
    print(" ¡  Gráfica Creada  !  ")
    matriz.to_dot(largo, ancho)

def menu():
    while True: 
        print("-----------------Coloréalo--------------")
        print("1. Crear Tablero")
        print("2. Mostrar Datos del Estudiante")
        print("3. Salida")
        print("-----------------Guatematel--------------")
        
        opcion = input("Ingrese una opción > ")
        if   opcion == "1":
            clear()
            crear_tablero()      
        elif opcion == "2":
            clear()
            print("-----------------Coloréalo--------------")
            print("-> 202112674")
            print("-> Alvaro Gabriel Ramirez Alvarez")
            print("-> Introducción a la Programación y Computación 2")
            print("-> Seccion A")
            print("-----------------Guatematel--------------")

        elif opcion == "3":
            break
        else:
            print("*** Opción inválida ***")
        input("Presione ENTER para continuar...")
        clear()

if __name__ == "__main__":
    menu()