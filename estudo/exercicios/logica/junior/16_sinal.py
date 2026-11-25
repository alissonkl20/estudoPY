"""
Logica junior 16 — Sinal do numero

Devolva "positivo", "negativo" ou "zero".

Como testar:
    python3 logica/junior/16_sinal.py
"""

def sinal(n: int) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = sinal(5)
    _verificar(veio == 'positivo', f"sinal(5) -> 'positivo', veio {veio!r}", falhas)
    veio = sinal(-2)
    _verificar(veio == 'negativo', f"sinal(-2) -> 'negativo', veio {veio!r}", falhas)
    veio = sinal(0)
    _verificar(veio == 'zero', f"sinal(0) -> 'zero', veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

