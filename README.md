# Minha Estante Virtual 

## Sobre o projeto

A Minha Estante Virtual é uma aplicação web que permite registrar livros já lidos e armazenar informações sobre cada um deles, como título, autor, avaliação, data de leitura, gênero e resenha.

O programa conta com três páginas principais:

**Página inicial**: exibe todos os livros cadastrados em formato de cards e disponibiliza uma barra de pesquisa por título.
**Página de detalhes**: apresenta todas as informações registradas sobre um livro selecionado.
**Página de cadastro**: contém um formulário para adicionar novos livros à estante.


## Tecnologias utilizadas

**Front-end**: HTML, CSS e JavaScript.
**Back-end**: Python e Flask.
**Armazenamento de dados**: arquivo CSV.

O back-end é responsável por processar os dados enviados pelo formulário, armazená-los no arquivo CSV e disponibilizar as informações necessárias para a exibição dos livros na interface.

## Como utilizar

**Adicionar um livro**: clique no botão "+" localizado no canto superior direito da página inicial.
Preencher o formulário: informe os dados do livro e envie o formulário pelo botão localizado na parte inferior da página.
**Visualizar os livros**: após o cadastro, um novo card será exibido na página inicial com as informações do livro.
**Consultar os detalhes**: clique em um card para acessar uma página com informações completas sobre o livro.
**Voltar à página inicial**: utilize o botão "Voltar", localizado na parte inferior da página de detalhes.
**Pesquisar livros**: utilize a barra de pesquisa na página inicial para encontrar livros pelo título.
**Alternar o tema**: clique no botão localizado ao lado do botão "+" para alternar entre os temas claro e escuro.

## Como executar o projeto
### Pré-requisitos

Antes de começar, você precisa ter instalado:

**Python**
Git (opcional, para clonar o repositório)
1. Clone o repositório
Se você já baixou o projeto, basta abrir a pasta no VS Code.

2. Crie um ambiente virtual
No terminal integrado do VS Code, execute:

**Windows**:
python -m venv venv
venv\Scripts\activate

**Linux/macOS**:
python3 -m venv venv
source venv/bin/activate

3. Instale as dependências
Com o ambiente virtual ativado, instale o Flask:
pip install Flask

4. Execute a aplicação
No terminal, dentro da pasta do projeto, execute:
python app.py

5. Acesse a aplicação
Após iniciar o servidor Flask, abra o navegador e acesse:
http://127.0.0.1:5000

A aplicação estará disponível enquanto o servidor estiver em execução no terminal.

Para encerrar o servidor, pressione Ctrl + C no terminal.