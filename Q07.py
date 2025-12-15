import pandas as pd
"""Exercício 7 Manipular JSON com Pandas
Contexto:
Os dados também foram salvos em JSON e precisam ser analisados pela equipe. O objetivo é treinar conversão e manipulação desse formato. A fonte é dados_scraping.json. O artefato de destino será um DataFrame filtrado. O impacto é reforçar manipulação multiformato.
Enunciado:
Carregue o arquivo JSON com pd.read_json.
Ajuste nomes das colunas com .rename.
Filtre registros com base em valores definidos pelo professor.
Exiba o resultado filtrado."""
import pandas as pd

def carregar_e_filtrar_json(caminho="dados_scraping.json"):
    try:
        # 1) Carregar JSON como DataFrame
        df = pd.read_json(caminho)

        print("\nDataFrame original carregado (jogos como colunas):")
        print(df.head())

        # 2) Transpor: jogos passam a ser linhas, atributos viram colunas
        df = df.T

        print("\nDataFrame transposto (jogos como linhas):")
        print(df.head())

        # 3) Ajustar nomes das colunas
        df = df.rename(columns={
            "Game": "Jogo",
            "Player count[a]": "Jogadores",
            "Release date": "Lancamento"
        })

        print("\nDataFrame com colunas renomeadas:")
        print(df.head())

        # 4) Exemplo de filtro (ajuste conforme o professor pedir)
        # Aqui: filtrar jogos lançados a partir de 2018
        # (filtro baseado em string, sem fazer parsing de data para manter simples)
        mascara = df["Lancamento"].str.contains("2018|2019|2020|2021|2022|2023", na=False)
        filtrado = df[mascara]

        print("\nResultado filtrado:")
        print(filtrado)

        return filtrado

    except FileNotFoundError:
        print("Arquivo JSON não encontrado.")
    except ValueError as e:
        print(f"Erro ao carregar JSON: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    carregar_e_filtrar_json()