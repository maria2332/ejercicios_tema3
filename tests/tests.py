#test ejercicios

import unittest
from ejercicios import *

class TestEjercicios(unittest.TestCase):
        
        def setUp(self):
             return super().setUp()
        
        def test_ejercicio1(self):    
            origen = Torre()
            destino = Torre()
            auxiliar = Torre()
    
            # Apilando discos en la torre de origen
            for i in range(6, 0, -1):
                print("Se ha movido el disco", i)
                disco = Disco(i)
                origen.apilar(disco)
    
            torres_hanoi(6, origen, destino, auxiliar)
    
            self.assertEqual(origen.obtener_altura(), 0)
            self.assertEqual(destino.obtener_altura(), 6)
            self.assertEqual(auxiliar.obtener_altura(), 0)

        def test_ejercicio2(self):
             
            matrix = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]
    
            self.assertEqual(determinant_sarrus_recursive(matrix), 0)
            self.assertEqual(determinant_sarrus_iterative(matrix), 0)             
            
        def test_ejercicio4(self):
