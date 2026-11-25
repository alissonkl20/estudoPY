"""
Logica pleno 39 — Indices de anagrama

Devolva os indices onde um anagrama de padrao comeca em texto. Padrao vazio devolve [].

Como testar:
    python3 logica/pleno/39_indices_anagrama.py
"""

def indices_anagrama(texto: str, padrao: str) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = indices_anagrama('cbaebabacd', 'abc')
    _verificar(veio == [0, 6], f"indices_anagrama('cbaebabacd', 'abc') -> [0, 6], veio {veio!r}", falhas)
    veio = indices_anagrama('abab', 'ab')
    _verificar(veio == [0, 1, 2], f"indices_anagrama('abab', 'ab') -> [0, 1, 2], veio {veio!r}", falhas)
    veio = indices_anagrama('', 'a')
    _verificar(veio == [], f"indices_anagrama('', 'a') -> [], veio {veio!r}", falhas)
    veio = indices_anagrama('a', '')
    _verificar(veio == [], f"indices_anagrama('a', '') -> [], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

