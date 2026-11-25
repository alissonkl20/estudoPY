"""
Logica junior 40 — Juntar textos

Junte os textos com o separador. Lista vazia devolve vazio. Item que nao e str levanta ValueError.

Como testar:
    python3 logica/junior/40_juntar.py
"""

def juntar(itens: list[str], separador: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = juntar(['a', 'b'], '-')
    _verificar(veio == 'a-b', f"juntar(['a', 'b'], '-') -> 'a-b', veio {veio!r}", falhas)
    veio = juntar([], '-')
    _verificar(veio == '', f"juntar([], '-') -> '', veio {veio!r}", falhas)
    veio = juntar(['so'], ',')
    _verificar(veio == 'so', f"juntar(['so'], ',') -> 'so', veio {veio!r}", falhas)
    try:
        juntar([1, 2], '-')
        _verificar(False, "juntar([1, 2], '-') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "juntar([1, 2], '-') levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

