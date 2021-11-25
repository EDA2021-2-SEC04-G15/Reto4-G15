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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT.graph import gr
from DISClib.ADT import list as lt
from DISClib.ADT import map as m
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
assert cf



# Construccion de modelos

def newAnalyzer():
    """ Inicializa el analizador

   airpots: Tabla de hash para guardar los vertices del grafo
   oneWayConnections: Grafo para representar las rutas unidireccionales entre aeropuertos
   twoWayConnections: Grafo para representar las rutas bidireccionales entre aeropuertos
   components: Almacena la informacion de los componentes conectados
   paths: Estructura que almancena los caminos de costo minimo desde un
           vertice determinado a todos los otros vértices del grafo
    """
    try:
        analyzer = {
                    'airports': None,
                    'oneWayConnections': None,
                    'doubleConnections': None,
                    'components': None,
                    'paths': None
                    }

        analyzer['airports'] = m.newMap(numelements=15000,
                                     maptype='PROBING',
                                     comparefunction=compareAirportIATAs)

        analyzer['oneWayConnections'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=15000,
                                              comparefunction=compareAirportIATAs)
        analyzer['doubleConnections'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=15000,
                                              comparefunction=compareAirportIATAs)
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')


# Funciones para agregar informacion al catalogo


def addAirport(analyzer, airport):
    """
    Adiciona un aeropuerto y su información al analyzer
    """

    airportID= airport['IATA']

    try:
        addAirportVertex(analyzer['oneWayConnections'], airportID)
        addAirportInfo(analyzer, airport)
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:addAirport')
    
def addAirportVertex(analyzer,airport):
    """
    Adiciona un aeropuerto como un vertice del grafo direccionado
    """
    try:
        if not gr.containsVertex(analyzer, airport):
            gr.insertVertex(analyzer, airport)
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:addAirport')


def addAirportInfo(analyzer, airport):
    """
    Agrega a un vertice, la informacion de ese aeropuerto
    """
    entry = m.get(analyzer['airports'], airport['IATA'])
    if entry is None:
        m.put(analyzer['airports'], airport['IATA'], airport)
    else:
        print('repeat')
    return analyzer

def addConnection(analyzer, origin, destination, distance):
    """
    Adiciona un arco entre dos aeropuertos en el grafo direccionado
    """
    edge = gr.getEdge(analyzer, origin, destination)
    if edge is None:
        gr.addEdge(analyzer, origin, destination, distance)
    return analyzer


def addDoubleGraph(analyzer):
    """
    Adiciona un arco entre dos aeropuertos
    """
    for airport in lt.iterator(gr.vertices(analyzer['oneWayConnections'])):
        for adjacent in lt.iterator(gr.adjacents(analyzer['oneWayConnections'],airport)):
            retorno = gr.getEdge(analyzer['oneWayConnections'], adjacent, airport)
            if retorno is not None:
                addAirportVertex(analyzer['doubleConnections'],airport)
                addAirportVertex(analyzer['doubleConnections'],adjacent)
                addConnection(analyzer['doubleConnections'], airport, adjacent, retorno['weight'])

    return analyzer

# Funciones para creacion de datos

# Funciones de consulta

def totalNodes(analyzer):
    """
    Retorna el total de aeropuertos (vertices) del grafo
    """
    return gr.numVertices(analyzer)


def totalConnections(analyzer):
    """
    Retorna el total arcos del grafo
    """
    return gr.numEdges(analyzer)

# Funciones utilizadas para comparar elementos dentro de una lista

def compareAirportIATAs(airport, keyvalueairport):
    """
    Compara dos aeropuertos
    """
    airportcode = keyvalueairport['key']
    if (airport == airportcode):
        return 0
    elif (airport > airportcode):
        return 1
    else:
        return -1

# Funciones de ordenamiento
