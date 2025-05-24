# API de Sorteio de Números

Uma API simples desenvolvida com Flask para realizar sorteios de números aleatórios únicos. Esta API é ideal para sorteios, seleções aleatórias ou qualquer situação que necessite de geração de números aleatórios únicos.

## Funcionalidades

- Geração de números aleatórios únicos dentro de um intervalo especificado
- Quantidade configurável de participantes e números sorteados
- Retorno dos resultados com data e hora do sorteio
- Endpoint REST para fácil integração

## Requisitos do Sistema

- Python 3.11.2
- Flask
- virtualenv (para gerenciamento do ambiente virtual)

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:

```bash
bash virtualenv venv
```

3. Ative o ambiente virtual:
   
- No Windows:
```bash
venv\Scripts\activate
```
- No Linux/MacOS:
```bash
source venv/bin/activate
```

4. Instale as dependências:

```bash
pip install flask
```

## Como Usar

Inicie a aplicação:

```bash
python app.py
```

O servidor será iniciado em `http://localhost:5000`

### Endpoint da API

#### GET /

Gera números aleatórios únicos.

Parâmetros de consulta:
- `pessoas` (opcional): O número máximo do intervalo (padrão: 10)
- `sorteados` (opcional): Quantidade de números a serem sorteados (padrão: 1)

Exemplo de Requisição:

```bash
curl "http://localhost:5000/?pessoas=100&sorteados=5"
```
Exemplo de Resposta:

```json
{
    "data": "2023-10-01 12:00:00",
    "sorteados": [1, 2, 3, 4, 5]
}
```

## Desenvolvimento

A aplicação roda em modo de desenvolvimento (debug) por padrão quando executada diretamente pelo Python, facilitando o desenvolvimento e testes.

## Exemplos de Uso

1. Sorteio simples (valores padrão):

```bash
curl "http://localhost:5000/"
```

2. Sorteio com intervalo de 1 a 50 e sorteando 5 números:

```bash
curl "http://localhost:5000/?pessoas=50&sorteados=5"
```

## Estrutura do Projeto

```
├── app.py # Arquivo principal da aplicação
├── README.md # Documentação do projeto
├── requirements.txt # Dependências do projeto
└── venv/ # Ambiente virtual Python
```

## Como Contribuir

1. Faça um Fork do projeto
2. Crie uma Branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Suporte

Para suporte, abra uma issue no repositório do projeto.

 