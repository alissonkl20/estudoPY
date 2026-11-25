"""
Logica junior 53 — Todos positivos

Verdadeiro se todo numero for maior que zero. Lista vazia e verdadeira. Zero nao e positivo.

Como testar:
    python3 logica/junior/53_todos_positivos.py
"""

def todos_positivos(nums: list[int]) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = todos_positivos([1, 2])
    _verificar(veio == True, f"todos_positivos([1, 2]) -> True, veio {veio!r}", falhas)
    veio = todos_positivos([1, 0])
    _verificar(veio == False, f"todos_positivos([1, 0]) -> False, veio {veio!r}", falhas)
    veio = todos_positivos([])
    _verificar(veio == True, f"todos_positivos([]) -> True, veio {veio!r}", falhas)
    veio = todos_positivos([-1])
    _verificar(veio == False, f"todos_positivos([-1]) -> False, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

