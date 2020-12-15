import random
mazo = [(1,"oro",1),(2,"oro",2),(3,"oro",3),(4,"oro",4),(5,"oro",5),(6,"oro",6),(7,"oro",7),("sota","oro",0.5),("caballo","oro",0.5),("rey","oro",0.5),
     (1,"copas",1),(2,"copas",2),(3,"copas",3),(4,"copas",4),(5,"copas",5),(6,"copas",6),(7,"copas",7),("sota","copas",0.5),("caballo","copas",0.5),("rey","copas",0.5),
     (1,"bastos",1),(2,"bastos",2),(3,"bastos",3),(4,"bastos",4),(5,"bastos",5),(6,"bastos",6),(7,"bastos",7),("sota","bastos",0.5),("caballo","bastos",0.5),("rey","bastos",0.5),
     (1,"espadas",1),(2,"espadas",2),(3,"espadas",3),(4,"espadas",4),(5,"espadas",5),(6,"espadas",6),(7,"espadas",7),("sota","espadas",0.5),("caballo","espadas",0.5),("rey","espadas",0.5)]
usuarios = []
while True:
    print("Bienvendios al juego de Siete y Medio, elige una opcion:\nA)Jugador vs Jugador\nB)Jugador vs CPU\nC)Que es el siete y medio\nD)Salir")
    menu0 = str(input("Opcion: "))
    if menu0 == "A" or menu0 == "a":    #Menu para seleccion de jugadores participantes y sus nombres
        while True:
            d = 0
            print("Especifica la cantidad de jugadores para jugar o escribe -1 para volver atras:\nMinimo: 2\nMaximo: 8")
            cantjug = int(input())
            if cantjug >= 2 and cantjug <= 8:
                for i in range(cantjug):
                    while True: #Bucle de seleccion de nombre
                        c = 0; t = 0
                        print("El nombre de usuario debe tener un maximo de 8 carácteres y que no comience por numero y "
                              "no contenga espacips\nNombre del jugador",i + 1)
                        usuario = input()
                        if len(usuario) <= 8 and not usuario[0].isnumeric(): #Comprueba que el nombre cumpla largo y que no comienze por numero
                            for j in range(len(usuario)):   #bucle secundario que comprueba que no haya espacio
                                if usuario[j] != " ":   #Si no es espacio, suma un valor a una variable
                                    c = c + 1
                                else:
                                    t = 1   #En case de detectar espacio, se establece una variable en 1 y se rompe bucle
                                    break
                        if c == len(usuario):   #En case que no encuentre espacio, se acepta nombre y se pasa a siguiente usuario
                            usuarios.append(usuario)
                            break
                        elif t == 1 or len(usuario) > 8 or usuario[0].isnumeric():  #cuando no se cumple criterios, se repite bucle
                            print("Escribe un nombre que siga las especificaciones\n")
                usuarios.insert(0, "Banca")
                break
            elif cantjug == -1:
                break
            else:
                print("Escribe un valor correcto\n")
        #A partir de aqui se desenvolupa el juego mismo
        dictjugar = {}
        temp = 0
        for i in usuarios:
            if i == "Banca":
                dictjugar[i] = [[], "Jugando", "Jugando", temp, float(0), float(0), float(20),0,0]
            else:
                dictjugar[i] = [[], "Jugando", "Jugando", temp, float(0), float(0), float(20),0,0]  # En ordern: Cartas, estado mano, estado partida, prioridad, puntos mano (o suma cartas), puntos apostados, puntos restantes, mano, manos ganadas
                temp += 1
        while True:     #Preparativos ronda
            mazo2 = []      #Matriz que servira para cartas, o bucle ronda
            for i in range(len(mazo)): #Creacion de lista equivalente a la del mazo, sin info dentro de esta
                mazo2.append(" ")
            while True:     #Nueva Mano
                for i in dictjugar:
                    a = random.randint(0,39)
                    while True:
                        if mazo2[a] != "X":
                            mazo2[a] = "X"
                            dictjugar[i][0].append(mazo[a])
                            dictjugar[i][1] = "Jugando"
                            dictjugar[i][5] = 0
                            dictjugar[i][4] = mazo[a][2]
                            break
                for i in dictjugar: #Mano por jugador
                    if dictjugar[i][1] == "Jugando" and dictjugar[i][2] == "Jugando" and i != "Banca":
                        print("Informacion actual de la ronda:")
                        for j in range(len(mazo)):
                            if mazo2[j] == "X":
                                print(mazo[j])
                        for j in dictjugar:
                            print(j,dictjugar[j][5],dictjugar[j][6])
                        if dictjugar[i][1] != "Eliminado":
                            while True: #Apuesta
                                print("Realiza una apuesta (Minimo 0.5)")
                                apuesta = float(input())
                                if apuesta > dictjugar[i][6]:
                                    print("Apostaste mas puntos de los que tienes")
                                elif apuesta < 0.5:
                                    print("Apostaste una cantidad inferior a la minima")
                                else:
                                    dictjugar[i][5] = apuesta
                                    dictjugar[i][6] = dictjugar[i][6] - apuesta
                                break
                            while True: #Subbucle mano por jugador
                                for j in range(len(dictjugar[i][0])):   #Bucle sacado de StackOverflow para imprimir cartas
                                    print("Carta",j+1,": ",dictjugar[i][0][j])
                                print("Que quieres hacer?\n1) Seguir Jugando\n2) Plantarse:")
                                elegir = int(input())
                                if elegir == 1:
                                    while True:
                                        a = random.randint(0, len(mazo))
                                        if mazo2[a] != "X":
                                            mazo2[a] = "X"
                                            dictjugar[i][0].append(mazo[a])
                                            dictjugar[i][4] = dictjugar[i][4] + mazo[a][2]
                                            break
                                        if dictjugar[i][4] > 7.5:
                                            dictjugar[i][1] = "Eliminado"
                                            dictjugar["Banca"][6] = dictjugar["Banca"][6] + dictjugar[i][5]
                                            break
                                        if dictjugar[i][6] <= 0:
                                            dictjugar[i][2] = "Eliminado"
                                            dictjugar["Banca"][6] = dictjugar["Banca"][6] + dictjugar[i][5]
                                            break
                                elif elegir== 2:
                                    dictjugar[i][1] = "Plantado"
                                    break
                                else:
                                    print("Elige una de las 2 opciones")
                #Turno de la Banca, se ejecuta cuando todos los otros han acabado
                print("Informacion actual de la ronda:")
                for j in range(len(mazo)):
                    if mazo2[j] == "X":
                        print(mazo[j])
                    for j in dictjugar:
                        print(j,dictjugar[j][5], dictjugar[j][6])
                    print("Banca, elije que hacer")
                    while True:  # Subbucle mano por jugador
                        for i in range(len(dictjugar[j][0])):  # Bucle sacado de StackOverflow para imprimir cartas
                            print(dictjugar[i][0][j])
                            print("Que quieres hacer?\n1) Seguir Jugando\n2) Plantarse:")
                            elegir2 = input()
                            if elegir2 == 1:
                                while True:
                                    a = random.randint(0, len(mazo))
                                    if mazo2[a] != "X":
                                       mazo2[a] = "X"
                                       dictjugar["Banca"][0].append(mazo[a])
                                       dictjugar["Banca"][4] = dictjugar["Banca"][4] + mazo[a][2]
                                       break
                                    if dictjugar["Banca"][4] > 7.5:
                                        mintemp = 0
                                        for k in dictjugar:
                                            if k != "Banca":
                                                if (dictjugar["Banca"][6] - dictjugar[k][5]) > 0:
                                                    dictjugar[k][6] = dictjugar[k][6] + 2*dictjugar[k][5]
                                                    mintemp = mintemp + dictjugar[k][5]
                                                    dictjugar["Banca"][6] = dictjugar["Banca"][6] - mintemp
                                                    dictjugar[k][5] = 0
                                                else:
                                                    dictjugar[k][6] = dictjugar[k][6] + dictjugar["Banca"][6]
                                                    dictjugar["Banca"][2] = "Eliminado"
                                                    for l in dictjugar:
                                                        if dictjugar[l][3] == dictjugar["Banca"][3] and dictjugar[l] != "Banca":
                                                            dictjugar[l][2] = "Eliminado"
                                                            dictjugar[l][3] += temp
                                                            break
                                        break
                            elif elegir2 == 2:
                                dictjugar[i][1] = "Plantado"
                                break
                            else:
                                print("Elige una de las 2 opciones")
                comprovarpuntos = 0
                temp2 = "a"
                empate = 0
                empat = []

                for i in dictjugar:
                    if dictjugar[i][4] >= comprovarpuntos and not dictjugar[i][4] > 7.5:
                        comprovarpuntos = dictjugar[i][4]
                        dictjugar[i][7] = 1
                        if temp2 != "a":
                            dictjugar[temp2][7] = 0
                            temp2 = dictjugar[i]
                            if dictjugar[i][4] == comprovarpuntos:
                                empate = comprovarpuntos
                                for j in dictjugar:
                                    if dictjugar[j][4] == dictjugar[i][4]:
                                        empat.append(dictjugar[j][4])
                            if dictjugar[i][4] == 7.5:
                                break
                        else:
                            temp2 = dictjugar[i]
                            if dictjugar[i][4] == 7.5:
                                break
                if empate is True:
                    for i in dictjugar:
                        if dictjugar[i][4] in empat:
                            print("pene")
                break
            break

    elif menu0 == "B" or menu0 == "b":
        while True:
            print("Especifica la cantidad de CPU's para jugar en contra o escribe -1 para volver atras:\nMinimo: 1\nMaximo: 7")
            cantcpu = int(input())
            if cantcpu >= 1 and cantcpu <= 7:
                for i in range(cantcpu + 1):
                    if i >= 1:
                        cpu = "CPU{}".format(i) #Buscar una forma de añadir nombre de forma incremental
                        usuarios.append(cpu)
                    else:
                        while True:  # Bucle de seleccion de nombre
                            c = 0;t = 0
                            print("El nombre de usuario debe tener un maximo de 8 carácteres y que no comience por numero y "
                                "no contenga espacips\nNombre del jugador")
                            usuario = input()
                            if len(usuario) <= 8 and not usuario[0].isnumeric():  # Comprueba que el nombre cumpla largo y que no comienze por numero
                                for j in range(len(usuario)):  # bucle secundario que comprueba que no haya espacio
                                    if usuario[j] != " ":  # Si no es espacio, suma un valor a una variable
                                        c = c + 1
                                    else:
                                        t = 1  # En case de detectar espacio, se establece una variable en 1 y se rompe bucle
                                        break
                            if c == len(
                                    usuario):  # En case que no encuentre espacio, se acepta nombre y se pasa a siguiente usuario
                                usuarios.append(usuario)
                                break
                            elif t == 1 or len(usuario) > 8 or usuario[
                                0].isnumeric():  # cuando no se cumple criterios, se repite bucle
                                print("Escribe un nombre que siga las especificaciones\n")
            elif cantcpu == -1:
                break
            else:
                print("Escribe un valor correcto\n")
            if usuarios == True:
                break
    elif menu0 == "C" or menu0 == "c": #Contiene info de que es el juego (Tambien sacado de StackOverflow)
        print("Siete y Medii:\n\nEl siete y medio es un juego de cartas que utiliza la baraja española de 40 cartas.\n "
              "Eljuego consiste en obtener siete puntos y medio, o acercarse a esta puntuación lo más\n"
              "posible. Las cartas tienen, indistintamente de su palo, el valor que indica su propio\n"
              "índice, excepto las figuras (sota, caballo y rey) que tienen una valor de medio punto\n"
              "cada una.\n"
              "El objetivo es ganar los puntos apostados en cada tanda. En cada apuesta, cada jugador\n"
              "compite contra la banca, para ganar la apuesta el objetivo es intentar sumar siete y\n"
              "medio o el número más cercano sin pasarse de esta cantidad.\n\nPresiona cualquier tecla para continuar")
        input()
    elif menu0 == "D" or menu0 == "d":
        break
    else:
        print("Elige una de las opciones en pantalla\n")


