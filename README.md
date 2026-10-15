# Python — da lógica ao avançado

Guia de estudo para quem **já programa** e está migrando para Python. Foco em: o que a linguagem *é*, como ela *pensa*, o que cada **símbolo** faz, e as estruturas que você usa o tempo todo.

> Python 3.11+ (exemplos válidos também em 3.10+).  
> `&&`, `||`, `++`, `--` **não existem**. Equivalentes: `and`, `or`, `+= 1`.

**Trilha completa (checklists, Big O, arquitetura, lacunas para especialista):** [ESTUDO.md](ESTUDO.md)  
**Sintaxe e tabelas do básico:** [readme.md](readme.md) · **Código para rodar:** [base.py](base.py)

---

## Índice

1. [Pilares do Python](#1-pilares-do-python)
2. [Paradigmas](#2-paradigmas)
3. [Dicionário de caracteres e sintaxe](#3-dicionário-de-caracteres-e-sintaxe) ← comece aqui se esquece `::` `.` `,` `range`
4. [Tipos, valores e o modelo de dados](#4-tipos-valores-e-o-modelo-de-dados)
5. [Operadores](#5-operadores)
6. [Condicionais e loops](#6-condicionais-e-loops)
7. [Lista](#7-lista)
8. [Tupla](#8-tupla)
9. [Array](#9-array)
10. [Linked list](#10-linked-list)
11. [Dict, set e outras coleções](#11-dict-set-e-outras-coleções)
12. [Funções](#12-funções)
13. [Orientação a objetos](#13-orientação-a-objetos)
14. [Iteradores, geradores e `next`](#14-iteradores-geradores-e-next)
15. [Comprehensions e unpacking](#15-comprehensions-e-unpacking)
16. [Exceções e context managers](#16-exceções-e-context-managers)
17. [Decorators](#17-decorators)
18. [Tipagem (type hints)](#18-tipagem-type-hints)
19. [Módulos, pacotes e o runtime](#19-módulos-pacotes-e-o-runtime)
20. [Concorrência: threads, processos, async](#20-concorrência-threads-processos-async)
21. [Dunder methods e metaprogramação](#21-dunder-methods-e-metaprogramação)
22. [Avançado extremo](#22-avançado-extremo)
23. [Cheat sheet: outra linguagem → Python](#23-cheat-sheet-outra-linguagem--python)
24. [Como estudar daqui](#24-como-estudar-daqui)
25. [Notação Big O](#25-notação-big-o)
26. [Arquitetura do Python (CPython)](#26-arquitetura-do-python-cpython)

---

## 1. Pilares do Python

Python não é “só uma sintaxe mais limpa”. Ele tem um **contrato de design**. Os pilares abaixo explicam *por que* o código Python parece do jeito que parece.

### 1.1 Legibilidade como feature

Indentação **é** o bloco. Não há `{}` para escopo. O código é escrito para humanos primeiro.

```python
def absoluto(n):
    if n < 0:
        return -n
    return n
```

Equivalente em C/Java/JS: chaves. Em Python, o `:` abre o bloco e a indentação o delimita.

### 1.2 Tudo é objeto

Números, funções, classes, módulos, `None` — tudo é objeto em memória, com tipo, identidade (`id()`) e valor.

```python
x = 10
print(type(x))   # <class 'int'>
print(id(x))     # endereço lógico do objeto
print(x.__class__)
```

Por isso `len`, `+`, `[]` na verdade chamam **métodos dunder** (`__len__`, `__add__`, `__getitem__`). Ver [seção 21](#21-dunder-methods-e-metaprogramação).

### 1.3 Tipagem dinâmica e forte

- **Dinâmica:** o tipo vive no *objeto*, não na variável. `x = 1` depois `x = "oi"` é legal.
- **Forte:** Python **não** converte tipos em silêncio. `"1" + 1` explode. `"1" + str(1)` ou `int("1") + 1` são explícitos.

Isso é o oposto de JS (`"1" + 1 → "11"`) e diferente de PHP (coerção frouxa).

### 1.4 Batteries included

A stdlib cobre filesystem, JSON, HTTP básico, regex, datetime, pathlib, unittest, itertools, collections, concurrent, asyncio… Você raramente precisa de lib para o básico.

### 1.5 Um jeito óbvio (Zen of Python)

Rode `import this` no REPL. Ideias centrais:

| Ideia | Na prática |
|---|---|
| Explicit is better than implicit | `and` em vez de `&&`; `self` explícito |
| Flat is better than nested | evite pirâmide de `if` |
| Readability counts | nomes claros, pouca magia |
| There should be one obvious way | *geralmente* um idioma oficial (EAFP, comprehensions) |
| Special cases aren't special enough to break the rules | consistência > exceção esperta |

### 1.6 EAFP, não LBYL

- **LBYL** (Look Before You Leap): checa antes (`if key in d: ...`).
- **EAFP** (Easier to Ask Forgiveness than Permission): tenta e trata o erro.

```python
# EAFP — o jeito pythônico
try:
    valor = dicionario[chave]
except KeyError:
    valor = padrao
```

### 1.7 Duck typing

“Se anda como pato e grasna como pato, é um pato.” Não importa a classe, importa o **comportamento** (protocolo): se tem `__iter__`, é iterável; se tem `read()`, é file-like.

### 1.8 Namespaces

“Namespaces are one honking great idea.” Tudo vive em um namespace: builtins, módulo, classe, função. `from x import *` polui o namespace — evite.

### 1.9 CPython e o GIL (pilar de runtime)

A implementação oficial é **CPython**. Há um **GIL** (Global Interpreter Lock): só uma thread de bytecode Python roda por vez. Consequência:

- Threads: boas para **I/O**.
- CPU-bound: use **multiprocessing**, **C extensions** (numpy), ou **asyncio** não resolve CPU.

Isso não muda a *sintaxe*; muda como você escala.

---

## 2. Paradigmas

Python é **multiparadigma**. Você mistura os três o tempo todo.

### 2.1 Imperativo / procedural

Sequência de instruções, funções, estado mutável.

```python
total = 0
for n in [1, 2, 3]:
    total += n
```

### 2.2 Orientado a objetos

Classes, herança, dunder methods, protocolos. Tudo já é objeto; OOP é opcional no *seu* código, mas obrigatória no *modelo da linguagem*.

```python
class Conta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
```

### 2.3 Funcional (não puro)

Funções são first-class: passam como argumento, retornam de funções, vivem em variáveis.

Ferramentas: `lambda`, `map`, `filter`, `reduce`, comprehensions, `functools`, geradores, closures, decorators.

```python
nums = [1, 2, 3, 4]
pares = [n for n in nums if n % 2 == 0]
dobro = list(map(lambda x: x * 2, nums))
```

Python **não** é Haskell: não há imutabilidade forçada, não há lazy default (exceto geradores), side effects são normais.

### 2.4 Orientado a protocolos (estrutural)

Em vez de herdar `Iterable`, implemente `__iter__`. Em vez de herdar `ContextManager`, implemente `__enter__` / `__exit__`. Isso é o coração avançado da linguagem.

### 2.5 Qual paradigma usar?

| Situação | Estilo |
|---|---|
| Script, ETL, CLI | procedural + funções |
| Domínio com entidades | classes |
| Transformar coleções | comprehensions / geradores |
| Cross-cutting (log, cache, permissão) | decorators |
| Recurso (arquivo, lock, conexão) | context manager (`with`) |

---

## 3. Dicionário de caracteres e sintaxe

Esta é a seção para quando você olha `xs[::-1]` ou `a, b = b, a` e trava.

### 3.1 Delimitadores de bloco e agrupamento

| Símbolo | Nome | O que faz |
|---|---|---|
| `:` | dois-pontos | Abre bloco (`if`, `for`, `def`, `class`, `try`) **ou** slice **ou** dict **ou** type hint |
| `#` | hash | Comentário até o fim da linha |
| `\` | barra invertida | Continua a linha (prefira parênteses) ou escape em string |
| `()` | parênteses | Chamada, agrupamento, tupla, gerador `(x for x in xs)` |
| `[]` | colchetes | Lista, indexação, slicing, list comprehension |
| `{}` | chaves | Dict, set, dict/set comprehension. **Não** é bloco |
| `;` | ponto-e-vírgula | Junta statements na mesma linha. Evite. Não é obrigatório no fim da linha |
| `indentação` | espaços | **É** o escopo. Padrão: 4 espaços, nunca tab misturado |

```python
# : de bloco
if True:
    pass

# : de dict
pessoa = {"nome": "Ana", "idade": 30}

# : de slice  →  ver :: abaixo
itens[1:4]

# : de type hint
def soma(a: int, b: int) -> int:
    return a + b
```

### 3.2 Ponto `.` — acesso

O `.` navega o objeto: atributo, método, submódulo.

```python
import math
math.sqrt(9)          # atributo do módulo → função → chamada

texto = "Python"
texto.upper()         # método
texto[0]              # NÃO usa ponto; usa []

obj.attr              # lê atributo
obj.attr = 1          # escreve (cria se não existir, em instâncias normais)
obj.metodo()          # chama

# encadeamento
Path("a") / "b"       # pathlib; / é operador sobrecarregado
```

Não existe `->` de ponteiro. Não existe `::` de resolução de escopo (C++). Escopo de classe/módulo é `.`.

### 3.3 Vírgula `,` — separa *e* cria tupla

A vírgula é um dos caracteres mais subestimados.

```python
# 1) separa argumentos / itens
max(1, 2, 3)
lista = [1, 2, 3]
def f(a, b, c): ...

# 2) a VÍRGULA cria a tupla, não o parêntese
t = 1, 2, 3          # tupla
t = (1,)             # tupla de 1 elemento — a vírgula é obrigatória
n = (1)              # isto é só int 1, NÃO tupla

# 3) unpacking / swap
a, b = b, a
nome, idade = ("Ana", 30)

# 4) unpacking em for
for chave, valor in d.items():
    ...

# 5) trailing comma é legal e útil em git diffs
pares = [
    1,
    2,
]
```

### 3.4 Dois-pontos duplo `::` — slice com passo

Sintaxe de slice: `sequencia[inicio:fim:passo]`

| Expressão | Significado |
|---|---|
| `s[i]` | um elemento no índice `i` |
| `s[i:j]` | do `i` (incluso) até `j` (**excluso**) |
| `s[i:j:k]` | idem, de `k` em `k` |
| `s[:]` | cópia rasa da sequência |
| `s[::]` | idem |
| `s[::-1]` | invertida |
| `s[::2]` | um sim, um não (índices pares) |
| `s[1::2]` | índices ímpares |
| `s[:-1]` | todos menos o último |
| `s[-1]` | último |
| `s[-3:]` | os 3 últimos |
| `s[2:]` | do índice 2 até o fim |
| `s[:5]` | os 5 primeiros |

Índices negativos contam do fim: `-1` é o último.

```python
s = "PYTHON"
#  índice:     0  1  2  3  4  5
#  negativo:  -6 -5 -4 -3 -2 -1

s[1:4]     # "YTH"
s[::2]     # "PTO"
s[::-1]    # "NOHTYP"
s[1:-1]    # "YTHO"

# slice é um objeto
sl = slice(1, 4, 2)
s[sl]      # equivalente a s[1:4:2]
```

`::` **não** é operador sozinho. São dois `:` do slice quando `inicio` e `fim` são omitidos: `[inicio=vazio : fim=vazio : passo]`.

### 3.5 Atribuição e setas

| Símbolo | O que faz |
|---|---|
| `=` | atribuição. **Não** é igualdade |
| `==` | igualdade de valor |
| `:=` | walrus — atribui *dentro* de uma expressão (3.8+) |
| `->` | anotação de retorno da função (type hint). **Não** executa nada |
| `=>` | **não existe** em Python (é JS/PHP arrow) |

```python
x = 10
x == 10

# walrus: lê e guarda na mesma expressão
while (linha := input()) != "sair":
    print(linha)

def f(x: int) -> str:   # -> só documentação/tipo
    return str(x)
```

### 3.6 Lógicos: Python **não** tem `&&` `||` `!`

| Outra linguagem | Python |
|---|---|
| `&&` | `and` |
| `\|\|` | `or` |
| `!` | `not` |
| `a ? b : c` | `b if a else c` |
| `true` / `false` | `True` / `False` (maiúsculas) |
| `null` / `nil` | `None` |
| `this` | `self` (convenção, não keyword) |

```python
if a and b or not c:
    ...

# and/or retornam OPERANDO, não necessariamente bool
x = "" or "padrão"     # "padrão"
y = "ok" and 42        # 42
```

### 3.7 Aritméticos e bitwise

| Símbolo | Significado | Extra |
|---|---|---|
| `+` `-` `*` `/` | soma, sub, mul, **divisão float** | `5 / 2 == 2.5` |
| `//` | divisão inteira (floor) | `5 // 2 == 2` |
| `%` | resto (módulo) | também formata string antiga `"%s" % x` |
| `**` | potência | `2 ** 10 == 1024`. `^` **não** é potência |
| `+=` `-=` `*=` … | in-place | não existe `++` nem `--` |
| `&` `\|` `^` | AND, OR, XOR bit a bit | em `set`: interseção, união, simétrica |
| `~` | NOT bit a bit | `~x == -x-1` |
| `<<` `>>` | shift | |

```python
2 ** 3          # 8
5 / 2           # 2.5
5 // 2          # 2
{1, 2} | {2, 3} # {1, 2, 3}  união de conjuntos
```

### 3.8 Comparação

```python
==  !=  <  >  <=  >=
is          # identidade (mesmo objeto), NÃO igualdade
is not
in          # pertence (item in coleção)
not in

# encadeamento — não existe em C/Java
1 < x < 10          # equivalente a 1 < x and x < 10
```

Use `is` **só** com `None`, `True`, `False` e singletons:

```python
if x is None: ...
if x == 10: ...     # valor
if x is 10: ...     # NÃO faça isso (funciona às vezes por internamento, é armadilha)
```

### 3.9 Asterisco `*` e `**`

| Uso | Significado |
|---|---|
| `*args` | empacota argumentos posicionais extras numa tupla |
| `**kwargs` | empacota argumentos nomeados extras num dict |
| `*` na chamada | unpacking de iterável em argumentos |
| `**` na chamada | unpacking de dict em kwargs |
| `*` no unpacking | “o resto” |
| `*` sózinho na def | força args seguintes a serem keyword-only |
| `/` na def | força args anteriores a serem positional-only (3.8+) |
| `*lista` em `[a, *lista, b]` | espalha itens |

```python
def f(a, b, /, c, *, d, **extra):
    ...

def g(*args, **kwargs):
    print(args, kwargs)

g(1, 2, x=3)                 # args=(1,2) kwargs={'x': 3}

nums = [1, 2, 3]
print(*nums)                 # print(1, 2, 3)

a, *meio, z = [1, 2, 3, 4]  # a=1 meio=[2,3] z=4

{**{"a": 1}, "b": 2}         # merge de dicts
```

### 3.10 Arroba `@`

```python
@staticmethod
@classmethod
@property
def f(): ...

# é açúcar para:
def f(): ...
f = decorator(f)

# também: matrix multiply (numpy)  A @ B
```

### 3.11 Underscore `_`

| Forma | Uso |
|---|---|
| `_` | “não me interessa” no unpacking; último resultado no REPL |
| `_nome` | convenção: interno |
| `__nome` | name mangling em classe (`_Classe__nome`) |
| `__nome__` | dunder — protocolo da linguagem. Você *implementa*, quase nunca *inventa* |
| `1_000_000` | separador visual em literais numéricos |

### 3.12 Strings e prefixos

```python
"texto" ou 'texto'      # iguais
"""multi
linha"""
f"olá {nome}"           # interpolação (f-string)
rf"bruto {nome}"        # raw + f
b"bytes"                # bytes, não str
r"c:\n"                 # raw: \n é duas chars, não newline
t"..."                  # template string (3.14+ / PEP 750) — saiba que existe
```

Escape comuns: `\n` `\t` `\\` `\'` `\"` `\uXXXX` `\UXXXXXXXX` `\N{NOME}`.

### 3.13 Outros que confundem

| Símbolo | Significado |
|---|---|
| `...` ou `Ellipsis` | placeholder; slicing numpy `a[..., 0]`; body de stub `def f(): ...` |
| `pass` | statement vazio (não é símbolo, mas ocupa o lugar de `{}`) |
| `~` | bitwise not; em pandas: negação de máscara booleana |
| `:=` | walrus |
| `\|` em type hint | union `int \| None` (3.10+) |
| `[]` em type hint | genéricos `list[int]` (3.9+) |
| `$` | **não existe** (PHP variável, JS template sem o `{}`) |
| `::` sozinho | **não** é resolução de escopo. Só slice |
| `->` | só type hint de retorno |
| `.next` | **não** é o jeito Python 3. Ver [seção 14](#14-iteradores-geradores-e-next) |

### 3.14 `range(...)`

`range` **não** é uma lista. É uma sequência **preguiçosa** de inteiros: ocupa memória constante, seja `range(10)` ou `range(10**12)`.

```python
range(5)           # 0, 1, 2, 3, 4     (fim exclusivo)
range(2, 5)        # 2, 3, 4
range(0, 10, 2)    # 0, 2, 4, 6, 8
range(5, 0, -1)    # 5, 4, 3, 2, 1
range(5, 0)        # vazio — passo default é +1

list(range(3))     # [0, 1, 2]  materializa
for i in range(3): # itera sem criar lista
    ...

# range tem índice e len, mas não é lista
r = range(10, 20)
r[0]               # 10
r[-1]              # 19
len(r)             # 10
15 in r            # True, O(1)
```

Comparação: em JS `Array.from({length: n}, (_, i) => i)`. Em Python, `range` já é isso, sem alocar.

### 3.15 `.next` vs `next()` vs `__next__`

Python 2 tinha `iterador.next()`. **Python 3 removeu**. Hoje:

```python
it = iter([10, 20, 30])   # pega o iterator
print(next(it))           # 10   builtin next()
print(next(it))           # 20
print(next(it))           # 30
print(next(it))           # StopIteration
print(next(it, "fim"))    # "fim"  — default evita exceção

# por baixo dos panos:
it.__next__()             # protocolo; você quase nunca chama direto
```

Arquivos, geradores, `map`, `zip`, dict views — todos são iteradores ou iteráveis. Detalhes na [seção 14](#14-iteradores-geradores-e-next).

---

## 4. Tipos, valores e o modelo de dados

### 4.1 Tipos built-in que importam

| Categoria | Tipos |
|---|---|
| Nulos / bool | `None`, `bool` (`True`/`False` são subclasses de `int`: `True == 1`) |
| Numéricos | `int` (ilimitado), `float` (IEEE-754), `complex` (`3+2j`), `decimal.Decimal`, `fractions.Fraction` |
| Texto / bytes | `str` (Unicode), `bytes`, `bytearray`, `memoryview` |
| Sequências | `list`, `tuple`, `range` |
| Conjuntos | `set`, `frozenset` |
| Mapeamento | `dict` |
| Outros | `function`, `type` (classes são instâncias de `type`) |

### 4.2 Mutável vs imutável

| Imutável | Mutável |
|---|---|
| `int`, `float`, `str`, `tuple`, `frozenset`, `bytes` | `list`, `dict`, `set`, `bytearray` |

Imutável = o *objeto* não muda. `x += 1` em `int` cria **outro** objeto e rebinda o nome `x`.

```python
a = [1, 2]
b = a          # b e a apontam para a MESMA lista
b.append(3)
print(a)       # [1, 2, 3]  — surpresa clássica

a = [1, 2]
b = a.copy()   # ou a[:]  ou list(a)
```

**Nunca** use mutável como default de argumento:

```python
def ruim(xs=[]):       # a mesma lista vive para sempre
    xs.append(1)
    return xs

def bom(xs=None):
    if xs is None:
        xs = []
    xs.append(1)
    return xs
```

### 4.3 Truthiness (o que é “falso”)

Valores **falsy**: `None`, `False`, `0`, `0.0`, `0j`, `""`, `b""`, `[]`, `()`, `{}`, `set()`, objetos com `__bool__` → `False` ou `__len__` → `0`.

Todo o resto é truthy, inclusive `"0"` e `[0]`.

```python
if itens:          # lista não-vazia
    ...
if not nome:       # string vazia ou None
    ...
```

### 4.4 Variável = nome, não caixa

Em C, `int x = 3` é uma caixa. Em Python, `x = 3` é uma **etiqueta** colada num objeto.

```
x ──► 3
depois x = "oi"
x ──► "oi"     (o 3 continua existindo se outra etiqueta apontar; senão o GC recolhe)
```

---

## 5. Operadores

Precedência (alta → baixa), resumida:

1. `()` `[]` `.` `await` `x(...)`
2. `**` (direita → esquerda)
3. `+x` `-x` `~x`
4. `*` `@` `/` `//` `%`
5. `+` `-`
6. `<<` `>>`
7. `&`
8. `^`
9. `|`
10. comparações (`in`, `is`, `==`…) — encadeiam
11. `not`
12. `and`
13. `or`
14. `if/else` ternário
15. `lambda`
16. `:=`

### 5.1 Operadores de sequência

```python
[1, 2] + [3]      # concat → [1, 2, 3]
"ab" * 3          # "ababab"
3 in [1, 2, 3]    # True
len("abc")        # 3
```

### 5.2 Operadores de conjunto

```python
a, b = {1, 2, 3}, {3, 4}
a | b    # união
a & b    # interseção
a - b    # diferença
a ^ b    # simétrica
a <= b   # subconjunto
```

### 5.3 Operador ternário

```python
# JS:  cond ? a : b
valor = a if cond else b
```

### 5.4 Sobrecarga

Qualquer operador pode ser redefinido na classe (`__add__`, `__eq__`, `__matmul__` para `@`…). Por isso `Path("a") / "b"` e `datetime` + `timedelta` funcionam.

---

## 6. Condicionais e loops

### 6.1 `if`

```python
if x > 0:
    ...
elif x == 0:
    ...
else:
    ...

# match/case  (3.10+) — pattern matching, NÃO é switch de C
match status:
    case 200:
        print("ok")
    case 404 | 410:
        print("sumiu")
    case {"erro": msg}:
        print(msg)
    case _:
        print("outro")
```

`_` em `case _` é o default.

### 6.2 `while`

```python
n = 3
while n > 0:
    n -= 1
else:
    # roda se o while TERMINOU sem break
    print("acabou natural")
```

O `else` de loop é único do Python: executa se **não** houve `break`.

### 6.3 `for` — sempre sobre iterável

Não existe `for (i=0; i<n; i++)`. O `for` Python é um `foreach`.

```python
for item in colecao:
    ...
else:
    # se não deu break
    ...

# precisa de índice? enumerate
for i, item in enumerate(colecao, start=0):
    ...

# precisa de C-style? range
for i in range(len(colecao)):   # pouco pythônico se só quer o item
    ...

# dois iteráveis em paralelo
for a, b in zip(lista1, lista2):
    ...

# zip para no mais curto; zip(..., strict=True) explode se tamanhos diferem (3.10+)
```

### 6.4 `break`, `continue`, `pass`

```python
for n in nums:
    if n < 0:
        continue     # pula o resto desta iteração
    if n == 0:
        break        # sai do loop
    ...
# pass = não faça nada (placeholder de bloco)
```

### 6.5 Loops e complexidade (lógica)

- `for` em lista: O(n)
- `x in lista`: O(n) — linear
- `x in set` / `x in dict`: O(1) médio
- loop aninhado: O(n²) — o clássico para otimizar

```python
# ruim: lookup em lista dentro de loop
for x in muitos:
    if x in lista: ...          # O(n*m)

# bom
s = set(lista)
for x in muitos:
    if x in s: ...              # O(n+m)
```

### 6.6 Comprehension vs loop

```python
# loop
out = []
for x in xs:
    if x > 0:
        out.append(x * 2)

# list comprehension — mesmo efeito, idioma padrão
out = [x * 2 for x in xs if x > 0]
```

Use comprehension para **map/filter**. Use loop quando há side effects (print, I/O, múltiplos passos).

---

## 7. Lista

A estrutura nº 1. Array dinâmico (vetor), **não** linked list.

Implementação CPython: array contíguo de *ponteiros* para objetos. Append no fim é amortizado O(1). Insert no início é O(n).

```python
xs = [1, 2, 3]
xs = list()                 # vazia
xs = list("abc")            # ['a', 'b', 'c']
xs = list(range(5))
```

### 7.1 Indexação e fatia (mutável)

```python
xs[0] = 99
xs[-1] = 0
xs[1:3] = [7, 8, 9]         # substitui um pedaço (tamanho pode mudar)
del xs[0]
del xs[1:3]
```

### 7.2 Métodos essenciais

| Método | Efeito | Complexidade |
|---|---|---|
| `append(x)` | adiciona no fim | O(1) amortizado |
| `extend(it)` | concatena iterável | O(k) |
| `insert(i, x)` | insere na posição | O(n) |
| `pop()` | remove o último | O(1) |
| `pop(i)` | remove no índice | O(n) |
| `remove(x)` | remove primeira ocorrência de valor | O(n) |
| `index(x)` | índice da primeira ocorrência | O(n) |
| `count(x)` | quantas vezes | O(n) |
| `sort()` | ordena in-place | O(n log n) Timsort |
| `reverse()` | inverte in-place | O(n) |
| `copy()` | cópia rasa | O(n) |
| `clear()` | esvazia | O(n) |

Funções: `sorted(xs)` devolve **nova** lista; `xs.sort()` altera a original. `reversed(xs)` devolve iterator.

```python
xs.sort(key=str.lower, reverse=True)
sorted(xs, key=lambda p: p.idade)
```

### 7.3 Lista como pilha / fila

```python
# pilha — perfeita
stack.append(x)
stack.pop()

# fila — NÃO use list.pop(0)  → O(n)
from collections import deque
q = deque()
q.append(x)       # direita
q.popleft()       # esquerda O(1)
```

### 7.4 Lista de listas (matriz)

```python
# armadilha
ruim = [[0] * 3] * 3        # 3 linhas APONTAM para a mesma lista
ruim[0][0] = 1              # altera as 3 linhas

bom = [[0] * 3 for _ in range(3)]
```

### 7.5 Cópia rasa vs profunda

```python
import copy
b = a[:]                    # rasa
b = copy.deepcopy(a)        # profunda (aninhadas)
```

---

## 8. Tupla

Sequência **imutável**. Depois de criada, não há `append` nem `t[0] = 1`.

```python
t = (1, 2, 3)
t = 1, 2, 3
unidade = (1,)              # vírgula obrigatória
vazia = ()
t = tuple("ab")             # ('a', 'b')
```

### 8.1 Para que serve se já existe lista?

1. **Sinal de contrato:** “isto não muda”. Chaves de dict, elementos de set (se os itens forem hashable).
2. **Empacotar registros heterogêneos:** `(nome, idade, ativo)` — hoje muita gente usa `dataclass` / `NamedTuple`.
3. **Retorno múltiplo:** `return x, y` é uma tupla.
4. **Um pouco mais leve** que lista (tamanho fixo).

```python
# hashable → pode ser chave
d = {(0, 0): "origem"}

# NÃO hashable se contém mutável
ruim = ([1], 2)             # tupla ok, mas não hashable porque tem lista
```

### 8.2 Named tuple / dataclass

```python
from typing import NamedTuple
from dataclasses import dataclass

class Ponto(NamedTuple):
    x: float
    y: float

@dataclass
class Pessoa:
    nome: str
    idade: int = 0
```

Unpacking funciona igual: `x, y = ponto`.

### 8.3 Tupla vs lista — regra prática

| Quer | Use |
|---|---|
| Coleção homogênea que cresce | `list` |
| Registro fixo, chave, retorno | `tuple` |
| Campos nomeados | `dataclass` / `NamedTuple` |

---

## 9. Array

Três coisas diferentes usam o nome “array”. Não misture.

### 9.1 `list` — “array” do dia a dia

Array de **referências a objetos**. Cada item pode ser de um tipo diferente. É o que você quer 95% do tempo.

```python
misto = [1, "a", None, [2]]
```

### 9.2 `array.array` — array homogêneo compacto (stdlib)

Tipo C, todos os elementos iguais. Economia de memória, não de sintaxe.

```python
from array import array
a = array("i", [1, 2, 3])   # "i" = signed int
a.append(4)
bytes(a)                    # buffer binário
```

Type codes: `b` `B` `h` `H` `i` `I` `f` `d`… (ver `help(array)`).

Quase ninguém usa no app comum. Entre `list` e `numpy`, este fica no meio.

### 9.3 `numpy.ndarray` — array científico

Contíguo, homogêneo, vetorizado, N-dimensional. Operações em C, sem loop Python.

```python
import numpy as np
v = np.array([1, 2, 3])
v * 2                       # array([2, 4, 6])  — não duplica como list*2
M = np.zeros((3, 3))
M[0, :] = 1
M @ M                       # multiplicação de matriz
```

`list * 2` **repete** a lista. `ndarray * 2` **multiplica** elemento a elemento.

### 9.4 `bytearray` / `memoryview`

Arrays de bytes mutáveis; `memoryview` fatia sem copiar (buffer protocol). Nível baixo: I/O, parsers, sockets.

### 9.5 Comparação rápida

| | list | array.array | numpy |
|---|---|---|---|
| Tipos mistos | sim | não | não |
| Sintaxe rica | sim | média | sim |
| Memória | ponteiros | compacta | compacta |
| Matemática vetorial | não | não | sim |
| Uso típico | tudo | binário/embarcado | data/ML/ciência |

---

## 10. Linked list

Python **não tem** linked list na sintaxe. `list` é vetor. Se você precisa de lista encadeada (inserção O(1) no meio *se já tem o nó*), você implementa ou usa `collections.deque` (lista duplamente ligada internamente, mas só nas pontas é O(1) na API).

### 10.1 Por que a stdlib não empurra linked list?

Cache-friendly: vetor ganha na prática. Linked list brilha em exercícios, kernels, undo de editor, e entrevistas.

### 10.2 Implementação clássica (simplesmente encadeada)

```python
from __future__ import annotations
from typing import Optional, Iterator, Iterable


class Node:
    def __init__(self, valor, proximo: Optional["Node"] = None):
        self.valor = valor
        self.proximo = proximo


class LinkedList:
    def __init__(self, itens: Iterable = ()):
        self.cabeca: Optional[Node] = None
        for item in itens:
            self.append(item)

    def append(self, valor) -> None:
        novo = Node(valor)
        if self.cabeca is None:
            self.cabeca = novo
            return
        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo

    def prepend(self, valor) -> None:
        self.cabeca = Node(valor, self.cabeca)

    def __iter__(self) -> Iterator:
        atual = self.cabeca
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __repr__(self) -> str:
        return " -> ".join(map(str, self)) + " -> None"


if __name__ == "__main__":
    ll = LinkedList([1, 2, 3])
    ll.prepend(0)
    print(ll)            # 0 -> 1 -> 2 -> 3 -> None
    print(list(ll))      # [0, 1, 2, 3]  — porque implementamos __iter__
```

### 10.3 Duplamente encadeada

Cada nó tem `anterior` e `proximo`. `deque` já resolve o caso “fila/pilha nas pontas”:

```python
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)
d.pop()
d.rotate(1)
```

### 10.4 Complexidade (lembrete de lógica)

| Operação | list (vetor) | linked list (com cabeça) |
|---|---|---|
| acesso `i`-ésimo | O(1) | O(n) |
| append fim | O(1) amort. | O(n) sem cauda; O(1) com cauda |
| insert início | O(n) | O(1) |
| insert meio | O(n) | O(1) se já tem o nó; O(n) para achar |
| busca valor | O(n) | O(n) |

Regra: **use `list`**. Use linked list quando o problema *é* a estrutura (algoritmos), não quando quer “uma lista”.

---

## 11. Dict, set e outras coleções

### 11.1 `dict` — mapa hash (ordenado por inserção, 3.7+)

```python
d = {"a": 1, "b": 2}
d = dict(a=1, b=2)
d["a"]
d.get("z", 0)               # default se faltar
d.setdefault("c", 3)
d.keys(); d.values(); d.items()

for k, v in d.items():
    ...

# merge
{**d1, **d2}
d1 | d2                     # 3.9+
d1 |= d2
```

Chaves: imutáveis hashable (`str`, `int`, `tuple` de imutáveis).  
Lookup médio O(1).

```python
from collections import defaultdict, Counter, ChainMap, OrderedDict

n = defaultdict(int)        # n[k] cria 0 se faltar
c = Counter("banana")       # {'a': 3, 'n': 2, 'b': 1}
```

### 11.2 `set`

Coleção sem duplicata, não indexável.

```python
s = {1, 2, 3}
s.add(4)
s.discard(9)                # não explode
{1, 2} & {2, 3}
```

`{}` é dict vazio, **não** set. Set vazio: `set()`.

### 11.3 Quando usar o quê

| Precisa | Estrutura |
|---|---|
| Sequência, índice, ordem, duplicatas | `list` |
| Sequência imutável / chave | `tuple` |
| Lookup por nome | `dict` |
| Pertinência, união, duplicata off | `set` |
| Fila/pilha nas pontas | `deque` |
| Heap (prioridade) | `heapq` (lista + funções) |
| Números compactos / matriz | `numpy` |
| Encadeamento de nós | sua `LinkedList` |

---

## 12. Funções

```python
def f(a, b=10, *args, flag=False, **kwargs):
    """Docstring: primeira linha do corpo."""
    return a + b

f(1, 2)
f(1, flag=True)
```

### 12.1 First-class e closures

```python
def externo(x):
    def interno(y):
        return x + y      # x “capturado”
    return interno

soma2 = externo(2)
soma2(5)                  # 7
```

### 12.2 `lambda`

Uma expressão, sem statements.

```python
chave = lambda p: p["idade"]
xs.sort(key=chave)
```

Prefira `def` se o corpo crescer.

### 12.3 Escopo: LEGB

Lookup de nome: **L**ocal → **E**nclosing → **G**lobal → **B**uiltins.

```python
x = 1

def f():
    global x
    x = 2

def externo():
    y = 1
    def interno():
        nonlocal y
        y += 1
```

Sem `global`/`nonlocal`, atribuição cria variável **local**.

### 12.4 Recursão

Há limite (`sys.getrecursionlimit()`, ~1000). Python não garante TCO (tail call). Recursão profunda → loop ou heap explícita.

---

## 13. Orientação a objetos

```python
class Animal:
    especie = "genérico"          # atributo de classe

    def __init__(self, nome):
        self.nome = nome          # atributo de instância

    def falar(self):
        raise NotImplementedError

    def __repr__(self):
        return f"Animal({self.nome!r})"


class Cachorro(Animal):
    def falar(self):
        return "au"


c = Cachorro("Bob")
c.falar()
Cachorro.falar(c)                 # o que o . faz por baixo
```

### 13.1 `self`

Não é keyword. É o primeiro parâmetro da instância, passado automaticamente na chamada `obj.metodo()`. Convenção universal: `self`. Em classmethod: `cls`.

### 13.2 `@property`, `classmethod`, `staticmethod`

```python
class C:
    def __init__(self, n):
        self._n = n

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, valor):
        self._n = valor

    @classmethod
    def from_str(cls, s):
        return cls(int(s))

    @staticmethod
    def util(x):
        return x + 1
```

### 13.3 Herança múltipla e MRO

```python
class C(A, B):
    pass

C.__mro__     # Method Resolution Order (C3)
super()       # próximo na MRO, não “a superclasse”
```

### 13.4 Dataclasses, slots, protocols

```python
from dataclasses import dataclass, field
from typing import Protocol

@dataclass(slots=True)
class Item:
    nome: str
    tags: list[str] = field(default_factory=list)

class Desenhavel(Protocol):
    def desenhar(self) -> None: ...
```

`Protocol` = duck typing com checagem estática (structural typing).

---

## 14. Iteradores, geradores e `next`

Este é o motor dos `for`. Entender isto = entender metade do Python avançado.

### 14.1 Iterável vs iterator

- **Iterável:** tem `__iter__` (lista, str, dict, arquivo, `range`). Pode produzir iterators.
- **Iterator:** tem `__iter__` (retorna self) e `__next__`. Consome-se: anda uma vez.

```python
xs = [10, 20]
it = iter(xs)           # xs.__iter__()
next(it)                # 10
next(it)                # 20
next(it)                # StopIteration → o for captura e encerra
```

`for x in xs:` é açúcar para:

```python
it = iter(xs)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    ...
```

### 14.2 Geradores (`yield`)

Função que pausa e devolve iterator.

```python
def contador(n):
    i = 0
    while i < n:
        yield i
        i += 1

g = contador(3)
next(g)                 # 0
list(contador(3))       # [0, 1, 2]
```

Generator expression (preguiçosa, parênteses):

```python
g = (x * x for x in range(10**9))   # não explode a RAM
```

`yield from subgerador` delega.

### 14.3 `send`, `throw`, `close` (avançado)

Gerador é uma coroutine primitiva: `g.send(valor)` injeta valor no `yield`. Hoje, para I/O, use `async def` / `await`.

### 14.4 itertools (kit avançado de loops)

```python
from itertools import count, cycle, islice, chain, groupby, product, permutations

count(10)                          # 10, 11, 12, ... infinito
islice(count(), 5)                 # 5 primeiros
chain(a, b)                        # concatena iteráveis
product("AB", repeat=2)            # AA AB BA BB
```

---

## 15. Comprehensions e unpacking

```python
[x * 2 for x in xs if x > 0]                    # list
{x * 2 for x in xs}                             # set
{k: v * 2 for k, v in d.items()}                # dict
(x * 2 for x in xs)                             # generator

# aninhada: equivalente a for externo depois interno
[c for linha in matriz for c in linha]

# unpacking
a, b = (1, 2)
a, *resto = [1, 2, 3, 4]
primeiro, *_, ultimo = seq

# unpacking em chamada
f(1, *args, **kwargs)

# unpacking em coleção (3.5+/3.9+)
[*xs, 99]
{**d, "k": 1}
```

Operador `*` no unpacking = “o resto vira lista”.

---

## 16. Exceções e context managers

```python
try:
    risco()
except ValueError as e:
    log(e)
except (TypeError, OSError):
    ...
else:
    # sem exceção
    ...
finally:
    # sempre
    ...

raise ValueError("msg")
raise                         # relança a atual
```

Hierarquia útil: `BaseException` → `Exception` → `ValueError`, `TypeError`, `KeyError`, `IndexError`, `StopIteration` (especial), `OSError`…

**Não** capture `Exception` genérico sem relançar, salvo borda do programa.

### 16.1 `with` — protocol `__enter__` / `__exit__`

```python
with open("a.txt", encoding="utf-8") as f:
    texto = f.read()
# arquivo fecha mesmo se der erro

from contextlib import contextmanager, suppress, ExitStack

with suppress(FileNotFoundError):
    os.remove("tmp")
```

```python
class Temp:
    def __enter__(self):
        return self
    def __exit__(self, exc_tipo, exc, tb):
        # return True engole a exceção
        return False
```

---

## 17. Decorators

Função (ou classe) que recebe uma função e devolve outra, aplicada com `@`.

```python
import functools
import time

def cronometro(fn):
    @functools.wraps(fn)          # preserva __name__, docstring
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            print(fn.__name__, time.perf_counter() - t0)
    return wrapper

@cronometro
def trabalho():
    ...

# decorator com parâmetro: factory
def repetir(n):
    def deco(fn):
        def wrapper(*a, **k):
            for _ in range(n):
                fn(*a, **k)
        return wrapper
    return deco

@repetir(3)
def oi():
    print("oi")
```

Built-ins: `@property` `@classmethod` `@staticmethod` `@functools.cache` `@functools.lru_cache` `@dataclasses.dataclass`.

---

## 18. Tipagem (type hints)

Hints **não** são checados em runtime pelo CPython (salvo `typing.cast` que também não checa). Ferramentas: `mypy`, `pyright`, `ty`.

```python
from typing import Callable, Sequence, TypeVar, Generic, Literal, Self

def busca(xs: Sequence[int], alvo: int) -> int | None:
    ...

T = TypeVar("T")

def primeiro(xs: list[T]) -> T:
    return xs[0]

Callback = Callable[[int, int], int]
```

Python 3.10+: `int | None` em vez de `Optional[int]`.  
3.12+: `def primeiro[T](xs: list[T]) -> T`.

---

## 19. Módulos, pacotes e o runtime

```python
import math
from math import sqrt as raiz
from . import irmao          # relativo, só dentro de pacote
from .sub import coisa

if __name__ == "__main__":
    # este arquivo foi executado, não importado
    main()
```

- Módulo: um `.py`.
- Pacote: pasta com `pyproject.toml` / (legado) `__init__.py`.
- `sys.path`: onde o import procura.
- Ambiente: use `venv` (`python -m venv .venv`). Nunca `sudo pip` no sistema.

```text
projeto/
  pyproject.toml
  src/pacote/
    __init__.py
    core.py
  tests/
```

---

## 20. Concorrência: threads, processos, async

| Problema | Ferramenta |
|---|---|
| I/O paralelo simples | `threading` / `concurrent.futures.ThreadPoolExecutor` |
| CPU-bound | `multiprocessing` / `ProcessPoolExecutor` |
| Muito I/O com uma thread | `asyncio` |
| Sem GIL (alternativa) | Jython não; hoje: subinterpreters (3.12+), free-threading experimental (3.13+) |

```python
import asyncio

async def busca(url):
    await asyncio.sleep(0.1)
    return url

async def main():
    urls = ["a", "b", "c"]
    return await asyncio.gather(*(busca(u) for u in urls))

asyncio.run(main())
```

`async def` devolve coroutine. Só roda se alguém `await` / `asyncio.run`. Não misture `time.sleep` dentro de async (bloqueia o loop); use `await asyncio.sleep`.

---

## 21. Dunder methods e metaprogramação

Dunder = *double underscore*. A linguagem chama; você implementa para plug-in no operador/sintaxe.

| Você escreve | Python chama |
|---|---|
| `len(x)` | `x.__len__()` |
| `x[i]` | `x.__getitem__(i)` |
| `x[i] = v` | `x.__setitem__(i, v)` |
| `x + y` | `x.__add__(y)` ou `y.__radd__(x)` |
| `x == y` | `x.__eq__(y)` |
| `str(x)` / `repr(x)` | `__str__` / `__repr__` |
| `for i in x` | `__iter__` |
| `next(x)` | `__next__` |
| `with x` | `__enter__` / `__exit__` |
| `x.attr` | `__getattribute__` / `__getattr__` |
| `Classe()` | `Classe.__call__` na metaclass; instância: `__new__` + `__init__` |
| `bool(x)` | `__bool__` ou `__len__` |

```python
class Vetor:
    def __init__(self, *coords):
        self._c = coords
    def __len__(self):
        return len(self._c)
    def __getitem__(self, i):
        return self._c[i]
    def __add__(self, outro):
        return Vetor(*(a + b for a, b in zip(self, outro, strict=True)))
    def __repr__(self):
        return f"Vetor{self._c}"
```

### 21.1 Descriptors e metaclass (extremo)

- **Descriptor:** objeto com `__get__`/`__set__` (`property` é um). ORM (`Model.campo`) usa isto.
- **Metaclass:** a classe da classe. `class A(metaclass=M)` — `type` é a default. Frameworks (Pydantic, ORM, ABC) usam; app de negócio quase nunca.

```python
class MinhaMeta(type):
    def __new__(mcs, nome, bases, ns):
        return super().__new__(mcs, nome, bases, ns)
```

---

## 22. Avançado extremo

Tópicos para quando o básico já está no músculo. Cada um é um capítulo de livro; aqui vai o *mapa*.

### 22.1 Modelo de memória e GC

- Contagem de referências + coletor cíclico.
- `del x` remove o *nome*, não necessariamente o objeto.
- `__del__` é frágil (não use para fechar recurso — use `with`).
- Internamento: pequenos `int` e algumas `str` podem ser o mesmo objeto (`is` engana).

### 22.2 GIL, bytecode, `dis`

```python
import dis
def f(x):
    return x + 1
dis.dis(f)
```

O interpretador executa bytecode (`.pyc` em `__pycache__`). O GIL protege o estado do interpretador.

### 22.3 Import system

`sys.meta_path`, finders, loaders, lazy import (`importlib.util.LazyLoader`). `from __future__ import annotations` adia avaliação de hints.

### 22.4 Data model extra

- Buffer protocol (`memoryview`, `__buffer__` em 3.12)
- Number protocol
- Weakref (`weakref.ref`, `WeakKeyDictionary`) — caches sem impedir GC
- `__slots__` — impede `__dict__`, economiza memória em milhões de instâncias

### 22.5 Concorrência avançada

- `queue.Queue` vs `asyncio.Queue`
- `contextvars` (contexto que atravessa await)
- subinterpreters (`concurrent.interpreters`, 3.14 rumo)
- free-threaded CPython (`PYTHON_GIL=0` em builds 3.13+)

### 22.6 C-API e aceleração

- `ctypes` / `cffi` — chamar C
- Cython, rust (PyO3), `mypyc`
- numpy, numba — vetorizar / JIT
- `multiprocessing.shared_memory`

### 22.7 Padrões pythônicos avançados

| Padrão | Onde |
|---|---|
| Strategy via função | `key=` em `sort` |
| Observer | callbacks, signals |
| Plugin | entry points (`importlib.metadata`) |
| Builder fluente | raramente; prefira kwargs |
| Monad-ish | geradores, `Optional` via `| None`, Result libs |
| DI | `fastapi.Depends`, simples kwargs |

### 22.8 Qualidade de produção

```text
venv + pyproject.toml (hatch/uv/poetry)
ruff          # lint + format
mypy/pyright  # tipos
pytest        # testes
pre-commit
logging (não print em lib)
```

Idiomas:

```python
# EAFP
# list comprehension para map/filter
# pathlib.Path em vez de os.path
# f-string em vez de % e .format, salvo templates
# enumerate, zip, unpacking
# context managers para recursos
# geradores para streams grandes
```

### 22.9 Armadilhas clássicas na migração

1. `list * n` com objetos mutáveis (matriz).
2. Default mutável em `def`.
3. `is` vs `==`.
4. `//` vs `/`.
5. Late binding em closure no `for`:

```python
funcoes = [lambda: i for i in range(3)]
funcoes[0]()    # 2  — todas veem o i final

funcoes = [lambda i=i: i for i in range(3)]
funcoes[0]()    # 0
```

6. Modificar lista enquanto itera (`for x in xs: xs.remove(x)`). Itere sobre `xs[:]` ou construa nova lista.
7. Escopo de `for`: em Python, `i` **vaza** para fora do loop (não é let de JS).
8. `==` de float. Use `math.isclose`.
9. Encoding: sempre `encoding="utf-8"` em `open`.
10. `from module import *`.

---

## 23. Cheat sheet: outra linguagem → Python

| Conceito | JS / Java / PHP / C# | Python |
|---|---|---|
| Bloco | `{ }` | indentação + `:` |
| E / OU / NÃO | `&& \|\| !` | `and or not` |
| Ternário | `?:` | `a if cond else b` |
| Null | `null` / `nil` | `None` |
| Bool | `true false` | `True False` |
| Const | `const` / `final` | convenção `NOME`; `Final` só no type checker |
| For C-style | `for(;;)` | `for i in range(n)` |
| Foreach | `for..of` / `foreach` | `for x in xs` |
| Função | `function` / `=>` | `def` / `lambda` |
| Classe | `this` | `self` |
| Interface | `interface` | `Protocol` / `ABC` |
| Array | `[]` mutável | `list` |
| Tuple | às vezes | `tuple` de verdade |
| Map | `Object` / `Map` / `array assoc` | `dict` |
| Set | `Set` | `set` |
| Spread | `...` | `*` e `**` |
| Nullish | `??` | `x if x is not None else y` ou `or` (cuidado com 0) |
| Optional chain | `?.` | `getattr(x, "a", None)` / `if x is not None` |
| Incremento | `++` | `x += 1` |
| String interp | `` `${x}` `` / `"$x"` | `f"{x}"` |
| Exception | `throw` / `catch` | `raise` / `except` |
| Finally | `finally` | `finally` + `with` |
| Import | `import` / `require` / `use` | `import` / `from` |
| Package | `namespace` | módulo = arquivo |
| Async | `async/await` | igual, com event loop `asyncio` |
| Types | estáticos ou JSDoc | hints opcionais |
| Switch | `switch` | `match` (3.10+) ou `if/elif` |
| Pointer | `*` `&` | não há; tudo referência a objeto |
| `::` | resolução (C++/PHP) | **slice** `[::]` |
| `.next()` | iterator JS | `next(it)` builtin |

---

## 24. Como estudar daqui

Ordem sugerida (você já programa: pule a lógica pura, foque no *idioma*):

1. **Símbolos** (seção 3) até não travar em `::`, `*`, `:=`, `and`.
2. **list / tuple / dict / set** + complexidade.
3. **for + iterador + range + next**.
4. **Funções** (args, closure, default mutável).
5. **OOP pythônico** (`__init__`, `__repr__`, `@property`) — sem copiar Java.
6. **Comprehensions e geradores.**
7. **with, exceções, pathlib.**
8. **Decorators e dataclasses.**
9. **Type hints + pytest.**
10. **asyncio** se for I/O; **numpy** se for dado; **[API.md](API.md)** se for backend HTTP.
11. **Dunders** até conseguir uma classe que se comporta como lista.
12. GIL, `dis`, descriptors — quando tiver curiosidade de runtime.

REPL diário:

```bash
python3
>>> import this
>>> help(str)
>>> dir(list)
```

Mini exercícios (lógica + Python):

- Inverter string sem `[::-1]` e depois *com* `[::-1]`.
- FizzBuzz com `match` e com comprehension.
- Frequência de palavras com `Counter`.
- Linked list: inverter in-place (ponteiros `a, b = b, a.proximo` mentalmente).
- Flatten de lista aninhada com gerador.
- Decorator `retry(n)`.
- Mini `Vector` com `__add__` e `__len__`.

Checklists por nível e mapa de tópicos: [ESTUDO.md](ESTUDO.md).

---

## 25. Notação Big O

Big O descreve **como o custo cresce** quando o tamanho da entrada \(n\) cresce (tempo ou memória). Ignora constantes: \(O(2n)\) e \(O(n)\) são a mesma classe.

| Classe | Exemplo típico |
| ------ | -------------- |
| \(O(1)\) | `d[chave]`, `deque.append` / `popleft` |
| \(O(\log n)\) | busca binária em sequência ordenada |
| \(O(n)\) | `for x in xs`, `sum(xs)`, `list.count` |
| \(O(n \log n)\) | `list.sort()` (Timsort) |
| \(O(n^2)\) | loop aninhado no mesmo \(n\) |
| \(O(n \cdot m)\) | `for x in a: if x in b` com `b` lista |

### Estruturas Python (referência rápida)

| Operação | `list` | `dict` / `set` |
| -------- | ------ | -------------- |
| `xs[i]` | \(O(1)\) | — |
| `append` / `pop()` fim | \(O(1)\)* | — |
| `insert(0, …)` / `pop(0)` | \(O(n)\) | — |
| `x in …` | \(O(n)\) | \(O(1)\)* médio |
| `sort()` | \(O(n \log n)\) | — |

\*Amortizado ou média em hash; ver §7.2 e §11.1.

### Armadilhas de complexidade

```python
# O(n²) — evite se n cresce
for x in muitos:
    if x in lista_grande:  # cada in é O(n)
        ...

# O(n + m) — melhor
conjunto = set(lista_grande)
for x in muitos:
    if x in conjunto:
        ...
```

Loops aninhados: [§6.5](#65-loops-e-complexidade-lógica). Linked list vs `list`: [§10.4](#104-complexidade-lembrete-de-lógica).

Capítulo expandido, checklists e exercícios: [ESTUDO.md § Big O](ESTUDO.md#notação-big-o). Demo: `python base.py bigo`.

---

## 26. Arquitetura do Python (CPython)

“Arquitetura” aqui é **como o interpretador executa seu código**, não arquitetura de microsserviços.

```text
arquivo .py
  → tokenize / parse → AST
  → compile → bytecode (.pyc em __pycache__)
  → CPython eval loop (bytecode + objetos C)
  → resultado / exceção
```

### Peças que afetam decisões de design

| Peça | O que é | Impacto |
| ---- | ------- | ------- |
| **Objeto único** | Tudo é `PyObject*` no CPython | Referências, `is` vs `==`, GC |
| **Bytecode** | Instruções da VM | `import dis; dis.dis(fn)` — [§22.2](#222-gil-bytecode-dis) |
| **GIL** | Lock global do interpretador | Threads: I/O ok; CPU-bound: multiprocessing / NumPy / C |
| **Import** | `sys.modules`, finders/loaders | Side effects em import; estrutura de pacotes — [§19](#19-módulos-pacotes-e-o-runtime) |
| **GC** | Refcount + ciclos | `del` remove nome; `__del__` frágil — [§22.1](#221-modelo-de-memória-e-gc) |

### Implementações alternativas (só para mapa mental)

| Implementação | Uso |
| ------------- | --- |
| **CPython** | Padrão; C + GIL (free-threading experimental em 3.13+) |
| **PyPy** | JIT; às vezes mais rápido em loops puros |
| **MicroPython** | Embarcados |
| **Jython / IronPython** | JVM / .NET (nicho) |

Para app comum: escreva para **CPython 3.11+** e use `venv` + `pyproject.toml`.

Trilha especialista (profiling, packaging, lacunas): [ESTUDO.md](ESTUDO.md).

---

## Referência rápida de uma linha

```text
#        comentário
:        abre bloco | chave de dict | slice | hint
.        atributo / método / submódulo
,        separa  +  cria tupla
;        dois statements (evite)
()       chamada, grupo, tupla, genexp
[]       lista, índice, slice, listcomp
{}       dict / set
=        atribui          == compara valor      is compara identidade
:=       walrus
->       hint de retorno (não executa)
::       slice [início:fim:passo]  ex: [::-1]
*        unpack / args / resto / kwargs é **
**       potência  OU  unpack de dict
@        decorator  OU  matmul
& | ^ ~  bitwise  (em set: ∩ ∪ Δ)
// %     div inteira, resto
**       potência          ^ é XOR, não potência
and or not     não existe && || !
in not in
lambda
...      Ellipsis
_        throwaway
f"" r"" b""
range(início, fim, passo)   fim exclusivo, lazy
next(it) / iter(xs)         .next() morreu no Py3
self     instância (convenção)
None True False
```

---

*Documento de estudo. Python muda (walrus, match, `int | None`, free-threading); a data model (`__iter__`, mutabilidade, names-as-labels) permanece.*
# estudoPY
