Projeto de Análise de Dados para Microempreendedores Locais
Visão Geral
Este projeto é uma iniciativa de extensão universitária desenvolvida em parceria com uma ONG local para apoiar microempreendedores da região. Utilizando a biblioteca Pandas do Python, criamos um sistema de análise de dados e um dashboard interativo para fornecer insights valiosos sobre o perfil socioeconômico da região, tendências de mercado e oportunidades de negócio.
Objetivos

Desenvolver um dashboard interativo de dados socioeconômicos e de mercado da região.
Treinar os funcionários da ONG e microempreendedores no uso e interpretação do dashboard.
Identificar oportunidades de negócio para os microempreendedores participantes.

Estrutura do Projeto
Copyprojeto-analise-dados-pandas/
│
├── data/
│   ├── dados_microempreendedores.csv
│   └── estatisticas_por_setor.csv
│
├── scripts/
│   ├── analise_dados.py
│   └── dashboard.py
│
├── notebooks/
│   └── exploracao_dados.ipynb
│
├── resultados/
│   └── distribuicao_renda.png
│
├── requirements.txt
├── README.md
└── .gitignore
Instalação

Clone este repositório:
Copygit clone https://github.com/fern14/estacio_dados_python

Navegue até o diretório do projeto:
Copycd projeto-analise-dados-pandas

Crie um ambiente virtual (opcional, mas recomendado):
Copypython -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`

Instale as dependências:
Copypip install -r requirements.txt


Uso

Para executar a análise de dados:
Copypython scripts/analise_dados.py

Para iniciar o dashboard interativo:
Copystreamlit run scripts/dashboard.py

Para explorar os dados no Jupyter Notebook:
Copyjupyter notebook notebooks/exploracao_dados.ipynb


Dados
Os dados utilizados neste projeto são fictícios e foram criados apenas para fins de demonstração. Em um cenário real, os dados seriam coletados de fontes confiáveis e tratados para remover informações pessoais identificáveis.
Contribuição
Este projeto foi desenvolvido como parte de uma atividade de extensão universitária. Contribuições são bem-vindas! Se você deseja contribuir, por favor:

Faça um fork do repositório
Crie uma nova branch para sua feature (git checkout -b feature/AmazingFeature)
Faça commit de suas mudanças (git commit -m 'Add some AmazingFeature')
Push para a branch (git push origin feature/AmazingFeature)
Abra um Pull Request

Contato
[David Delfino Fernandes] - [contatodavidfernandes@hotmail.com]
Link do Projeto: https://github.com/fern14/estacio_dados_python

Agradecimentos
Todos os microempreendedores participantes
[Estácio] pela oportunidade de realizar este projeto de extensão