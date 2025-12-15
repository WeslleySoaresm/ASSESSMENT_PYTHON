"""Exercício 8 Gerar relatório em Excel
Contexto:
Moderadores que não usam Python precisam acessar os dados em Excel. O DataFrame deve ser salvo nesse formato. A fonte é o DataFrame do exercício anterior. O destino será um arquivo .xlsx. O impacto é criar relatórios acessíveis a todos.
Enunciado:
Salve o DataFrame em relatorio_final.xlsx usando .to_excel.
Certifique-se de não incluir o índice como coluna.
Mostre uma mensagem confirmando o salvamento."""

import pandas as pd
from Q07 import carregar_e_filtrar_json

def salvar_excel(df, caminho="relatorio_final.xlsx"):
    try:
        df.to_excel(caminho, index=False)
        print(f"Relatório Excel salvo com sucesso em: {caminho}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo Excel: {e}")


if __name__ == "__main__":
    # Carrega o DataFrame filtrado do exercício anterior
    df_filtrado = carregar_e_filtrar_json()

    # Salva em Excel
    salvar_excel(df_filtrado)