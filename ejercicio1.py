"""
En el momento de la creación del mundo, los sacerdotes del templo de Brahma recibieron una plataforma de bronce sobre la cual había tres agujas de diamante. 
En la primera aguja estaban apilados setenta y cuatro discos de oro, cada una ligeramente menor que la que estaba debajo. 
A los sacerdotes se les encomendó la tarea de pasarlos todos desde la primera aguja a la tercera, con dos condiciones, solo puede moverse un disco a la vez, 
y ningún disco podrá ponerse en- cima de otro más pequeño. Se dijo a los sacerdotes que, cuando hubieran terminado de mover los discos, 
llegaría el fin del mundo. Resolver este problema de la Torre de Hanói.
"""

def torre_hanoi(n, origen, destino, temporal):
    if n == 1:
        print("Mueva el disco 1 de la aguja", origen, "a la aguja", destino)
        return
    torre_hanoi(n-1, origen, temporal, destino)
    print("Mueva el disco", n, "de la aguja", origen, "a la aguja", destino)
    torre_hanoi(n-1, temporal, destino, origen)

# Ejemplo de uso: mover 3 discos desde la aguja 1 a la aguja 3
torre_hanoi(3, 1, 3, 2)


# def torre_hanoi(n, origen, destino, temporal):
#     movimientos = {}  # diccionario para guardar los movimientos calculados
#     cola = [(n, origen, destino, temporal)]  # cola para iteración por cola
    
#     while cola:
#         n, origen, destino, temporal = cola.pop(0)
        
#         if n == 1:
#             print("Mueva el disco 1 de la aguja", origen, "a la aguja", destino)
#             movimientos[(n, origen, destino)] = 1
#         else:
#             # verificar si el movimiento ya ha sido calculado
#             if (n-1, origen, temporal) not in movimientos:
#                 cola.insert(0, (n-1, origen, temporal, destino))
#                 continue
#             if (1, origen, destino) not in movimientos:
#                 cola.insert(0, (1, origen, destino, temporal))
#                 continue
#             if (n-1, temporal, destino) not in movimientos:
#                 cola.insert(0, (n-1, temporal, destino, origen))
#                 continue
            
#             # mover los discos y actualizar el diccionario de movimientos
#             print("Mueva el disco", n, "de la aguja", origen, "a la aguja", destino)
#             movimientos[(n, origen, destino)] = 1
#             movimientos[(n-1, origen, temporal)] = 1
#             movimientos[(1, origen, destino)] = 1
#             movimientos[(n-1, temporal, destino)] = 1

# # Ejemplo de uso: mover 3 discos desde la aguja 1 a la aguja 3
# torre_hanoi(3, 1, 3, 2)
