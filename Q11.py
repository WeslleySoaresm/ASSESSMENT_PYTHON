"""Exercício 11 Tratamento avançado: TypeError, ValueError e KeyError
Contexto:
Após o diagnóstico inicial, a equipe precisa corrigir o pipeline para que a etapa de carregamento do CSV e a manipulação das colunas funcione sem interrupções. A fonte continua sendo o mesmo código defeituoso, mas agora o objetivo é aplicar blocos try, except, else e pass para tornar o carregamento robusto. O artefato é uma versão parcialmente corrigida que permita a progressão do script. O impacto é garantir que operações críticas como leitura de arquivo e cálculo de métricas não interrompam a execução.
Enunciado:
Reescreva apenas as partes necessárias do código defeituoso para:
Usar try-except para corrigir a leitura do CSV:
O aluno deve converter a string para um objeto compatível com read_csv usando io.StringIO.
Caso a leitura falhe, exibir mensagem e interromper apenas essa etapa, não o programa inteiro.
Proteger o cálculo da coluna "valor" usando:
try para capturar KeyError
else para imprimir a média somente se a coluna existir
Tratar a coluna inexistente "origem":
usar try-except KeyError
aplicar pass caso a coluna não exista
imprimir mensagem informando que a coluna será ignorada
Garantir que o DataFrame resultante seja exibido com print(df.head())."""

import pandas as pd
from sqlalchemy import create_engine
from io import StringIO

csv_dados = """id,valor,categoria,descricao
1,250,credito,Deposito realizado no app
2,-100,debito,Pagamento de boleto
3,480,credito,Recebimento TED
4,-50,debito,Compra online
5,1020,credito,Salario mensal
6,-200,debito,Supermercado
"""

df = None  # garante que a variável existe

# -1. Leitura robusta do CSV
try:
    buffer = StringIO(csv_dados)
    df = pd.read_csv(buffer)
    print("CSV carregado com sucesso!")
except Exception as e:
    print("Falha ao carregar CSV:", e)

# -2. Cálculo protegido da coluna 'valor'
try:
    media_valor = df["valor"].mean()
except KeyError:
    print("Coluna 'valor' não encontrada. Média não será calculada.")
else:
    print("Média da coluna 'valor':", media_valor)

# -3. Tratamento da coluna inexistente 'origem'
try:
    contagem_origem = df["origem"].value_counts()
except KeyError:
    print("Coluna 'origem' não existe. Será ignorada.")
    pass

# -4. Exibir DataFrame resultante
if df is not None:
    print("\nPrévia do DataFrame:")
    print(df.head())