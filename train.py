"""
Treino de lógica e Python — básico → avançado → especialista (+ estilo LeetCode).

Implemente cada função marcada com ``raise NotImplementedError``.
Quando estiver pronta, rode os testes:

  python3 train.py             # lista exercícios + roda todos os testes possíveis
  python train.py list           # só lista
  python train.py basico         # testa nível básico
  python train.py leetcode       # só tag leetcode
  python train.py b001           # um exercício
  python train.py run avancado   # alias: testa avançado

Materiais: readme.md · README.md · ESTUDO.md · base.py (exemplos)
"""

from __future__ import annotations

from re import match
import sys
from dataclasses import dataclass
from typing import Any, Callable, Iterable
from unittest import case

# =============================================================================
# NÍVEL BÁSICO — LÓGICA
# =============================================================================


def b001_soma_1_a_n(n: int) -> int:
    """Retorna 1 + 2 + … + n. Para n <= 0, retorne 0."""
    if n <= 0:
        return 0
    return n + b001_soma_1_a_n(n - 1)


def b002_par_ou_impar(n: int) -> str:
    if n % 2 == 0:
        return "par"
    else:
        return "impar"
       


def b003_maximo_de_tres(a: int, b: int, c: int) -> int:
    """Maior dos três inteiros (sem usar max())."""
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def b004_fizzbuzz(n: int) -> list[str]:
    """
    Para i de 1..n, append:
    'FizzBuzz' se múltiplo de 3 e 5, 'Fizz' se 3, 'Buzz' se 5, senão str(i).
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
    


def b005_inverter_string(s: str) -> str:
    """Inverte s (pode usar slice [::-1] ou loop)."""
    return s[::-1]
    return s


def b006_contar_vogais(s: str) -> int:
    """Conta a,e,i,o,u (maiúsculas/minúsculas)."""
    count = 0  
    for char in s:
        if char.lower() in "aeiou":
            count += 1
    return count




def b007_soma_digitos(n: int) -> int:
    """Soma dos dígitos de n (n >= 0). Ex.: 123 -> 6."""
    sum = 0 
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


def b008_primo(n: int) -> bool:
    """True se n >= 2 e primo."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def b009_fatorial(n: int) -> int:
    """n! para n >= 0; 0! = 1."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



def b010_palindromo(s: str) -> bool:
    """True se s é palíndromo (ignore espaços e case). Ex.: 'Ana' -> True."""
    x = s.lower().replace(" ", "")

    match x == x[::-1]:
        case True:
            return True
        case False:
            return False


def b011_segundo_maior(xs: list[int]) -> int | None:
    """Segundo maior valor distinto, ou None se não existir."""
    xs = set(xs)
    if len(xs) < 2:
        return None
    return sorted(xs)[-2]


def b012_collatz_passos(n: int) -> int:
    """
    Sequência: n -> n/2 se par, senão 3n+1. Quantos passos até chegar em 1?
    Ex.: n=3 -> 4 passos (3,10,5,16,8,4,2,1) -> 7? actually 3->10->5->16->8->4->2->1 = 7 steps
    Para n=1 retorne 0.
    """
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

## feito ##

# =============================================================================
# NÍVEL BÁSICO — PYTHON (tipos, coleções, funções)
# =============================================================================


def b101_media(xs: list[float]) -> float:
    """Média aritmética; lista vazia -> 0.0."""
    if len(xs) == 0:
        return 0.0
    return sum(xs) / len(xs)


def b102_maior_menor(xs: list[int]) -> tuple[int | None, int | None]:
    """(maior, menor) ou (None, None) se vazia."""
    if len(xs) == 0:
        return None, None
    return max(xs), min(xs)



def b103_remover_duplicatas(xs: list) -> list:
    """Remove duplicatas mantendo a primeira ocorrência."""
    return list(set(xs))


def b104_contagem(xs: list) -> dict:
    """Frequência de cada elemento (como Counter manual)."""
    result = {}
    for i in range(len(xs)):
        if xs[i] in result:
            result[xs[i]] += 1
        else:
            result[xs[i]] = 1
    return result


def b105_merge_ordenadas(a: list[int], b: list[int]) -> list[int]:
    """Merge de duas listas já ordenadas em uma ordenada."""
    return sorted(a + b)


def b106_matriz_transposta(m: list[list[int]]) -> list[list[int]]:
    """Transpõe matriz retangular (linhas viram colunas)."""
    return [list(row) for row in zip(*m)]


def b107_chunk(xs: list, tamanho: int) -> list[list]:
    """Divide xs em pedaços de tamanho (último pode ser menor). tamanho<=0 -> []."""
    return [xs[i:i+tamanho] for i in range(0, len(xs), tamanho)]


def b108_zip_soma(a: list[int], b: list[int]) -> list[int]:
    """Soma elemento a elemento até o menor comprimento."""
    return [x + y for x, y in zip(a, b)]


# =============================================================================
# NÍVEL BÁSICO — ESTRUTURAS (pilha, fila, conjunto)
# =============================================================================


def b201_parenteses_validos(s: str) -> bool:
    """True se (), [], {} estão balanceados. Ex.: '([])' True, '([)]' False."""
    stack = []
    t = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in t.values():
            stack.append(char)
        elif char in t.keys():
            if not stack or stack[-1] != t[char]:
                return False
            stack.pop()
    return not stack


def b202_fila_simulada(ops: list[str]) -> list[int]:
    """
    ops: 'E x' enfileira x, 'D' desenfileira (ignora se vazia).
    Retorna lista do que foi desenfileirado, na ordem.
    """
    queue = []
    result = []
    for op in ops:
        if op.startswith("E"):
            _, x = op.split()
            queue.append(int(x))
        elif op == "D":
            if queue:
                result.append(queue.pop(0))
    return result


def b203_intersecao(a: list, b: list) -> list:
    """Elementos em a e b, sem repetir, ordem da primeira aparição em a."""
    return list(set(a) & set(b))


# =============================================================================
# NÍVEL AVANÇADO — LÓGICA + ALGORITMOS
# =============================================================================


def a001_busca_binaria(xs: list[int], alvo: int) -> int:
    """Índice de alvo em xs ordenada, ou -1. O(log n)."""
    E, D = 0, len(xs) - 1
    while E <= D:
        mid = (E + D) // 2
        if xs[mid] == alvo:
            return mid
        elif xs[mid] < alvo:
            E = mid + 1
        else:
            D = mid - 1
    return -1


def a002_dois_soma(xs: list[int], alvo: int) -> tuple[int, int] | None:
    """Índices i,j com xs[i]+xs[j]==alvo, i<j. None se não existir. O(n) com dict."""
    s = {}
    for i, num in enumerate(xs):
        complement = alvo - num
        if complement in s:
            return (s[complement], i)
        s[num] = i
    return None


def a003_anagrama(a: str, b: str) -> bool:
    """True se mesmas letras (ignore espaços e case)."""
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    return sorted(a) == sorted(b)


def a004_maior_substring_sem_repetir(s: str) -> int:
    i




def a005_ordenar_contagem(xs: list[int]) -> list[int]:
    """Ordena inteiros não negativos com contagem (O(n+k)), sem .sort()."""
    raise NotImplementedError


def a006_flatten(xs: list) -> list:
    """Achata listas aninhadas um nível: [1,[2,3],4] -> [1,2,3,4]."""
    raise NotImplementedError


def a007_fibonacci(n: int) -> int:
    """n-ésimo Fibonacci (0-index: F0=0, F1=1) em O(n) tempo, O(1) espaço."""
    raise NotImplementedError


def a008_produto_exceto_self(xs: list[int]) -> list[int]:
    """Lista onde out[i] = produto de todos exceto xs[i]. Sem divisão."""
    raise NotImplementedError


def a009_rotacionar_lista(xs: list, k: int) -> list:
    """Rotaciona à direita k posições. Ex.: [1,2,3], k=1 -> [3,1,2]."""
    raise NotImplementedError


def a010_bfs_menor_caminho(
    grafo: dict[str, list[str]], h: str, fim: str
) -> int | None:
    """
    Menor número de arestas em grafo não ponderado.
    None se fim inalcançável.
    """
    raise NotImplementedError


def a011_k_maiores(xs: list[int], k: int) -> list[int]:
    """k maiores valores em ordem decrescente (use heapq ou sort)."""
    raise NotImplementedError


def a012_lru_manual_get_put(
    capacidade: int, operacoes: list[tuple[str, Any]]
) -> list[Any]:
    """
    Simula LRU: ops ('put', chave, valor) e ('get', chave).
    get retorna valor ou -1; retorne lista dos resultados de cada get.
    """
    raise NotImplementedError


# =============================================================================
# NÍVEL AVANÇADO — PYTHON (OOP, geradores, comprehensions)
# =============================================================================


class Retangulo:
    def __init__(self, largura: float, altura: float) -> None:
        self.largura = largura
        self.altura = altura

    def area(self) -> float:
        raise NotImplementedError


def _gerador_pares_interno(n: int) -> Iterable[int]:
    """Gera inteiros pares em [0, n). Ex.: n=5 -> 0, 2, 4."""
    raise NotImplementedError


def a102_gerador_pares(n: int) -> list[int]:
    """Retorne list(_gerador_pares_interno(n))."""
    raise NotImplementedError


def a103_decorador_repetir(n: int) -> Callable:
    """Decorator que executa a função n vezes e retorna o último resultado."""
    raise NotImplementedError


# =============================================================================
# LEETCODE — FÁCIL (referência de padrão, não cópia oficial)
# =============================================================================


def lc001_two_sum(nums: list[int], target: int) -> list[int]:
    """LC 1 — índices dos dois números que somam target."""
    raise NotImplementedError


def lc009_palindrome_number(n: int) -> bool:
    """LC 9 — inteiro é palíndromo?"""
    raise NotImplementedError


def lc013_roman_to_int(s: str) -> int:
    """LC 13 — romano para int (I,V,X,L,C,D,M)."""
    raise NotImplementedError


def lc020_valid_parentheses(s: str) -> bool:
    """LC 20 — mesmo que b201."""
    raise NotImplementedError


def lc026_remove_duplicates_sorted(nums: list[int]) -> int:
    """
    LC 26 — nums ordenado in-place; retorne novo comprimento dos únicos.
    Primeiros k elementos devem ser os únicos.
    """
    raise NotImplementedError


def lc053_max_subarray(nums: list[int]) -> int:
    """LC 53 — maior soma de subarray contínuo (Kadane)."""
    raise NotImplementedError


def lc070_climbing_stairs(n: int) -> int:
    """LC 70 — formas de subir n degraus (1 ou 2 por vez)."""
    raise NotImplementedError


def lc121_best_time_stock(prices: list[int]) -> int:
    """LC 121 — lucro máximo comprando antes de vender (uma transação)."""
    raise NotImplementedError


def lc125_valid_palindrome(s: str) -> bool:
    """LC 125 — palíndromo só alfanumérico, ignore case."""
    raise NotImplementedError


def lc217_contains_duplicate(nums: list[int]) -> bool:
    """LC 217 — existe duplicata?"""
    raise NotImplementedError


# =============================================================================
# LEETCODE — MÉDIO
# =============================================================================


def lc003_longest_substring(s: str) -> int:
    """LC 3 — igual a004."""
    raise NotImplementedError


def lc015_3sum(nums: list[int]) -> list[list[int]]:
    """LC 15 — triplas únicas que somam 0 (ordem dos trios não importa)."""
    raise NotImplementedError


def lc049_group_anagrams(strs: list[str]) -> list[list[str]]:
    """LC 49 — agrupa anagramas."""
    raise NotImplementedError


def lc056_merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """LC 56 — merge intervalos sobrepostos [[1,3],[2,6]] -> [[1,6]]."""
    raise NotImplementedError


def lc238_product_except_self(nums: list[int]) -> list[int]:
    """LC 238 — igual a008."""
    raise NotImplementedError


def lc347_top_k_frequent(nums: list[int], k: int) -> list[int]:
    """LC 347 — k elementos mais frequentes (qualquer ordem entre eles)."""
    raise NotImplementedError


def lc424_longest_repeating_char_replace(s: str, k: int) -> int:
    """
    LC 424 — maior substring onde pode trocar até k chars para ficarem iguais.
    """
    raise NotImplementedError


# =============================================================================
# ESPECIALISTA — GRAFOS, ÁRVORES, DESIGN
# =============================================================================


def e001_num_ilhas(grid: list[list[str]]) -> int:
    """
    LC 200 — grid '1' terra '0' água; conta componentes conectados (4 direções).
    """
    raise NotImplementedError


def e002_inorder_traversal(root: dict | None) -> list[int]:
    """
    Árvore binária como dict: {'v': int, 'l': esq, 'r': dir} ou None.
    Percursão in-order.
    """
    raise NotImplementedError


def e003_lca_bst(root: dict | None, p: int, q: int) -> int | None:
    """LC 235 — LCA em BST representada como dict (v,l,r)."""
    raise NotImplementedError


def e004_median_two_sorted_arrays(a: list[int], b: list[int]) -> float:
    """LC 4 — mediana de dois arrays ordenados (desafio O(log(m+n)))."""
    raise NotImplementedError


def e005_trapping_rain_water(height: list[int]) -> int:
    """LC 42 — água presa entre barras."""
    raise NotImplementedError


def e006_serialize_btree(root: dict | None) -> str:
    """Serializa árvore dict para string e e007 deserializa."""
    raise NotImplementedError


def e007_deserialize_btree(data: str) -> dict | None:
    raise NotImplementedError


def e008_word_ladder_length(begin: str, end: str, word_list: list[str]) -> int:
    """LC 127 — menor cadeia de palavras mudando 1 letra; 0 se impossível."""
    raise NotImplementedError


# =============================================================================
# REGISTRO E TESTES
# =============================================================================


@dataclass(frozen=True)
class Exercise:
    key: str
    nivel: str  # basico | avancado | especialista
    tags: tuple[str, ...]  # logica | python | estruturas | leetcode | grafos
    titulo: str
    func: Callable[..., Any]


def _test_b001() -> None:
    assert b001_soma_1_a_n(5) == 15
    assert b001_soma_1_a_n(0) == 0
    assert b001_soma_1_a_n(-3) == 0


def _test_b002() -> None:
    assert b002_par_ou_impar(4) == "par"
    assert b002_par_ou_impar(7) == "impar"


def _test_b003() -> None:
    assert b003_maximo_de_tres(1, 2, 3) == 3
    assert b003_maximo_de_tres(-1, -5, -2) == -1


def _test_b004() -> None:
    assert b004_fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def _test_b005() -> None:
    assert b005_inverter_string("abc") == "cba"


def _test_b006() -> None:
    assert b006_contar_vogais("Hello") == 2


def _test_b007() -> None:
    assert b007_soma_digitos(123) == 6


def _test_b008() -> None:
    assert b008_primo(2) and b008_primo(17) and not b008_primo(1)


def _test_b009() -> None:
    assert b009_fatorial(5) == 120 and b009_fatorial(0) == 1


def _test_b010() -> None:
    assert b010_palindromo("Ana") and not b010_palindromo("ab")


def _test_b011() -> None:
    assert b011_segundo_maior([1, 3, 2]) == 2
    assert b011_segundo_maior([5, 5, 5]) is None


def _test_b012() -> None:
    assert b012_collatz_passos(1) == 0
    assert b012_collatz_passos(3) == 7


def _test_b101() -> None:
    assert b101_media([2, 4]) == 3.0
    assert b101_media([]) == 0.0


def _test_b102() -> None:
    assert b102_maior_menor([1, 5, 2]) == (5, 1)
    assert b102_maior_menor([]) == (None, None)


def _test_b103() -> None:
    assert b103_remover_duplicatas([1, 2, 1, 3]) == [1, 2, 3]


def _test_b104() -> None:
    assert b104_contagem(["a", "b", "a"]) == {"a": 2, "b": 1}


def _test_b105() -> None:
    assert b105_merge_ordenadas([1, 3], [2, 4]) == [1, 2, 3, 4]


def _test_b106() -> None:
    assert b106_matriz_transposta([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]


def _test_b107() -> None:
    assert b107_chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def _test_b108() -> None:
    assert b108_zip_soma([1, 2], [10, 20, 30]) == [11, 22]


def _test_b201() -> None:
    assert b201_parenteses_validos("()[]{}")
    assert not b201_parenteses_validos("(]")


def _test_b202() -> None:
    out = b202_fila_simulada(["E 1", "E 2", "D", "E 3", "D", "D"])
    assert out == [1, 2, 3]


def _test_b203() -> None:
    assert b203_intersecao([1, 2, 2, 3], [2, 4]) == [2]


def _test_a001() -> None:
    assert a001_busca_binaria([1, 3, 5, 7], 5) == 2
    assert a001_busca_binaria([1, 3, 5, 7], 4) == -1


def _test_a002() -> None:
    assert a002_dois_soma([2, 7, 11, 15], 9) == (0, 1)


def _test_a003() -> None:
    assert a003_anagrama("listen", "silent")


def _test_a004() -> None:
    assert a004_maior_substring_sem_repetir("abcabcbb") == 3


def _test_a005() -> None:
    assert a005_ordenar_contagem([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]


def _test_a006() -> None:
    assert a006_flatten([1, [2, 3], 4]) == [1, 2, 3, 4]


def _test_a007() -> None:
    assert a007_fibonacci(10) == 55


def _test_a008() -> None:
    assert a008_produto_exceto_self([1, 2, 3, 4]) == [24, 12, 8, 6]


def _test_a009() -> None:
    assert a009_rotacionar_lista([1, 2, 3], 1) == [3, 1, 2]


def _test_a010() -> None:
    g = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
    assert a010_bfs_menor_caminho(g, "A", "D") == 2
    assert a010_bfs_menor_caminho(g, "A", "C") == 1


def _test_a011() -> None:
    assert a011_k_maiores([3, 1, 4, 1, 5], 2) == [5, 4]


def _test_a012() -> None:
    ops = [
        ("put", 1, 1),
        ("put", 2, 2),
        ("get", 1),
        ("put", 3, 3),
        ("get", 2),
        ("put", 4, 4),
        ("get", 1),
        ("get", 3),
        ("get", 4),
    ]
    assert a012_lru_manual_get_put(2, ops) == [1, -1, -1, 3, 4]


def _test_a101() -> None:
    r = Retangulo(3, 4)
    assert r.area() == 12


def _test_a102() -> None:
    assert a102_gerador_pares(5) == [0, 2, 4]
    assert list(_gerador_pares_interno(4)) == [0, 2]


def _test_a103() -> None:
    @a103_decorador_repetir(3)
    def soma1() -> int:
        soma1.c = getattr(soma1, "c", 0) + 1
        return soma1.c

    assert soma1() == 3


def _test_lc001() -> None:
    r = lc001_two_sum([2, 7, 11, 15], 9)
    assert sorted(r) == [0, 1]


def _test_lc009() -> None:
    assert lc009_palindrome_number(121)
    assert not lc009_palindrome_number(12)


def _test_lc013() -> None:
    assert lc013_roman_to_int("III") == 3
    assert lc013_roman_to_int("LVIII") == 58


def _test_lc020() -> None:
    assert lc020_valid_parentheses("()")


def _test_lc026() -> None:
    nums = [1, 1, 2]
    k = lc026_remove_duplicates_sorted(nums)
    assert k == 2 and nums[:2] == [1, 2]


def _test_lc053() -> None:
    assert lc053_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def _test_lc070() -> None:
    assert lc070_climbing_stairs(3) == 3


def _test_lc121() -> None:
    assert lc121_best_time_stock([7, 1, 5, 3, 6, 4]) == 5


def _test_lc125() -> None:
    assert lc125_valid_palindrome("A man, a plan, a canal: Panama")


def _test_lc217() -> None:
    assert lc217_contains_duplicate([1, 2, 3, 1])


def _test_lc003() -> None:
    assert lc003_longest_substring("abcabcbb") == 3


def _test_lc015() -> None:
    r = lc015_3sum([-1, 0, 1, 2, -1, -4])
    assert sorted([sorted(t) for t in r]) == [[-1, -1, 2], [-1, 0, 1]]


def _test_lc049() -> None:
    r = lc049_group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted([sorted(g) for g in r]) == [
        ["ate", "eat", "tea"],
        ["bat"],
        ["nat", "tan"],
    ]


def _test_lc056() -> None:
    assert lc056_merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]


def _test_lc238() -> None:
    assert lc238_product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]


def _test_lc347() -> None:
    r = lc347_top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    assert sorted(r) == [1, 2]


def _test_lc424() -> None:
    assert lc424_longest_repeating_char_replace("ABAB", 2) == 4


def _test_e001() -> None:
    grid = [
        ["1", "1", "0"],
        ["1", "0", "0"],
        ["0", "0", "1"],
    ]
    assert e001_num_ilhas(grid) == 2


def _test_e002() -> None:
    tree = {"v": 2, "l": {"v": 1, "l": None, "r": None}, "r": {"v": 3, "l": None, "r": None}}
    assert e002_inorder_traversal(tree) == [1, 2, 3]


def _test_e003() -> None:
    tree = {
        "v": 6,
        "l": {"v": 2, "l": {"v": 0, "l": None, "r": None}, "r": {"v": 4, "l": None, "r": None}},
        "r": {"v": 8, "l": None, "r": {"v": 10, "l": None, "r": None}},
    }
    assert e003_lca_bst(tree, 2, 4) == 2


def _test_e004() -> None:
    assert e004_median_two_sorted_arrays([1, 3], [2]) == 2.0


def _test_e005() -> None:
    assert e005_trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def _test_e006_e007() -> None:
    tree = {"v": 1, "l": {"v": 2, "l": None, "r": None}, "r": None}
    s = e006_serialize_btree(tree)
    back = e007_deserialize_btree(s)
    assert e002_inorder_traversal(back) == [2, 1]


def _test_e008() -> None:
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert e008_word_ladder_length("hit", "cog", words) == 5


EXERCISES: list[tuple[Exercise, Callable[[], None]]] = [
    (Exercise("b001", "basico", ("logica",), "Soma 1..n", b001_soma_1_a_n), _test_b001),
    (Exercise("b002", "basico", ("logica",), "Par ou ímpar", b002_par_ou_impar), _test_b002),
    (Exercise("b003", "basico", ("logica",), "Máximo de três", b003_maximo_de_tres), _test_b003),
    (Exercise("b004", "basico", ("logica",), "FizzBuzz", b004_fizzbuzz), _test_b004),
    (Exercise("b005", "basico", ("logica",), "Inverter string", b005_inverter_string), _test_b005),
    (Exercise("b006", "basico", ("logica",), "Contar vogais", b006_contar_vogais), _test_b006),
    (Exercise("b007", "basico", ("logica",), "Soma dos dígitos", b007_soma_digitos), _test_b007),
    (Exercise("b008", "basico", ("logica",), "É primo?", b008_primo), _test_b008),
    (Exercise("b009", "basico", ("logica",), "Fatorial", b009_fatorial), _test_b009),
    (Exercise("b010", "basico", ("logica",), "Palíndromo", b010_palindromo), _test_b010),
    (Exercise("b011", "basico", ("logica",), "Segundo maior", b011_segundo_maior), _test_b011),
    (Exercise("b012", "basico", ("logica",), "Passos Collatz", b012_collatz_passos), _test_b012),
    (Exercise("b101", "basico", ("python",), "Média da lista", b101_media), _test_b101),
    (Exercise("b102", "basico", ("python",), "Maior e menor", b102_maior_menor), _test_b102),
    (Exercise("b103", "basico", ("python",), "Remover duplicatas", b103_remover_duplicatas), _test_b103),
    (Exercise("b104", "basico", ("python",), "Contagem manual", b104_contagem), _test_b104),
    (Exercise("b105", "basico", ("python",), "Merge ordenadas", b105_merge_ordenadas), _test_b105),
    (Exercise("b106", "basico", ("python",), "Transposta", b106_matriz_transposta), _test_b106),
    (Exercise("b107", "basico", ("python",), "Chunk lista", b107_chunk), _test_b107),
    (Exercise("b108", "basico", ("python",), "Zip soma", b108_zip_soma), _test_b108),
    (Exercise("b201", "basico", ("estruturas",), "Parênteses válidos", b201_parenteses_validos), _test_b201),
    (Exercise("b202", "basico", ("estruturas",), "Simular fila", b202_fila_simulada), _test_b202),
    (Exercise("b203", "basico", ("estruturas",), "Interseção", b203_intersecao), _test_b203),
    (Exercise("a001", "avancado", ("algoritmos",), "Busca binária", a001_busca_binaria), _test_a001),
    (Exercise("a002", "avancado", ("algoritmos",), "Dois soma", a002_dois_soma), _test_a002),
    (Exercise("a003", "avancado", ("algoritmos",), "Anagrama", a003_anagrama), _test_a003),
    (Exercise("a004", "avancado", ("algoritmos",), "Substring sem repetir", a004_maior_substring_sem_repetir), _test_a004),
    (Exercise("a005", "avancado", ("algoritmos",), "Sort por contagem", a005_ordenar_contagem), _test_a005),
    (Exercise("a006", "avancado", ("python",), "Flatten 1 nível", a006_flatten), _test_a006),
    (Exercise("a007", "avancado", ("algoritmos",), "Fibonacci O(n)", a007_fibonacci), _test_a007),
    (Exercise("a008", "avancado", ("algoritmos",), "Produto exceto self", a008_produto_exceto_self), _test_a008),
    (Exercise("a009", "avancado", ("python",), "Rotacionar lista", a009_rotacionar_lista), _test_a009),
    (Exercise("a010", "avancado", ("grafos",), "BFS distância", a010_bfs_menor_caminho), _test_a010),
    (Exercise("a011", "avancado", ("algoritmos",), "K maiores", a011_k_maiores), _test_a011),
    (Exercise("a012", "avancado", ("estruturas",), "LRU simulado", a012_lru_manual_get_put), _test_a012),
    (Exercise("a101", "avancado", ("python", "oop"), "Retangulo.area", Retangulo.area), _test_a101),
    (Exercise("a102", "avancado", ("python",), "Gerador pares", a102_gerador_pares), _test_a102),
    (Exercise("a103", "avancado", ("python",), "Decorator repetir", a103_decorador_repetir), _test_a103),
    (Exercise("lc001", "avancado", ("leetcode",), "LC 1 Two Sum", lc001_two_sum), _test_lc001),
    (Exercise("lc009", "basico", ("leetcode",), "LC 9 Palindrome Number", lc009_palindrome_number), _test_lc009),
    (Exercise("lc013", "basico", ("leetcode",), "LC 13 Roman to Int", lc013_roman_to_int), _test_lc013),
    (Exercise("lc020", "basico", ("leetcode",), "LC 20 Valid Parentheses", lc020_valid_parentheses), _test_lc020),
    (Exercise("lc026", "avancado", ("leetcode",), "LC 26 Remove Dup", lc026_remove_duplicates_sorted), _test_lc026),
    (Exercise("lc053", "avancado", ("leetcode",), "LC 53 Max Subarray", lc053_max_subarray), _test_lc053),
    (Exercise("lc070", "avancado", ("leetcode",), "LC 70 Climbing Stairs", lc070_climbing_stairs), _test_lc070),
    (Exercise("lc121", "avancado", ("leetcode",), "LC 121 Stock", lc121_best_time_stock), _test_lc121),
    (Exercise("lc125", "basico", ("leetcode",), "LC 125 Valid Palindrome", lc125_valid_palindrome), _test_lc125),
    (Exercise("lc217", "basico", ("leetcode",), "LC 217 Contains Dup", lc217_contains_duplicate), _test_lc217),
    (Exercise("lc003", "avancado", ("leetcode",), "LC 3 Longest Substring", lc003_longest_substring), _test_lc003),
    (Exercise("lc015", "especialista", ("leetcode",), "LC 15 3Sum", lc015_3sum), _test_lc015),
    (Exercise("lc049", "avancado", ("leetcode",), "LC 49 Group Anagrams", lc049_group_anagrams), _test_lc049),
    (Exercise("lc056", "avancado", ("leetcode",), "LC 56 Merge Intervals", lc056_merge_intervals), _test_lc056),
    (Exercise("lc238", "avancado", ("leetcode",), "LC 238 Product Except Self", lc238_product_except_self), _test_lc238),
    (Exercise("lc347", "avancado", ("leetcode",), "LC 347 Top K Frequent", lc347_top_k_frequent), _test_lc347),
    (Exercise("lc424", "especialista", ("leetcode",), "LC 424 Longest Repeating", lc424_longest_repeating_char_replace), _test_lc424),
    (Exercise("e001", "especialista", ("leetcode", "grafos"), "LC 200 Number of Islands", e001_num_ilhas), _test_e001),
    (Exercise("e002", "especialista", ("grafos",), "In-order traversal", e002_inorder_traversal), _test_e002),
    (Exercise("e003", "especialista", ("leetcode",), "LC 235 LCA BST", e003_lca_bst), _test_e003),
    (Exercise("e004", "especialista", ("leetcode",), "LC 4 Median Two Arrays", e004_median_two_sorted_arrays), _test_e004),
    (Exercise("e005", "especialista", ("leetcode",), "LC 42 Trapping Rain", e005_trapping_rain_water), _test_e005),
    (Exercise("e006", "especialista", ("estruturas",), "Serialize tree", e006_serialize_btree), _test_e006_e007),
    (Exercise("e008", "especialista", ("leetcode", "grafos"), "LC 127 Word Ladder", e008_word_ladder_length), _test_e008),
]


def list_exercises(filtro: str = "") -> None:
    f = filtro.lower()
    print(f"{'CHAVE':<8} {'NÍVEL':<12} {'TAGS':<24} TÍTULO")
    print("-" * 72)
    for ex, _ in EXERCISES:
        if f and f not in ex.key and f not in ex.nivel and not any(f in t for t in ex.tags):
            continue
        tags = ",".join(ex.tags)
        print(f"{ex.key:<8} {ex.nivel:<12} {tags:<24} {ex.titulo}")


def run_tests(filtro: str = "") -> int:
    f = filtro.lower().strip()
    ok = fail = skip = 0
    for ex, test_fn in EXERCISES:
        if f and f not in ex.key and f not in ex.nivel and not any(f in t for t in ex.tags):
            if f not in ("run", "test"):
                continue
        try:
            test_fn()
            print(f"  OK   {ex.key} — {ex.titulo}")
            ok += 1
        except NotImplementedError:
            print(f"  …    {ex.key} — pendente (implemente {ex.func.__name__})")
            skip += 1
        except AssertionError as e:
            print(f"  FAIL {ex.key} — {ex.titulo}: {e}")
            fail += 1
        except Exception as e:
            print(f"  ERR  {ex.key} — {ex.titulo}: {type(e).__name__}: {e}")
            fail += 1
    print("-" * 72)
    print(f"Resumo: {ok} ok, {fail} falha(s), {skip} pendente(s)")
    return 0 if fail == 0 else 1


def main(argv: list[str] | None = None) -> None:
    argv = argv if argv is not None else sys.argv[1:]
    cmd = argv[0].lower() if argv else ""
    filtro = " ".join(argv[1:]) if cmd in ("list", "run") else " ".join(argv)
    if cmd in ("", "run", "test"):
        if not argv or cmd in ("run", "test"):
            filtro_run = filtro
        else:
            filtro_run = " ".join(argv)
        print("=" * 72)
        print("  train.py — treino de lógica e Python")
        print("=" * 72)
        list_exercises(filtro_run)
        print()
        run_tests(filtro_run)
    elif cmd == "list":
        list_exercises(filtro)
    else:
        print("=" * 72)
        print("  train.py — treino de lógica e Python")
        print("=" * 72)
        list_exercises(cmd)
        print()
        run_tests(cmd)


if __name__ == "__main__":
    raise SystemExit(main())
