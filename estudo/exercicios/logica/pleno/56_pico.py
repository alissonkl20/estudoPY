"""
Logica pleno 56 — Indice do pico

Devolva o indice do maior valor. Ele e estritamente maior que os vizinhos que existirem. Lista vazia levanta ValueError.

Como testar:
    python3 logica/pleno/56_pico.py
"""

def pico(nums: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = pico([1, 2, 3, 1])
    _verificar(veio == 2, f"pico([1, 2, 3, 1]) -> 2, veio {veio!r}", falhas)
    veio = pico([1, 2, 1, 3, 5, 6, 4])
    _verificar(veio == 5, f"pico([1, 2, 1, 3, 5, 6, 4]) -> 5, veio {veio!r}", falhas)
    veio = pico([1])
    _verificar(veio == 0, f"pico([1]) -> 0, veio {veio!r}", falhas)
    try:
        pico([])
        _verificar(False, "pico([]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "pico([]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

