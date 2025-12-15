import pandas as pd
"""Exercício 6 Carregar CSV parcialmente com Pandas
Contexto:
Para otimizar memória, a comunidade deseja carregar apenas parte das colunas do CSV. Isso simula cenários reais em que datasets são grandes. A fonte é o arquivo dados_scraping.csv. O artefato será um DataFrame contendo apenas colunas selecionadas. O impacto é ensinar carregamento eficiente.
Enunciado:
Leia apenas algumas colunas específicas usando pd.read_csv(..., usecols=[...]).
Exiba as primeiras linhas.
Ordene o DataFrame por uma das colunas escolhidas pelo professor.
Imprima o resultado ordenado."""
def carregar_parcialmente(caminho="dados_scraping.csv"):
    try:
        # Escolha das colunas que serão carregadas
        colunas = ["Game", "Player count[a]", "Release date"]

        df = pd.read_csv(caminho, usecols=colunas)

        print("\nPrimeiras linhas do DataFrame:")
        print(df.head())

        # Ordenar por uma das colunas (exemplo: Release date)
        df_ordenado = df.sort_values(by="Release date")

        print("\nDataFrame ordenado por 'Release date':")
        print(df_ordenado)

        return df_ordenado

    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")
    except ValueError as e:
        print(f"Erro ao carregar colunas: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    carregar_parcialmente()