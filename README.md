# ProductFlow - Sistema de Cadastro de Produtos

ProductFlow é um projeto em Flask para gerenciamento de produtos, permitindo cadastrar, atualizar, listar e remover produtos de um banco de dados SQLite. É um projeto simples, ideal para aprendizado ou como base para aplicações mais complexas.

## Funcionalidades

- Listar todos os produtos cadastrados
- Cadastrar um novo produto
- Atualizar informações de um produto existente
- Remover produtos
- Validação de formulários com Flask-WTF

## Tecnologias utilizadas

- Python 3.10+
- Flask
- Flask-WTF
- Flask-SQLAlchemy
- SQLite (banco de dados)
- HTML/Jinja2 para templates

## Estrutura do projeto
```
app/
├── __init__.py        Criação e configuração do app Flask
├── models.py          Modelos de banco de dados (Product)
├── views.py           Rotas e lógica de controle
├── forms.py           Formulários Flask-WTF
├── templates/         Templates HTML (index, register, update)
static/
└── img/
    ├── edit.png # Ícone para botão de edição
    └── remove.png # Ícone para botão de remoção
main.py                Script principal para rodar o app
requirements.txt       Dependências do projeto
.gitignore             Arquivos e pastas ignoradas pelo Git
README.md              Este arquivo
```

## Instalação

1. Clone o repositório:
   `git clone https://github.com/saulcastro-dev/ProductFlow.git`

2. Crie e ative um virtual environment:
   # Windows
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
   # Linux / macOS
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Crie um arquivo .env na raiz do projeto e defina a chave secreta:
   `SECRET_KEY=sua_chave_super_secreta`

## Como rodar

Execute o seguinte comando em um terminal
`flask run`

O servidor Flask iniciará em http://127.0.0.1:5000 por padrão. Você poderá acessar a aplicação pelo navegador e gerenciar os produtos.

## Observações importantes

- Banco de dados: O projeto usa SQLite (datasabe.db). Ele é criado automaticamente em ambiente de desenvolvimento.  
- SECRET_KEY: Nunca suba sua chave secreta para o GitHub. Use **.env** ou variáveis de ambiente.  
- Formulários: Todos os formulários possuem validação básica com **Flask-WTF**.  

## Boas práticas

- Use virtual environments para isolar dependências.  
- Não versionar arquivos sensíveis (**.env**, ***.db**) no Git.  
- Use `url_for` para redirecionamentos, evitando URLs fixas.  
- Em produção, configure corretamente a **SECRET_KEY** e o banco de dados.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
