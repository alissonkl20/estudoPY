"""
Logica pleno 22 — Formas de decodificar

1 vale A e 26 vale Z. Conte as formas. Um zero isolado nao forma letra. Texto vazio ou com nao digito levanta ValueError.

Como testar:
    python3 logica/pleno/22_formas_de_decodificar.py
"""

def formas_de_decodificar(texto: str) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = formas_de_decodificar('12')
    _verificar(veio == 2, f"formas_de_decodificar('12') -> 2, veio {veio!r}", falhas)
    veio = formas_de_decodificar('226')
    _verificar(veio == 3, f"formas_de_decodificar('226') -> 3, veio {veio!r}", falhas)
    veio = formas_de_decodificar('0')
    _verificar(veio == 0, f"formas_de_decodificar('0') -> 0, veio {veio!r}", falhas)
    veio = formas_de_decodificar('10')
    _verificar(veio == 1, f"formas_de_decodificar('10') -> 1, veio {veio!r}", falhas)
    veio = formas_de_decodificar('06')
    _verificar(veio == 0, f"formas_de_decodificar('06') -> 0, veio {veio!r}", falhas)
    try:
        formas_de_decodificar('')
        _verificar(False, "formas_de_decodificar('') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "formas_de_decodificar('') levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

