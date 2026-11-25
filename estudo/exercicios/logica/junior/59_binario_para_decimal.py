"""
Logica junior 59 — Binario para decimal

Converta um texto de 0 e 1. Texto vazio ou com outro caractere levanta ValueError.

Como testar:
    python3 logica/junior/59_binario_para_decimal.py
"""

def binario_para_decimal(texto: str) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = binario_para_decimal('1010')
    _verificar(veio == 10, f"binario_para_decimal('1010') -> 10, veio {veio!r}", falhas)
    veio = binario_para_decimal('0')
    _verificar(veio == 0, f"binario_para_decimal('0') -> 0, veio {veio!r}", falhas)
    veio = binario_para_decimal('111')
    _verificar(veio == 7, f"binario_para_decimal('111') -> 7, veio {veio!r}", falhas)
    try:
        binario_para_decimal('')
        _verificar(False, "binario_para_decimal('') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "binario_para_decimal('') levanta ValueError", falhas)
    try:
        binario_para_decimal('102')
        _verificar(False, "binario_para_decimal('102') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "binario_para_decimal('102') levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

