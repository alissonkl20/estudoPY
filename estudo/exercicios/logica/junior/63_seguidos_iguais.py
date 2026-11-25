"""
Logica junior 63 — Seguidos iguais

Verdadeiro se dois itens vizinhos forem iguais. Lista curta e falsa.

Como testar:
    python3 logica/junior/63_seguidos_iguais.py
"""

def seguidos_iguais(itens: list) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = seguidos_iguais([1, 2, 2])
    _verificar(veio == True, f"seguidos_iguais([1, 2, 2]) -> True, veio {veio!r}", falhas)
    veio = seguidos_iguais([1, 2, 1])
    _verificar(veio == False, f"seguidos_iguais([1, 2, 1]) -> False, veio {veio!r}", falhas)
    veio = seguidos_iguais([])
    _verificar(veio == False, f"seguidos_iguais([]) -> False, veio {veio!r}", falhas)
    veio = seguidos_iguais([5])
    _verificar(veio == False, f"seguidos_iguais([5]) -> False, veio {veio!r}", falhas)
    veio = seguidos_iguais(['a', 'a'])
    _verificar(veio == True, f"seguidos_iguais(['a', 'a']) -> True, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

