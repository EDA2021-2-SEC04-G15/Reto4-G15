"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo 

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # analyzer es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadServices(analyzer):
    """
    Carga los datos de los archivos CSV en el modelo.
    Para el primer grafo, se crea un arco entre cada par de aeropuertos que
    tienen un vuelo en común.

    addRouteConnection crea conexiones entre diferentes rutas
    servidas en una misma estación.
    """
    airportsfile = cf.data_dir + 'airports_full.csv'
    airports_input_file = csv.DictReader(open(airportsfile, encoding="utf-8"),
                                delimiter=",")
    routesfile = cf.data_dir + 'routes_full.csv'
    routes_input_file = csv.DictReader(open(routesfile, encoding="utf-8"),
                                delimiter=",")


    for airport in airports_input_file:
        model.addAirport(analyzer, airport)
    
    for flight in routes_input_file:
        origin = flight['Departure']
        destination = flight['Destination']
        distance = float(flight['distance_km'])
        model.addConnection(analyzer['oneWayConnections'], origin, destination, distance)
    
    model.addDoubleGraph(analyzer)

    return analyzer

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo


def totalNodes(analyzer):
    """
    Total de paradas de autobus
    """
    return model.totalNodes(analyzer)


def totalConnections(analyzer):
    """
    Total de enlaces entre las paradas
    """
    return model.totalConnections(analyzer)
