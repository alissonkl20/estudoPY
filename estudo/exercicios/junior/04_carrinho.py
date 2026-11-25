"""
Teste tecnico 04 — Carrinho

Nivel junior. O carrinho acumula itens. O mesmo nome soma a quantidade.
Nome igual com preco diferente e erro.

Implemente Carrinho.

adicionar(nome, preco, qtd=1)
- nome: str nao vazia depois do strip; guarde sem espacos nas pontas
- preco: int ou float maior que 0 (bool nao vale)
- qtd: int maior ou igual a 1 (bool nao vale)
- se o nome ja existe e o preco e o mesmo, some a quantidade
- se o nome ja existe e o preco mudou, ValueError e o carrinho fica igual

total() -> float com 2 casas
quantidade() -> soma das quantidades
itens() -> lista de {"nome", "preco", "qtd"}, na ordem da primeira inclusao
itens() devolve copia

Como testar:
    python3 junior/04_carrinho.py
"""


class Carrinho:
    def adicionar(self, nome: str, preco: float, qtd: int = 1) -> None:
        return None

    def total(self) -> float:
        return 0.0

    def quantidade(self) -> int:
        return 0

    def itens(self) -> list[dict]:
        return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    carrinho = Carrinho()
    _verificar(
        carrinho.total() == 0.0 and carrinho.quantidade() == 0 and carrinho.itens() == [],
        "carrinho vazio",
        falhas,
    )
    carrinho.adicionar("Caneta", 2.5, 2)
    carrinho.adicionar("  Caneta ", 2.5)
    carrinho.adicionar("Lapis", 1)
    _verificar(
        carrinho.itens()
        == [
            {"nome": "Caneta", "preco": 2.5, "qtd": 3},
            {"nome": "Lapis", "preco": 1.0, "qtd": 1},
        ],
        f"itens, veio {carrinho.itens()}",
        falhas,
    )
    _verificar(carrinho.total() == 8.5, f"total, veio {carrinho.total()}", falhas)
    _verificar(carrinho.quantidade() == 4, "soma das quantidades", falhas)

    lista = carrinho.itens()
    if lista:
        lista.pop()
        _verificar(carrinho.quantidade() == 4, "itens devolve copia", falhas)
    else:
        _verificar(False, "itens devolve copia", falhas)

    try:
        carrinho.adicionar("Caneta", 9, 1)
        _verificar(False, "preco diferente deveria falhar", falhas)
    except ValueError:
        _verificar(carrinho.total() == 8.5, "preco diferente nao grava", falhas)

    for nome, preco, qtd in ((" ", 1, 1), ("X", 0, 1), ("X", True, 1), ("X", 1, 0), ("X", 1, True)):
        try:
            Carrinho().adicionar(nome, preco, qtd)  # type: ignore[arg-type]
            _verificar(False, f"adicionar({nome!r}, {preco!r}, {qtd!r}) deveria falhar", falhas)
        except ValueError:
            _verificar(True, f"adicionar({nome!r}, {preco!r}, {qtd!r}) levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
