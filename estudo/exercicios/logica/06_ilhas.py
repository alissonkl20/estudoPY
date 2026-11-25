"""
Exercicio 06 — Contar ilhas

O mapa e uma grade de 0 (agua) e 1 (terra).
Terra ligada na horizontal ou na vertical forma uma ilha. Diagonal nao liga.

Implemente contar_ilhas(mapa) -> int.

- mapa vazio devolve 0
- nao altere o mapa recebido
- pode usar pilha ou recursao para visitar cada ilha uma vez

Como testar:
    python3 logica/06_ilhas.py
"""


def contar_ilhas(mapa: list[list[int]]) -> int:
    # seu codigo aqui
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(contar_ilhas([]) == 0, "mapa vazio", falhas)
    _verificar(contar_ilhas([[]]) == 0, "linha vazia", falhas)
    _verificar(contar_ilhas([[0, 0], [0, 0]]) == 0, "so agua", falhas)
    _verificar(contar_ilhas([[1]]) == 1, "uma celula de terra", falhas)

    mapa = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
    copia = [list(linha) for linha in mapa]
    _verificar(contar_ilhas(mapa) == 2, "duas ilhas, diagonal nao junta", falhas)
    _verificar(mapa == copia, "mapa original intacto", falhas)

    _verificar(contar_ilhas([[1, 0, 1], [0, 1, 0]]) == 3, "tres ilhas separadas", falhas)
    _verificar(contar_ilhas([[1, 1], [1, 0]]) == 1, "terra conectada", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
