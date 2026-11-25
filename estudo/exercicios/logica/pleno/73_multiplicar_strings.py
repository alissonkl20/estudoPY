"""
Logica pleno 73 — Multiplicar numeros em texto

Os textos seguem a mesma regra da soma: digitos, sem zero a esquerda, exceto 0. Devolva o produto como texto.

Como testar:
    python3 logica/pleno/73_multiplicar_strings.py
"""

def multiplicar_strings(a: str, b: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = multiplicar_strings('12', '3')
    _verificar(veio == '36', f"multiplicar_strings('12', '3') -> '36', veio {veio!r}", falhas)
    veio = multiplicar_strings('123', '45')
    _verificar(veio == '5535', f"multiplicar_strings('123', '45') -> '5535', veio {veio!r}", falhas)
    veio = multiplicar_strings('0', '99')
    _verificar(veio == '0', f"multiplicar_strings('0', '99') -> '0', veio {veio!r}", falhas)
    try:
        multiplicar_strings('01', '2')
        _verificar(False, "multiplicar_strings('01', '2') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "multiplicar_strings('01', '2') levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

