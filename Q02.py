from bs4 import BeautifulSoup
"""Exercício 2 Extração de tabela com BeautifulSoup
Contexto:
Após salvar a página localmente, a equipe precisa extrair a tabela principal contida nela. Essa tabela apresenta dados padronizados que serão usados em todo o fluxo analítico. A fonte é o arquivo pagina_original.html gerado no exercício anterior. O artefato desejado é uma lista de dicionários representando linhas estruturadas da tabela. O impacto esperado é habilitar o processamento limpo dos dados coletados.
Enunciado:
Abra o arquivo pagina_original.html e processe seu conteúdo usando BeautifulSoup.
Localize a primeira tabela estruturada da página navegando pela árvore HTML.
Extraia cabeçalhos e valores em uma lista de dicionários.
Exiba os cinco primeiros registros extraídos.
Utilize try-except para evitar falhas caso a tabela não exista.
"""
def extrair_tabela(caminho_html: str = "pagina_original.html"):
    try:
        # Abrir arquivo HTML salvo no exercício anterior
        with open(caminho_html, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

        soup = BeautifulSoup(conteudo, "html.parser")

        # Localizar a primeira tabela estruturada
        tabela = soup.find("table", {"class": "wikitable"})
        if tabela is None:
            print("Nenhuma tabela encontrada no arquivo HTML.")
            return []

        # Extrair cabeçalhos
        cabecalhos = []
        header_row = tabela.find("tr")
        if header_row:
            for th in header_row.find_all(["th", "td"]):
                cabecalhos.append(th.get_text(strip=True))

        # Extrair linhas
        dados = []
        for linha in tabela.find_all("tr")[1:]:  # Ignora cabeçalho
            colunas = linha.find_all(["td", "th"])
            if len(colunas) != len(cabecalhos):
                continue  # pula linhas quebradas
            valores = [col.get_text(strip=True) for col in colunas]
            dados.append(dict(zip(cabecalhos, valores)))

        return dados

    except FileNotFoundError:
        print("Arquivo pagina_original.html não encontrado.")
        return []

    except Exception as e:
        print(f"Erro inesperado: {e}")
        return []


if __name__ == "__main__":
    registros = extrair_tabela()

    # Exibir os cinco primeiros registros
    for item in registros[:5]:
        print(item)