"""Exercício 4 Exportar para CSV usando módulo csv
Contexto:
Os analistas precisam compartilhar o conjunto de dados processado com outras equipes que usam programas diferentes. O CSV é o formato mais aceito. A fonte é o dicionário estruturado no exercício anterior. O artefato desejado é um arquivo CSV salvo em disco, compatível com outras ferramentas.
Enunciado:
Converta o dicionário para uma estrutura apropriada para escrita em CSV.
Salve o arquivo como dados_scraping.csv utilizando o módulo csv.
Trate exceções de escrita com try-except.
Mostre mensagem confirmando o salvamento."""

mport csv
from Q02 import extrair_tabela
from Q03 import construir_dicionario

def exportar_para_csv(dicionario, caminho="dados_scraping.csv"):
    try:
        # Extrair todas as colunas a partir do primeiro registro
        exemplo = next(iter(dicionario.values()))
        colunas = list(exemplo.keys())

        with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=colunas)
            escritor.writeheader()

            for registro in dicionario.values():
                escritor.writerow(registro)

        print(f"Arquivo CSV salvo com sucesso em: {caminho}")

    except Exception as e:
        print(f"Erro ao escrever o arquivo CSV: {e}")


if __name__ == "__main__":
    registros = extrair_tabela()
    coluna_identificador = "Game"

    dicionario, conjunto_valores, duplicados = construir_dicionario(registros, coluna_identificador)

    exportar_para_csv(dicionario)