"""Exercício 9 Criar e consultar banco SQL com SQLAlchemy
Contexto:
A comunidade quer armazenar dados de forma estruturada em um banco relacional leve para possibilitar consultas rápidas e combinadas. A fonte é o arquivo CSV salvo anteriormente. O artefato desejado é uma base SQL em memória com consultas realizadas via Pandas. O impacto é integrar SQL ao fluxo analítico.
Enunciado:
Crie uma engine SQLite em memória com SQLAlchemy.
Carregue dados_scraping.csv em um DataFrame.
Salve o DataFrame na tabela SQL tabela_scraping.
Execute uma consulta SQL simples com pd.read_sql_query e imprima o resultado.
O código apresentado abaixo não roda em sua forma atual e contém diversos problemas estruturais que impedem qualquer execução completa. Ele tenta carregar arquivos que não existem, acessar colunas que podem não estar disponíveis, gravar dados em um banco mesmo quando o DataFrame não foi carregado e executar queries SQL sem garantir que a tabela foi criada. Além disso, nenhum desses pontos possui tratamento de exceção, o que faz o script quebrar logo nas primeiras linhas.
Alguns exemplos claros dos problemas:
Tenta abrir um arquivo CSV que não existe, causando FileNotFoundError.
Calcula média usando uma coluna que pode não existir, gerando KeyError.
Usa um DataFrame possivelmente não criado, produzindo UnboundLocalError.
Tenta escrever em SQL mesmo sem dados válidos, causando ValueError ou erros de conexão.
Executa consultas SQL em tabelas que podem não ter sido criadas.
Não há qualquer uso de try, except, else ou pass.
Nos Exercícios 10, 11 e 12, você irá corrigir progressivamente esse código, implementando tratamento de exceções e garantindo que o pipeline seja capaz de continuar funcionando mesmo quando algumas etapas falham.
A execução esperada ao final dos três exercícios é um pipeline robusto que:
Tenta carregar o CSV e informa claramente se falhou ou teve sucesso.
Realiza cálculos somente quando o DataFrame existe e tem as colunas necessárias.
Conecta ao banco sem interromper o programa em caso de falha.
Grava dados em SQL apenas quando há dados válidos.
Executa consultas com segurança.
Ao final, imprime um relatório com o status de cada etapa (sucesso ou falha).
Nunca interrompe o pipeline por causa de um erro não tratado.
import pandas as pd
from sqlalchemy import create_engine

csv_dados = id,valor,categoria,descricao
1,250,credito,Deposito realizado no app
2,-100,debito,Pagamento de boleto
3,480,credito,Recebimento TED
4,-50,debito,Compra online
5,1020,credito,Salario mensal
6,-200,debito,Supermercado

# Tentativa de carregar CSV diretamente da string (inválido)
df = pd.read_csv(csv_dados)

print("Arquivo carregado!")

# Tentativa de acessar coluna que pode não existir
media_valor = df["valor"].mean()
print("Média calculada:", media_valor)

# Manipulação de coluna inexistente
media_categoria = df["origem"].value_counts()
print("Contagem:", media_categoria)

# Criar conexão com banco SQL (em arquivo)
engine = create_engine("sqlite:///meubanco.db")

conn = engine.connect()

# Tentativa de escrever tabela sem verificar df
df.to_sql("tabela_dados", conn, if_exists="replace", index=False)
print("Tabela gravada com sucesso!")

# Tentativa de consulta sem validação
consulta = conn.execute("SELECT * FROM tabela_dados;")
for linha in consulta:
    print(linha)

conn.close()

print("Pipeline executado com sucesso!")
"""

import pandas as pd
from sqlalchemy import create_engine

# 1. Criar engine SQLite em memória
engine = create_engine("sqlite:///:memory:")

# 2. Carregar CSV salvo anteriormente
df = pd.read_csv("dados_scraping.csv")

print("CSV carregado com sucesso!")
print(df.head())

# 3. Salvar DataFrame na tabela SQL
df.to_sql("tabela_scraping", engine, if_exists="replace", index=False)
print("Tabela SQL criada com sucesso!")

# 4. Executar consulta SQL simples
consulta = pd.read_sql_query("SELECT * FROM tabela_scraping LIMIT 5;", engine)

print("\nResultado da consulta SQL:")
print(consulta)