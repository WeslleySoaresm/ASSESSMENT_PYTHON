"""Exercício 12 Corrigir a etapa SQL e garantir execução completa
Contexto:
Mesmo após corrigir leitura e manipulação, o restante do pipeline ainda depende da gravação e consulta SQL. A fonte continua sendo o código original, mas modificado no exercício anterior. O artefato final é um pipeline completo que executa sem erros, gravando os dados em banco SQLite e realizando uma consulta SQL válida. O impacto é permitir que o pipeline represente um processo real de persistência, análise e recuperação de dados.
Enunciado:
Continue a correção do código implementando:
Uso de try-except ao criar a conexão com o banco:
exibir mensagem caso o arquivo não possa ser criado ou aberto.
Uso de try-except ao salvar o DataFrame com to_sql():
garantir que erros de escrita sejam capturados, como DataFrame vazio ou problemas de conexão.
Aplicar bloco else para confirmar operação bem-sucedida.
Realizar a query SQL usando:
try-except para capturar erros como "no such table"
imprimir o resultado apenas em caso de sucesso
Garantir que a conexão seja encerrada com finally.
Ao final, imprimir:

"Pipeline corrigido e executado com sucesso!"""

import pandas as pd
from sqlalchemy import create_engine, text
from io import StringIO

csv_dados = """id,valor,categoria,descricao
1,250,credito,Deposito realizado no app
2,-100,debito,Pagamento de boleto
3,480,credito,Recebimento TED
4,-50,debito,Compra online
5,1020,credito,Salario mensal
6,-200,debito,Supermercado
"""

df = None

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

# -4. Exibir DataFrame
if df is not None:
    print("\nPrévia do DataFrame:")
    print(df.head())

# -5. Criar conexão SQL com tratamento de erro
engine = None
conn = None

try:
    engine = create_engine("sqlite:///meubanco.db")
    conn = engine.connect()
    print("\nConexão com banco criada com sucesso!")
except Exception as e:
    print("Erro ao criar conexão com o banco:", e)

# -6. Gravar DataFrame no banco com try/except/else
if conn is not None and df is not None:
    try:
        df.to_sql("tabela_dados", conn, if_exists="replace", index=False)
    except Exception as e:
        print("Erro ao salvar DataFrame no banco:", e)
    else:
        print("Tabela gravada com sucesso!")

# -7. Consulta SQL com try/except
if conn is not None:
    try:
        resultado = conn.execute(text("SELECT * FROM tabela_dados LIMIT 5;"))
        print("\nResultado da consulta SQL:")
        for linha in resultado:
            print(linha)
    except Exception as e:
        print("Erro ao executar consulta SQL:", e)
    finally:
        conn.close()
        print("Conexão encerrada.")

print("\nPipeline corrigido e executado com sucesso!")