"""Exercício 5 Exportar para JSON usando módulo json
Contexto:
Alguns membros da comunidade utilizam sistemas que consomem exclusivamente JSON por causa da compatibilidade com ferramentas de jogos. A fonte será novamente o dicionário criado previamente. O destino é um arquivo JSON. O impacto esperado é garantir interoperabilidade com APIs internas.
Enunciado:
Exporte os dados para dados_scraping.json usando o módulo json.
Reabra o arquivo e exiba seu conteúdo.
Utilize try-except para lidar com erros de leitura e escrita."""

import json
from Q02 import extrair_tabela
from Q03 import construir_dicionario

def exportar_json(dados, caminho="dados_scraping.json"):
    try:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print(f"Arquivo JSON salvo com sucesso em: {caminho}")
    except Exception as e:
        print(f"Erro ao salvar JSON: {e}")


def ler_json(caminho="dados_scraping.json"):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            conteudo = json.load(arquivo)
        print("Conteúdo do JSON carregado:")
        print(conteudo)
        return conteudo
    except FileNotFoundError:
        print("Arquivo JSON não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao decodificar o JSON.")
    except Exception as e:
        print(f"Erro inesperado ao ler JSON: {e}")


if __name__ == "__main__":
    registros = extrair_tabela()
    coluna_identificador = "Game"

    dicionario, conjunto_valores, duplicados = construir_dicionario(registros, coluna_identificador)

    exportar_json(dicionario)
    ler_json()