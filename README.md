

```markdown
# 🐍 Assessment Python — Pipeline Completo de Dados  
Web Scraping • Estruturas de Dados • CSV • JSON • Pandas • Excel • SQLAlchemy • Tratamento de Exceções

Este repositório contém um pipeline completo de processamento de dados desenvolvido ao longo de 12 exercícios progressivos.  
O objetivo é demonstrar domínio de:

- Extração de dados estruturados  
- Manipulação com listas, dicionários e sets  
- Exportação para CSV e JSON  
- Carregamento parcial com Pandas  
- Filtragem e transformação  
- Geração de relatórios em Excel  
- Persistência em banco SQLite com SQLAlchemy  
- Tratamento robusto de exceções  

---

# 🔄 Pipeline Completo — Visão Geral / Full Pipeline Overview

```mermaid
flowchart TD

A[Q01 - Extrair HTML / Extract HTML] --> B[Q02 - Lista de Dicionários / List of Dicts]
B --> C[Q03 - Dicionário Indexado + Sets / Indexed Dict + Sets]
C --> D[Q04 - Exportar CSV / Export CSV]
D --> E[Q05 - Exportar e Ler JSON / Export & Read JSON]
E --> F[Q06 - Carregar CSV Parcial / Partial CSV Load]
F --> G[Q07 - Manipular JSON com Pandas / JSON Manipulation]
G --> H[Q08 - Exportar Excel / Export Excel]
H --> I[Q09 - SQLAlchemy Básico / Basic SQLAlchemy]
I --> J[Q10 - Diagnóstico de Erros / Error Diagnosis]
J --> K[Q11 - Correção de Leitura / CSV Fix + KeyError]
K --> L[Q12 - Pipeline SQL Robusto / Robust SQL Pipeline]

style A fill:#d4f1f9,stroke:#0aa
style B fill:#d4f1f9,stroke:#0aa
style C fill:#d4f1f9,stroke:#0aa
style D fill:#f9f1d4,stroke:#aa0
style E fill:#f9f1d4,stroke:#aa0
style F fill:#f9e3d4,stroke:#a50
style G fill:#f9e3d4,stroke:#a50
style H fill:#e3f9d4,stroke:#0a5
style I fill:#e3f9d4,stroke:#0a5
style J fill:#f4d4f9,stroke:#a0a
style K fill:#f4d4f9,stroke:#a0a
style L fill:#d4f9e3,stroke:#0a5
```

---

# ✅ Estrutura do Repositório

Cada arquivo representa uma etapa incremental do pipeline:

- **Q01** — Extração HTML com BeautifulSoup  
- **Q02** — Conversão para lista de dicionários  
- **Q03** — Dicionário indexado + detecção de duplicatas  
- **Q04** — Exportação para CSV  
- **Q05** — Exportação e leitura de JSON  
- **Q06** — Carregamento parcial de CSV com Pandas  
- **Q07** — Manipulação de JSON com Pandas  
- **Q08** — Exportação para Excel  
- **Q09** — Pipeline SQL básico com SQLAlchemy  
- **Q10** — Diagnóstico de erros do pipeline  
- **Q11** — Correção da leitura + tratamento de KeyError  
- **Q12** — Pipeline SQL robusto com try/except/finally  

---

# ✅ Como Executar

```bash
git clone https://github.com/seuusuario/ASSESSMENT_PYTHON.git
cd ASSESSMENT_PYTHON
pip install -r requirements.txt
python3 Q012.py
```

---

# ✅ Requirements

```txt
beautifulsoup4
pandas
sqlalchemy
openpyxl
lxml
requests
```

---

# ✅ Licença

MIT — livre para estudo e evolução.

```

---

