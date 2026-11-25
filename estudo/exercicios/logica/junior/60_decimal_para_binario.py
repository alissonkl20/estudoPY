"""
Logica junior 60 — Decimal para binario

Converta um inteiro nao negativo para texto binario, sem o prefixo 0b. 0 vira "0". Negativo levanta ValueError.

Como testar:
    python3 logica/junior/60_decimal_para_binario.py
"""

def decimal_para_binario(n: int) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = decimal_para_binario(0)
    _verificar(veio == '0', f"decimal_para_binario(0) -> '0', veio {veio!r}", falhas)
    veio = decimal_para_binario(10)
    _verificar(veio == '1010', f"decimal_para_binario(10) -> '1010', veio {veio!r}", falhas)
    veio = decimal_para_binario(1)
    _verificar(veio == '1', f"decimal_para_binario(1) -> '1', veio {veio!r}", falhas)
    veio = decimal_para_binario(8)
    _verificar(veio == '1000', f"decimal_para_binario(8) -> '1000', veio {veio!r}", falhas)
    try:
        decimal_para_binario(-1)
        _verificar(False, "decimal_para_binario(-1) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "decimal_para_binario(-1) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

