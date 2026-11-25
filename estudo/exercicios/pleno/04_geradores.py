"""
Teste tecnico 04 — Geradores

Nivel pleno. Nao transforme a entrada inteira em lista antes de entregar
o primeiro lote. Quem consome decide ate onde ler.

Implemente lotes(itens, tamanho) e filtrar_linhas(linhas).
Os dois sao geradores.

lotes:
- entrega listas com ate `tamanho` itens
- o ultimo lote pode vir menor
- tamanho < 1 levanta ValueError antes de consumir a entrada
- entrada vazia nao entrega nenhum lote

filtrar_linhas:
- ignora linha vazia ou so com espaco
- ignora linha cujo texto, depois do strip, comeca com #
- devolve a linha ja com strip

Como testar:
    python3 pleno/04_geradores.py
"""


def lotes(itens, tamanho: int):
    # seu codigo aqui
    if False:
        yield []


def filtrar_linhas(linhas):
    # seu codigo aqui
    if False:
        yield ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(
        list(lotes([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]],
        "lotes com sobra",
        falhas,
    )
    _verificar(list(lotes([], 3)) == [], "entrada vazia", falhas)

    produzidos: list[int] = []

    def fonte():
        for numero in range(5):
            produzidos.append(numero)
            yield numero

    gerador = lotes(fonte(), 2)
    try:
        primeiro = next(gerador)
    except StopIteration:
        _verificar(False, "gerador nao entregou o primeiro lote", falhas)
    else:
        _verificar(primeiro == [0, 1], f"primeiro lote, veio {primeiro}", falhas)
        _verificar(produzidos == [0, 1], f"nao leu a fonte inteira, leu {produzidos}", falhas)

    linhas = filtrar_linhas(["  a  ", "", "   ", "# comentario", "  #nao", "b"])
    try:
        primeira = next(linhas)
        segunda = next(linhas)
    except StopIteration:
        _verificar(False, "filtrar_linhas nao entregou as linhas", falhas)
    else:
        _verificar(primeira == "a", "primeira linha limpa", falhas)
        _verificar(segunda == "b", "pula comentario", falhas)
        try:
            next(linhas)
            _verificar(False, "deveria ter acabado", falhas)
        except StopIteration:
            _verificar(True, "gerador termina", falhas)

    try:
        next(lotes([1, 2, 3], 0))
        _verificar(False, "tamanho 0 deveria levantar ValueError", falhas)
    except ValueError:
        _verificar(True, "tamanho 0 levanta ValueError", falhas)
    except StopIteration:
        _verificar(False, "tamanho 0 deveria levantar ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
