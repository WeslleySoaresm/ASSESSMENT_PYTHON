
"""Exercício 10 Tratamento de exceções em leitura de arquivos
Contexto:
A equipe técnica da comunidade identificou que um dos scripts centrais do pipeline está falhando antes de concluir qualquer etapa de gravação ou análise. O script tenta carregar um CSV a partir de uma string, manipula colunas inexistentes e ainda cria uma conexão SQL sem verificar se os dados foram carregados corretamente. A fonte será exatamente o código fornecido abaixo, contendo erros estruturais e lógicos. O artefato esperado é uma análise diagnóstica inicial do comportamento defeituoso. O impacto deste exercício é garantir que o aluno compreenda onde e por que o pipeline quebra.
Enunciado:
Execute o código acima em um bloco Python do Deepnote e observe onde ocorrem os erros.
Identifique quais linhas causam falhas e explique no caderno a causa de cada erro.
Não altere o código ainda. Sua tarefa aqui é diagnosticar, não corrigir.
Liste no terminal cada erro encontrado e descreva o tipo de exceção esperado."""
import pandas as pd
from sqlalchemy import create_engine

csv_dados = """id,valor,categoria,descricao
1,250,credito,Deposito realizado no app
2,-100,debito,Pagamento de boleto
3,480,credito,Recebimento TED
4,-50,debito,Compra online
5,1020,credito,Salario mensal
6,-200,debito,Supermercado
"""
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

"""ERRO 1: FileNotFoundError ao tentar ler CSV a partir de uma string.
ERRO 2: UnboundLocalError ao acessar df["valor"] porque df não foi criado.
ERRO 3: UnboundLocalError ao acessar df["origem"]; se df existisse, seria KeyError.
ERRO 4: OK — conexão SQLite criada com sucesso.
ERRO 5: UnboundLocalError ao tentar df.to_sql() porque df não existe.
ERRO 6: OperationalError: tabela não existe ao executar SELECT.
ERRO 7: Loop não executado devido ao erro anterior."""