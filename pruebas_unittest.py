import unittest
import funciones_calculo as fc

class Pruebas_unitarias(unittest.TestCase):

    # Prueba de control de la función area_triangulo
    def test1(self):
        self.assertEqual(fc.area_triangulo(3, 4), 6)

    # Prueba de control de la función area_triangulo2
    def test1(self):
        self.assertEqual(fc.area_triangulo2([3, 4]), 6)

    # Prueba de control de la función volumen_prisma    
    def test2(self):
        self.assertEqual(fc.volumen_prisma(1, 4, 10), 20)

    # Prueba de control de la función area_cuadrado
    def test3(self):
        self.assertEqual(fc.area_cuadrado(4), 16)

    # Prueba de control de la función volumen_cubo
    def test4(self):
        self.assertEqual(fc.volumen_cubo(3), 27)

    # Prueba de control de la función area_circulo
    def test5(self):
        self.assertEqual(fc.area_circulo(6), 113.097336)         

    # Prueba de control de la función volumen_esfera     
    def test6(self):
        self.assertEqual(fc.volumen_esfera(2), 33.510322)   

    # Prueba de control de la función contar
    def test7(self):
        self.assertGreater(fc.contar([0]), 0)
    
    # Prueba de control de la función minimo
    def test8(self):
        self.assertEqual(fc.minimo([3, 9, 2]), 2)

    # Prueba de control de la función maximo
    def test9(self):
        self.assertEqual(fc.maximo([3, 9, 2]), 9)         

    # Prueba de control de la función media   
    def test10(self):
        self.assertEqual(fc.media([2, 4]), 3)  

if __name__ == '__main__':
    unittest.main()