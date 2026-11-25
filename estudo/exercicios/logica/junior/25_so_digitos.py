"""
Logica junior 25 — So digitos

Verdadeiro se o texto tiver ao menos um caractere e todos forem digitos.

Como testar:
    python3 logica/junior/25_so_digitos.py
"""

def so_digitos(texto: str) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = so_digitos('012')
    _verificar(veio == True, f"so_digitos('012') -> True, veio {veio!r}", falhas)
    veio = so_digitos('')
    _verificar(veio == False, f"so_digitos('') -> False, veio {veio!r}", falhas)
    veio = so_digitos('12a')
    _verificar(veio == False, f"so_digitos('12a') -> False, veio {veio!r}", falhas)
    veio = so_digitos('7')
    _verificar(veio == True, f"so_digitos('7') -> True, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

