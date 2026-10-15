# Tipos de dados

> **Índice mestre da trilha (básico → especialista):** [ESTUDO.md](ESTUDO.md)  
> **Idioma, runtime e avançado:** [README.md](README.md) · **Exemplos executáveis:** [base.py](base.py)  
> **Big O + estruturas complexas (neste arquivo):** [Notação Big O](#notação-big-o-e-análise-de-complexidade) · [Estruturas avançadas](#estruturas-de-dados-complexas-referência-completa)

Tipos de dados definem **o que um valor é** e **o que você pode fazer com ele**.
Em Python, o tipo é descoberto automaticamente pelo valor (não precisa declarar `int`, `float`, etc.).

## INT (inteiro)

Número **inteiro**: sem parte decimal.

Exemplos: `1`, `2`, `3`, `-10`, `0`

```python
idade = 25
quantidade = 0
temperatura = -3
```

Use inteiro para contagem, idade, índices, quantidade de itens.

## FLOAT (número decimal)

Número **não inteiro**, com parte decimal.
Em Python (e na maioria das linguagens) usa-se **ponto**, não vírgula: `2.4445`, `2.90`.

Exemplos: `2.4445`, `2.90`, `3.14`, `-0.5`

```python
preco = 2.90
pi = 3.14
media = 7.5
```

Use float para dinheiro, medidas, médias, qualquer valor com casas decimais.

## STRING (texto)

Sequência de caracteres. Serve para **texto**, não para cálculo matemático.
Pode ser curta ou longa. Fica entre aspas: `"ABCD"` ou `'ABCD'`.

Exemplos: `"ABCD"`, `"olá"`, `"123"` (isso é texto, não número)

```python
nome = "Alisson"
frase = "Estudar Python"
codigo = "123"   # string, não dá para somar como número
```

`"123"` é texto. `123` é inteiro. São coisas diferentes.

## CHAR (caractere)

**Uma** letra ou símbolo: `"A"`, `"B"`, `"C"`.

Em algumas linguagens (C, Java) existe o tipo `char`.
**Em Python não existe `char` separado**: um caractere é uma string de tamanho 1.

```python
letra = "A"      # string com 1 caractere
print(len(letra))  # 1
```

## BOOLEAN (booleano)

Valor lógico: **verdadeiro** ou **falso**. Usado em validações e decisões.

Em Python: `True` e `False` (sem aspas, com letra maiúscula).
`"TRUE"` e `"FALSE"` com aspas seriam strings, não booleanos.

```python
ligado = True
maior_de_idade = False

if ligado:
    print("está ligado")
```

Use boolean para respostas do tipo sim/não, condições de `if` e `while`.

## BIT (bit)

A menor unidade de informação: **0** ou **1**.

Convenção usual:

- `0` = falso / desligado
- `1` = verdadeiro / ligado

(Não o contrário: 0 não é verdadeiro.)

Um bit sozinho guarda só duas possibilidades. Computadores agrupam bits para formar números, textos e o resto.

```python
bit = 0   # desligado
bit = 1   # ligado
```

## BYTES (byte / memória)

**Byte** é unidade de espaço na memória. 1 byte = **8 bits**.

Tamanhos comuns (potências de 2): `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, `256`...

Exemplos aproximados:

| Quantidade | Significado aproximado      |
| ---------- | --------------------------- |
| 1 byte     | 1 caractere simples (ASCII) |
| 1024 bytes | 1 KB                        |
| 1 MB       | cerca de 1 milhão de bytes  |

Em Python também existe o tipo `bytes`, que guarda uma sequência de bytes (dados brutos), diferente de string de texto.

```python
dados = b"ABC"   # tipo bytes
```

---

# Operadores aritméticos

Operadores aritméticos **calculam** valores numéricos.

| Operador | Nome           | O que faz                         | Exemplo        | Resultado |
| -------- | -------------- | --------------------------------- | -------------- | --------- |
| `+`      | soma           | soma valores                      | `5 + 3`        | `8`       |
| `-`      | subtração      | diminui valores                   | `5 - 3`        | `2`       |
| `*`      | multiplicação  | multiplica valores                | `5 * 3`        | `15`      |
| `/`      | divisão        | divide (resultado float)          | `5 / 2`        | `2.5`     |
| `//`     | divisão inteira| divide e descarta a parte decimal | `5 // 2`       | `2`       |
| `%`      | módulo         | **resto** da divisão              | `5 % 2`        | `1`       |
| `**`     | potência       | eleva a um expoente               | `2 ** 3`       | `8`       |

Observações importantes:

- Multiplicação é `*`, não `x`.
- `%` **não é divisão**. Divisão é `/`. `%` devolve o que sobrou: `10 % 3` vale `1`, porque 10 = 3×3 + 1.
- Operadores ficam **entre** os valores (operandos): em `5 + 3`, `5` e `3` são os operandos e `+` é o operador.

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

---

# Operadores lógicos (operandos lógicos)

Operadores lógicos combinam ou invertem valores **booleanos** (`True` / `False`).
Servem para montar condições: “isso **e** aquilo”, “isso **ou** aquilo”, “**não** isso”.

Os valores que entram na operação também são chamados de **operandos**.

## `and` (e)

Só é `True` se **os dois** lados forem verdadeiros.

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

```python
idade = 20
tem_ingresso = True

if idade >= 18 and tem_ingresso:
    print("pode entrar")
```

## `or` (ou)

É `True` se **pelo menos um** lado for verdadeiro.

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

```python
feriado = False
fim_de_semana = True

if feriado or fim_de_semana:
    print("não tem aula")
```

## `not` (não)

Inverte o valor: `True` vira `False`, e `False` vira `True`.

```python
ligado = False

if not ligado:
    print("está desligado")
```

---

# Operadores de comparação

Comparam dois valores e devolvem `True` ou `False`. São a base do `if` e do `while`.

| Operador | Nome              | Exemplo     | Resultado |
| -------- | ----------------- | ----------- | --------- |
| `==`     | igual a           | `5 == 5`    | `True`    |
| `!=`     | diferente de      | `5 != 3`    | `True`    |
| `>`      | maior que         | `5 > 3`     | `True`    |
| `<`      | menor que         | `5 < 3`     | `False`   |
| `>=`     | maior ou igual    | `5 >= 5`    | `True`    |
| `<=`     | menor ou igual    | `3 <= 5`    | `True`    |

`=` atribui valor. `==` compara se é igual. Não misture os dois.

```python
x = 10          # guarda 10 em x
print(x == 10)  # pergunta: x é igual a 10? True
```

---

# Operadores de atribuição

Guardam (ou atualizam) um valor em uma variável.

| Operador | Significado      | Equivale a     |
| -------- | ---------------- | -------------- |
| `=`      | recebe           | `x = 5`        |
| `+=`     | soma e guarda    | `x = x + 1`    |
| `-=`     | subtrai e guarda | `x = x - 1`    |
| `*=`     | multiplica       | `x = x * 2`    |
| `/=`     | divide           | `x = x / 2`    |
| `//=`    | divisão inteira  | `x = x // 2`   |
| `%=`     | resto e guarda   | `x = x % 2`    |
| `**=`    | potência         | `x = x ** 2`   |

```python
x = 10
x += 5   # agora x vale 15
x -= 3   # agora x vale 12
```

---

# Operadores de identidade e pertinência

| Operador   | O que faz                                      | Exemplo            |
| ---------- | ---------------------------------------------- | ------------------ |
| `is`       | `True` se for **o mesmo objeto** na memória    | `a is b`           |
| `is not`   | `True` se **não** for o mesmo objeto           | `a is not None`    |
| `in`       | `True` se o valor **está dentro** da sequência | `"a" in "casa"`    |
| `not in`   | `True` se o valor **não está** dentro          | `3 not in [1, 2]`  |

```python
lista = [1, 2, 3]
print(2 in lista)        # True
print(5 not in lista)    # True

x = None
print(x is None)         # True: x não tem valor
```

`==` compara **valor**. `is` compara **identidade** (se é o mesmo objeto).

---

# Estruturas de controle

Estruturas de controle decidem **o fluxo do programa**: repetir, parar, pular, escolher um caminho ou tratar erro.

## `if` / `elif` / `else` — decisão (se / senão se / senão)

Executa um bloco **somente se** a condição for verdadeira.

```python
a = 20
if a > 12:
    print("a é maior que 12")
```

Forma completa:

```python
if a > 12:
    print("maior")
elif a == 12:
    print("igual")
else:
    print("menor")
```

- `if`: se (primeira condição)
- `elif`: senão, se (outra condição; pode ter vários)
- `else`: senão (quando nenhuma condição anterior foi verdadeira)

### `if` aninhado (um if dentro de outro)

```python
idade = 20
tem_ingresso = True

if idade >= 18:
    if tem_ingresso:
        print("pode entrar")
    else:
        print("falta ingresso")
else:
    print("menor de idade")
```

### Operador ternário (if em uma linha)

Escolhe um valor conforme a condição.

```python
idade = 20
status = "adulto" if idade >= 18 else "menor"
```

Equivale a: se idade >= 18 então `"adulto"`, senão `"menor"`.

## `match` / `case` — escolha por valor (padrão)

Compara um valor com vários casos, parecido com `switch` de outras linguagens.
Existe a partir do Python 3.10.

```python
dia = 2

match dia:
    case 1:
        print("segunda")
    case 2:
        print("terça")
    case 3:
        print("quarta")
    case _:
        print("outro dia")
```

`case _` é o padrão padrão (qualquer coisa que não bateu nos casos anteriores), como o `else`.

Use `match` quando for comparar **o mesmo valor** com várias opções. Use `if`/`elif` quando as condições forem diferentes (`idade > 18`, `tem_ingresso`, etc.).

## `for` — repetição com quantidade conhecida

Percorre uma sequência. `range()` gera números.

```python
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4
```

Formas de `range`:

| Código            | Gera                    |
| ----------------- | ----------------------- |
| `range(5)`        | 0, 1, 2, 3, 4           |
| `range(1, 6)`     | 1, 2, 3, 4, 5           |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8           |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1           |

Percorrer lista, texto ou dicionário:

```python
for nome in ["Ana", "Bia", "Caio"]:
    print(nome)

for letra in "Python":
    print(letra)

for i, nome in enumerate(["Ana", "Bia"]):
    print(i, nome)   # 0 Ana / 1 Bia
```

Use `for` quando souber quantas vezes vai repetir, ou quando for percorrer uma coleção.

## `while` — repetição enquanto a condição for verdadeira

Repete **enquanto** a condição for `True`. A condição precisa poder virar `False`, senão vira loop infinito.

```python
x = 3
while x > 1:
    print(x)
    x = x - 1
```

Imprime `3` e `2`. Quando `x` vira `1`, `x > 1` é falso e o loop para.

```python
# loop infinito (só para com break ou Ctrl+C)
while True:
    texto = input("digite sair: ")
    if texto == "sair":
        break
```

Python **não tem `do-while`**. O equivalente é `while True` + `break` no fim, quando você quer executar **pelo menos uma vez**.

Use `while` quando não souber exatamente quantas voltas vai dar, só a condição de continuar.

## `else` em `for` e `while`

O `else` do loop roda **somente se o loop terminou normal** (não foi interrompido por `break`).

```python
for n in [2, 4, 6]:
    if n % 2 != 0:
        print("achou ímpar")
        break
else:
    print("todos são pares")
```

## Loops aninhados (um loop dentro de outro)

Útil para tabelas, matrizes, combinações.

```python
for linha in range(3):
    for coluna in range(3):
        print(linha, coluna)
```

## `break` — sai do loop agora

Interrompe o `for` ou `while` imediatamente.

```python
for i in range(10):
    if i == 3:
        break
    print(i)   # 0, 1, 2  (para no 3)
```

## `continue` — pula só esta volta

Não sai do loop: ignora o resto desta repetição e vai para a próxima.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)   # 0, 1, 3, 4  (pula o 2)
```

## `pass` — não faz nada (placeholder)

Útil quando a sintaxe exige um bloco, mas você ainda não vai escrever o código.

```python
if idade >= 18:
    pass   # depois eu implemento
```

## `try` / `except` / `else` / `finally` — tratamento de erro

Controla o fluxo quando algo **pode falhar** (dividir por zero, arquivo inexistente, digitação inválida).

```python
try:
    n = int("abc")        # pode dar erro
except ValueError:
    print("não é número")
else:
    print("conversão ok")  # só se NÃO deu erro
finally:
    print("sempre roda")   # com erro ou sem erro
```

- `try`: tenta executar
- `except`: o que fazer se der aquele erro
- `else`: se não deu erro
- `finally`: sempre executa (limpeza)

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("não pode dividir por zero")
```

## `with` — contexto (abre e fecha sozinho)

Garante que um recurso (arquivo, conexão) seja **fechado** no fim, mesmo se der erro.

```python
with open("arquivo.txt", "r") as f:
    texto = f.read()
# aqui o arquivo já foi fechado
```

## `return` — sai da função e devolve um valor

Não é um loop, mas controla o fluxo: **encerra a função** na hora.

```python
def dobro(n):
    return n * 2
    print("isso nunca roda")
```

---

# Estruturas de dados

Estruturas de dados organizam **vários valores** na memória e definem **como inserir, remover e buscar**.

Há dois grupos úteis de lembrar:

1. **Nativas do Python** — lista, tupla, set, dicionário (você usa o tempo todo)
2. **Clássicas da computação** — fila, pilha, lista ligada, árvore, grafo, heap (ideias de organização)

## Lista (`list`)

Sequência **ordenada** e **mutável** (pode alterar). Aceita tipos mistos. Índice começa em `0`.

```python
numeros = [10, 20, 30]
numeros.append(40)     # adiciona no fim
numeros[0] = 99        # altera a primeira posição
print(numeros[1])      # 20
print(len(numeros))    # quantidade de itens
```

Use lista para coleções que mudam: nomes, notas, itens de um carrinho.

## Tupla (`tuple`)

Parecida com lista, mas **imutável**: depois de criada, não altera.

```python
ponto = (10, 20)
# ponto[0] = 99  # erro: tupla não muda
x, y = ponto     # desempacota: x=10, y=20
```

Use tupla para pares fixos (coordenada, RGB, registro que não deve mudar).

## Conjunto (`set`)

Coleção **sem ordem** e **sem duplicata**. Ótimo para união, interseção e “já existe?”.

```python
a = {1, 2, 3, 3}
print(a)              # {1, 2, 3}  — o 3 repetido some
print(2 in a)         # True, busca rápida
print(a | {3, 4})     # união: {1, 2, 3, 4}
print(a & {2, 9})     # interseção: {2}
```

`frozenset` é um set que não pode ser alterado.

Use set para remover duplicatas e testar pertinência rápido.

## Dicionário (`dict`) — tabela hash

Pares **chave → valor**. Busca pela chave, não pela posição.

```python
pessoa = {"nome": "Ana", "idade": 20}
print(pessoa["nome"])      # Ana
pessoa["cidade"] = "SP"    # adiciona chave
print(pessoa.get("idade")) # 20
```

Por baixo, o dict é uma **tabela hash**: a chave vira um endereço, então a busca é muito rápida.

Use dict para cadastros, configurações, contagem (`{"a": 3, "b": 1}`), JSON.

## Array (arranjo)

Sequência de tamanho fixo, em geral **do mesmo tipo**, em posições contínuas na memória.
Acesso por índice é rápido: `arr[0]`, `arr[1]`.

Em Python o dia a dia usa `list`. Array “de verdade” aparece em `array.array` ou no NumPy.

```python
from array import array
arr = array("i", [1, 2, 3])  # i = inteiros
```

Use array quando precisar de muitos números do mesmo tipo com pouco uso de memória.

## Matriz (array 2D)

Tabela de linhas e colunas: lista de listas.

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
]
print(matriz[1][0])  # 4  (linha 1, coluna 0)
```

Use matriz para planilhas, imagens (pixels), tabuleiro de jogo.

## Lista ligada (linked list)

Cada elemento (nó) guarda o **valor** e um **ponteiro para o próximo**.
Não fica tudo junto na memória, então inserir/remover no meio é fácil; acesso por índice é mais lento (precisa caminhar do início).

```
[10] → [20] → [30] → None
```

- **simples**: cada nó aponta só para o próximo
- **dupla**: cada nó aponta para o próximo **e** para o anterior
- **circular**: o último aponta de volta para o primeiro

```python
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

inicio = No(10)
inicio.proximo = No(20)
inicio.proximo.proximo = No(30)
```

Use lista ligada quando inserções/remoções no meio forem frequentes.

## Fila (queue)

Como fila de banco: **o primeiro a entrar é o primeiro a sair** (FIFO — First In, First Out).

- Entra no **fim**
- Sai do **início**

Exemplo: senha 1, depois senha 2. Atende primeiro a senha 1.

```python
from collections import deque

fila = deque()
fila.append("pessoa 1")    # entra
fila.append("pessoa 2")
atendido = fila.popleft()  # sai o primeiro: "pessoa 1"
```

Use fila para atendimento, impressão, tarefas em ordem de chegada, BFS em grafos.

## Fila de duas pontas (`deque`)

Dá para entrar/sair **dos dois lados** (início e fim). Serve de fila **e** de pilha.

```python
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)  # entra no início
d.pop()          # sai do fim
```

## Fila de prioridade / Heap

Não atende por ordem de chegada: atende o **mais importante** (menor ou maior prioridade) primeiro.

Em Python, `heapq` é um **min-heap**: o menor valor sai primeiro.

```python
import heapq

tarefas = []
heapq.heappush(tarefas, (1, "urgente"))
heapq.heappush(tarefas, (3, "pode esperar"))
heapq.heappush(tarefas, (2, "normal"))
print(heapq.heappop(tarefas))  # (1, "urgente")
```

Use heap para filas de hospital, agendador de CPU, Dijkstra.

## Pilha (stack)

Como pilha de pratos: **o último a entrar é o primeiro a sair** (LIFO — Last In, First Out).

- Entra no **topo**
- Sai do **topo**

Exemplo: empilha A, depois B. O próximo a sair é B.

```python
pilha = []
pilha.append("A")   # empilha
pilha.append("B")
topo = pilha.pop()  # desempilha: "B"
```

Use pilha para desfazer (Ctrl+Z), histórico de navegação, avaliação de expressões, chamadas de função.

## Árvore (tree)

Hierarquia: um **raiz** no topo, cada nó pode ter vários filhos. Sem ciclos.

```
        pasta
       /     \
    docs     fotos
    / \
  a.md  b.md
```

Use árvore para pastas do computador, organograma, HTML/DOM, menus.

## Binary (árvore binária)

Árvore em que cada nó tem no máximo **dois filhos**: esquerda e direita.

```
        8
       / \
      3   10
     / \
    1   6
```

```python
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

raiz = No(8)
raiz.esquerda = No(3)
raiz.direita = No(10)
```

## Árvore binária de busca (BST)

Árvore binária com regra:

- valores **menores** à esquerda
- valores **maiores** à direita

Busca, inserção e remoção ficam mais rápidas em média (como um dicionário ordenado em árvore).

Use BST / árvore binária para busca eficiente, ordenação e hierarquias.

## Grafo (graph)

Conjunto de **vértices** (nós) ligados por **arestas**. Pode ter ciclos. Pode ser:

- **não direcionado**: A ligado a B (rua de mão dupla)
- **direcionado**: A → B (mão única)
- **ponderado**: a aresta tem peso (distância, custo)

```python
# lista de adjacência
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
}
```

```
A — B — D
|
C
```

Use grafo para redes sociais, mapas, rotas, dependências entre tarefas.

## Hash table (tabela hash)

A chave passa por uma função hash e vira um índice. Acesso quase instantâneo.
Em Python, `dict` e `set` usam hash table.

Use quando a operação principal for “pegar o valor desta chave” ou “este item já existe?”.

---

# Notação Big O e análise de complexidade

**Big O** (leia-se “O de…”) é a forma mais usada de descrever **como o trabalho de um algoritmo cresce** quando o tamanho da entrada cresce. Você usa Big O para comparar ideias (“isso escala?”) sem depender de um computador específico.

Não mede segundos no relógio. Mede **ordem de crescimento**: se \(n\) (tamanho da entrada) dobra, o tempo **dispara linearmente, quadraticamente, logaritmicamente**…?

**Mais detalhe no mesmo repositório:** [README.md §25](README.md#25-notação-big-o) · [ESTUDO.md § Big O](ESTUDO.md#notação-big-o) · demo: `python base.py bigo`

---

## O que Big O realmente significa

Imagine que você processa uma lista com \(n\) itens.

| Pergunta | Resposta com Big O |
| -------- | ------------------ |
| Se \(n\) passar de 1 000 para 10 000, o tempo fica ~10× maior? | Provavelmente **\(O(n)\)** — linear |
| Fica ~100× maior? | Provavelmente **\(O(n^2)\)** — quadrático |
| Quase não muda? | **\(O(1)\)** ou **\(O(\log n)\)** |

**Regras que simplificam a notação:**

1. **Ignora constantes:** \(O(2n)\) e \(O(5n)\) viram **\(O(n)\)**.
2. **Ignora termos menores:** \(O(n^2 + n)\) viram **\(O(n^2)\)** — o \(n^2\) domina quando \(n\) é grande.
3. Fala do **comportamento quando \(n\) tende ao infinito** (análise assintótica).

```python
# Mesma classe O(n) — constante diferente não muda a "letra"
def soma_a(xs):
    total = 0
    for x in xs:
        total += x
    return total

def soma_b(xs):
    total = 0
    for x in xs:
        total += x
        total += 0  # trabalho extra fixo por item
    return total
```

---

## O que Big O **não** é

| Mito | Realidade |
| ---- | --------- |
| “Big O = tempo em segundos” | É **crescimento**; hardware, cache e linguagem mudam o fator constante |
| “Sempre é o pior caso” | Na prática você cita **qual caso** (pior, médio, melhor) |
| “Só importa tempo” | Existe **complexidade de espaço** (memória extra) |
| “\(O(n)\) sempre é rápido” | Para \(n = 10^9\), linear ainda pode ser inviável |

---

## Entrada \(n\) — o que conta como tamanho?

Depende do problema. Exemplos:

| Problema | \(n\) costuma ser |
| -------- | ----------------- |
| Percorrer uma lista | `len(lista)` |
| Ordenar um array | número de elementos |
| Busca em string | tamanho da string |
| Grafo | \(V\) vértices e \(E\) arestas (use **\(O(V + E)\)** em BFS/DFS) |
| Dois arrays aninhados | às vezes **\(n\)** e **\(m\)** separados → **\(O(n \cdot m)\)** |

---

## Todas as classes Big O que você precisa conhecer

Da mais barata (em escala) à mais cara:

| Classe | Nome | \(n = 1000\) → \(n = 2000\) (intuição) | Exemplo típico |
| ------ | ---- | ---------------------------------------- | -------------- |
| **\(O(1)\)** | constante | trabalho ~igual | `dict[chave]`, índice `lista[i]` |
| **\(O(\log n)\)** | logarítmica | dobra \(n\), +1 “etapa” lógica | busca binária |
| **\(O(\sqrt{n})\)** | raiz | cresce devagar | alguns problemas de fatores |
| **\(O(n)\)** | linear | dobra \(n\), ~dobra tempo | um `for` na lista |
| **\(O(n \log n)\)** | linearítmica | um pouco pior que linear | `list.sort()` (Timsort) |
| **\(O(n^2)\)** | quadrática | dobra \(n\), ~4× tempo | dois loops no mesmo \(n\) |
| **\(O(n^3)\)** | cúbica | matriz \(n \times n\) com triplo loop | multiplicação ingênua de matrizes |
| **\(O(2^n)\)** | exponencial | +1 item pode **dobrar** o trabalho | subconjuntos ingênuos |
| **\(O(n!)\)** | fatorial | explode imediatamente | permutações ingênuas |

### Gráfico mental (qual domina na prática?)

```text
n pequeno     → constantes importam; qualquer código “parece rápido”
n médio       → O(n log n) vs O(n²) já dá diferença visível
n grande      → só O(n), O(log n), O(n log n) costumam ser aceitáveis
```

### Tabela numérica (só para sentir a explosão)

Valores **relativos** de operações (não são segundos):

| \(n\) | \(\log_2 n\) | \(n\) | \(n \log n\) | \(n^2\) | \(2^n\) |
| ----- | ------------ | ----- | ------------ | ------- | ------- |
| 10 | ~3 | 10 | ~33 | 100 | 1024 |
| 100 | ~7 | 100 | ~664 | 10 000 | astronômico |
| 1000 | ~10 | 1000 | ~9966 | 1 000 000 | inviável |

---

## Outras notações: O, Ω, Θ, o, ω

| Notação | Significado informal |
| ------- | -------------------- |
| **\(O(g)\)** | “No **máximo** cresce como \(g\)” (limite superior — o que você mais usa) |
| **\(\Omega(g)\)** | “No **mínimo** cresce como \(g\)” (limite inferior) |
| **\(\Theta(g)\)** | “Cresce **exatamente** na mesma ordem que \(g\)” (apertado: O e Ω) |
| **\(o(g)\)** | cresce **estritamente** mais devagar que \(g\) |
| **\(\omega(g)\)** | cresce **estritamente** mais rápido que \(g\) |

No dia a dia, quando alguém diz “é log n”, em geral está falando de **\(O(\log n)\)** no pior ou caso médio.

---

## Melhor, médio e pior caso

| Caso | Exemplo: busca linear em lista não ordenada |
| ---- | --------------------------------------------- |
| **Melhor** | achou no primeiro → **\(O(1)\)** |
| **Médio** | achou no meio → **\(O(n)\)** |
| **Pior** | não achou / último → **\(O(n)\)** |

| Caso | Exemplo: busca binária em lista **ordenada** |
| ---- | --------------------------------------------- |
| Pior / médio / melhor | **\(O(\log n)\)** — divide pela metade |

| Caso | `dict` / `set` (hash) |
| ---- | --------------------- |
| Médio | **\(O(1)\)** |
| Pior (muitas colisões) | **\(O(n)\)** — raro com hash bom |

Sempre diga: “inserção na BST é **\(O(h)\)** onde \(h\) é a altura” — em árvore balanceada \(h = O(\log n)\); em árvore degenerada \(h = O(n)\).

---

## Complexidade de espaço (memória)

Além do **tempo**, conte memória **extra** alocada pelo algoritmo (não conte a entrada inteira se o problema já recebe \(n\) elementos — convenção varia; em estudo, deixe claro).

| Código | Tempo | Espaço extra |
| ------ | ----- | ------------ |
| `sum(xs)` | \(O(n)\) | \(O(1)\) |
| `sorted(xs)` | \(O(n \log n)\) | \(O(n)\) cópia |
| BFS em grafo | \(O(V + E)\) | \(O(V)\) fila + visitados |
| Merge sort | \(O(n \log n)\) | \(O(n)\) |
| Busca binária iterativa | \(O(\log n)\) | \(O(1)\) |
| Busca binária recursiva | \(O(\log n)\) | \(O(\log n)\) pilha de chamadas |

---

## Amortizado (análise “no longo prazo”)

Algumas operações são caras **às vezes**, mas baratas na média de muitas operações.

| Estrutura | Operação | Complexidade |
| --------- | -------- | ------------ |
| `list` | `append` no fim | **\(O(1)\)** *amortizado* (às vezes realoca e copia tudo — \(O(n)\) — mas raro espalhado) |
| `dict` | `resize` quando enche | ocasional \(O(n)\), inserções **amortizadas** \(O(1)\) médio |

---

## Como analisar código Python (receita)

1. Encontre o que é **\(n\)** (ou \(n\) e \(m\)).
2. Conte **loops** e **aninhamento**.
3. Veja se o problema **divide pela metade** → \(\log n\).
4. Veja chamadas a métodos com custo conhecido (`sort`, `in lista`, `in set`).

### Regras rápidas

| Padrão | Complexidade típica |
| ------ | ------------------- |
| Um loop em `range(n)` | \(O(n)\) |
| Dois loops aninhados em `n` | \(O(n^2)\) |
| Loop `i = n; i //= 2` | \(O(\log n)\) |
| `for x in a: for y in b` | \(O(\|a\| \cdot \|b\|)\) |
| `for x in a: if x in b` com `b` lista | \(O(n \cdot m)\) |
| `for x in a: if x in b` com `b` set | \(O(n + m)\) |
| Recursão que divide em 2 partes iguais | \(O(n \log n)\) se processa tudo em cada nível (merge sort) |
| Recursão Fibonacci ingênua | \(O(2^n)\) |

### Exemplos comentados

```python
# O(n)
def maximo(xs):
    m = xs[0]
    for x in xs:
        if x > m:
            m = x
    return m

# O(n²)
def pares_que_somam_zero(xs):
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] + xs[j] == 0:
                return (i, j)

# O(n) tempo, O(n) espaço — set de vistos
def tem_duplicata(xs):
    vistos = set()
    for x in xs:
        if x in vistos:   # O(1) médio
            return True
        vistos.add(x)
    return False

# O(log n) — lista ORDENADA
def busca_binaria(xs, alvo):
    lo, hi = 0, len(xs) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if xs[mid] == alvo:
            return mid
        if xs[mid] < alvo:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

---

## Python: tabela de complexidade das estruturas nativas

### `list`

| Operação | Complexidade | Nota |
| -------- | ------------ | ---- |
| `xs[i]`, `xs[-1]` | \(O(1)\) | vetor de ponteiros |
| `append` / `pop()` fim | \(O(1)\) amortizado | |
| `insert(0, x)`, `pop(0)` | \(O(n)\) | desloca elementos |
| `x in xs` | \(O(n)\) | compara um a um |
| `sort()` | \(O(n \log n)\) | Timsort |
| `count`, `index` | \(O(n)\) | |

### `dict` e `set` (hash)

| Operação | Médio | Pior |
| -------- | ----- | ---- |
| `get`, `in`, `insert`, `delete` | \(O(1)\) | \(O(n)\) |
| Iterar todos | \(O(n)\) | |

Chaves devem ser **hashable** (imutáveis: `int`, `str`, `tuple` de imutáveis…).

### `collections.deque`

| Operação | Complexidade |
| -------- | ------------ |
| `append`, `appendleft`, `pop`, `popleft` | \(O(1)\) |
| `x in deque` | \(O(n)\) |

### `heapq` (min-heap em lista)

| Operação | Complexidade |
| -------- | ------------ |
| `heappush`, `heappop` | \(O(\log n)\) |
| `heapify` | \(O(n)\) |

---

## Armadilhas clássicas (memorize)

```python
# ARMADILHA: O(n²)
for usuario in usuarios:
    if usuario.id in lista_de_ids:  # lista → cada in é O(n)
        ...

# MELHOR: O(n) — constrói set uma vez O(m)
ids = set(lista_de_ids)
for usuario in usuarios:
    if usuario.id in ids:
        ...

# ARMADILHA: list.pop(0) em fila — O(n) por chamada
# USE: collections.deque com popleft() — O(1)

# ARMADILHA: concatenar string em loop
s = ""
for x in muitos:
    s += x          # O(n²) no total — strings são imutáveis
# MELHOR:
s = "".join(muitos)  # O(n)
```

---

# Estruturas de dados complexas (referência completa)

Acima você viu **estruturas básicas** (lista, dict, pilha, fila, árvore, grafo). Aqui entram as **estruturas complexas**: mais regras internas, mais operações, e custos que mudam conforme o **equilíbrio** da estrutura (árvore balanceada vs “viciada”).

**Objetivo:** saber **o que é**, **para que serve** e **qual Big O** das operações que você mais usa.

---

## Mapa: simples → complexa

```text
Simples (uma ideia)          Complexa (várias invariantes)
─────────────────────        ───────────────────────────────
array / list                 árvore AVL, rubro-negra
pilha / fila                 heap binário, fila de prioridade
hash table (dict)            tabela hash perfeita / cuckoo (teoria)
lista ligada                 skip list
grafo (lista de adj.)        grafo com índices + Dijkstra + heap
BST simples                  B-tree (disco/DB), trie
```

---

## Tabela mestre — estrutura × operações × Big O

Legenda: **M** = médio, **P** = pior, \(n\) = tamanho, \(h\) = altura da árvore, \(V/E\) = vértices/arestas.

| Estrutura | Busca | Inserir | Remover | Observação |
| --------- | ----- | ------- | ------- | ---------- |
| **Array / `list` (índice)** | \(O(1)\) por índice | fim \(O(1)\)*, início \(O(n)\) | fim \(O(1)\), início \(O(n)\) | *amortizado |
| **Lista ligada** | \(O(n)\) | \(O(1)\) se já tem o nó | \(O(1)\) com ponteiro | índice \(O(n)\) |
| **Hash (`dict`/`set`)** | \(O(1)\) M, \(O(n)\) P | \(O(1)\) M | \(O(1)\) M | ordem não garantida |
| **BST não balanceada** | \(O(h)\) | \(O(h)\) | \(O(h)\) | \(h\) pode ser \(n\) |
| **BST balanceada (AVL, RB)** | \(O(\log n)\) | \(O(\log n)\) | \(O(\log n)\) | usada em `map` de C++ |
| **Heap (min/max)** | min/max \(O(1)\) | \(O(\log n)\) | \(O(\log n)\) | não busca arbitrária rápida |
| **Trie** | \(O(L)\) | \(O(L)\) | \(O(L)\) | \(L\) = tamanho da chave/string |
| **Union-Find** | \(O(\alpha(n))\)* | \(O(\alpha(n))\)* | — | *quase constante |
| **Grafo lista adj.** | — | aresta \(O(1)\) | — | espaço \(O(V + E)\) |
| **Grafo matriz adj.** | aresta \(O(1)\) | \(O(1)\) | \(O(1)\) | espaço \(O(V^2)\) |

---

## Pilha, fila, deque (com complexidade)

| Estrutura | Regra | Implementação Python | Operações principais |
| --------- | ----- | -------------------- | -------------------- |
| **Pilha (LIFO)** | último entra, primeiro sai | `list` com `append`/`pop` | push/pop **\(O(1)\)** |
| **Fila (FIFO)** | primeiro entra, primeiro sai | `deque` | enqueue/dequeue **\(O(1)\)** |
| **Deque** | duas pontas | `collections.deque` | quatro lados **\(O(1)\)** |

**Por que importa:** BFS usa **fila** \(O(1)\) por nível; DFS usa **pilha** (ou recursão — cuidado com profundidade e espaço \(O(h)\)).

---

## Lista ligada — variantes e custos

| Variante | Próximo | Anterior | Uso |
| -------- | ------- | -------- | --- |
| Simples | sim | não | fila encadeada mínima |
| Dupla | sim | sim | LRU, editores |
| Circular | fecha o ciclo | — | round-robin, buffers |

| Operação | Lista ligada | `list` Python |
| -------- | ------------ | ------------- |
| Acesso `k`-ésimo | \(O(k)\) | \(O(1)\) |
| Inserir após nó conhecido | \(O(1)\) | \(O(n)\) deslocando |
| Inserir no índice `i` sem nó | \(O(i)\) para chegar | \(O(n)\) |

`collections.deque` é lista duplamente ligada **nas pontas** — não substitui lista ligada no meio com ponteiros expostos.

---

## Tabela hash — por dentro (conceito)

1. Função **hash(chave)** → índice em um vetor.
2. **Colisão:** duas chaves no mesmo índice → lista encadeada ou open addressing.
3. **Load factor:** quando enche demais, **redimensiona** (custo ocasional \(O(n)\), inserções amortizadas \(O(1)\)).

Por isso `dict` é rápido, mas **não ordenado** (até 3.7+ ordem de inserção é efeito de implementação, não use como garantia de algoritmo).

---

## Heap (fila de prioridade)

Árvore binária completa “embutida” em array/lista; pai sempre menor (min-heap) ou maior (max-heap).

| Operação | `heapq` |
| -------- | ------- |
| Ver mínimo | `heap[0]` — \(O(1)\) |
| Inserir | `heappush` — \(O(\log n)\) |
| Remover mínimo | `heappop` — \(O(\log n)\) |

**Não serve para:** “ache o 5º maior” ou busca por valor arbitrário em \(O(1)\) — use BST ou ordenação.

**Serve para:** Dijkstra, agendador, mediana em stream (com dois heaps), `n` maiores elementos.

---

## Árvores binárias de busca (BST) e balanceamento

### BST (regra)

- Esquerda < raiz < direita (para ordem crescente).
- Inserir/buscar: caminha da raiz comparando — **\(O(h)\)**.

Se inserir `1,2,3,4,5` em ordem, a árvore vira uma “lista” → **\(h = n\)** → **\(O(n)\)** por operação.

### Árvores balanceadas (complexas)

Mantêm **altura \(O(\log n)\)** com rotações ou regras de cor:

| Tipo | Ideia | Onde aparece |
| ---- | ----- | ------------ |
| **AVL** | balanceamento estrito | teoria, algumas libs |
| **Rubro-negra** | regras de cor em nós | `std::map` C++, Java `TreeMap` |
| **B-tree / B+tree** | nós com muitas chaves | **bancos de dados**, disco |

Em Python puro você raramente implementa RB; usa `dict` (hash) ou `bisect` em lista ordenada (\(O(\log n)\) busca, \(O(n)\) inserir).

### Percursos em árvore (tempo \(O(n)\) — visita cada nó uma vez)

| Ordem | Nome | Uso |
| ----- | ---- | --- |
| Esq, raiz, dir | **in-order** | BST → lista ordenada |
| Raiz, esq, dir | **pre-order** | copiar árvore |
| Esq, dir, raiz | **post-order** | apagar árvore |

---

## Trie (árvore de prefixos)

Cada nível representa um caractere; caminho da raiz à folha forma uma string.

```text
        (raiz)
       /  |  \
      c   p   t
      |   |   |
      a   y   o
      |       |
      t       p
      |       |
      e       (fim "top")
    (fim "cat")
```

| Operação | Complexidade |
| -------- | ------------ |
| Buscar prefixo / palavra | \(O(L)\) |
| Inserir palavra | \(O(L)\) |

**Use para:** autocomplete, dicionário de strings, IP routing (bits).

**Python:** não há na stdlib; implemente nós `dict` de filhos ou use libs.

---

## Union-Find (Disjoint Set)

Conjuntos disjuntos com **unir** e **perguntar se mesmo conjunto** — quase \(O(1)\) amortizado com path compression + rank.

**Use para:** Kruskal (árvore geradora mínima), componentes conectados, detecção de ciclo em grafos undirected.

```python
# Esboço educativo (sem otimizações completas)
class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n))

    def find(self, x):
        while self.pai[x] != x:
            x = self.pai[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.pai[rb] = ra
```

Com **path compression**, `find`/`union` ficam **\(O(\alpha(n))\)** — cresce tão devagar que é tratado como constante na prática.

---

## Grafos — representação e algoritmos

### Como guardar

| Forma | Espaço | Testar aresta A—B | Listar vizinhos de A |
| ----- | ------ | ------------------- | -------------------- |
| **Lista de adjacência** | \(O(V + E)\) | \(O(\deg(A))\) | \(O(\deg(A))\) |
| **Matriz de adjacência** | \(O(V^2)\) | \(O(1)\) | \(O(V)\) |

```python
# Lista de adjacência — comum em Python
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
}
```

### Algoritmos essenciais

| Algoritmo | Complexidade | Para quê |
| --------- | ------------ | -------- |
| **BFS** | \(O(V + E)\) | menor caminho em arestas **não ponderadas** |
| **DFS** | \(O(V + E)\) | ciclo, componentes, topological sort |
| **Dijkstra** | \(O((V + E) \log V)\) com heap | menor caminho com pesos **≥ 0** |
| **Bellman-Ford** | \(O(V \cdot E)\) | pesos negativos (com cuidado) |
| **Floyd-Warshall** | \(O(V^3)\) | todos os pares (grafo pequeno) |
| **Kruskal / Prim** | \(O(E \log E)\) aprox. | árvore geradora mínima |

```python
from collections import deque

def bfs(grafo, inicio):
    visitado = {inicio}
    fila = deque([inicio])
    ordem = []
    while fila:
        u = fila.popleft()
        ordem.append(u)
        for v in grafo.get(u, []):
            if v not in visitado:
                visitado.add(v)
                fila.append(v)
    return ordem
```

---

## Skip list (lista com “atalhos”)

Lista ordenada com múltiplos níveis de ponteiros — busca **\(O(\log n)\)** médio, implementação mais simples que rubro-negra em alguns cenários. Usada em alguns bancos chave-valor (ex.: Redis ordenado — conceito relacionado).

---

## Árvore de segmentos / Fenwick (BIT) — intro

Estruturas para **consultas e atualizações em intervalo** em um array:

| Problema | Solução ingênua | Estrutura |
| -------- | --------------- | --------- |
| Soma em intervalo `[l, r]` | \(O(n)\) por query | Segment tree / Fenwick **\(O(\log n)\)** query e update |

Estude depois de dominar árvores e recursão — comum em competição e em sistemas de agregação.

---

## Bloom filter

Estrutura probabilística: “**definitivamente não está**” ou “**talvez esteja**”. Espaço pequeno, **sem remoção** fácil na versão básica.

**Use para:** cache de consultas caras, spam filter, CDNs.

---

## LRU cache (Least Recently Used)

Remove o item **menos usado recentemente** quando a capacidade estoura. Implementação clássica: **hash + lista dupla** — get/put **\(O(1)\)**.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

`functools.lru_cache` transforma recursão exponencial em **\(O(n)\)** tempo e espaço para Fibonacci — memoização.

---

## Quando usar qual estrutura? (guia de decisão)

| Preciso de… | Escolha |
| ----------- | ------- |
| Acesso por índice rápido | `list` / array |
| Busca por chave rápida, sem ordem | `dict` / `set` |
| Ordem de chegada | `deque` (fila) |
| Próximo item mais urgente | `heapq` |
| Menor caminho em mapa com pesos | grafo + **Dijkstra** + heap |
| Strings por prefixo | **trie** |
| Conjuntos que se fundem | **union-find** |
| Ordenado + busca log | BST balanceada / `bisect` em lista |
| Muitas consultas em intervalo em array estático | prefix sum \(O(1)\) query; dinâmico → segment tree |

---

## Algoritmos clássicos e sua complexidade

| Algoritmo | Tempo | Espaço | Nota |
| --------- | ----- | ------ | ---- |
| Busca linear | \(O(n)\) | \(O(1)\) | lista não ordenada |
| Busca binária | \(O(\log n)\) | \(O(1)\) | precisa ordenado |
| Bubble / insertion sort | \(O(n^2)\) | \(O(1)\) | só didático |
| Merge sort | \(O(n \log n)\) | \(O(n)\) | estável |
| Quick sort | \(O(n \log n)\) médio, \(O(n^2)\) pior | \(O(\log n)\) pilha | `list.sort` usa Timsort |
| Contagem com `Counter` | \(O(n)\) | \(O(k)\) chaves distintas | |

---

## Checklist de estudo — Big O e estruturas

### Big O

- [ ] Explicar com suas palavras o que é \(O(n)\) e por que ignoramos constantes
- [ ] Dizer diferença entre pior, médio e melhor caso
- [ ] Classificar: loop simples, loop aninhado, dividir por 2, `in` em list vs set
- [ ] Ler tabela `list` vs `dict` de memória
- [ ] Implementar busca binária e citar \(O(\log n)\)

### Estruturas

- [ ] Implementar pilha e fila com `list` / `deque`
- [ ] Desenhar BST e caso degenerado (lista)
- [ ] Implementar BFS em grafo com `deque`
- [ ] Explicar quando heap vence BST
- [ ] Explicar colisão em hash table
- [ ] (Extra) union-find com path compression
- [ ] (Extra) trie com `dict` de filhos

### Prática

- [ ] `python base.py bigo`
- [ ] Medir `in list` vs `in set` com `timeit` para \(n = 10^4\) ([ESTUDO.md exercícios](ESTUDO.md#exercícios-dos-readmes--extras))

---

# Resumo rápido

| Tema                         | O que é                                              |
| ---------------------------- | ---------------------------------------------------- |
| `int`                        | número inteiro                                       |
| `float`                      | número com decimal                                   |
| `string`                     | texto                                                |
| `char`                       | um caractere (em Python: string de 1 letra)          |
| `boolean`                    | `True` ou `False`                                    |
| `bit`                        | 0 ou 1 (menor unidade de informação)                 |
| `byte`                       | 8 bits; unidade de memória                           |
| `+ - * / // % **`            | operadores aritméticos                               |
| `and or not`                 | operadores lógicos                                   |
| `== != > < >= <=`            | operadores de comparação                             |
| `= += -= *=`                 | operadores de atribuição                             |
| `is` / `in`                  | identidade / pertence a                              |
| `if` / `elif` / `else`       | decidir um caminho                                   |
| ternário                     | `a if cond else b`                                   |
| `match` / `case`             | escolher entre vários valores                        |
| `for`                        | repetir percorrendo uma sequência                    |
| `while`                      | repetir enquanto a condição for verdadeira           |
| `break`                      | sair do loop                                         |
| `continue`                   | pular esta volta do loop                             |
| `pass`                       | não fazer nada                                       |
| `try` / `except`             | tratar erro                                          |
| `with`                       | abrir recurso e fechar sozinho                       |
| `return`                     | sair da função e devolver valor                      |
| lista                        | sequência mutável e ordenada                         |
| tupla                        | sequência imutável                                   |
| set                          | sem duplicata, sem ordem                             |
| dict                         | chave → valor (tabela hash)                          |
| array                        | sequência homogênea, acesso por índice               |
| matriz                       | tabela (linhas e colunas)                            |
| lista ligada                 | nós ligados por ponteiros                            |
| fila                         | primeiro a entrar, primeiro a sair (FIFO)            |
| deque                        | fila de duas pontas                                  |
| heap / fila de prioridade    | sai o de maior prioridade                            |
| pilha                        | último a entrar, primeiro a sair (LIFO)              |
| árvore                       | hierarquia sem ciclo                                 |
| binary / BST                 | árvore com no máximo 2 filhos (busca à esquerda/dir) |
| grafo                        | nós ligados por arestas (pode ter ciclo)             |
| hash table                   | busca rápida por chave                               |
| Big O                        | ordem de crescimento de tempo/memória                |
| \(O(1)\) … \(O(n!)\)         | classes de complexidade (ver seção dedicada)         |
| trie                         | árvore de prefixos para strings                      |
| union-find                   | unir conjuntos, componentes em grafos                 |
| Dijkstra / BFS               | caminhos em grafos                                   |

---

# Operadores, delimitadores e símbolos sintáticos

O código Python é lido como uma sequência de **tokens**.
Além de nomes, números e textos, o interpretador reconhece:

- **operadores** — combinam ou transformam valores (`+`, `==`, `:=`…)
- **delimitadores** — organizam a sintaxe (`( )`, `[ ]`, `{ }`, `,`, `:`…)
- **símbolos especiais** — fazem parte de outro token (`"`, `#`, `\`…)

Alguns tokens servem nos **dois** papéis, conforme o contexto:

- `*` multiplica **e** desempacota uma sequência
- `@` multiplica matrizes **e** marca um decorator
- `=` atribui **e** aparece em f-string de depuração (`f"{x=}"`)

A documentação oficial do Python lista os tokens abaixo.
Os que já apareceram nas seções anteriores (`+`, `and`, `==`, `=`) estão aqui de novo para a lista ficar **completa**.

---

## Operadores (tokens oficiais)

Estes são **todos** os tokens classificados como operadores:

```
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=
```

| Símbolo | Nome                         | O que faz                                      | Exemplo        | Resultado      |
| ------- | ---------------------------- | ---------------------------------------------- | -------------- | -------------- |
| `+`     | soma / positivo              | soma, ou deixa o sinal positivo                | `5 + 3`        | `8`            |
| `-`     | subtração / negativo         | diminui, ou inverte o sinal                    | `-5`           | `-5`           |
| `*`     | multiplicação / repetição    | multiplica números; também repete texto        | `"ab" * 2`     | `"abab"`       |
| `**`    | potência                     | eleva a um expoente                            | `2 ** 3`       | `8`            |
| `/`     | divisão                      | divide; o resultado é `float`                  | `5 / 2`        | `2.5`          |
| `//`    | divisão inteira              | divide e descarta a parte decimal              | `5 // 2`       | `2`            |
| `%`     | módulo                       | resto da divisão                               | `5 % 2`        | `1`            |
| `@`     | matmul                       | multiplicação de matrizes (NumPy / objetos)    | `A @ B`        | matriz produto |
| `<<`    | deslocamento à esquerda      | empurra bits para a esquerda (multiplica por 2)| `5 << 1`       | `10`           |
| `>>`    | deslocamento à direita       | empurra bits para a direita (divide por 2)     | `5 >> 1`       | `2`            |
| `&`     | E bit a bit                  | bit 1 só se os dois bits forem 1               | `6 & 3`        | `2`            |
| `\|`    | OU bit a bit                 | bit 1 se pelo menos um bit for 1               | `6 \| 3`       | `7`            |
| `^`     | XOR bit a bit                | bit 1 se os bits forem **diferentes**          | `6 ^ 3`        | `5`            |
| `~`     | NÃO bit a bit                | inverte todos os bits                          | `~5`           | `-6`           |
| `:=`    | morsa (walrus)               | atribui **e** usa o valor na mesma expressão   | `(n := 3)`     | `3` (e `n=3`)  |
| `<`     | menor que                    | compara se o da esquerda é menor               | `3 < 5`        | `True`         |
| `>`     | maior que                    | compara se o da esquerda é maior               | `5 > 3`        | `True`         |
| `<=`    | menor ou igual               | menor **ou** igual                             | `5 <= 5`       | `True`         |
| `>=`    | maior ou igual               | maior **ou** igual                             | `5 >= 5`       | `True`         |
| `==`    | igual a                      | compara **valor**                              | `5 == 5`       | `True`         |
| `!=`    | diferente de                 | o contrário de `==`                            | `5 != 3`       | `True`         |

`=` sozinho **não** está nesta lista: lexicamente ele é um **delimitador** (atribuição), não um operador de expressão.

### Operadores unários (`+`, `-`, `~`)

Ficam **antes** de um único valor:

```python
x = 5
print(+x)   # 5   (positivo)
print(-x)   # -5  (inverte o sinal)
print(~x)   # -6  (inverte bits: ~n vale -(n + 1))
```

### Operadores bit a bit

Trabalham nos **bits** do número (0 e 1), não no valor decimal “de cara”.

```python
a = 6        # bits: 110
b = 3        # bits: 011

print(a & b)   # 2   (010)  os dois 1
print(a | b)   # 7   (111)  pelo menos um 1
print(a ^ b)   # 5   (101)  bits diferentes
print(~a)      # -7
print(a << 1)  # 12  (1100)  deslocou e preencheu 0 à direita
print(a >> 1)  # 3   (011)
```

Use bit a bit em flags, máscaras, permissões e quando o valor for tratado como conjunto de bits.
Não confunda `|` / `&` com `or` / `and`: aqueles são **lógicos** (`True`/`False`); estes são **bit a bit**.

### `@` — multiplicação de matrizes

Em números comuns, `*` multiplica item a item (ou o número inteiro).
`@` é o operador de **produto de matrizes** (PEP 465). Tipos nativos (`int`, `list`) **não** implementam `@`; quem usa é NumPy e classes que definem `__matmul__`.

```python
# ideia (NumPy):
# A @ B   → produto de matrizes
# A * B   → multiplicação elemento a elemento
```

O mesmo símbolo `@` no começo de uma linha, **antes** de `def` ou `class`, é decorator (ver delimitadores).

### `:=` — operador morsa (walrus)

Atribui um valor **dentro** de uma expressão (if, while, compreensão).
Existe a partir do Python 3.8.

```python
# sem morsa: precisa de duas linhas
texto = input("nome: ")
if texto:
    print(texto)

# com morsa: atribui e testa ao mesmo tempo
if texto := input("nome: "):
    print(texto)
```

O nome “morsa” vem do desenho `:=` parecer uns olhos e presas.

---

## Operadores que são palavras (não símbolos)

Alguns operadores **não** são `+` ou `==`: são **palavras reservadas**.

| Palavra      | O que faz                                      | Exemplo                    |
| ------------ | ---------------------------------------------- | -------------------------- |
| `and`        | `True` só se os dois lados forem verdadeiros   | `idade >= 18 and ok`       |
| `or`         | `True` se pelo menos um lado for verdadeiro    | `feriado or domingo`       |
| `not`        | inverte o booleano                             | `not ligado`               |
| `is`         | mesmo **objeto** na memória                    | `x is None`                |
| `is not`     | não é o mesmo objeto                           | `x is not None`            |
| `in`         | o valor está **dentro** da sequência           | `"a" in "casa"`            |
| `not in`     | o valor **não** está dentro                    | `3 not in [1, 2]`          |

`and` / `or` / `not` são lógicos. `&` / `|` / `~` são bit a bit. Não troque um pelo outro.

---

## Delimitadores (tokens oficiais)

Estes tokens **organizam** a gramática. A segunda metade também **opera** (atribuição aumentada):

```
(       )       [       ]       {       }
,       :       !       .       ;       @       =
->      +=      -=      *=      /=      //=     %=
@=      &=      |=      ^=      >>=     <<=     **=
```

### Parênteses `( )`

Vários usos:

```python
print(2 + 3)          # chamada de função: argumentos ficam dentro
ordem = (2 + 3) * 4   # agrupa a conta: primeiro 2+3
tupla = (1, 2, 3)     # tupla
vazia = ()            # tupla vazia

def soma(a, b):       # parâmetros da função
    return a + b

# continuar linha sem \
total = (1 + 2 +
         3 + 4)
```

Uma tupla de **um** item precisa de vírgula: `(1,)` é tupla; `(1)` é só o número 1.

### Colchetes `[ ]`

```python
lista = [10, 20, 30]     # cria lista
print(lista[0])          # índice: primeiro item
print(lista[0:2])        # fatiamento (slice): [10, 20]
print(lista[::-1])       # fatia invertida
matriz[1][0]             # lista dentro de lista

# compreensão de lista
dobros = [n * 2 for n in lista]
```

No fatiamento, `:` **dentro** dos colchetes separa início, fim e passo: `lista[inicio:fim:passo]`.

### Chaves `{ }`

```python
conjunto = {1, 2, 3}                      # set
pessoa = {"nome": "Ana", "idade": 20}     # dict
vazio_dict = {}                           # {} é dict vazio, não set
vazio_set = set()                         # set vazio precisa de set()

# compreensões
quadrados = {n: n ** 2 for n in range(3)}
unicos = {n % 2 for n in range(5)}
```

Também delimitam o miolo de uma **f-string**: `f"olá {nome}"`.

### Vírgula `,`

Separa itens. É o que transforma vários valores em sequência.

```python
a, b, c = 1, 2, 3     # desempacota
print(1, 2, 3)        # vários argumentos
ponto = 10, 20        # tupla (os parênteses são opcionais)
um = (1,)             # vírgula obrigatória na tupla de 1 item
```

### Dois pontos `:`

Marca o **começo de um bloco** ou separa chave/valor, fatia, rótulo.

```python
if x > 0:                 # bloco do if
    print("positivo")

def f(n):                 # bloco da função
    return n

pessoa = {"nome": "Ana"}  # chave : valor
lista[1:3]                # fatia
rotulo: int = 10          # anotação de tipo (opcional)
```

Sem `:` depois de `if`, `for`, `def`, `class`, `while`, `try`, `match`… o Python aponta erro de sintaxe.

### Ponto `.`

Acesso a atributo, método, ou parte decimal de número.

```python
texto = "python"
print(texto.upper())   # método do objeto
print(math.pi)         # atributo do módulo
preco = 2.90           # ponto decimal (não é operador aqui)
```

Três pontos seguidos (`...`) são o literal **Ellipsis** (reticências), não “três acessos”.

### Ponto e vírgula `;`

Separa **várias instruções na mesma linha**. Quase não se usa: o estilo Python prefere uma instrução por linha.

```python
x = 1; y = 2; print(x + y)
```

### Exclamação `!`

Sozinha, `!` **não** é “não lógico” (isso é `not`).
Aparece em:

- `!=` — diferente de (já é um operador)
- f-string: conversão de valor

```python
x = "olá"
print(f"{x!s}")   # str(x)   → olá
print(f"{x!r}")   # repr(x)  → 'olá'  (mostra aspas)
print(f"{x!a}")   # ascii(x)
```

### Seta `->`

Anota o **tipo de retorno** da função. É só documentação para o leitor e para ferramentas; o Python **não** impede de devolver outro tipo.

```python
def dobro(n: int) -> int:
    return n * 2
```

### `@` como decorator

Linha **acima** de `def` ou `class`. Envolve a função/classe em outra função.

```python
@property
def idade(self):
    return self._idade
```

Dá para empilhar vários `@`. Não é a mesma coisa que `A @ B` (matmul).

### `=` e atribuições aumentadas

`=` guarda valor. Os compostos fazem a conta **e** guardam.

| Símbolo | Equivale a      | Grupo            |
| ------- | --------------- | ---------------- |
| `=`     | `x = 5`         | atribuição       |
| `+=`    | `x = x + 1`     | aritmética       |
| `-=`    | `x = x - 1`     | aritmética       |
| `*=`    | `x = x * 2`     | aritmética       |
| `/=`    | `x = x / 2`     | aritmética       |
| `//=`   | `x = x // 2`    | aritmética       |
| `%=`    | `x = x % 2`     | aritmética       |
| `**=`   | `x = x ** 2`    | aritmética       |
| `@=`    | `x = x @ y`     | matriz           |
| `&=`    | `x = x & y`     | bit a bit        |
| `\|=`   | `x = x \| y`    | bit a bit        |
| `^=`    | `x = x ^ y`     | bit a bit        |
| `<<=`   | `x = x << n`    | bit a bit        |
| `>>=`   | `x = x >> n`    | bit a bit        |

```python
flags = 0
flags |= 1    # liga o bit 1
flags &= ~1   # desliga o bit 1
```

---

## `*` e `**` além da conta

O mesmo símbolo da multiplicação/potência também **desempacota** e marca parâmetros.

```python
# desempacotar sequência / dicionário
nums = [1, 2, 3]
print(*nums)              # print(1, 2, 3)

a, *meio, z = [1, 2, 3, 4]
# a=1, meio=[2, 3], z=4

d1 = {"a": 1}
d2 = {**d1, "b": 2}       # junta dicts

# na função: vários argumentos
def f(*args, **kwargs):
    print(args, kwargs)

f(1, 2, nome="Ana")       # args=(1, 2)  kwargs={"nome": "Ana"}
```

Na **assinatura**, `/` e `*` separam como o argumento pode ser passado:

```python
def f(so_posicao, /, os_dois, *, so_nome):
    pass

f(1, 2, so_nome=3)        # ok
# f(so_posicao=1, ...)    # erro: antes da / só por posição
# f(1, 2, 3)              # erro: depois do * só por nome
```

`except*` (Python 3.11+) trata **grupos de exceção**, diferente de `except` comum.

---

## Símbolos especiais (parte de outros tokens)

Não são operadores sozinhos. Fora de string/comentário, o analisador léxico trata assim:

| Símbolo | Nome            | O que faz                                                                 |
| ------- | --------------- | ------------------------------------------------------------------------- |
| `'`     | aspas simples   | delimita string: `'texto'`                                                |
| `"`     | aspas duplas    | delimita string: `"texto"`                                                |
| `'''` / `"""` | aspas triplas | string de várias linhas (docstring costuma usar `"""`)                    |
| `#`     | cerquilha       | começa **comentário** até o fim da linha                                  |
| `\`     | barra invertida | escapa caractere na string (`\n`) **ou** continua a linha                 |

```python
# isto é comentário: o Python ignora

frase = "ele disse \"oi\""   # aspas dentro da string
quebra = "linha1\nlinha2"    # \n = nova linha

# continuar instrução na linha de baixo
total = 1 + 2 + \
        3 + 4
```

Aspas simples e duplas são iguais. Use uma para poder colocar a outra no texto: `"it's ok"` ou `'ela disse "oi"'`.

### Prefixos de string e bytes

Colados **antes** das aspas, sem espaço:

| Prefixo | Tipo                         | Exemplo                |
| ------- | ---------------------------- | ---------------------- |
| (nenhum)| string normal                | `"Ana"`                |
| `r`     | raw: `\` não escapa          | `r"C:\nova"`           |
| `f`     | f-string: embute expressão   | `f"oi {nome}"`         |
| `b`     | bytes (dados brutos)         | `b"ABC"`               |
| `u`     | string (legado, igual ao normal) | `u"texto"`          |
| `fr`/`rf` | f-string raw               | `fr"{x}\n"`            |
| `br`/`rb` | bytes raw                  | `br"a\n"`              |

```python
nome = "Ana"
print(f"olá {nome}")     # olá Ana
print(r"\n")             # \n  (duas letras, não quebra de linha)
```

Dentro da f-string:

| Símbolo   | O que faz                         | Exemplo            |
| --------- | --------------------------------- | ------------------ |
| `{expr}`  | coloca o valor da expressão       | `f"{1 + 1}"` → `2` |
| `{{` `}}` | chave literal                     | `f"{{x}}"` → `{x}` |
| `{x=}`    | mostra nome e valor (depuração)   | `f"{x=}"` → `x=10` |
| `{x!r}`   | conversão `repr`                  | ver `!` acima      |
| `{x:.2f}` | formato (2 casas decimais)        | `f"{pi:.2f}"`      |

### Prefixos e símbolos de número

| Forma     | Significado              | Exemplo        |
| --------- | ------------------------ | -------------- |
| `0b`      | binário (base 2)         | `0b1010` → 10  |
| `0o`      | octal (base 8)           | `0o17` → 15    |
| `0x`      | hexadecimal (base 16)    | `0xFF` → 255   |
| `_`       | separa dígitos (ignorado)| `1_000_000`    |
| `.`       | parte decimal            | `3.14`, `.5`   |
| `e` / `E` | notação científica       | `1e3` → 1000.0 |
| `j` / `J` | imaginário (complexo)    | `3+4j`         |

```python
print(0b1010)      # 10
print(0xFF)        # 255
print(1_000_000)   # 1000000
print(1e3)         # 1000.0
print(3 + 4j)      # (3+4j)
```

---

## Reticências `...` (Ellipsis)

Três pontos são um **literal**: o objeto `Ellipsis`.
Aparece em fatiamento avançado (NumPy), stubs (`pass` de tipo) e como valor sentinela.

```python
print(...)           # Ellipsis
print(... is Ellipsis)  # True

def ainda_nao_implementei():
    ...
```

---

## Símbolos que o Python **não** usa

Fora de string e comentário, estes caracteres ASCII **dão erro** de sintaxe:

| Símbolo | Nome        |
| ------- | ----------- |
| `$`     | cifrão      |
| `?`     | interrogação|
| `` ` `` | crase       |

Não existe operador `? :` (ternário de C/Java). Em Python o ternário é `a if cond else b`.
Não existe interpolação `$nome`. Use f-string: `f"{nome}"`.

---

## Indentação, espaço e quebra de linha

Em Python o **espaço no começo da linha** faz parte da sintaxe: abre e fecha blocos.
Não existem `{ }` de bloco como em C/Java. O bloco começa depois de `:` e vai pelo recuo.

```python
if True:
    print("dentro")    # indentado: pertence ao if
print("fora")          # sem indent: depois do if
```

| Token implícito | Quando aparece                         |
| --------------- | -------------------------------------- |
| `NEWLINE`       | fim de uma linha lógica                |
| `INDENT`        | a linha recuou mais (entrou no bloco)  |
| `DEDENT`        | a linha recuou menos (saiu do bloco)   |

Regras práticas:

- Use **4 espaços** por nível (convenção oficial, PEP 8).
- Não misture **tab** e espaço no mesmo arquivo.
- Linha em branco é ignorada.
- `\` no fim da linha **junta** com a de baixo.
- Dentro de `( )`, `[ ]` ou `{ }` a quebra de linha é livre (não precisa `\`).

```python
# implícito: parênteses permitem várias linhas
nomes = [
    "Ana",
    "Bia",
]
```

---

## Palavras reservadas (keywords)

Não podem ser nome de variável. Precisam ser escritas **exatamente** assim:

```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

| Palavra     | Papel curto                                      |
| ----------- | ------------------------------------------------ |
| `False`     | booleano falso                                   |
| `True`      | booleano verdadeiro                              |
| `None`      | “sem valor”                                      |
| `and` `or` `not` | operadores lógicos                          |
| `is` `in`   | identidade / pertinência                         |
| `if` `elif` `else` | decisão                                    |
| `for` `while` | repetição                                      |
| `break` `continue` `pass` | controlar loop / placeholder          |
| `def`       | define função                                    |
| `return`    | sai da função e devolve valor                    |
| `class`     | define classe                                    |
| `lambda`    | função anônima de uma expressão                  |
| `try` `except` `finally` | tratamento de erro                    |
| `raise`     | lança um erro                                    |
| `assert`    | testa uma condição; falha se for falsa           |
| `with` `as` | contexto (arquivo, etc.) e apelido               |
| `import` `from` | traz código de outro módulo                  |
| `global` `nonlocal` | usa variável de fora da função            |
| `del`       | apaga nome ou item                               |
| `yield`     | devolve valor e **pausa** um gerador             |
| `async` `await` | programação assíncrona                        |

```python
# lambda: função sem nome
dobro = lambda n: n * 2
print(dobro(4))   # 8

# yield: gerador
def contagem(n):
    for i in range(n):
        yield i

# assert: trava se a condição for falsa
assert idade >= 0, "idade não pode ser negativa"
```

### Soft keywords (parecem palavra-chave só em alguns lugares)

`match`, `case`, `type` e `_` **podem** ser nome de variável.
Só viram palavra especial no contexto certo (Python 3.10+; `type` a partir de 3.12).

```python
match = 10          # ok: match como variável
type = "texto"      # ok (mas evita: sombreia a função type)

match dia:          # aqui match é a estrutura
    case 1:
        print("segunda")
    case _:         # _ = qualquer outro valor
        print("outro")

type Ponto = tuple[int, int]   # apelido de tipo (3.12+)
```

---

## Identificadores e o símbolo `_`

O nome de variável pode ter letras, dígitos (não no começo) e `_`.

| Forma      | Significado usual                                      |
| ---------- | ------------------------------------------------------ |
| `nome`     | identificador normal                                   |
| `_`        | “não vou usar este valor”; wildcard do `case`          |
| `_nome`    | “interno”; `from modulo import *` **não** importa      |
| `__nome`   | nome “privado” da classe (o Python reescreve o nome)   |
| `__nome__` | método/atributo especial do Python (`__init__`, `__len__`) |

```python
for _ in range(3):     # não interessa o contador
    print("oi")

class Pessoa:
    def __init__(self, nome):   # construtor
        self.nome = nome
```

---

## Precedência (quem calcula primeiro)

Quando vários operadores aparecem juntos, o Python segue uma ordem.
Do que resolve **primeiro** para o que resolve **por último**:

| Prioridade | Operadores / formas                                      |
| ---------- | -------------------------------------------------------- |
| 1 (maior)  | `( )` `[ ]` `{ }` `.` chamada `f()`                      |
| 2          | `await x`                                                |
| 3          | `x ** y`                                                 |
| 4          | `+x` `-x` `~x`                                           |
| 5          | `*` `@` `/` `//` `%`                                     |
| 6          | `+` `-`                                                  |
| 7          | `<<` `>>`                                                |
| 8          | `&`                                                      |
| 9          | `^`                                                      |
| 10         | `\|`                                                     |
| 11         | `in` `not in` `is` `is not` `<` `<=` `>` `>=` `==` `!=` |
| 12         | `not x`                                                  |
| 13         | `and`                                                    |
| 14         | `or`                                                     |
| 15         | `a if cond else b`                                       |
| 16         | `lambda`                                                 |
| 17 (menor) | `:=`                                                     |

Na dúvida, use parênteses. `2 + 3 * 4` vale `14`, não `20`.
`(2 + 3) * 4` vale `20`.

---

# Resumo — símbolos e sintaxe

| Símbolo / palavra        | Família        | O que é                                      |
| ------------------------ | -------------- | -------------------------------------------- |
| `+ - * / // % **`        | aritmético     | contas numéricas                             |
| `@`                      | aritmético     | produto de matrizes **ou** decorator         |
| `+x -x ~x`               | unário         | sinal e inversão de bits                     |
| `& \| ^ ~ << >>`         | bit a bit      | opera nos bits do número                     |
| `== != < > <= >=`        | comparação     | devolve `True` / `False`                     |
| `and or not`             | lógico         | combina booleanos                            |
| `is` `in`                | identidade     | mesmo objeto / pertence a                    |
| `=` `+=` `-=` … `:=`     | atribuição     | guarda valor (`:=` também na expressão)      |
| `( )`                    | delimitador    | chamada, agrupamento, tupla                  |
| `[ ]`                    | delimitador    | lista, índice, fatia                         |
| `{ }`                    | delimitador    | dict, set, f-string                          |
| `,`                      | delimitador    | separa itens                                 |
| `:`                      | delimitador    | começa bloco, chave/valor, fatia             |
| `.`                      | delimitador    | atributo **ou** decimal                      |
| `...`                    | literal        | Ellipsis                                     |
| `;`                      | delimitador    | várias instruções na mesma linha             |
| `->`                     | delimitador    | tipo de retorno da função                    |
| `!`                      | delimitador    | conversão em f-string (`!r`)                 |
| `*` `**`                 | misto          | conta, desempacota, `*args` / `**kwargs`     |
| `/` `*` na `def`         | sintaxe        | só posição / só nome                         |
| `'` `"` `'''` `"""`      | literal        | delimita texto                               |
| `#`                      | comentário     | ignora o resto da linha                      |
| `\`                      | especial       | escape ou continua a linha                   |
| `f` `r` `b`              | prefixo        | f-string, raw, bytes                         |
| `0b` `0o` `0x` `_` `j`   | literal        | bases, milhar, imaginário                    |
| indentação               | sintaxe        | abre/fecha bloco                             |
| `$` `?` `` ` ``          | —              | **proibidos** fora de string/comentário      |
| `if cond else`           | ternário       | escolhe um valor                             |
| `match` `case` `_`       | soft keyword   | escolha por padrão                           |

---

**Próximo passo:** [Big O e estruturas complexas](#notação-big-o-e-análise-de-complexidade) (neste arquivo) → trilha completa [ESTUDO.md](ESTUDO.md) → runtime [README.md §26](README.md#26-arquitetura-do-python-cpython)
