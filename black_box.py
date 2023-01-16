import unittest # modulo para poder crear "tests"

def suma(number_1, number_2):
    return abs(number_1) + number_2 # alteramos el valor del numero negativo lo que va a disparar la alerta de nuestro test

class CajaNegraTest(unittest.TestCase): # Creamos una clasa que alberga nuestro test con este modulo

    def test_suma_dos_positivos(self): # "Self" hace una referencia a la misma version
        number_1 = 10
        number_2 = 5

        resultado = suma(number_1, number_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        number_1 = -10
        number_2 = -7

        resultado = suma(number_1, number_2)

        self.assertEqual(resultado, -17)



if __name__ == '__main__':
    unittest.main() # Ejecutamos nuestras pruebas

    