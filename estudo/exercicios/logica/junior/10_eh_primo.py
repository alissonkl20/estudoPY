"""
Logica junior 10 — Numero primo

2 e primo. 1, 0 e negativo nao sao.

Como testar:
    python3 logica/junior/10_eh_primo.py
"""

def eh_primo(n: int) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = eh_primo(2)
    _verificar(veio == True, f"eh_primo(2) -> True, veio {veio!r}", falhas)
    veio = eh_primo(1)
    _verificar(veio == False, f"eh_primo(1) -> False, veio {veio!r}", falhas)
    veio = eh_primo(9)
    _verificar(veio == False, f"eh_primo(9) -> False, veio {veio!r}", falhas)
    veio = eh_primo(13)
    _verificar(veio == True, f"eh_primo(13) -> True, veio {veio!r}", falhas)
    veio = eh_primo(0)
    _verificar(veio == False, f"eh_primo(0) -> False, veio {veio!r}", falhas)
    veio = eh_primo(-5)
    _verificar(veio == False, f"eh_primo(-5) -> False, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

