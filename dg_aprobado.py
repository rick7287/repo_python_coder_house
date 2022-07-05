"""
Crear un script llamado aprobado.py que realice lo siguiente:

Debe tomar 2 argumentos, ambos números enteros del 0 al 10, sino, mostrar un error.
Si ambos valores son mayores o igual a 7 devolver imprimir “Promocionado”
Si ambos valores son mayor o igual a 4 imprimir “Aprobado, debe rendir final”

"""
"""
Crear un script llamado aprobado.py que realice lo siguiente:

Debe tomar 2 argumentos, ambos números enteros del 0 al 10, sino, mostrar un error.
Si ambos valores son mayores o igual a 7 devolver imprimir “Promocionado”
Si ambos valores son mayor o igual a 4 imprimir “Aprobado, debe rendir final”
Si uno de los dos valores es menor a 4 imprimir “Desaprobado, debe recuperar el primer parcial” (Si el primer argumento es 3 debe recuperar el primer parcial, si no, debe decir lo mismo pero con segundo parcial)
Si ambos argumentos son menores a 4 debe imprimir “Desaprobó ambos parciales, debe recursar”
En caso de no mostrar uno o ambos argumentos debe mostrar información de como usar el script.


"""




import sys

try:

    if len(sys.argv) !=3:
        print("Error, necesito 2 argumentos")
        print("Ejemplo de argumentos validos: num_1 num_2, donde num_1 y num_2 son valores enteros del 1 al 10")

    elif int(sys.argv[1]) >= 7 and int(sys.argv[2]) >= 7 :
        print("Promocionado")

    elif int(sys.argv[1]) >= 4 and int(sys.argv[2]) >= 4 :
        print("Aprovado, debe rendir final")

    elif int(sys.argv[1]) < 4 and int(sys.argv[2]) >= 4 :
        print("Desaprobado, debe recuperar el primer parcial")

    elif int(sys.argv[1]) >= 4 and int(sys.argv[2]) < 4 :
        print("Desaprobado, debe recuperar el segundo parcial")    

    elif int(sys.argv[1]) < 4 and int(sys.argv[2]) < 4 :
        print("Desaprobó ambos parciales, debe recursar")    

except (ValueError):
    print("Solo ingresar numeros enteros")
    print("Ejemplo de argumentos validos: num_1 num_2, donde num_1 y num_2 son valores enteros del 1 al 10")
