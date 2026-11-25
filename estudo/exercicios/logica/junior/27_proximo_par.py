"""
Logica junior 27 — Proximo par

Se n ja e par, devolva n. Senao devolva o proximo par na direcao positiva.

Como testar:
    python3 logica/junior/27_proximo_par.py
"""

def proximo_par(n: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = proximo_par(4)
    _verificar(veio == 4, f"proximo_par(4) -> 4, veio {veio!r}", falhas)
    veio = proximo_par(5)
    _verificar(veio == 6, f"proximo_par(5) -> 6, veio {veio!r}", falhas)
    veio = proximo_par(-3)
    _verificar(veio == -2, f"proximo_par(-3) -> -2, veio {veio!r}", falhas)
    veio = proximo_par(-4)
    _verificar(veio == -4, f"proximo_par(-4) -> -4, veio {veio!r}", falhas)
    veio = proximo_par(0)
    _verificar(veio == 0, f"proximo_par(0) -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

