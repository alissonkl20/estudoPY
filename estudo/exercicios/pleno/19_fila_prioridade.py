"""
Teste tecnico 19 — Fila de prioridade

Nivel pleno. Numero menor sai primeiro. Empate de prioridade respeita
a ordem de chegada. Use heapq ou outra estrutura, desde que o contrato feche.

Implemente FilaPrioridade.

- adicionar(item, prioridade)
- prioridade e int (bool nao vale); senao ValueError
- proximo() devolve o item e tira da fila
- fila vazia em proximo() levanta ValueError
- len(fila) e a quantidade que ainda falta sair

Como testar:
    python3 pleno/19_fila_prioridade.py
"""


class FilaPrioridade:
    def adicionar(self, item, prioridade: int) -> None:
        return None

    def proximo(self):
        return None

    def __len__(self) -> int:
        return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    fila = FilaPrioridade()
    fila.adicionar("baixa", 2)
    fila.adicionar("alta", 1)
    fila.adicionar("alta2", 1)
    _verificar(len(fila) == 3, "tres itens", falhas)
    _verificar(fila.proximo() == "alta", "menor numero sai primeiro", falhas)
    _verificar(fila.proximo() == "alta2", "empate respeita a chegada", falhas)
    _verificar(len(fila) == 1, "sobrou um", falhas)
    _verificar(fila.proximo() == "baixa", "por ultimo a prioridade 2", falhas)

    try:
        fila.proximo()
        _verificar(False, "fila vazia deveria falhar", falhas)
    except ValueError:
        _verificar(True, "fila vazia levanta ValueError", falhas)

    try:
        fila.adicionar("x", True)  # type: ignore[arg-type]
        _verificar(False, "bool nao e prioridade", falhas)
    except ValueError:
        _verificar(len(fila) == 0, "prioridade bool nao entra", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
