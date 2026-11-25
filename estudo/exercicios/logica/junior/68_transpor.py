"""
Logica junior 68 — Transpor matriz

Troque linhas por colunas. Matriz vazia devolve []. Linhas de tamanhos diferentes levantam ValueError.

Como testar:
    python3 logica/junior/68_transpor.py
"""

def transpor(matriz: list[list[int]]) -> list[list[int]]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = transpor([[1, 2, 3], [4, 5, 6]])
    _verificar(veio == [[1, 4], [2, 5], [3, 6]], f"transpor([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]], veio {veio!r}", falhas)
    veio = transpor([])
    _verificar(veio == [], f"transpor([]) -> [], veio {veio!r}", falhas)
    veio = transpor([[1]])
    _verificar(veio == [[1]], f"transpor([[1]]) -> [[1]], veio {veio!r}", falhas)
    try:
        transpor([[1, 2], [3]])
        _verificar(False, "transpor([[1, 2], [3]]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "transpor([[1, 2], [3]]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

