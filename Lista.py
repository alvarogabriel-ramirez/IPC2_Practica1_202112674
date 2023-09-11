from Nodo import nodo
import os
class Lista:
    def __init__(self):
        self.primero = None

    def insertar(self, item):
        nodo_nuevo = nodo(item=item)
        if self.primero is None:
            self.primero = nodo_nuevo
            self.ultimo = nodo_nuevo
        else:
            self.ultimo.siguiente = nodo_nuevo
            self.ultimo = nodo_nuevo

    def guardarEnTablero(self, fila, columna, color):
        encontrado = True
        actual = self.primero
        while actual!= None:
            if actual.item.fila == fila and actual.item.columna == columna:
                if color in ('AZUL', 'A'):
                    actual.item.inicial_color= "A"
                    actual.item.color = color
                    encontrado =False
                elif color in ('ROJO', 'R'):
                    actual.item.inicial_color="R"
                    actual.item.color = color
                    encontrado =False
                elif color in ('VERDE', 'V'):
                    actual.item.inicial_color="V"
                    actual.item.color = color
                    encontrado = False
                elif color in ('PURPURA', 'P'):
                    actual.item.inicial_color="P"
                    actual.item.color = color
                    encontrado =False
                elif color in ('NARANJA', 'N'):
                    actual.item.inicial_color="N"
                    actual.item.color = color
                    encontrado =False
                else:
                    print('*** El color: '+color+" No existe o no fue ingresado correctamente ***")
                    encontrado =False
            actual = actual.siguiente
        if  encontrado :
            print('*** El valor de la columna o fila no se encuentra entre el tablero***')
        
    def imprimir(self):
        actual = self.primero
        texto = ""
        fila_actual = 1  #fila actual
        while actual:
            if actual.item.fila == fila_actual:
                texto += "|" + actual.item.inicial_color + "|"
            else:
                print(texto)
                texto = "|" + actual.item.inicial_color + "|"
                fila_actual = actual.item.fila
            actual = actual.siguiente
        print(texto)  #ultima fila



    def to_dot(self, rows, columns):

        dot_string = 'digraph G {\n'
        dot_string += """start[label=\"Coloréalo \n Guatematel\"]"""
        # filas
        dot_string += "a"+str(0)+"""[label=\""""+str(0)+"""\"]"""
        # columnas
        dot_string += """start->a"""+str(0)+""";\n"""

        for row in range(rows):
            dot_string += "a"+str(row + 1)+"""[label=\""""+str(row + 1)+"""\"]"""
            dot_string += "a"+str(row)+"""->a"""+str(row + 1)+""";\n"""
        contador = 1
        for column in range(columns):
            dot_string += str(column + 1) + \
                """[label=\""""+str(column + 1)+"""\"]"""
            dot_string += """start->"""+str(column+1)+""";\n"""
            contador += 1
        reciente = self.primero
        
        while reciente != None:
            color_actual = reciente.item.color
            if color_actual in ('AZUL', 'A'):
                dot_string += str(contador)+"""[label=\" \"]"""
                dot_string += str(contador-int(columns)) + \
                    """->"""+str(contador)+""";\n"""
                dot_string += str(contador) + \
                    """[fillcolor=\"blue\"style=filled]"""
            elif color_actual in ('ROJO', 'R'):
                dot_string += str(contador)+"""[label=\" \"]"""
                dot_string += str(contador-int(columns)) + \
                    """->"""+str(contador)+""";\n"""
                dot_string += str(contador) + \
                    """[fillcolor=\"red\"style=filled]"""
            elif color_actual in ('VERDE', 'V'):
                dot_string += str(contador)+"""[label=\" \"]"""
                dot_string += str(contador-int(columns)) + \
                    """->"""+str(contador)+""";\n"""
                dot_string += str(contador) + \
                    """[fillcolor=\"green\"style=filled]"""
            elif color_actual in ('PURPURA', 'P'):
                dot_string += str(contador)+"""[label=\" \"]"""
                dot_string += str(contador-int(columns)) + \
                    """->"""+str(contador)+""";\n"""
                dot_string += str(contador) + \
                    """[fillcolor=\"purple\"style=filled]"""
            elif color_actual in ('NARANJA', 'N'):
                dot_string += str(contador)+"""[label=\" \"]"""
                dot_string += str(contador-int(columns)) + \
                    """->"""+str(contador)+""";\n"""
                dot_string += str(contador) + \
                    """[fillcolor=\"orange\"style=filled]"""
            else:
                dot_string += str(contador)+"""[label=\" \"]"""
                dot_string += str(contador-int(columns)) + \
                    """->"""+str(contador)+""";\n"""
            contador += 1
            reciente = reciente.siguiente
        dot_string += """}"""

        with open("matriz.dot", "w") as archivo:
            archivo.write(dot_string)
        os.system("dot -Tpng -Gcharset=latin1 matriz.dot -o matriz.png")

