import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("datos/sri_ventas_2024.csv")

    def test_valores_no_negativos(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        for valor in resumen.values():
            self.assertGreaterEqual(valor, 0)

    def test_cantidad_provincias_logica(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        total = len(resumen)
        # Ecuador tiene entre 15 y 30 provincias en diferentes datasets
        self.assertTrue(15 <= total <= 30)

    def test_provincia_existente(self):
        resultado = self.analizador.ventas_por_provincia("PICHINCHA")
        self.assertGreater(resultado, 0)

    def test_provincia_inexistente(self):
        with self.assertRaises(KeyError):
            self.analizador.ventas_por_provincia("NARNIA")

if __name__ == "__main__":
    unittest.main()
