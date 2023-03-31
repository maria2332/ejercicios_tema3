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

import csv 

class Naves:
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros

    def __str__(self):
        return f"{self.nombre} {self.largo} {self.tripulacion} {self.pasajeros}"

def leer_archivo():
    with open('starships.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        naves = []
        for row in reader:
            naves.append(Naves(row[0], int(row[1]), int(row[2]), int(row[3])))
        return naves
    
class Main:
    def ordenar_nombre(naves):
        naves.sort()
        return naves

    def ordenar_largo(naves):
        naves.sort(reverse=True)
        return naves

    def mostrar_info(naves):
        for nave in naves:
            if nave.nombre == "Millennium Falcon" or nave.nombre == "Death Star":
                print(nave)

    def mayor_pasajeros(naves):
        naves.sort(key=lambda nave: nave.pasajeros, reverse=True)
        return naves[:5]

    def mayor_tripulacion(naves):
        naves.sort(key=lambda nave: nave.tripulacion, reverse=True)
        return naves[0]

    def comienzan_con_AT(naves):
        for nave in naves:
            if nave.nombre.startswith("AT"):
                print(nave)

    def seis_o_mas_pasajeros(naves):
        for nave in naves:
            if nave.pasajeros >= 6:
                print(nave)

    def nave_mas_pequenia(naves):
        naves.sort(key=lambda nave: nave.largo)
        return naves[0]

    def nave_mas_grande(naves):
        naves.sort(key=lambda nave: nave.largo, reverse=True)
        return naves[0]

def main():
    naves = leer_archivo()
    print("Listado ordenado por nombre de las naves de manera ascendente")
    print(Main.ordenar_nombre(naves))
    print("Listado ordenado por largo de las naves de manera descendente")
    print(Main.ordenar_largo(naves))
    print("Mostrar toda la información del Halcón Milenario y la Estrella de la Muerte")
    Main.mostrar_info(naves)
    print("Determinar cuáles son las cinco naves con mayor cantidad de pasajeros")
    print(Main.mayor_pasajeros(naves))
    print("Indicar cuál es la nave que requiere mayor cantidad de tripulación")
    print(Main.mayor_tripulacion(naves))
    print("Mostrar todas las naves que comienzan con AT")
    Main.comienzan_con_AT(naves)
    print("Listar todas las naves que pueden llevar seis o más pasajeros")
    Main.seis_o_mas_pasajeros(naves)
    print("Mostrar toda la información de la nave más pequeña y la más grande")
    print(Main.nave_mas_pequenia(naves))
    print(Main.nave_mas_grande(naves))

if __name__ == "__main__":
    main() 