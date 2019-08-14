import os
#libreria pydot

class grafica:
    def graphMATRIZ(self,fila,columna,posY,posX):
        #INICIO DE LA LISTA
        #SE CREA EL PUNTO DOT.; W ES PARA ESCRIBIR EN EL ARCHIVO
        f=open("graficoMATRIZ.dot","w")
        #SE INICIA EL DIAGRAMA
        f.write("digraph G {\n")
        #SE ESTABLECE LA FORMA CUADRADA
        f.write(" node [shape=record];\n")
        #SE ESTABLECE FORMA HORIZONTAL
        f.write("struct3 [shape=record,label=\" {\n")
        #SE CREAN DOS NODOS NULL
        Struct = ''
        #RELACIONES ENTRE NODOS
        for i in range (fila):#filas
            Struct += "{"
            for c in range (columna):#columnas
                if c == columna-1:
                    if c == posX-1 and i== posY-1:
                        Struct +="X"
                    else:
                        Struct +=str(matriz[i][c])
                else:
                    if c == posX-1 and i== posY-1:
                        Struct +="X"+"|"
                    else:
                        Struct +=str(matriz[i][c])+"|"
            if i == fila-1:
                Struct += "}"
            else:
                Struct += "}|"
        #SE CIERRA EL GRAFICO
        f.write(Struct+'\n')
        f.write("}\" \n ];"+'\n')
        f.write('}')
        f.close()
        #SE TRANSFORMA EL .DOT A .JPG (EL NOMBRE .DOT TIENE QUE SER EL DE ARRIBA, EL .JPG PUEDE SER DIFERENTE)
        os.system("dot.exe -Tjpg graficoMATRIZ.dot -o graficoMATRIZ.jpg")
        #SE ABRE EL ARCHIVO .JPG
        os.system("graficoMATRIZ.jpg")




    

if __name__ == "__main__":
    Gra = grafica()
    fila = 0
    columna = 0
    salir = False 
    
    while (not salir):
        print ("""************
        Mapeo Lexicografico
        ************
        Menu
        1) Ingrese las dimensiones del arreglo
        2) Mapeo por filas
        3) Mapeo por columnas
        4) Salir""") 

        opc = int(input("Selecione Opcion\n"))

        if (opc==1):
            print("Ingrese dimensiones del arreglo\n")
            fila = int(input("Ingrese las filas del arreglo\n"))
            columna = int(input("Ingrese las columnas del arreglo\n"))
            matriz = []
            lista = []

            for i in range (int(fila)):
                matriz.append([0]*int(columna))
            
            cont = 0
            for i in range (int(fila)):#filas
                for c in range (int(columna)):#columnas
                    matriz[i][c] = cont
                    lista.extend([cont])
                    cont += 1

            
            print(matriz)

        if (opc==2):
            posicion = 0
            x = int(input("Ingrese cordenada x \n"))
            y = int(input("Ingrese cordenada y \n"))
            posicion = x*columna+y
            print ("La posicion es:", posicion)
            #Gra.graphMATRIZ(int(fila),int(columna),int(x),int(y))

            f=open("graficoFILAConsecutiva2.dot","w")
            f.write("digraph G {\n")
            f.write("rankdir=LR;\n")
            f.write(" node [shape=record];\n")
            f.write("struct3 [shape=record,label=\" \n")
            Struct = '{'
            for i in range (len(lista)):#filas
                if i == len(lista)-1:
                    if i == posicion:
                            Struct +="X"
                    else:
                        Struct +=str(lista[i])
                else:
                    if i == posicion:
                        Struct +="X|"
                    else:
                        Struct +=str(lista[i])+"|"
            f.write(Struct+'\n')
            f.write("}\" \n ];"+'\n')
            f.write('}')
            f.close()
            os.system("dot.exe -Tjpg graficoFILAConsecutiva2.dot -o graficoFILAConsecutiva2.jpg")
            os.system("graficoFILAConsecutiva2.jpg")
        elif(opc==3):
            posicion = 0
            x = int(input("Ingrese cordenada x\n"))
            y = int(input("Ingrese cordenada y\n"))
            posicion = y*fila+x
            print ("La posicion es:", posicion)
            print(lista)
            #Gra.graphMATRIZ(int(fila),int(columna),int(x),int(y))

            f=open("graficoColumnaConsecutiva2.dot","w")
            f.write("digraph G {\n")
            f.write("rankdir=LR;\n")
            f.write(" node [shape=record];\n")
            f.write("struct3 [shape=record,label=\" \n")
            Struct = '{'
            for i in range (len(lista)):#filas
                if i == len(lista)-1:
                    if i == posicion:
                            Struct +="X"
                    else:
                        Struct +=str(lista[i])
                else:
                    if i == posicion:
                        Struct +="X|"
                    else:
                        Struct +=str(lista[i])+"|"
            f.write(Struct+'\n')
            f.write("}\" \n ];"+'\n')
            f.write('}')
            f.close()
            os.system("dot.exe -Tjpg graficoColumnaConsecutiva2.dot -o graficoColumnaConsecutiva2.jpg")
            os.system("graficoColumnaConsecutiva2.jpg")
        elif(opc==4):
            print( " Nos vemos O/ " )
            salir =  True

