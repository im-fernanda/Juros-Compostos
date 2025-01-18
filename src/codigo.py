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

def gerar_tabela_evolucao(capital, taxa, tempo):
    """
    Gera uma tabela mostrando a evolução do montante ao longo dos períodos.

    Args:
        capital (float): Valor inicial investido.
        taxa (float): Taxa de juros por período (em decimal).
        tempo (int): Número de períodos.

    Returns:
        pandas.DataFrame: Tabela com evolução do montante.
    """
    dados = []
    montante = capital
    for t in range(1, tempo + 1):
        juros = montante * taxa
        montante += juros
        dados.append({"Período": t, "Montante Inicial": montante - juros, "Juros": juros, "Montante Final": montante})
    return pd.DataFrame(dados)

def plotar_grafico_evolucao(tabela):
    """
    Plota um gráfico mostrando a evolução do montante ao longo do tempo.
    
    Args:
        tabela (pandas.DataFrame): Tabela com os dados de evolução.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(tabela["Período"], tabela["Montante Final"], marker='o', label="Montante Final")
    plt.title("Evolução do Montante ao Longo do Tempo")
    plt.xlabel("Período")
    plt.ylabel("Montante (R$)")
    plt.grid()
    plt.legend()
    plt.show()

def main():
    print("Calculadora de Juros Compostos")
    capital = float(input("Digite o capital inicial (R$): "))
    taxa = float(input("Digite a taxa de juros (% ao período): ")) / 100
    tempo = int(input("Digite o número de períodos: "))

    montante_final = calcular_montante(capital, taxa, tempo)
    juros_totais = calcular_juros_totais(montante_final, capital)
    tabela = gerar_tabela_evolucao(capital, taxa, tempo)

    print("\nResumo:")
    print(f"Montante Final: R$ {montante_final:,.2f}")
    print(f"Juros Totais: R$ {juros_totais:,.2f}")
    print("\nEvolução dos Juros:")
    print(tabela)

    salvar = input("\nDeseja salvar os resultados em Excel? (s/n): ").strip().lower()
    if salvar == 's':
        tabela.to_excel("evolucao_juros_compostos.xlsx", index=False)
        print("Tabela salva como 'evolucao_juros_compostos.xlsx'.")

    plotar = input("Deseja visualizar o gráfico de evolução? (s/n): ").strip().lower()
    if plotar == 's':
        plotar_grafico_evolucao(tabela)

if __name__ == "__main__":
    main()