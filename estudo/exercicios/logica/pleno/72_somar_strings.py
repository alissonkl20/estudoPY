"""
Logica pleno 72 — Somar numeros em texto

Os textos sao inteiros nao negativos, sem zero a esquerda, exceto o proprio 0. Devolva a soma como texto.

Como testar:
    python3 logica/pleno/72_somar_strings.py
"""

def somar_strings(a: str, b: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = somar_strings('11', '123')
    _verificar(veio == '134', f"somar_strings('11', '123') -> '134', veio {veio!r}", falhas)
    veio = somar_strings('999', '1')
    _verificar(veio == '1000', f"somar_strings('999', '1') -> '1000', veio {veio!r}", falhas)
    veio = somar_strings('0', '0')
    _verificar(veio == '0', f"somar_strings('0', '0') -> '0', veio {veio!r}", falhas)
    try:
        somar_strings('00', '1')
        _verificar(False, "somar_strings('00', '1') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "somar_strings('00', '1') levanta ValueError", falhas)
    try:
        somar_strings('', '1')
        _verificar(False, "somar_strings('', '1') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "somar_strings('', '1') levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

