import unittest
from juros_compostos import calcular_montante

class TestCalculoJurosCompostos(unittest.TestCase):
    def test_calculo_valores_positivos(self):
        """
        Testa o cálculo de juros compostos com valores positivos.
        """
        capital = 1000.0  # Capital inicial
        taxa = 0.05       # 5% de juros por período
        tempo = 12        # 12 períodos (ex.: meses)

        montante = calcular_montante(capital, taxa, tempo)
        esperado = 1000.0 * (1 + 0.05) ** 12  # Montante esperado
        self.assertAlmostEqual(montante, esperado, places=2)

  def test_calculo_valores_negativos(self):
        """
        Testa o comportamento com capital inicial negativo.
        """
        capital = -1000.0  # Capital inicial negativo
        taxa = 0.05        # 5% de juros por período
        tempo = 12         # 12 períodos (ex.: meses)

        montante = calcular_montante(capital, taxa, tempo)
        esperado = -1000.0 * (1 + 0.05) ** 12  # Montante esperado
        self.assertAlmostEqual(montante, esperado, places=2)
