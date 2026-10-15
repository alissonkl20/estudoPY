# Trilha de estudo Python — básico → avançado → especialista

Este arquivo é o **índice mestre** do repositório. Use-o para saber *o que estudar*, *em que ordem* e *onde está cada tema*.

| Recurso | Função |
| -------- | ------ |
| [readme.md](readme.md) | Sintaxe, tipos, operadores, delimitadores, controle, estruturas de dados (visão de curso + tabelas) |
| [README.md](README.md) | Pilares, idioma, modelo de dados, coleções avançadas, OOP, runtime, migração de outras linguagens |
| [API.md](API.md) | Construir APIs (HTTP, REST, FastAPI, camadas, imports entre arquivos, checklist) |
| [API-AVANCADO.md](API-AVANCADO.md) | Redes (TCP/DNS/TLS), HTTP a fundo, REST/HATEOAS, CORS, OAuth, escala, GraphQL/gRPC, OWASP |
| [base.py](base.py) | Código executável — rode e altere para fixar cada tópico |
| **ESTUDO.md** (este) | Checklists, Big O, arquitetura, padrões, lacunas para especialista |

**Como usar:** marque `[x]` conforme dominar. Não precisa ser linear — volte aos símbolos quando travar em `::` ou `*`.

---

## Níveis de proficiência

| Nível | Você consegue… | Materiais principais |
| ----- | -------------- | -------------------- |
| **Básico** | Ler/escrever scripts; tipos; `if`/`for`; list/dict | readme.md + `base.py` (demos `tipos` … `grafo`) |
| **Intermediário** | Código idiomático; erros; funções/OOP leve; coleções certas | README §4–16 + `base.py` (`modelo` … `comprehension`) |
| **Avançado** | Geradores, decorators, hints, async intro, dunders | README §14–21 + `base.py` (`decorator` … `dunder`) |
| **Especialista** | Runtime, performance, produção, domínio (web/dados/etc.) | README §22 + seções abaixo + projetos reais |

---

## Checklist — Básico

- [ ] Big O + estruturas complexas — [readme.md#notação-big-o-e-análise-de-complexidade](readme.md#notação-big-o-e-análise-de-complexidade)
- [ ] Tipos: `int`, `float`, `str`, `bool`, `bytes` — [readme.md#int-inteiro](readme.md)
- [ ] Operadores aritméticos, lógicos, comparação, atribuição — [readme.md#operadores-aritméticos](readme.md)
- [ ] `is` / `in` vs `==` — [readme.md#operadores-de-identidade-e-pertinência](readme.md)
- [ ] `if` / `elif` / `else`, ternário — [readme.md#if--elif--else--decisão-se--senão-se--senão](readme.md)
- [ ] `match` / `case` — [readme.md#match--case--escolha-por-valor-padrão](readme.md)
- [ ] `for`, `range`, `enumerate` — [readme.md#for--repetição-com-quantidade-conhecida](readme.md)
- [ ] `while`, `break`, `continue`, `pass` — [readme.md#while--repetição-enquanto-a-condição-for-verdadeira](readme.md)
- [ ] `try` / `except` / `finally`, `with` — [readme.md#try--except--else--finally--tratamento-de-erro](readme.md)
- [ ] `list`, `tuple`, `set`, `dict` — [readme.md#estruturas-de-dados](readme.md)
- [ ] Pilha, fila, `deque`, `heapq` (conceito) — [readme.md#fila-queue](readme.md)
- [ ] Delimitadores e `::` slice — [readme.md#operadores-delimitadores-e-símbolos-sintáticos](readme.md)
- [ ] Keywords e soft keywords — [readme.md#palavras-reservadas-keywords](readme.md)
- [ ] Precedência de operadores — [readme.md#precedência-quem-calcula-primeiro](readme.md)
- [ ] Praticar: `python base.py` e `python base.py controle`
- [ ] Exercícios: `python train.py basico` → `avancado` → `leetcode` → `especialista`

---

## Checklist — Intermediário

- [ ] Pilares: objetos, EAFP, duck typing — [README.md#1-pilares-do-python](README.md)
- [ ] Paradigmas (procedural, OOP, funcional) — [README.md#2-paradigmas](README.md)
- [ ] Símbolos: `*`, `**`, walrus, `range`, `next` — [README.md#3-dicionário-de-caracteres-e-sintaxe](README.md)
- [ ] Mutável/imutável, truthiness, default mutável — [README.md#4-tipos-valores-e-o-modelo-de-dados](README.md)
- [ ] Operadores de sequência e conjunto — [README.md#5-operadores](README.md)
- [ ] Loops + complexidade intro — [README.md#65-loops-e-complexidade-lógica](README.md)
- [ ] Lista (métodos, matriz, deque) — [README.md#7-lista](README.md)
- [ ] Tupla, `NamedTuple`, `dataclass` — [README.md#8-tupla](README.md)
- [ ] `dict` / `set`, `Counter`, `defaultdict` — [README.md#11-dict-set-e-outras-coleções](README.md)
- [ ] Funções: `*args`, closure, LEGB — [README.md#12-funções](README.md)
- [ ] OOP: herança, `@property` — [README.md#13-orientação-a-objetos](README.md)
- [ ] Comprehensions — [README.md#15-comprehensions-e-unpacking](README.md)
- [ ] Exceções e context managers — [README.md#16-exceções-e-context-managers](README.md)
- [ ] Big O aplicado a estruturas Python — [README.md#25-notação-big-o](README.md) + [§ Big O abaixo](#notação-big-o)
- [ ] Praticar: `python base.py lista_av dict funcoes`

---

## Checklist — Avançado

- [ ] Iteradores, geradores, `itertools` — [README.md#14-iteradores-geradores-e-next](README.md)
- [ ] Decorators — [README.md#17-decorators](README.md)
- [ ] Type hints — [README.md#18-tipagem-type-hints](README.md)
- [ ] Módulos, pacotes, `venv`, `__main__` — [README.md#19-módulos-pacotes-e-o-runtime](README.md)
- [ ] Threads vs processos vs `asyncio` — [README.md#20-concorrência-threads-processos-async](README.md)
- [ ] Dunder methods — [README.md#21-dunder-methods-e-metaprogramação](README.md)
- [ ] Linked list (implementação) — [README.md#10-linked-list](README.md)
- [ ] `array`, NumPy (quando usar) — [README.md#9-array](README.md)
- [ ] Armadilhas de migração — [README.md#229-armadilhas-clássicas-na-migração](README.md)
- [ ] Cheat sheet de outra linguagem — [README.md#23-cheat-sheet-outra-linguagem--python](README.md)
- [ ] Praticar: `python base.py iterador decorator async dunder`

---

## Checklist — Especialista (além dos READMEs)

- [ ] Arquitetura CPython (visão) — [README.md#26-arquitetura-do-python-cpython](README.md)
- [ ] GC, `dis`, import system — [README.md#22-avançado-extremo](README.md)
- [ ] Profiling (`cProfile`, `timeit`) — ver [lacunas](#o-que-estudar-fora-dos-readmes)
- [ ] Testes (`pytest`), lint (`ruff`), tipos (`mypy`/`pyright`) — README §22.8
- [ ] Packaging (`pyproject.toml`, `uv`/`hatch`) — README §22.8
- [ ] Design patterns em código real (não só teoria) — [§ Padrões abaixo](#padrões-idiomas-vs-design-patterns)
- [ ] Algoritmos clássicos + análise formal — [§ Big O](#notação-big-o)
- [ ] Trilha de carreira: web **ou** dados **ou** automação **ou** sistemas — [lacunas](#o-que-estudar-fora-dos-readmes)
- [ ] Projeto próprio versionado com testes e README

---

## Mapa de tópicos → onde ler

| Tema | readme.md | README.md | base.py (filtro) |
| ---- | --------- | --------- | ---------------- |
| O que é Python / Zen | — | §1 | `pilares` |
| Arquitetura / GIL | — | §1.9, §26 | `dis`, `async` |
| Operadores (tabelas) | § aritméticos … símbolos | §3, §5 | `aritmetico`, `bitwise` |
| Delimitadores | § delimitadores | §3 | `slice`, `unpack` |
| Keywords | § keywords | §3.6 | `lambda` |
| Tipos de dados | § tipos | §4 | `tipos` |
| Controle / decisão | § estruturas de controle | §6 | `controle` |
| Estruturas de dados | § estruturas | §7–11 | `lista`, `linked`, `fila` |
| Funções | § lambda/yield | §12 | `funcoes` |
| OOP | — | §13 | `oop` |
| Iteração | § for/range | §14 | `iterador` |
| Async | — | §20 | `async` |
| Big O | — | §25 | `bigo` |
| Patterns | — | §22.7 + abaixo | `exercicios` |
| Produção | — | §22.8 | — |

---

## Notação Big O

**Capítulo completo (classes \(O(1)\)…\(O(n!)\), espaço, armadilhas, trie, grafos, union-find):** [readme.md § Big O e estruturas complexas](readme.md#notação-big-o-e-análise-de-complexidade)

**Big O** descreve como o **tempo** ou **memória** de um algoritmo cresce quando o tamanho da entrada \(n\) cresce. Não é “segundos no relógio” — é **ordem de crescimento** (ignora constantes e termos menores).

| Notação | Nome usual | Significado intuitivo |
| ------- | ---------- | --------------------- |
| \(O(1)\) | constante | Não depende de \(n\) (média em hash) |
| \(O(\log n)\) | logarítmica | Divide o problema (busca binária em array ordenado) |
| \(O(n)\) | linear | Um passe sobre \(n\) itens |
| \(O(n \log n)\) | linearítmica | Sort eficiente (Timsort do `list.sort`) |
| \(O(n^2)\) | quadrática | Loop dentro de loop no mesmo \(n\) |
| \(O(2^n)\) | exponencial | Exploração combinatória ingênua |
| \(O(n!)\) | fatorial | Permutações ingênuas |

Também existem **Ω** (limite inferior) e **Θ** (crescimento apertado). Na prática, “Big O” no dia a dia costuma ser o **pior caso assintótico**.

### Estruturas built-in do Python (média / típico)

| Operação | `list` | `dict` / `set` | `deque` |
| -------- | ------ | -------------- | ------- |
| Acesso por índice `[i]` | \(O(1)\) | — | \(O(n)\) no meio* |
| `append` fim | \(O(1)\)* amort. | — | \(O(1)\) |
| `insert(0, x)` / `pop(0)` | \(O(n)\) | — | \(O(1)\) nas pontas |
| `x in coleção` | \(O(n)\) | \(O(1)\)* | \(O(n)\) |
| Busca por chave | — | \(O(1)\)* | — |
| `sort()` | \(O(n \log n)\) | — | — |

\*Amortizado ou “média” em hash tables; pior caso patológico de hash existe mas é raro na prática.

Detalhes de lista: [README.md §7.2](README.md#72-métodos-essenciais). Lista vs linked list: [README.md §10.4](README.md#104-complexidade-lembrete-de-lógica).

### Padrões de loop (regra de bolso)

```text
for x in xs:                    → O(n)   onde n = len(xs)
for x in xs: if x in ys:        → O(n·m) se ys é list; O(n) se ys é set
for i in range(n):
    for j in range(n):          → O(n²)
while n > 1: n //= 2             → O(log n)
```

### Exemplo mental

```python
# O(n) — uma passagem
total = sum(nums)

# O(n²) — para cada item, varre a lista de novo
pares = [(a, b) for a in nums for b in nums if a < b]

# O(n) médio — set para pertinência
vistos = set()
for x in muitos:
    if x in vistos:  # O(1) médio
        ...
    vistos.add(x)
```

### Quando o README não basta

Para **especialista em algoritmos**, estude à parte: ordenação, busca, grafos (BFS/DFS/Dijkstra), árvores (BST, heap), programação dinâmica, e prove complexidade em exercícios. Os READMEs ligam Big O às **estruturas que você usa em Python**, não substituem um curso completo de algoritmos.

**Prática:** `python base.py bigo`

---

## Arquitetura do Python (resumo)

Python como **linguagem** ≠ uma única implementação. O que quase todo mundo usa:

```text
Seu código .py
    → lexer/parser (gera AST)
    → compilador (gera bytecode .pyc)
    → CPython VM (executa bytecode)
    → objetos C + API de objetos Python
```

Pontos que mudam *como* você programa em escala:

| Peça | Efeito prático |
| ---- | -------------- |
| **GIL** | Uma thread executa bytecode Python por vez → threads ajudam em **I/O**; CPU-bound → `multiprocessing` ou libs nativas |
| **Objetos em heap** | Tudo é referência; `is` vs `==`; custo de memória |
| **Tipagem dinâmica** | Flexível; erros de tipo aparecem em runtime (hints + mypy mitigam) |
| **Import system** | Módulos cacheados em `sys.modules`; pacotes com `pyproject.toml` |

Visão expandida: [README.md §26](README.md#26-arquitetura-do-python-cpython).

---

## Padrões: idiomas vs design patterns

### Idiomas pythônicos (prioridade máxima)

| Idioma | Use quando |
| ------ | ---------- |
| **EAFP** | `try`/`except` em vez de checar tudo antes |
| **Comprehension / gerador** | transformar filtrar coleções sem mutar à toa |
| **`with`** | arquivos, locks, conexões |
| **`enumerate` / `zip`** | índice + valor; dois iteráveis em paralelo |
| **`pathlib.Path`** | caminhos de arquivo |
| **f-string** | formatação de texto |
| **`dataclass`** | registros de dados |
| **Função first-class** | `key=`, callbacks, decorators |

Mapa no README: [§22.7](README.md#227-padrões-pythônicos-avançados), [§22.9](README.md#229-armadilhas-clássicas-na-migração).

### Design patterns (GoF) em Python

Python **não exige** classes para muitos patterns:

| Pattern | Em Python costuma ser… |
| ------- | ---------------------- |
| Strategy | função passada como `key` / argumento |
| Observer | callbacks, eventos, signals |
| Factory | função ou `@classmethod` |
| Singleton | módulo único ou instância em módulo (evite overuse) |
| Decorator | `@decorator` literalmente |

Estude patterns **depois** dos idiomas — aplicados em um projeto seu (API, CLI, jogo simples).

### Pattern matching (`match` / `case`)

É **recurso da linguagem** (3.10+), não o GoF “Pattern”. Ver [readme.md](readme.md) e [README.md §6.1](README.md#61-if).

---

## O que estudar fora dos READMEs

Use esta lista como **glossário de lacunas** para o nível especialista. Nenhum único arquivo cobre tudo.

| Área | Por quê | Por onde começar |
| ---- | ------- | ---------------- |
| **Algoritmos & Big O formal** | Entrevistas, performance previsível | Livro/course + LeetCode/HackerRank; [§ Big O](#notação-big-o) |
| **pytest** | Código que não quebra ao mudar | `pytest` docs; README §22.8 |
| **mypy / pyright** | Tipos em projeto grande | Tipar um módulo seu e rodar checker |
| **ruff** | Estilo + bugs comuns | `ruff check .` no projeto |
| **packaging** | Distribuir libs/apps | `pyproject.toml`, tutorial hatch/uv |
| **logging** | Produção sem `print` | `logging` stdlib |
| **HTTP / APIs** | Web backends | [API.md](API.md) → [API-AVANCADO.md](API-AVANCADO.md) + FastAPI ou Django |
| **Bancos de dados** | Persistência | SQLite + SQLAlchemy ou Django ORM |
| **NumPy / pandas** | Dados e ciência | Após dominar list/dict e comprehensions |
| **Profiling** | Otimizar de verdade | `cProfile`, `timeit` — medir antes de “otimizar” |
| **Segurança** | Input, secrets, SQL injection | OWASP básico; nunca commitar `.env` |
| **CPython internals** | Curiosidade / extensões | Talks, “Python Internals”, `dis`, código fonte opcional |
| **Concorrência avançada** | Alta escala I/O | `asyncio` profundo, `trio`, filas externas |
| **C extensions / Rust (PyO3)** | CPU extremo | Só quando profiling mostrar gargalo em Python puro |

---

## Ordem sugerida (12 passos)

1. [readme.md](readme.md) tipos → operadores → controle → estruturas.  
2. [README.md](README.md) §3 símbolos até fluir.  
3. README §4–6 modelo + loops + complexidade.  
4. README §7–11 coleções + [§25 Big O](README.md#25-notação-big-o).  
5. README §12–13 funções e OOP.  
6. README §14–15 iteradores e comprehensions.  
7. README §16–17 exceções e decorators.  
8. README §18–19 hints e módulos.  
9. README §20 async **se** for I/O.  
10. README §21 dunders + mini `Vetor`.  
11. README §22 + §26 runtime.  
12. Projeto pessoal + pytest + um tópico da tabela [lacunas](#o-que-estudar-fora-dos-readmes).

REPL diário: `import this`, `help(str)`, `dir(list)`.

---

## Exercícios (dos READMEs + extras)

- [ ] Inverter string sem e com `[::-1]`
- [ ] FizzBuzz com `match` e com comprehension
- [ ] Frequência com `Counter`
- [ ] Inverter linked list in-place
- [ ] Flatten com gerador
- [ ] Decorator `retry(n)`
- [ ] Classe com `__add__` e `__len__`
- [ ] **Extra:** implementar busca binária e citar complexidade
- [ ] **Extra:** medir `in list` vs `in set` com `timeit` para \(n = 10^4\)

---

## Referência rápida dos arquivos

```text
python-estudo/
  ESTUDO.md      ← você está aqui (trilha e checklists)
  readme.md      ← sintaxe e fundamentos
  README.md      ← idioma e avançado
  API.md         ← guia para construir APIs (base)
  API-AVANCADO.md← redes, REST maduro, segurança e escala
  base.py        ← exemplos executáveis
  train.py       ← exercícios com testes (básico → LeetCode → especialista)
```

*Atualize os checklists conforme avança. Python evolui (match, walrus, free-threading); o modelo (objetos, iteradores, namespaces) permanece.*
