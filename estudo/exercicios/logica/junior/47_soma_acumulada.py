"""
Logica junior 47 — Soma acumulada

Cada posicao guarda a soma desde o inicio ate ela.

Como testar:
    python3 logica/junior/47_soma_acumulada.py
"""

def soma_acumulada(nums: list[int]) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = soma_acumulada([1, 2, 3])
    _verificar(veio == [1, 3, 6], f"soma_acumulada([1, 2, 3]) -> [1, 3, 6], veio {veio!r}", falhas)
    veio = soma_acumulada([])
    _verificar(veio == [], f"soma_acumulada([]) -> [], veio {veio!r}", falhas)
    veio = soma_acumulada([5, -2])
    _verificar(veio == [5, 3], f"soma_acumulada([5, -2]) -> [5, 3], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

