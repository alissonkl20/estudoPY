"""
Exemplos de uso consolidados de README.md e readme.md — estudo de Python.

Trilha e checklists (básico → especialista): ESTUDO.md

Execute:  python base.py          # todos os demos
          python base.py pilares  # só seções cujo nome contém o filtro (minúsculas)
          python base.py bigo     # Big O (list vs set)
"""

from __future__ import annotations

import asyncio
import copy
import dis
import functools
import heapq
import io
import math
import os
import sys
import tempfile
import time
import timeit
from array import array
from collections import Counter, defaultdict, deque
from contextlib import contextmanager, suppress
from dataclasses import dataclass, field
from itertools import chain, count, islice, product
from pathlib import Path
from typing import Callable, Iterator, Iterable, NamedTuple, Optional, Protocol, Sequence, TypeVar

# ---------------------------------------------------------------------------
# Utilitários de visualização
# ---------------------------------------------------------------------------


def titulo(nome: str) -> None:
    linha = "─" * min(72, max(40, len(nome) + 4))
    print(f"\n{linha}\n  {nome}\n{linha}")


def mostra(*args, **kwargs) -> None:
    print(*args, **kwargs)


# =============================================================================
# readme.md — tipos e operadores básicos
# =============================================================================


def demo_tipos_primitivos() -> None:
    titulo("Tipos: int, float, str, bool, bytes (readme.md)")
    idade = 25
    preco = 2.90
    nome = "Alisson"
    ligado = True
    dados = b"ABC"
    letra = "A"
    mostra("int:", idade, type(idade))
    mostra("float:", preco, type(preco))
    mostra("str:", nome, repr(codigo := "123"), "≠", 123)
    mostra("bool:", ligado, type(ligado))
    mostra("bytes:", dados, len(letra))


def demo_operadores_aritmeticos() -> None:
    titulo("Operadores aritméticos (readme.md)")
    a, b = 10, 3
    mostra(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)
    mostra("2 ** 3 =", 2 ** 3, "| 5/2 =", 5 / 2, "| 5//2 =", 5 // 2)


def demo_operadores_logicos_comparacao() -> None:
    titulo("Lógicos, comparação, atribuição (readme.md)")
    idade, tem_ingresso = 20, True
    mostra("and:", idade >= 18 and tem_ingresso)
    mostra("or:", False or True)
    mostra("not:", not False)
    x = 10
    mostra("==", x == 10)
    x += 5
    x -= 3
    mostra("+=/-=:", x)
    mostra('"" or "padrão":', "" or "padrão")
    mostra('"ok" and 42:', "ok" and 42)


def demo_identidade_pertinencia() -> None:
    titulo("is / in (readme.md)")
    lista = [1, 2, 3]
    mostra(2 in lista, 5 not in lista)
    mostra((None is None), ("a" in "casa"))


def demo_controle_fluxo() -> None:
    titulo("if, match, for, while, break, continue (readme.md)")
    a = 20
    if a > 12:
        mostra("if: a > 12")
    status = "adulto" if a >= 18 else "menor"
    mostra("ternário:", status)

    dia = 2
    match dia:
        case 1:
            mostra("match: segunda")
        case 2:
            mostra("match: terça")
        case _:
            mostra("match: outro")

    mostra("range(5):", list(range(5)))
    for i, nome in enumerate(["Ana", "Bia"], start=0):
        mostra("enumerate:", i, nome)

    x = 3
    while x > 1:
        mostra("while:", x)
        x -= 1

    for n in [2, 4, 6]:
        if n % 2 != 0:
            break
    else:
        mostra("for-else: todos pares")

    for i in range(5):
        if i == 2:
            continue
        if i == 4:
            break
        mostra("continue/break loop:", i)

    if True:
        pass  # placeholder


def demo_excecoes_contexto() -> None:
    titulo("try/except e with (readme.md)")
    try:
        int("abc")
    except ValueError:
        mostra("except: não é número")
    else:
        mostra("else: conversão ok")
    finally:
        mostra("finally: sempre")

    try:
        _ = 10 / 0
    except ZeroDivisionError:
        mostra("except: divisão por zero")

    with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as f:
        caminho = f.name
        f.write("conteúdo de estudo")
    try:
        with open(caminho, encoding="utf-8") as arq:
            mostra("with read:", arq.read())
    finally:
        os.remove(caminho)


def demo_retorno_funcao() -> None:
    titulo("return (readme.md)")

    def dobro(n: int) -> int:
        return n * 2

    mostra("dobro(7):", dobro(7))


# =============================================================================
# readme.md — estruturas de dados
# =============================================================================


def demo_lista_tupla_set_dict() -> None:
    titulo("list, tuple, set, dict (readme.md)")
    numeros = [10, 20, 30]
    numeros.append(40)
    numeros[0] = 99
    mostra("lista:", numeros, "len:", len(numeros))

    ponto = (10, 20)
    x, y = ponto
    mostra("tupla unpack:", x, y)

    a = {1, 2, 3, 3}
    mostra("set:", a, "| :", a | {3, 4}, "& :", a & {2, 9})

    pessoa = {"nome": "Ana", "idade": 20}
    pessoa["cidade"] = "SP"
    mostra("dict:", pessoa, pessoa.get("idade"))


def demo_array_matriz() -> None:
    titulo("array.array e matriz (readme.md)")
    arr = array("i", [1, 2, 3])
    mostra("array:", list(arr), "bytes:", bytes(arr))
    matriz = [[1, 2, 3], [4, 5, 6]]
    mostra("matriz[1][0]:", matriz[1][0])


def demo_lista_ligada_simples() -> None:
    titulo("Lista ligada simples (readme.md)")

    class No:
        def __init__(self, valor):
            self.valor = valor
            self.proximo = None

    inicio = No(10)
    inicio.proximo = No(20)
    inicio.proximo.proximo = No(30)
    vals = []
    atual = inicio
    while atual:
        vals.append(atual.valor)
        atual = atual.proximo
    mostra("cadeia:", vals)


def demo_fila_deque_heap_pilha() -> None:
    titulo("fila, deque, heap, pilha (readme.md)")
    fila = deque()
    fila.append("pessoa 1")
    fila.append("pessoa 2")
    mostra("fila popleft:", fila.popleft())

    d = deque([1, 2, 3])
    d.appendleft(0)
    d.pop()
    mostra("deque:", list(d))

    tarefas = []
    heapq.heappush(tarefas, (1, "urgente"))
    heapq.heappush(tarefas, (3, "pode esperar"))
    heapq.heappush(tarefas, (2, "normal"))
    mostra("heap pop:", heapq.heappop(tarefas))

    pilha = []
    pilha.append("A")
    pilha.append("B")
    mostra("pilha pop:", pilha.pop())


def demo_arvore_grafo() -> None:
    titulo("árvore binária e grafo (readme.md)")

    class NoArvore:
        def __init__(self, valor):
            self.valor = valor
            self.esquerda = None
            self.direita = None

    raiz = NoArvore(8)
    raiz.esquerda = NoArvore(3)
    raiz.direita = NoArvore(10)

    grafo = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}
    mostra("raiz.valor:", raiz.valor, "| grafo A:", grafo["A"])


# =============================================================================
# readme.md — símbolos, bitwise, walrus, strings
# =============================================================================


def demo_bitwise_walrus_unarios() -> None:
    titulo("unários, bit a bit, walrus (readme.md)")
    x = 5
    mostra(+x, -x, ~x)
    a, b = 6, 3
    mostra(a & b, a | b, a ^ b, ~a, a << 1, a >> 1)
    n = 3
    if (n := n + 1) > 3:
        mostra("walrus n:", n)


def demo_delimitadores_slice() -> None:
    titulo("(), [], {}, slice :: (readme.md)")
    s = "PYTHON"
    mostra(s[1:4], s[::2], s[::-1], s[1:-1])
    sl = slice(1, 4, 2)
    mostra("slice obj:", s[sl])
    lista = [10, 20, 30]
    mostra(lista[0:2], lista[::-1])
    pessoa = {"nome": "Ana", "idade": 20}
    mostra(pessoa)
    t = 1, 2, 3
    um = (1,)
    mostra("tupla:", t, "um item:", um, type((1)))


def demo_args_unpacking() -> None:
    titulo("*args, **kwargs, unpacking (readme.md)")

    def f(*args, **kwargs):
        return args, kwargs

    mostra(f(1, 2, nome="Ana"))
    nums = [1, 2, 3]
    mostra("print unpack:", end=" ")
    print(*nums)
    a, *meio, z = [1, 2, 3, 4]
    mostra("a, meio, z:", a, meio, z)
    mostra({**{"a": 1}, "b": 2})


def demo_strings_literals() -> None:
    titulo("f-string, raw, bytes, literais numéricos (readme.md)")
    nome = "Ana"
    pi = 3.14159
    x = 10
    mostra(f"olá {nome}", f"{x=}", f"{pi:.2f}", r"\n", f"{nome!r}")
    mostra(0b1010, 0xFF, 1_000_000, 1e3, 3 + 4j)
    mostra(... is Ellipsis)


def demo_lambda_yield_assert() -> None:
    titulo("lambda, yield, assert (readme.md)")
    dobro = lambda n: n * 2
    mostra("lambda:", dobro(4))

    def contagem(n: int):
        for i in range(n):
            yield i

    mostra("gerador:", list(contagem(4)))
    assert 25 >= 0


def demo_precedencia() -> None:
    titulo("precedência (readme.md)")
    mostra("2+3*4 =", 2 + 3 * 4, "| (2+3)*4 =", (2 + 3) * 4)


# =============================================================================
# README.md — pilares, sintaxe, paradigmas
# =============================================================================


def demo_pilares() -> None:
    titulo("Pilares: objetos, EAFP (README.md)")

    def absoluto(n: int) -> int:
        if n < 0:
            return -n
        return n

    x = 10
    mostra(type(x), id(x), x.__class__)
    mostra("absoluto(-5):", absoluto(-5))

    dicionario = {}
    chave, padrao = "z", 0
    try:
        valor = dicionario[chave]
    except KeyError:
        valor = padrao
    mostra("EAFP valor:", valor)


def demo_paradigmas() -> None:
    titulo("Paradigmas: procedural, OOP, funcional (README.md)")
    total = 0
    for n in [1, 2, 3]:
        total += n
    mostra("procedural total:", total)

    class Conta:
        def __init__(self, saldo=0):
            self.saldo = saldo

        def depositar(self, valor):
            self.saldo += valor

    c = Conta()
    c.depositar(100)
    mostra("Conta saldo:", c.saldo)

    nums = [1, 2, 3, 4]
    pares = [n for n in nums if n % 2 == 0]
    dobro = list(map(lambda x: x * 2, nums))
    mostra("pares:", pares, "dobro:", dobro)


def demo_sintaxe_avancada() -> None:
    titulo("range, next, operadores de conjunto (README.md)")
    mostra(list(range(5)), list(range(2, 5)), list(range(0, 10, 2)))
    r = range(10, 20)
    mostra(r[0], r[-1], len(r), 15 in r)

    it = iter([10, 20, 30])
    mostra(next(it), next(it), next(it, "fim"))

    a, b = {1, 2, 3}, {3, 4}
    mostra(a | b, a & b, a - b, a ^ b)


def demo_modelo_dados() -> None:
    titulo("mutabilidade, truthiness, default mutável (README.md)")
    a = [1, 2]
    b = a
    b.append(3)
    mostra("mesma lista:", a)

    a2 = [1, 2]
    b2 = a2.copy()
    b2.append(3)
    mostra("cópia:", a2, b2)

    def bom(xs=None):
        if xs is None:
            xs = []
        xs.append(1)
        return xs

    mostra("bom():", bom(), bom())

    itens = [1]
    mostra("truthy lista:", bool(itens), "| vazia:", bool([]))


# =============================================================================
# README.md — listas, tuplas, arrays
# =============================================================================


def demo_lista_avancada() -> None:
    titulo("lista: métodos, matriz, pilha/deque (README.md)")
    xs = [1, 2, 3]
    xs.append(4)
    xs.extend([5])
    xs.insert(0, 0)
    mostra("xs:", xs, "pop:", xs.pop(), "sorted:", sorted(xs))

    ruim = [[0] * 3] * 3
    ruim[0][0] = 1
    bom = [[0] * 3 for _ in range(3)]
    bom[0][0] = 1
    mostra("armadilha *3 linhas iguais:", ruim[1][0], "| bom:", bom[1][0])

    stack = []
    stack.append(1)
    stack.append(2)
    mostra("pilha pop:", stack.pop())

    q = deque()
    q.append("x")
    mostra("deque popleft:", q.popleft())


def demo_tupla_avancada() -> None:
    titulo("tupla, NamedTuple, dataclass (README.md)")
    t = 1, 2, 3
    unidade = (1,)
    mostra(t, unidade, tuple("ab"))

    d = {(0, 0): "origem"}
    mostra(d[(0, 0)])

    class Ponto(NamedTuple):
        x: float
        y: float

    @dataclass
    class Pessoa:
        nome: str
        idade: int = 0

    p = Ponto(1.0, 2.0)
    mostra(p, Pessoa("Ana", 30))


def demo_arrays_tipos() -> None:
    titulo("list mista, array.array, numpy opcional (README.md)")
    misto = [1, "a", None, [2]]
    mostra(misto)
    a = array("i", [1, 2, 3])
    a.append(4)
    mostra(list(a), len(bytes(a)))
    try:
        import numpy as np

        v = np.array([1, 2, 3])
        mostra("numpy v*2:", v * 2)
        M = np.zeros((2, 2))
        M[0, :] = 1
        mostra("numpy M:", M)
    except ImportError:
        mostra("(numpy não instalado — pule ou pip install numpy)")


# =============================================================================
# README.md — linked list completa, coleções
# =============================================================================


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


def demo_linked_list() -> None:
    titulo("LinkedList (README.md)")
    ll = LinkedList([1, 2, 3])
    ll.prepend(0)
    mostra(ll, list(ll))


def demo_dict_set_collections() -> None:
    titulo("dict/set e collections (README.md)")
    d = {"a": 1, "b": 2}
    mostra(d.get("z", 0), d.setdefault("c", 3))
    d1, d2 = {"a": 1}, {"b": 2}
    mostra(d1 | d2)

    n = defaultdict(int)
    n["x"] += 1
    c = Counter("banana")
    mostra("defaultdict:", dict(n), "Counter:", dict(c))

    s = {1, 2, 3}
    s.add(4)
    s.discard(99)
    mostra(s)


# =============================================================================
# README.md — funções e OOP
# =============================================================================


def demo_funcoes() -> None:
    titulo("funções: closure, lambda, LEGB (README.md)")

    def externo(x):
        def interno(y):
            return x + y

        return interno

    soma2 = externo(2)
    mostra("closure:", soma2(5))

    xs = [{"idade": 30}, {"idade": 20}]
    xs.sort(key=lambda p: p["idade"])
    mostra("sort key:", xs)

    x_global = 1

    def f():
        nonlocal x_global
        x_global = 2

    f()
    mostra("nonlocal x:", x_global)


def demo_oop() -> None:
    titulo("OOP: herança, property (README.md)")

    class Animal:
        especie = "genérico"

        def __init__(self, nome):
            self.nome = nome

        def falar(self):
            raise NotImplementedError

        def __repr__(self):
            return f"Animal({self.nome!r})"

    class Cachorro(Animal):
        def falar(self):
            return "au"

    c = Cachorro("Bob")
    mostra(c.falar(), Cachorro.falar(c))

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

    obj = C.from_str("5")
    obj.n = 10
    mostra(obj.n, C.util(1))


@dataclass(slots=True)
class Item:
    nome: str
    tags: list[str] = field(default_factory=list)


class Desenhavel(Protocol):
    def desenhar(self) -> None: ...


def demo_dataclass_protocol() -> None:
    titulo("dataclass slots e Protocol (README.md)")
    mostra(Item("livro", tags=["py"]))


# =============================================================================
# README.md — iteradores, comprehensions, exceções, decorators
# =============================================================================


def demo_iteradores_geradores() -> None:
    titulo("iter, yield, itertools (README.md)")
    xs = [10, 20]
    it = iter(xs)
    mostra(next(it), next(it))

    def contador(n):
        i = 0
        while i < n:
            yield i
            i += 1

    mostra(list(contador(3)))
    g = (x * x for x in range(5))
    mostra("genexp:", list(g))
    mostra("islice:", list(islice(count(10), 5)))
    mostra("product:", list(product("AB", repeat=2)))


def demo_comprehensions() -> None:
    titulo("comprehensions e unpacking (README.md)")
    xs = [1, -2, 3]
    out = [x * 2 for x in xs if x > 0]
    mostra(out)
    matriz = [[1, 2], [3, 4]]
    flat = [c for linha in matriz for c in linha]
    mostra(flat, [*xs, 99])


def demo_excecoes_cm() -> None:
    titulo("exceções e context manager (README.md)")

    def risco():
        raise ValueError("ops")

    try:
        risco()
    except ValueError as e:
        mostra("capturado:", e)
    finally:
        mostra("finally ok")

    @contextmanager
    def temp_ctx():
        mostra("enter")
        try:
            yield 42
        finally:
            mostra("exit")

    with temp_ctx() as v:
        mostra("valor ctx:", v)

    with suppress(FileNotFoundError):
        os.remove("/tmp/arquivo_que_nao_existe_estudo")


def demo_decorators() -> None:
    titulo("decorators (README.md)")

    def cronometro(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            t0 = time.perf_counter()
            try:
                return fn(*args, **kwargs)
            finally:
                mostra(f"  {fn.__name__} em {time.perf_counter() - t0:.6f}s")

        return wrapper

    @cronometro
    def trabalho():
        return sum(range(1000))

    mostra("resultado:", trabalho())


def demo_type_hints() -> None:
    titulo("type hints (README.md)")

    def busca(xs: Sequence[int], alvo: int) -> int | None:
        for i, v in enumerate(xs):
            if v == alvo:
                return i
        return None

    T = TypeVar("T")

    def primeiro(xs: list[T]) -> T:
        return xs[0]

    mostra(busca([1, 2, 3], 2), primeiro([10, 20]))


# =============================================================================
# README.md — async, dunder, dis, exercícios
# =============================================================================


def demo_asyncio() -> None:
    titulo("asyncio (README.md)")

    async def busca(url: str):
        await asyncio.sleep(0.01)
        return url

    async def main_async():
        urls = ["a", "b", "c"]
        return await asyncio.gather(*(busca(u) for u in urls))

    mostra("gather:", asyncio.run(main_async()))


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


def demo_dunder() -> None:
    titulo("dunder methods — Vetor (README.md)")
    v1 = Vetor(1, 2)
    v2 = Vetor(3, 4)
    mostra(len(v1), v1[0], v1 + v2)


def demo_dis_runtime() -> None:
    titulo("dis — bytecode (README.md)")

    def f(x):
        return x + 1

    buf = io.StringIO()
    dis.dis(f, file=buf)
    mostra(buf.getvalue().splitlines()[0])


def demo_armadilhas_exercicios() -> None:
    titulo("armadilhas e mini exercícios (README.md)")
    funcoes_ruim = [lambda: i for i in range(3)]
    funcoes_bom = [lambda i=i: i for i in range(3)]
    mostra("late binding:", funcoes_ruim[0](), funcoes_bom[0]())

    mostra("Counter banana:", dict(Counter("banana")))

    def flatten(gen):
        for item in gen:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item

    aninhada = [1, [2, [3, 4]], 5]
    mostra("flatten:", list(flatten(aninhada)))

    def inverter(s: str) -> str:
        out = ""
        for ch in s:
            out = ch + out
        return out

    mostra("invert:", inverter("Python"), "|[::-1]:", "Python"[::-1])

    def fizz_match(n: int) -> list[str]:
        out = []
        for i in range(1, n + 1):
            match (i % 3 == 0, i % 5 == 0):
                case (True, True):
                    out.append("FizzBuzz")
                case (True, False):
                    out.append("Fizz")
                case (False, True):
                    out.append("Buzz")
                case _:
                    out.append(str(i))
        return out

    mostra("FizzBuzz match:", fizz_match(15)[:6], "...")

    # match avançado (README.md)
    status = 404
    match status:
        case 200:
            mostra("match status: ok")
        case 404 | 410:
            mostra("match status: sumiu")
        case {"erro": msg}:
            mostra(msg)
        case _:
            mostra("match status: outro")


def demo_pathlib_operadores_sequencia() -> None:
    titulo("pathlib, concat, comprehension vs loop (README.md)")
    p = Path(".") / "base.py"
    mostra("path existe:", p.exists(), p.name)
    mostra([1, 2] + [3], "ab" * 3, 3 in [1, 2, 3])
    xs = [1, 2, -1]
    out_loop = []
    for x in xs:
        if x > 0:
            out_loop.append(x * 2)
    out_comp = [x * 2 for x in xs if x > 0]
    mostra("loop vs comp:", out_loop, out_comp)


def demo_copia_profunda() -> None:
    titulo("copy shallow / deep (README.md)")
    a = [[1], [2]]
    b = a[:]
    c = copy.deepcopy(a)
    a[0].append(9)
    mostra("shallow compartilha:", b[0])
    mostra("deep isolado:", c[0])


def demo_soma_path_operadores() -> None:
    titulo("def com / e * keyword-only (README.md)")

    def f(a, b, /, c, *, d, **extra):
        return a + b + c + d + len(extra)

    mostra(f(1, 2, 3, d=4, x=1))


def demo_big_o() -> None:
    titulo("Big O — pertinência list O(n) vs set O(1) médio (ESTUDO.md / README §25)")
    n = 8000
    lista = list(range(n))
    conjunto = set(lista)
    alvo = n - 1
    mostra(f"n={n}, buscar {alvo} repetido 2000x:")
    t_lista = timeit.timeit(lambda: alvo in lista, number=2000)
    t_set = timeit.timeit(lambda: alvo in conjunto, number=2000)
    mostra(f"  in list: {t_lista:.4f}s")
    mostra(f"  in set:  {t_set:.4f}s")
    mostra("  loop aninhado n=200 → ~O(n²) comparações:", 200 * 200)
    mostra("  sort de n itens → O(n log n); len(lista):", len(lista))


# ---------------------------------------------------------------------------
# Registro de demos (nome da função → rótulo para filtro)
# ---------------------------------------------------------------------------

DEMOS: list[tuple[str, Callable[[], None]]] = [
    ("tipos", demo_tipos_primitivos),
    ("aritmetico", demo_operadores_aritmeticos),
    ("logico", demo_operadores_logicos_comparacao),
    ("identidade", demo_identidade_pertinencia),
    ("controle", demo_controle_fluxo),
    ("excecoes", demo_excecoes_contexto),
    ("return", demo_retorno_funcao),
    ("lista", demo_lista_tupla_set_dict),
    ("array", demo_array_matriz),
    ("ligada_simples", demo_lista_ligada_simples),
    ("fila", demo_fila_deque_heap_pilha),
    ("grafo", demo_arvore_grafo),
    ("bitwise", demo_bitwise_walrus_unarios),
    ("slice", demo_delimitadores_slice),
    ("unpack", demo_args_unpacking),
    ("strings", demo_strings_literals),
    ("lambda", demo_lambda_yield_assert),
    ("precedencia", demo_precedencia),
    ("bigo", demo_big_o),
    ("pilares", demo_pilares),
    ("paradigmas", demo_paradigmas),
    ("sintaxe", demo_sintaxe_avancada),
    ("modelo", demo_modelo_dados),
    ("lista_av", demo_lista_avancada),
    ("tupla", demo_tupla_avancada),
    ("arrays", demo_arrays_tipos),
    ("linked", demo_linked_list),
    ("dict", demo_dict_set_collections),
    ("funcoes", demo_funcoes),
    ("oop", demo_oop),
    ("dataclass", demo_dataclass_protocol),
    ("iterador", demo_iteradores_geradores),
    ("comprehension", demo_comprehensions),
    ("context", demo_excecoes_cm),
    ("decorator", demo_decorators),
    ("types", demo_type_hints),
    ("async", demo_asyncio),
    ("dunder", demo_dunder),
    ("dis", demo_dis_runtime),
    ("exercicios", demo_armadilhas_exercicios),
    ("pathlib", demo_pathlib_operadores_sequencia),
    ("copy", demo_copia_profunda),
    ("assinatura", demo_soma_path_operadores),
]


def main(argv: list[str] | None = None) -> None:
    argv = argv if argv is not None else sys.argv[1:]
    filtro = " ".join(argv).lower().strip()
    print("=" * 72)
    print("  base.py — exemplos README.md + readme.md")
    if filtro:
        print(f"  filtro: {filtro!r}")
    print("=" * 72)
    for nome, fn in DEMOS:
        if filtro and filtro not in nome and all(p not in nome for p in filtro.split()):
            continue
        fn()
    print("\n" + "=" * 72)
    print("  Fim dos demos.")
    print("=" * 72)


if __name__ == "__main__":
    main()
