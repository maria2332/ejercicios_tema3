"""
Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves– de las que conocemos su nombre, largo, tripulación y c
antidad de pasajeros, desarrollar los algoritmos necesarios para resolver las actividades detalladas a continuación:

realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente;

mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
indicar cuál es la nave que requiere mayor cantidad de tripulación;
mostrar todas las naves que comienzan con AT;
listar todas las naves que pueden llevar seis o más pasajeros;
mostrar toda la información de la nave más pequeña y la más grande.
"""

class Nave:
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros
        self.siguiente = None

class Lista:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def insertar(self, nave):
        if self.primero is None:
            self.primero = nave
            self.ultimo = nave
        else:
            self.ultimo.siguiente = nave
            self.ultimo = nave
        self.tamanio += 1

    def obtener_primero(self):
        return self.primero

    def obtener_ultimo(self):
        return self.ultimo

    def obtener_tamanio(self):
        return self.tamanio

    def esta_vacia(self):
        return self.primero is None

    def __iter__(self):
        self.nave_actual = self.primero
        return self

    def __next__(self):
        if self.nave_actual is None:
            raise StopIteration
        else:
            nave = self.nave_actual
            self.nave_actual = self.nave_actual.siguiente
            return nave

#     def __str__(self):
#         cadena = ""
#         for nave in self:
#             cadena += str(nave.nombre) + " - " + str(nave.largo) + " - " + str(nave.tripulacion) + " - " + str(nave.pasajeros) + " - " + str(nave.siguiente) + " - " + " - " + " - " + "

# "
#             return cadena

