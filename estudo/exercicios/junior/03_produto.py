"""
Teste tecnico 03 — Produto com desconto

Nivel junior. Uma classe guarda nome e preco. O desconto so calcula
um valor novo: o preco guardado continua o mesmo.

Implemente Produto(nome, preco).

- nome: str que, depois do strip, nao fica vazia. Guarde sem espacos nas pontas
- preco: int ou float maior que 0 (bool nao vale)
- aplicar_desconto(percentual) devolve o preco com desconto, com 2 casas
- percentual: int de 0 a 50, inclusive (bool nao vale)
- entrada invalida levanta ValueError

Como testar:
    python3 junior/03_produto.py
"""


class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual: int) -> float:
        return 0.0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    produto = Produto("  Caneta ", 2.5)
    _verificar(produto.nome == "Caneta" and produto.preco == 2.5, "guarda nome e preco", falhas)
    _verificar(produto.aplicar_desconto(10) == 2.25, "desconto de 10%", falhas)
    _verificar(produto.preco == 2.5, "desconto nao altera o preco", falhas)
    _verificar(Produto("Lapis", 10).aplicar_desconto(0) == 10.0, "zero por cento", falhas)
    _verificar(Produto("Lapis", 10).aplicar_desconto(50) == 5.0, "cinquenta por cento", falhas)

    for nome, preco in (("  ", 2), ("Caneta", 0), ("Caneta", -1), ("Caneta", True)):
        try:
            Produto(nome, preco)
            _verificar(False, f"Produto({nome!r}, {preco!r}) deveria falhar", falhas)
        except ValueError:
            _verificar(True, f"Produto({nome!r}, {preco!r}) levanta ValueError", falhas)

    caneta = Produto("Caneta", 10)
    for ruim in (51, -1, True, 10.5):
        try:
            caneta.aplicar_desconto(ruim)  # type: ignore[arg-type]
            _verificar(False, f"desconto {ruim!r} deveria falhar", falhas)
        except ValueError:
            _verificar(caneta.preco == 10, f"desconto {ruim!r} nao muda o preco", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
