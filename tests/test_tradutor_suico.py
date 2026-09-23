import unittest

from tradutor_suico import ComparadorDialetoSuico


class TestComparadorDialetoSuico(unittest.TestCase):
    def setUp(self):
        self.comparador = ComparadorDialetoSuico()

    def test_termo_conhecido(self):
        resultado = self.comparador.traduzir_para_suico("Kartoffel")
        self.assertIn("Härdöpfel", resultado)

    def test_espacos_sao_ignorados(self):
        resultado = self.comparador.traduzir_para_suico("  Samstag  ")
        self.assertIn("Samschtig", resultado)

    def test_termo_desconhecido(self):
        resultado = self.comparador.traduzir_para_suico("Haus")
        self.assertIn("não foi encontrado", resultado)

    def test_termo_vazio(self):
        with self.assertRaises(ValueError):
            self.comparador.traduzir_para_suico("   ")


if __name__ == "__main__":
    unittest.main()
