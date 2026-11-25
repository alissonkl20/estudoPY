"""
Logica junior 18 — Lista ordenada

Verdadeiro se cada numero for menor ou igual ao proximo. Lista vazia e de um item sao ordenadas.

Como testar:
    python3 logica/junior/18_esta_ordenado.py
"""

def esta_ordenado(nums: list[int]) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = esta_ordenado([1, 2, 2, 3])
    _verificar(veio == True, f"esta_ordenado([1, 2, 2, 3]) -> True, veio {veio!r}", falhas)
    veio = esta_ordenado([1, 3, 2])
    _verificar(veio == False, f"esta_ordenado([1, 3, 2]) -> False, veio {veio!r}", falhas)
    veio = esta_ordenado([])
    _verificar(veio == True, f"esta_ordenado([]) -> True, veio {veio!r}", falhas)
    veio = esta_ordenado([5])
    _verificar(veio == True, f"esta_ordenado([5]) -> True, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

