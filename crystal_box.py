import unittest

# Funcion que vamos a "Testear"
def es_mayor_de_edad(edad):
    if edad >= 18:
        return False # Aca intencionalmento hicimo que se activo el Test de mayor de edad y nos avise que salio mal
    else:
        return False



class PruebaDeCristalTest(unittest.TestCase):
    # Hacemos un Test para que verifica que sea mayor de edad
    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    # Hacemos un Test para que verifica que sea menor de edad   
    def test_es_menor_de_edad(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)




if __name__ == '__main__':
    unittest.main(verbosity=2) # "verbosity" es un parametro para que el resultado en la consola sea mas detallado