"""
Logica junior 66 — Somar matriz

Some todos os inteiros. Matriz vazia vale 0. Linhas de tamanhos diferentes levantam ValueError.

Como testar:
    python3 logica/junior/66_soma_matriz.py
"""

def soma_matriz(matriz: list[list[int]]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = soma_matriz([[1, 2], [3, 4]])
    _verificar(veio == 10, f"soma_matriz([[1, 2], [3, 4]]) -> 10, veio {veio!r}", falhas)
    veio = soma_matriz([])
    _verificar(veio == 0, f"soma_matriz([]) -> 0, veio {veio!r}", falhas)
    veio = soma_matriz([[]])
    _verificar(veio == 0, f"soma_matriz([[]]) -> 0, veio {veio!r}", falhas)
    veio = soma_matriz([[5]])
    _verificar(veio == 5, f"soma_matriz([[5]]) -> 5, veio {veio!r}", falhas)
    try:
        soma_matriz([[1, 2], [3]])
        _verificar(False, "soma_matriz([[1, 2], [3]]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "soma_matriz([[1, 2], [3]]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

