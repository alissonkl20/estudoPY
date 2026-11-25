"""
Logica junior 72 — Distancia de Hamming

Conte as posicoes diferentes. Textos de tamanhos diferentes levantam ValueError.

Como testar:
    python3 logica/junior/72_hamming.py
"""

def hamming(a: str, b: str) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = hamming('karolin', 'kathrin')
    _verificar(veio == 3, f"hamming('karolin', 'kathrin') -> 3, veio {veio!r}", falhas)
    veio = hamming('abc', 'abc')
    _verificar(veio == 0, f"hamming('abc', 'abc') -> 0, veio {veio!r}", falhas)
    veio = hamming('', '')
    _verificar(veio == 0, f"hamming('', '') -> 0, veio {veio!r}", falhas)
    try:
        hamming('ab', 'a')
        _verificar(False, "hamming('ab', 'a') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "hamming('ab', 'a') levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

