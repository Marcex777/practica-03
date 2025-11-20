import unittest
from src.procesador import Analizador

class TestProcesador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("datos/sri_ventas_2024.csv")

    def test_provincia_existente(self):
        valor = self.analizador.ventas_por_provincia("PICHINCHA")
        self.assertGreater(valor, 0)

    def test_provincia_inexistente(self):
        with self.assertRaises(KeyError):
            self.analizador.ventas_por_provincia("NARNIA")

if __name__ == "__main__":
    unittest.main()
