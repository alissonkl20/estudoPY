"""
Logica pleno 51 — Passos no labirinto

1 e chao e 0 e parede. Ande para cima, baixo, esquerda e direita. Devolva a quantidade de passos. Se nao der, -1. Começar na parede vale -1. Origem e destino iguais e livres valem 0.

Como testar:
    python3 logica/pleno/51_passos_labirinto.py
"""

def passos_labirinto(grade: list[list[int]], inicio: tuple[int, int], fim: tuple[int, int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = passos_labirinto([[1, 1, 1], [1, 0, 1], [1, 1, 1]], (0, 0), (2, 2))
    _verificar(veio == 4, f"passos_labirinto([[1, 1, 1], [1, 0, 1], [1, 1, 1]], (0, 0), (2, 2)) -> 4, veio {veio!r}", falhas)
    veio = passos_labirinto([[1]], (0, 0), (0, 0))
    _verificar(veio == 0, f"passos_labirinto([[1]], (0, 0), (0, 0)) -> 0, veio {veio!r}", falhas)
    veio = passos_labirinto([[0]], (0, 0), (0, 0))
    _verificar(veio == -1, f"passos_labirinto([[0]], (0, 0), (0, 0)) -> -1, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

