"""
Logica junior 56 — Par ou impar

Devolva "par" ou "impar". Zero e par. Negativo impar continua impar.

Como testar:
    python3 logica/junior/56_par_ou_impar.py
"""

def par_ou_impar(n: int) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = par_ou_impar(0)
    _verificar(veio == 'par', f"par_ou_impar(0) -> 'par', veio {veio!r}", falhas)
    veio = par_ou_impar(4)
    _verificar(veio == 'par', f"par_ou_impar(4) -> 'par', veio {veio!r}", falhas)
    veio = par_ou_impar(7)
    _verificar(veio == 'impar', f"par_ou_impar(7) -> 'impar', veio {veio!r}", falhas)
    veio = par_ou_impar(-3)
    _verificar(veio == 'impar', f"par_ou_impar(-3) -> 'impar', veio {veio!r}", falhas)
    veio = par_ou_impar(-2)
    _verificar(veio == 'par', f"par_ou_impar(-2) -> 'par', veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

