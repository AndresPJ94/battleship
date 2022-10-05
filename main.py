import numpy as np
import random
from tablero import *

#Importamos numpy, random y las funciones de funciones.py
lista_posiciones = [] # constante que va en el main, vamos recorriendo todas las posibles coordenadas
#y eliminándolas de la lista

for x in range(0,10): # se rellena con este bucle
    for i in range(0,10):
        lista_posiciones.append(tuple((x,i)))

posiciones_validas = (0,1,2,3,4,5,6,7,8,9)  #Para chequear que el input del usuario es correcto

tablero_maquina = Tablero()
tablero_maquina.tablero

print('Tablero máquina')
tablero_maquina = tablero_maquina.colocar_barcos_random()
print(tablero_maquina)


tablero_jugador = Tablero()
tablero_jugador.tablero

print('Tu tablero')
tablero_jugador = tablero_jugador.colocar_barcos_manual()
print(tablero_jugador)

#Disparo del jugador

def dispara_jugador(fila, col):                            
    if tablero_maquina[fila,col] == ' ':
        tablero_maquina[fila, col] = 'A'
    elif tablero_maquina[fila, col] == '1':
        tablero_maquina[fila,col] = 'X'
        
    return tablero_maquina

#Funcion disparo de la máquina

def disparar_maquina():                                    
    coord = random.choice(lista_posiciones)
    if tablero_jugador[coord[0], coord[1]] == ' ':
        tablero_jugador[coord[0], coord[1]] = 'A'
    else:
        tablero_jugador[coord[0], coord[1]] = 'X'

    lista_posiciones.remove(coord)
    return tablero_jugador, print(tablero_jugador)

print ("Bienvenido al juego de hundir la flota, coloca los barcos de la máquina. Tienes que colocar 4 de 1, 2 de 3, 3 de 2 y 1 de 4")
#Generamos un tablero para el usuario y otro para la máquina
while '1' in tablero_jugador or '1' in tablero_maquina:  #Mientras haya 1's en ambos tableros, el bucle continúa
    tablero_jugador
    tablero_maquina
    
    fila = int(input('Introduzca una coordenada para la fila dentro del rango 0 a 9: '))
    col = int(input('Introduzca una coordenada para la columna dentro del rango 0 a 9: '))

    #Funcion disparo para usuario y máquina. Por defecto siempre empieza el usuario pero se puede randomizar quien realiza el primer mov.
    dispara_jugador(fila, col)
    disparar_maquina()
 #Aquí el bucle while se rompe si alguno de los dos tableros (usuario y máquina) se queda sin barcos (1)
    if '1' not in tablero_jugador or '1' not in tablero_maquina:
        print('El juego ha terminado.')
        if '1' not in tablero_jugador:   #Si ya no quedan 1 en nuestro tablero, gana la máquina.
            print('La máquina te ha ganado. All your bases are belong to us.')
            break
        else:    #Si ya no le quedan 1 a la máquina, hemos ganado.
            print('Enhorabuena, has ganado a Skynet.')
            break

