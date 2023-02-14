import random
#Trabajo Hecho por carlos cifuentes Mora

opcion = "s"
numero_juego = 0
while opcion.lower() == "s":
    a=int(random.randrange(1, 6))
    b=int(random.randrange(1, 6))

    print("El numero del primer dado es: " , a)
    print("El numero del segundo dado es: ", b)

    print("La suma de ambos dados es: " , (a + b))

    opcion = input("Desea continuar  (s/n): ")
    if opcion.lower() == "s":
        print('*' * 20)
        print("Empieza el " , numero_juego + 2 , "juego" )
        print('*' * 20)
        numero_juego += 1
        continue
    else:
        opcion.lower()== "n"
        print('*' * 20)
        print("Decidiste dejar de jugar")
        print('*' * 20)
        break