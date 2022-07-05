import sys

#print(f"hola {sys.argv[1]}")

#Realizar un script que imprima una palabra una cantidad de veces pasada por parametro
#Ejemplo: Imprimir hola 5 --> hola hola hola hola hola

if len(sys.argv) != 3:
    print("Error, necesito 2 argumentos")
else:
    for i in range(int(sys.argv[2])):
        print(sys.argv[1]) 

        
#recordemos que sys.argv es una lista con [nombrescript, parametro_1, parametro_2]