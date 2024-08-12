# API de Cadastro e Consulta de Cartões

Uma API para cadastro e consulta de números de cartão de crédito, com autenticação JWT, criptografia AES, e suporte para upload de arquivos TXT.

## Tabela de Conteúdos
- [Descrição](#descrição)
- [Instalação](#instalação)
- [Uso](#uso)
- [Documentação da API](#documentação-da-api)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Autores](#autores)
- [Considerações Finais](#considerações-finais)

## Descrição
Esta API permite cadastrar e consultar números de cartão de crédito com segurança, utilizando criptografia e autenticação JWT. Também suporta upload de arquivos TXT para processamento em massa.

## Instalação
Siga os passos abaixo para configurar o ambiente:

### Pré-requisitos
- Python 3.8+
- Sqlite3
- Redis

### Passos para Instalação

1. Clone o repositório:
```bash
git clone https://github.com/rubens-mariano/desafio-hyperativa.git
cd seu-repositorio
```
2. Crie um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Configure o banco de dados:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Crie um superusuário:
```bash
python manage.py createsuperuser
```
6. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```


## Uso
### Autenticação
Obtenha o token JWT:
```bash
POST /api/token/
{
  "username": "seu-usuario",
  "password": "sua-senha"
}
```
Use o token JWT para autenticação em outras requisições:
```bash
Authorization: Bearer <seu-token-jwt>
```

## Inserção de Dados
Modelo de cadastro de um novo cartão:
```bash
POST /api/cards/
{
  "card_number": "1234567812345678"
}
```

### Upload de Arquivo TXT
Faça o upload de um arquivo TXT com números de cartão:
```bash
POST /api/upload/
Arquivo: Modelo.txt
```

## Documentação da API

### Endpoints

#### Autenticação
- **POST /api/token/**: Gera um token JWT.
- **POST /api/token/refresh/**: Renova o token JWT.

#### Cartões
- **POST /api/cards/**: Cadastra um novo cartão.
- **POST /api/upload/**: Faz upload de um arquivo TXT contendo números de cartões.
- **GET /api/cards/{card_number}/**: Consulta se um cartão existe no banco de dados.

## Licença
Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autores
- **Rubens Mariano Lindner** - Desenvolvedor Principal - [[GitHub](https://github.com/rubens-mariano)](https://github.com/rubens-mariano)




