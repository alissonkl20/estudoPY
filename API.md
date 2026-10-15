# Construir APIs com Python — o que aprender e como organizar o código

Guia prático para quem já sabe Python básico/intermediário ([readme.md](readme.md), [README.md](README.md)) e quer **criar uma API web** (backend que responde HTTP, em geral JSON).

**Pré-requisitos no repositório:** módulos e pacotes ([README §19](README.md#19-módulos-pacotes-e-o-runtime)), funções, OOP leve, exceções, type hints (recomendado), `async` (útil com FastAPI).

**Trilha geral:** [ESTUDO.md](ESTUDO.md)

---

## Índice

1. [O que é uma API (na prática)](#1-o-que-é-uma-api-na-prática)
2. [Mapa do que estudar (ordem sugerida)](#2-mapa-do-que-estudar-ordem-sugerida)
3. [HTTP — o protocolo que você precisa dominar](#3-http--o-protocolo-que-você-precisa-dominar)
4. [REST e desenho de endpoints](#4-rest-e-desenho-de-endpoints)
5. [JSON, validação e contratos](#5-json-validação-e-contratos)
6. [Escolha de stack (FastAPI em foco)](#6-escolha-de-stack-fastapi-em-foco)
7. [Arquitetura em camadas (como dividir arquivos)](#7-arquitetura-em-camadas-como-dividir-arquivos)
8. [Usar código de outro arquivo — guia completo](#8-usar-código-de-outro-arquivo--guia-completo)
9. [Persistência (banco de dados)](#9-persistência-banco-de-dados)
10. [Autenticação e autorização](#10-autenticação-e-autorização)
11. [Erros, logs e status HTTP](#11-erros-logs-e-status-http)
12. [Testes de API](#12-testes-de-api)
13. [Rodar localmente e variáveis de ambiente](#13-rodar-localmente-e-variáveis-de-ambiente)
14. [Produção (visão geral)](#14-produção-visão-geral)
15. [Checklist “API pronta para aprender de verdade”](#15-checklist-api-pronta-para-aprender-de-verdade)
16. [Projeto mínimo de referência (estrutura + exemplos)](#16-projeto-mínimo-de-referência-estrutura--exemplos)

**Nível avançado (redes, REST a fundo, OAuth, escala, GraphQL/gRPC):** [API-AVANCADO.md](API-AVANCADO.md)

---

## 1. O que é uma API (na prática)

Uma **API** (Application Programming Interface) aqui significa, quase sempre, um **servidor HTTP** que:

1. **Escuta** uma porta (ex.: `8000`).
2. **Recebe** pedidos: método (`GET`, `POST`…), URL (`/users/1`), cabeçalhos, corpo (muitas vezes JSON).
3. **Executa** lógica (validar, buscar no banco, calcular).
4. **Responde** com status (`200`, `404`…), cabeçalhos e corpo (JSON, texto, arquivo).

Quem chama não precisa ser um navegador: app mobile, outro backend, script Python, `curl`, Postman.

```text
Cliente                    Servidor (sua API)
   |  GET /produtos/3           |
   | ------------------------>  |
   |                            | lê banco, monta JSON
   |  200 + {"id":3,"nome":"…"} |
   | <------------------------  |
```

Você **não** precisa decorar tudo de rede no início; precisa saber **método + URL + corpo + status + JSON**.

---

## 2. Mapa do que estudar (ordem sugerida)

| Fase | Tópico | Por quê | Onde no repo / fora |
| ---- | ------ | ------- | ------------------- |
| 0 | Python sólido: `dict`, funções, classes, exceções, módulos | API é vários arquivos trabalhando juntos | [readme.md](readme.md), [README §12–19](README.md) |
| 1 | HTTP: métodos, status, headers, body | Cada rota é um pedido HTTP | [§3](#3-http--o-protocolo-que-você-precisa-dominar) |
| 2 | JSON + `json` stdlib | Troca de dados padrão | [§5](#5-json-validação-e-contratos) |
| 3 | REST (recursos, URLs, verbos) | Linguagem comum de APIs | [§4](#4-rest-e-desenho-de-endpoints) |
| 4 | Framework: **FastAPI** (ou Flask/Django depois) | Roteamento, servidor, docs automáticas | [§6](#6-escolha-de-stack-fastapi-em-foco) |
| 5 | Pydantic (modelos de entrada/saída) | Validação + documentação | [§5](#5-json-validação-e-contratos) |
| 6 | Organização em pastas e **imports** | Projeto real = muitos `.py` | [§7](#7-arquitetura-em-camadas-como-dividir-arquivos), [§8](#8-usar-código-de-outro-arquivo--guia-completo) |
| 7 | Banco (SQLite → PostgreSQL) + ORM | Dados que sobrevivem ao restart | [§9](#9-persistência-banco-de-dados) |
| 8 | Auth (JWT ou sessão) | Quem pode fazer o quê | [§10](#10-autenticação-e-autorização) |
| 9 | Testes (`pytest` + `TestClient`) | Não quebrar ao mudar código | [§12](#12-testes-de-api) |
| 10 | Deploy, HTTPS, env vars | Colocar na internet com segurança | [§13–14](#13-rodar-localmente-e-variáveis-de-ambiente) |
| 11+ | Redes, REST maduro, cache, CORS, OAuth, filas, observabilidade | APIs em produção e arquitetura | [API-AVANCADO.md](API-AVANCADO.md) |

**Paralelo útil:** [README §20 async](README.md#20-concorrência-threads-processos-async) — FastAPI é `async`-friendly (I/O de banco e HTTP externo).

---

## 3. HTTP — o protocolo que você precisa dominar

### 3.1 Métodos (verbos)

| Método | Uso típico | Corpo no pedido? | Exemplo |
| ------ | ---------- | ---------------- | ------- |
| `GET` | Ler recurso | Não (em geral) | Listar usuários |
| `POST` | Criar recurso | Sim (JSON) | Criar usuário |
| `PUT` | Substituir recurso inteiro | Sim | Atualizar perfil completo |
| `PATCH` | Atualizar parte | Sim | Só mudar email |
| `DELETE` | Remover | Raro | Apagar produto |

### 3.2 Status HTTP (memorize os principais)

| Código | Significado | Quando usar |
| ------ | ----------- | ----------- |
| `200` | OK | `GET`/`PATCH` com sucesso |
| `201` | Created | `POST` criou algo |
| `204` | No Content | `DELETE` ok, sem corpo |
| `400` | Bad Request | JSON inválido, regra de negócio no cliente |
| `401` | Unauthorized | Não autenticado |
| `403` | Forbidden | Autenticado, mas sem permissão |
| `404` | Not Found | ID não existe |
| `422` | Unprocessable Entity | Dados não passam na validação (FastAPI/Pydantic) |
| `500` | Internal Server Error | Bug ou falha inesperada no servidor |

### 3.3 Cabeçalhos comuns

| Header | Função |
| ------ | ------ |
| `Content-Type: application/json` | Corpo é JSON |
| `Authorization: Bearer <token>` | Token JWT (muito comum) |
| `Accept: application/json` | Cliente prefere JSON na resposta |

### 3.4 Exemplo com `curl` (sem escrever Python ainda)

```bash
# GET
curl -s http://127.0.0.1:8000/health

# POST com JSON
curl -s -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"nome": "Caneta", "preco": 2.5}'
```

---

## 4. REST e desenho de endpoints

**REST** não é uma lei; é um **estilo**: URLs nomeiam **recursos** (substantivos), métodos HTTP indicam a **ação**.

| Ruim (ação na URL) | Melhor (recurso + verbo HTTP) |
| ------------------ | ----------------------------- |
| `POST /criarUsuario` | `POST /users` |
| `GET /deletarProduto/5` | `DELETE /products/5` |
| `GET /getAllOrders` | `GET /orders` |

**Boas práticas:**

- URLs em **plural** e **minúsculas**: `/users`, `/order-items` (ou `order_items` — escolha um padrão).
- **IDs** no path: `/users/{user_id}`.
- **Filtros** na query string: `GET /products?categoria=livros&limit=10`.
- **Versionar** se a API for pública: `/v1/users` ou header `Accept-Version`.

```text
GET    /users           → lista
POST   /users           → cria
GET    /users/42        → um usuário
PATCH  /users/42        → atualiza parcial
DELETE /users/42        → remove
```

---

## 5. JSON, validação e contratos

### 5.1 JSON em Python

```python
import json

texto = '{"nome": "Ana", "idade": 30}'
dados = json.loads(texto)          # str → dict
outro = json.dumps(dados, ensure_ascii=False)  # dict → str
```

Na API, o framework costuma fazer isso por você quando você declara **modelos**.

### 5.2 Pydantic (FastAPI)

Você descreve **o formato esperado**; se o cliente mandar errado, a API responde `422` com detalhes.

```python
from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    preco: float = Field(gt=0)

class ItemOut(BaseModel):
    id: int
    nome: str
    preco: float
```

| Conceito | Papel na API |
| -------- | ------------ |
| **Schema / DTO** (`ItemCreate`) | O que **entra** (body) |
| **Schema de saída** (`ItemOut`) | O que **sai** (resposta) |
| **Model de domínio** (classe ou ORM) | Como você representa no código/banco |

Não misture tudo no mesmo arquivo para sempre; veja [§7](#7-arquitetura-em-camadas-como-dividir-arquivos).

---

## 6. Escolha de stack (FastAPI em foco)

| Ferramenta | Quando considerar |
| ---------- | ----------------- |
| **FastAPI** | API moderna, tipos, docs automáticas (`/docs`), async |
| **Flask** | Minimalista, muito material, você monta peças |
| **Django + DRF** | Site + admin + API grande no mesmo projeto |

Este guia usa **FastAPI** nos exemplos.

### 6.1 Instalação (ambiente virtual)

```bash
cd "/home/alisson/Documentos/apps de aprendizado/python-estudo"
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
pip install "fastapi[standard]" uvicorn
```

### 6.2 App mínima (um arquivo só — só para começar)

```python
# main.py
from fastapi import FastAPI

app = FastAPI(title="Minha API")

@app.get("/health")
def health():
    return {"status": "ok"}

# Rodar: uvicorn main:app --reload
```

- `main` = nome do arquivo `main.py` (sem `.py`).
- `app` = variável `FastAPI` dentro desse módulo.
- `--reload` = reinicia ao salvar (desenvolvimento).

Abra `http://127.0.0.1:8000/docs` — documentação interativa gerada dos tipos e rotas.

### 6.3 Rota com body e resposta tipada

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ItemCreate(BaseModel):
    nome: str
    preco: float

_items: dict[int, dict] = {}
_next_id = 1

@app.post("/items", status_code=201)
def criar_item(body: ItemCreate):
    global _next_id
    item = {"id": _next_id, **body.model_dump()}
    _items[_next_id] = item
    _next_id += 1
    return item

@app.get("/items/{item_id}")
def obter_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return _items[item_id]
```

---

## 7. Arquitetura em camadas (como dividir arquivos)

Quando o projeto cresce, **um `main.py` gigante** fica difícil de testar e de entender. Divisão comum:

| Camada | Responsabilidade | Exemplo de arquivo |
| ------ | ---------------- | ------------------ |
| **Rotas / controllers** | HTTP: path, método, status, chamar serviço | `routers/items.py` |
| **Serviços** | Regras de negócio (sem saber de HTTP) | `services/item_service.py` |
| **Repositório** | Acesso a dados (SQL, arquivo) | `repositories/item_repo.py` |
| **Schemas** | Pydantic entrada/saída | `schemas/item.py` |
| **Models** | Tabelas ORM (SQLAlchemy etc.) | `models/item.py` |
| **Config** | Settings, URL do banco, secrets | `config.py` |
| **Main** | Cria `app`, registra routers | `main.py` |

```text
minha_api/
  pyproject.toml          # ou requirements.txt
  .env                    # NÃO commitar — secrets locais
  src/
    minha_api/
      __init__.py
      main.py             # app = FastAPI(); include_router(...)
      config.py
      schemas/
        __init__.py
        item.py
      services/
        __init__.py
        item_service.py
      repositories/
        __init__.py
        item_repo.py
      routers/
        __init__.py
        items.py
  tests/
    test_items.py
```

**Regra prática:** rota **fina** — só valida HTTP, chama serviço, devolve schema. Lógica pesada no **serviço**.

---

## 8. Usar código de outro arquivo — guia completo

Esta é a parte que mais trava quem vem de um único script. Resumo: **Python só usa o que você importou** e que **existe no caminho de importação** (`sys.path`).

### 8.1 O que você precisa saber (checklist mental)

Quando você está em `arquivo_a.py` e quer usar `funcao_x` de `arquivo_b.py`, responda:

| Pergunta | O que decidir |
| -------- | ------------- |
| **Onde está o outro arquivo?** | Mesma pasta? Subpasta? Pacote `src/`? |
| **Qual é o nome do módulo?** | Nome do arquivo **sem** `.py` → `item_service.py` → módulo `item_service` |
| **O que eu quero usar?** | Função `criar_item`, classe `ItemService`, constante `MAX_ITENS` |
| **Está definido no topo do outro arquivo?** | Só nomes definidos (ou importados) lá podem ser reexportados |
| **É pacote ou script solto?** | Pasta com `__init__.py` (ou projeto moderno com `pyproject`) = pacote |
| **Como eu executo o programa?** | `python main.py` vs `uvicorn pacote.main:app` muda o **diretório de trabalho** e o path |

### 8.2 Módulo = um arquivo `.py`

```text
pasta/
  util.py
  main.py
```

`util.py`:

```python
def somar(a: int, b: int) -> int:
    return a + b

PI = 3.14159
```

`main.py`:

```python
import util

print(util.somar(2, 3))
print(util.PI)

from util import somar

print(somar(10, 1))
```

**Informação necessária:** o arquivo `util.py` precisa estar no **mesmo diretório** de onde o Python resolve imports (geralmente a pasta de onde você rodou o comando, ou entradas em `PYTHONPATH` / pacote instalado).

### 8.3 Pacote = pasta com código organizado

```text
minha_api/
  minha_api/
    __init__.py      # pode estar vazio
    math_util.py
    main.py
```

`math_util.py`:

```python
def dobro(n: int) -> int:
    return n * 2
```

`main.py`:

```python
from minha_api.math_util import dobro

print(dobro(21))
```

Aqui o **nome do pacote** é a pasta `minha_api` (a interna). Você importa `minha_api.math_util`, não só `math_util`, a menos que esteja **dentro** do pacote (imports relativos).

### 8.4 `import` vs `from ... import`

```python
import services.item_service as item_svc
item_svc.criar_item(...)

from services.item_service import criar_item
criar_item(...)

from services import item_service   # exige services/__init__.py
item_service.criar_item(...)
```

| Forma | Vantagem | Cuidado |
| ----- | -------- | ------- |
| `import modulo` | Namespace claro | Digitação maior |
| `from modulo import nome` | Curto | Nome pode colidir com outro |
| `from pacote import *` | — | **Evite** — polui e esconde origem |

### 8.5 Imports relativos (dentro do mesmo pacote)

Só funcionam **dentro de um pacote**, não em script executado como `python arquivo.py` na raiz errada.

`routers/items.py`:

```python
from ..schemas.item import ItemCreate      # sobe um nível, entra em schemas
from ..services.item_service import ItemService
```

| Sintaxe | Significado |
| ------- | ----------- |
| `from .modulo import x` | mesmo pacote |
| `from ..modulo import x` | pacote pai |
| `from ...modulo import x` | dois níveis acima |

Se der `ImportError: attempted relative import with no known parent package`, você rodou o arquivo como script solto — use `uvicorn minha_api.main:app` a partir da raiz do projeto ou `python -m minha_api.main`.

### 8.6 O que pode ser importado?

Python importa **nomes** ligados no outro módulo:

```python
# service.py
def publica():
    ...

def _interna():
    ...   # convenção: não importar de fora (mas não é proibido)

__all__ = ["publica"]   # opcional: controla `from service import *`
```

Você precisa saber o **nome exato** (`publica`, não `Publica` — Python é case-sensitive).

### 8.7 `if __name__ == "__main__"`

```python
# item_service.py
def listar():
    return []

def main():
    print(listar())

if __name__ == "__main__":
    main()
```

- **Importado:** só carrega funções; **não** roda `main()`.
- **Executado** `python item_service.py`: roda o bloco de teste/manual.

### 8.8 Exemplo API: rota usa serviço e schema

`schemas/item.py`:

```python
from pydantic import BaseModel

class ItemCreate(BaseModel):
    nome: str
    preco: float

class ItemOut(BaseModel):
    id: int
    nome: str
    preco: float
```

`services/item_service.py`:

```python
from minha_api.schemas.item import ItemCreate, ItemOut

_db: dict[int, ItemOut] = {}
_seq = 0

def criar_item(dados: ItemCreate) -> ItemOut:
    global _seq
    _seq += 1
    item = ItemOut(id=_seq, nome=dados.nome, preco=dados.preco)
    _db[_seq] = item
    return item

def obter_item(item_id: int) -> ItemOut | None:
    return _db.get(item_id)
```

`routers/items.py`:

```python
from fastapi import APIRouter, HTTPException

from minha_api.schemas.item import ItemCreate, ItemOut
from minha_api.services.item_service import criar_item, obter_item

router = APIRouter(prefix="/items", tags=["items"])

@router.post("", response_model=ItemOut, status_code=201)
def post_item(body: ItemCreate):
    return criar_item(body)

@router.get("/{item_id}", response_model=ItemOut)
def get_item(item_id: int):
    item = obter_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Não encontrado")
    return item
```

`main.py`:

```python
from fastapi import FastAPI

from minha_api.routers.items import router as items_router

app = FastAPI()
app.include_router(items_router)
```

**Informações que você usou entre arquivos:**

1. Caminho do pacote: `minha_api`.
2. Nomes exportados: `ItemCreate`, `ItemOut`, `criar_item`, `obter_item`, `router`.
3. Tipos para o FastAPI: `body: ItemCreate`, `response_model=ItemOut`.

### 8.9 Erros comuns de import

| Erro | Causa provável | Correção |
| ---- | -------------- | -------- |
| `ModuleNotFoundError: No module named 'minha_api'` | Pacote não está no path | Rodar da raiz; `pip install -e .`; ou `PYTHONPATH=src` |
| `ImportError: cannot import name 'x'` | Nome não existe ou import circular | Abrir o arquivo; conferir ortografia; extrair terceiro módulo |
| Relative import failed | `python routers/items.py` direto | `uvicorn minha_api.main:app` ou `python -m ...` |
| Importa mas dá `None` / comportamento estranho | Import circular parcial | Serviços não devem importar routers |

### 8.10 Import circular (evitar)

```text
A importa B  e  B importa A  → muitas vezes quebra
```

**Solução:** dependência em uma direção só: `routers → services → repositories → models`. Schemas não importam services.

---

## 9. Persistência (banco de dados)

API de verdade **guarda dados** fora da memória do processo.

| Estágio | Ferramenta |
| ------- | ---------- |
| Aprender SQL | SQLite (arquivo `.db`, zero servidor) |
| API séria | PostgreSQL ou MySQL |
| ORM comum em FastAPI | SQLAlchemy 2.x + Alembic (migrações) |
| Alternativa | SQLModel (Pydantic + SQLAlchemy) |

Fluxo típico:

1. **Model** ORM ↔ tabela.
2. **Repositório** executa queries.
3. **Serviço** aplica regras.
4. **Rota** chama serviço.

Conceitos SQL mínimos: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `WHERE`, chave primária, foreign key, transação.

**Nunca** monte SQL com f-string de input do usuário — risco de **SQL injection**. Use parâmetros do ORM/driver.

---

## 10. Autenticação e autorização

| Termo | Significado |
| ----- | ----------- |
| **Autenticação** | Quem é você? (login, token) |
| **Autorização** | O que você pode fazer? (admin vs user) |

Padrões comuns em APIs:

- **JWT** no header `Authorization: Bearer ...` — stateless, popular em mobile/SPAs.
- **Sessão + cookie** — comum em sites Django.
- **API Key** — scripts e integrações simples.

Estude depois dos CRUDs básicos: hash de senha (`passlib` / `bcrypt`), expiração de token, rotas protegidas com `Depends()` no FastAPI.

---

## 11. Erros, logs e status HTTP

- Use **`HTTPException`** para erros esperados (`404`, `400`).
- Não exponha stack trace ao cliente em produção.
- Troque `print` por **`logging`** ([README §22 / ESTUDO lacunas](ESTUDO.md#o-que-estudar-fora-dos-readmes)).

```python
import logging

logger = logging.getLogger(__name__)

def criar_item(dados):
    logger.info("criando item nome=%s", dados.nome)
    ...
```

---

## 12. Testes de API

```python
from fastapi.testclient import TestClient
from minha_api.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
```

Rode com `pytest`. Testes chamam a API **sem** subir servidor na rede — rápidos e repetíveis.

---

## 13. Rodar localmente e variáveis de ambiente

Secrets (senha do banco, chave JWT) vêm de **ambiente**, não do código:

```python
# config.py (exemplo com pydantic-settings)
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./app.db"
    secret_key: str = "troque-em-producao"

    class Config:
        env_file = ".env"

settings = Settings()
```

```bash
# .env (não commitar)
DATABASE_URL=postgresql://user:pass@localhost/db
SECRET_KEY=uma-chave-longa-e-aleatoria
```

---

## 14. Produção (visão geral)

| Tópico | O que aprender |
| ------ | -------------- |
| Servidor ASGI | Gunicorn + Uvicorn workers, ou Hypercorn |
| HTTPS | Certificado (Let's Encrypt), reverse proxy (Nginx, Caddy) |
| Docker | Imagem com seu app + variáveis de ambiente |
| Migrações | Alembic antes de deploy |
| CORS | Configurar origens permitidas se o front for outro domínio |
| Rate limit / cache | Depois do básico estável |

---

## 15. Checklist “API pronta para aprender de verdade”

### Conceitos

- [ ] Explicar diferença entre `GET` e `POST`
- [ ] Saber quando usar `201`, `404`, `422`, `401`
- [ ] Desenhar URLs REST para um recurso (ex.: tarefas)
- [ ] Ler e escrever JSON em Python

### Python / projeto

- [ ] Criar `venv` e instalar dependências
- [ ] Dividir projeto em pelo menos: `main`, `router`, `service`, `schema`
- [ ] Importar função de outro módulo sem `ImportError`
- [ ] Explicar `if __name__ == "__main__"`

### FastAPI

- [ ] App com `/health` e `/docs`
- [ ] `POST` com Pydantic e `GET` por id
- [ ] `HTTPException` para não encontrado
- [ ] `APIRouter` + `include_router`
- [ ] Um teste com `TestClient`

### Próximo nível

- [ ] SQLite + SQLAlchemy (CRUD)
- [ ] Alembic (migração)
- [ ] Login + JWT em rota protegida
- [ ] `.env` e settings
- [ ] Deploy em um VPS ou PaaS (um ambiente só)

---

## 16. Projeto mínimo de referência (estrutura + exemplos)

Copie mentalmente esta árvore ao praticar (pode criar na pasta `api_exemplo/` do repo):

```text
api_exemplo/
  requirements.txt       # fastapi[standard], uvicorn
  src/
    api_exemplo/
      __init__.py
      main.py
      schemas/
        __init__.py
        task.py
      services/
        __init__.py
        task_service.py
      routers/
        __init__.py
        tasks.py
```

Comandos:

```bash
cd api_exemplo
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn api_exemplo.main:app --reload --app-dir src
```

Documentação interativa: `http://127.0.0.1:8000/docs`.

---

## Referências rápidas

| Recurso | Link / comando |
| ------- | -------------- |
| FastAPI tutorial | https://fastapi.tiangolo.com/tutorial/ |
| HTTP (visão geral) | MDN Web Docs — HTTP |
| Módulos Python | [README §19](README.md#19-módulos-pacotes-e-o-runtime) |
| Async | [README §20](README.md#20-concorrência-threads-processos-async) |
| Trilha completa | [ESTUDO.md](ESTUDO.md) |
| Redes, REST avançado, OWASP, GraphQL/gRPC | [API-AVANCADO.md](API-AVANCADO.md) |

---

*Atualize os checklists conforme for implementando. O caminho mais eficiente: uma API pequena (CRUD de uma entidade) com 4–5 arquivos, testes, depois banco e auth.*
