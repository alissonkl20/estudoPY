"""
Logica pleno 01 — Maior soma contigua

Ache a maior soma de um trecho continuo. Se todos forem negativos, devolva o maior deles. Lista vazia levanta ValueError.

Como testar:
    python3 logica/pleno/01_maior_soma_contigua.py
"""

def maior_soma_contigua(nums: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = maior_soma_contigua([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    _verificar(veio == 6, f"maior_soma_contigua([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> 6, veio {veio!r}", falhas)
    veio = maior_soma_contigua([-1, -2])
    _verificar(veio == -1, f"maior_soma_contigua([-1, -2]) -> -1, veio {veio!r}", falhas)
    veio = maior_soma_contigua([5])
    _verificar(veio == 5, f"maior_soma_contigua([5]) -> 5, veio {veio!r}", falhas)
    try:
        maior_soma_contigua([])
        _verificar(False, "maior_soma_contigua([]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "maior_soma_contigua([]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

