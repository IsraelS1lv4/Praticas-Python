INTRODUÇÃO A CIÊNCIA DE DADOS COM PANDAS
Pandas é uma biblioteca para manipulação e análise de dados, escrita em Python. Ela fornece
ferramentas de análise de dados e estruturas de dados de alta performance e fáceis de usar. Por ser a
principal e mais completa biblioteca para estes objetivos, Pandas é fundamental para Análise de Dados.
Em uma simples definição, DataFrame (df), ou quadro de dados, é como se fosse uma planilha de Excel
ou uma tabela de banco de dados. É composto por colunas, linhas e índice. Quando nós lemos algum
arquivo de dados, ele se torna um DataFrame para o Pandas.
Após instalar e importar o Pandas, é possível utilizar muitas funções nativas para ler seus dados,
normalmente iniciando por pd.read_[extensão], exemplo:
df = pd.read_csv('caminho_arquivo.csv', sep='separador')
df = pd.read_csv ('vendas_202005.csv', set = ';')
Os seguintes comandos permitem conhecer um pouco os seus dados:
df.head ()
df.shape ()
df.info ()
df.describe ()
Há diversos outros comandos importantes e úteis, como adicionar nova coluna, remover coluna, filtrar,
agrupar, calcular valores estatísticos, plotar gráficos etc. O objetivo deste trabalho é fazer o aluno
pesquisar sobre a biblioteca Pandas e realizar algumas operações básicas utilizando o ambiente Google
Colaboratory. 
PARTE 1 – Analisar os dados da série NBA-ELO
Você deve acessar e baixar o dataset (conjunto de dados) no endereço indicado no Link 1 abaixo. Tratase de um histórico de resultados e outras informações sobre os jogos da NBA. O arquivo completo
possui 17 Mb. Os seus dados deverão ser analisados utilizando TODAS as operações, filtragens e
gráficos conforme explicados e apresentados no Link 2 abaixo. Se preferir você pode adicionar outras
análises além daquelas indicadas no Link 2, ou seja, os itens do Link 2 são os mínimos.
[Link 1] https://github.com/fivethirtyeight/data/tree/master/nba-elo
[Link 2] https://realpython.com/pandas-python-explore-dataset/
PARTE 2 – Analisar os dados de um outro dataset
Você deve escolher um outro dataset dentre os disponíveis no Link 3 a seguir e proceder a análise de
dados (incluindo operações simples, estatísticas e gráficos) conforme proposto no Link 2 acima.
Novamente, você pode adicionar outras análises além daquelas indicadas no Link 2. Não esqueça de
explicar brevemente o que representam/o que são os datasets que você está analisando.
[Link 3] https://github.com/fivethirtyeight/data
As soluções das PARTES 1 e 2 devem ser submetidas no SIGAA em um único arquivo .PDF com a tela do
trabalho resolvido no Google Colaboratory (com todas as células expandidas e executadas), com um
link público para o seu respectivo Colab. 
Um exemplo em PDF com a estrutura de saída do trabalho está disponível no ambiente Solar para
simples consulta. 
Referências:
https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
https://medium.com/data-hackers/uma-introdu%C3%A7%C3%A3o-simples-ao-pandas-1e15eea37fa1
https://medium.com/data-hackers/uma-introdu%C3%A7%C3%A3o-simples-ao-pandas-1e15eea37fa1
https://assets.datacamp.com/blog_assets/PandasPythonForDataScience.pdf
https://www.datacamp.com/community/blog/python-pandas-cheat-shee