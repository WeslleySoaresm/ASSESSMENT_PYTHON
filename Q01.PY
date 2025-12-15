import urllib.request
import urllib.error
"""Exercício 1 Download da página HTML com urllib
Contexto:
Analistas de uma comunidade de jogadores de videogame mantêm um sistema colaborativo que coleta estatísticas públicas sobre rankings, populações, lançamentos ou dados de desempenho. O professor selecionou previamente uma página da web que contém uma tabela estruturada e dados estáveis, utilizada como fonte primária. A equipe precisa baixar essa página para iniciar o fluxo de análise. A fonte será essa URL definida pelo professor, e o artefato gerado será um arquivo HTML salvo em disco.
Enunciado:
Usando a URL definida pelo professor, faça o download da página HTML utilizando exclusivamente urllib.request.
Salve o conteúdo bruto em um arquivo local chamado pagina_original.html.
Trate possíveis falhas de conexão utilizando try e except, imprimindo mensagens informativas.
Ao final, imprima confirmação de salvamento."""

URL = "https://en.wikipedia.org/wiki/List_of_most-played_mobile_games_by_player_count"

def baixar_pagina(url: str, destino: str = "pagina_original.html") -> None:
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        resposta = urllib.request.urlopen(req)
        conteudo = resposta.read()

        with open(destino, "wb") as arquivo:
            arquivo.write(conteudo)

        print(f"Arquivo salvo com sucesso em: {destino}")

    except urllib.error.HTTPError as e:
        print(f"Erro HTTP ao acessar a URL: {e.code} - {e.reason}")

    except urllib.error.URLError as e:
        print(f"Falha de conexão: {e.reason}")

    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    baixar_pagina(URL)