﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


sys.setrecursionlimit(2 ** 20)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar informacion de aeropuertos y vuelos")
    print("3- Calcular...")
    print("0- Salir")
    print("*******************************************")

"""
'oneWayConnections': None, 'doubleConnections': None 

"""

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando ....\n")
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de aeropuertos y vuelos ....\n")
        controller.loadServices(cont)
        numedges1 = controller.totalConnections(cont['oneWayConnections'])
        numvertex1 = controller.totalNodes(cont['oneWayConnections'])
        numedges2 = controller.totalConnections(cont['doubleConnections'])
        numvertex2 = controller.totalNodes(cont['doubleConnections'])
        print('\nDatos grafo dirijido:\n')
        print('Numero de vertices: ' + str(numvertex1))
        print('Numero de arcos: ' + str(numedges1))
        print('\nDatos grafo NOdirijido:\n')
        print('Numero de vertices: ' + str(numvertex2))
        print('Numero de arcos: ' + str(numedges2))
        print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))


        pass

    elif int(inputs[0]) == 3:
        pass

    else:
        sys.exit(0)
sys.exit(0)
