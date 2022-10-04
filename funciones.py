import numpy as np
import random

#Clase tablero, aquí generamos el tablero del usuario y el de la máquina.
class Tablero:

    def __init__ (self, dimensiones = (10, 10)):
        self.dim = dimensiones
        self.tablero = np.full(self.dim, ' ')
    

    def colocar_barcos_random(self):
        barcos = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)

        for barco in barcos:
            while True:
            
                # Orientacion aleatoria
                nseo = random.choice(['N', 'S', 'E', 'O'])
                
                # Posicion inicial del barco
                current_pos = np.random.randint(10, size=2)
                fila = current_pos[0]
                col = current_pos[1]
                
                # 4 posibles posiciones
                coors_posiN = self.tablero[fila:fila-barco:-1, col]
                coors_posiE = self.tablero[fila, col:col+barco]
                coors_posiS = self.tablero[fila:fila + barco, col]
                coors_posiO = self.tablero[fila, col:col - barco:-1]
                
                # Chequeamos N
                if (nseo == 'N') and len(coors_posiN) == barco and ('1' not in coors_posiN):
                    self.tablero[fila:fila-barco:-1, col] = '1'
                    break
                
                # Chequeamos E
                elif (nseo == 'E') and len(coors_posiE) == barco and ('1' not in coors_posiE):
                    self.tablero[fila, col:col+barco] = '1'
                    break
                
                # Chequeamos S
                elif (nseo == 'S') and len(coors_posiS) == barco and ('1' not in coors_posiS):
                    self.tablero[fila:fila + barco, col] = '1'
                    break
                
                # Chequeamos O
                elif (nseo == 'O') and len(coors_posiO) == barco and ('1' not in coors_posiO):
                    self.tablero[fila, col: col - barco:-1] = '1'
                    break
        return self.tablero
    
    def colocar_barcos_manual(self):
        barcos = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)
        
        nseo = ("N", "S", "E", "O")
        coordenadas = (0, 1, 2 ,3 ,4, 5, 6, 7, 8, 9)
        
        for barco in barcos:
                i=int(input("Inserte la coordenada X deseada. Tamaño " + str(barco) + " "))
                j=int(input("Inserte la coordenada Y deseada. Tamaño " + str(barco) + " "))
                while i and j not in coordenadas:
                    i=int(input("Coordenada inválida. Por favor inserte la coordenada X deseada dentro del rango del juego. Tamaño " + str(barco) + " "))
                    j=int(input("Coordenada inválida. Por favor inserte la coordenada Y deseada dentro del rango del juego. Tamaño " + str(barco) + " "))

                orientacion = input("Elija la orientación del barco, opciones válidas son N, S, E y O: ")
                orientacion = orientacion.upper()
                while orientacion not in nseo:
                    orientacion = input("Elija la orientación del barco, opciones válidas son N, S, E y O: ")
                    orientacion = orientacion.upper()
                    
                if orientacion=="N":
                    self.tablero[(i-barco):i,j] = '1'

                if orientacion=="S":
                    self.tablero[i:(i+barco),j] = '1'

                if orientacion=="E":
                    self.tablero[i,j:(j+barco)] = '1'

                if orientacion == "O":
                    self.tablero[i,(j-barco):j] = '1'
        return self.tablero

