## Pré requisitos

```
Python == 3.9.13
```

Crie e habilite um ambiente python
```console
  python -m venv venv
```
```console
  venv\Script\activate | windows
  . venv/bin/activate | linux e macOs
```
Instale as dependências do projeto

```console
  pip install -r requirements.txt
```
Se tiver utilizando em ambiente de desenvolvimento
```console
  pip install -r requirements-dev.txt
```

## Uso

Rode o servidor:
```console
uvicorn main:app --reload
```

O servidor estará disponível em: 
```console
http://localhost:8000
```

Para rodas os testes
```
pytest
```
## Rotas

Todas as rotas estão disponíveis nas urls:  /docs ou /redoc, com Swagger or ReDoc.

## Exemplo de rota

http://127.0.0.1:8000/api/adicao?numero1=10&numero2=10