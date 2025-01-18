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
        
    def test_calculo_taxa_zero(self):
        """
        Testa o cálculo de juros compostos com taxa de juros igual a zero.
        """
        capital = 1000.0  # Capital inicial
        taxa = 0.0        # Taxa de juros zero
        tempo = 12        # 12 períodos

        montante = calcular_montante(capital, taxa, tempo)
        esperado = 1000.0  # O montante não muda
        self.assertEqual(montante, esperado)

    def test_calculo_tempo_zero(self):
        """
        Testa o cálculo de juros compostos com tempo igual a zero.
        """
        capital = 1000.0  # Capital inicial
        taxa = 0.05       # 5% de juros por período
        tempo = 0         # Nenhum período

        montante = calcular_montante(capital, taxa, tempo)
        esperado = 1000.0  # O montante é igual ao capital inicial
        self.assertEqual(montante, esperado)

if __name__ == "__main__":
    unittest.main()
