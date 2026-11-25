"""
Logica junior 37 — Contar uma letra

Conte sem diferenciar maiusculas. A letra precisa ter tamanho 1.

Como testar:
    python3 logica/junior/37_contar_letra.py
"""

def contar_letra(texto: str, letra: str) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = contar_letra('Abca', 'a')
    _verificar(veio == 2, f"contar_letra('Abca', 'a') -> 2, veio {veio!r}", falhas)
    veio = contar_letra('abc', 'z')
    _verificar(veio == 0, f"contar_letra('abc', 'z') -> 0, veio {veio!r}", falhas)
    veio = contar_letra('', 'a')
    _verificar(veio == 0, f"contar_letra('', 'a') -> 0, veio {veio!r}", falhas)
    try:
        contar_letra('abc', 'ab')
        _verificar(False, "contar_letra('abc', 'ab') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "contar_letra('abc', 'ab') levanta ValueError", falhas)
    try:
        contar_letra('abc', '')
        _verificar(False, "contar_letra('abc', '') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "contar_letra('abc', '') levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

