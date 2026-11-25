"""
Logica pleno 47 — Frota de carros

Carros vao ate o alvo. Um mais rapido atras nao ultrapassa: entra na frota da frente. Devolva quantas frotas chegam. Listas de tamanhos diferentes levantam ValueError.

Como testar:
    python3 logica/pleno/47_frota.py
"""

def frota(alvo: int, posicao: list[int], velocidade: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = frota(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
    _verificar(veio == 3, f"frota(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) -> 3, veio {veio!r}", falhas)
    veio = frota(10, [0], [1])
    _verificar(veio == 1, f"frota(10, [0], [1]) -> 1, veio {veio!r}", falhas)
    veio = frota(10, [], [])
    _verificar(veio == 0, f"frota(10, [], []) -> 0, veio {veio!r}", falhas)
    try:
        frota(10, [0, 1], [1])
        _verificar(False, "frota(10, [0, 1], [1]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "frota(10, [0, 1], [1]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

