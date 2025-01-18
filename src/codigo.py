import pandas as pd
import matplotlib.pyplot as plt

def calcular_montante(capital, taxa, tempo):
    """
    Calcula o montante com base em juros compostos.
    
    Args:
        capital (float): Valor inicial investido.
        taxa (float): Taxa de juros por período (em decimal, ex: 5% -> 0.05).
        tempo (int): Número de períodos.

    Returns:
        float: Montante final.
    """
    return capital * (1 + taxa) ** tempo

def calcular_juros_totais(montante, capital):
    """
    Calcula os juros totais acumulados.
    
    Args:
        montante (float): Valor final acumulado.
        capital (float): Valor inicial investido.

    Returns:
        float: Juros acumulados.
    """
    return montante - capital