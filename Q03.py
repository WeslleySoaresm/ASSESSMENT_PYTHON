"""Exercício 3 Construção de dicionário e uso de sets
Contexto:
A equipe responsável pela análise de dados precisa reorganizar as informações coletadas no exercício anterior em estruturas mais eficientes.
A fonte consiste na lista de dicionários gerada pela extração da tabela HTML, onde cada item da lista representa uma linha da tabela e cada chave do dicionário corresponde a uma coluna.
O objetivo é transformar essa lista em um dicionário indexado por uma coluna escolhida e, em paralelo, usar um conjunto (set) para detectar valores repetidos nessa mesma coluna.
O artefato esperado é um dicionário bem estruturado e um relatório de unicidade.
O impacto esperado é facilitar consultas rápidas, análises posteriores e a detecção de eventuais duplicidades no conjunto de dados original.
Enunciado:
Utilize a lista de dicionários gerada no exercício anterior. Cada elemento da lista representa uma linha da tabela e cada chave do dicionário representa uma coluna.
Escolha uma coluna (por exemplo "coluna_x") que servirá como identificador único. Essa coluna deve existir em todos os registros.
Construa um dicionário onde:
a chave será o valor da coluna escolhida
o valor será o dicionário completo da linha correspondente
Formato esperado:

{
    valor_chave_1: {coluna: valor, coluna: valor, ...},
    valor_chave_2: {coluna: valor, coluna: valor, ...},
    ...
}
Crie um set contendo todos os valores presentes na coluna escolhida.
Compare:
o número total de linhas da lista original
o número total de valores únicos no conjunto e identifique duplicatas produzindo uma lista com todos os valores que aparecem mais de uma vez.
Imprima um relatório final no seguinte formato:
Total de registros: X
Total de valores únicos: Y
Duplicatas encontradas: [...]"""


from Q02 import extrair_tabela

def construir_dicionario(registros, coluna_chave):
    dicionario_indexado = {}
    valores_vistos = set()
    duplicados = set()

    for linha in registros:
        if coluna_chave not in linha:
            # Caso raro, mas evita quebra
            continue

        valor = linha[coluna_chave]

        # Detectar duplicidade
        if valor in valores_vistos:
            duplicados.add(valor)
        else:
            valores_vistos.add(valor)

        # Construir dicionário indexado
        dicionario_indexado[valor] = linha

    return dicionario_indexado, valores_vistos, duplicados


if __name__ == "__main__":
    registros = extrair_tabela()
    coluna_identificador = "Game"   # coluna escolhida

    # Construir estruturas
    dicionario, conjunto_valores, duplicados = construir_dicionario(registros, coluna_identificador)

    # Comparações solicitadas
    total_registros = len(registros)
    total_unicos = len(conjunto_valores)
    lista_duplicados = list(duplicados)

    # Relatório final
    print(f"Total de registros: {total_registros}")
    print(f"Total de valores únicos: {total_unicos}")
    print(f"Duplicatas encontradas: {lista_duplicados}")