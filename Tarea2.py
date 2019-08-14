import os
#libreria pydot

class grafica:


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

