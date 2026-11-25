"""
Logica pleno 13 — Caminhos na grade

Ande so para a direita ou para baixo, de (1, 1) ate (m, n). m ou n menor que 1 levanta ValueError.

Como testar:
    python3 logica/pleno/13_caminhos_grade.py
"""

def caminhos_grade(m: int, n: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = caminhos_grade(3, 2)
    _verificar(veio == 3, f"caminhos_grade(3, 2) -> 3, veio {veio!r}", falhas)
    veio = caminhos_grade(1, 1)
    _verificar(veio == 1, f"caminhos_grade(1, 1) -> 1, veio {veio!r}", falhas)
    veio = caminhos_grade(2, 2)
    _verificar(veio == 2, f"caminhos_grade(2, 2) -> 2, veio {veio!r}", falhas)
    veio = caminhos_grade(3, 7)
    _verificar(veio == 28, f"caminhos_grade(3, 7) -> 28, veio {veio!r}", falhas)
    try:
        caminhos_grade(0, 1)
        _verificar(False, "caminhos_grade(0, 1) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "caminhos_grade(0, 1) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

