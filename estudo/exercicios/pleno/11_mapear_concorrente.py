"""
Teste tecnico 11 — Mapear em paralelo

Nivel pleno. Rode a funcao em varias threads e devolva os resultados
na mesma ordem da entrada, mesmo que um item mais tardio termine antes.

Implemente mapear(func, itens, trabalhadores=4) -> list.

- trabalhadores < 1 levanta ValueError
- lista vazia devolve []
- se func levantar excecao, mapear levanta a excecao do menor indice
- as outras tarefas podem terminar; o erro escolhido e o do menor indice,
  nao o que chegou primeiro

Como testar:
    python3 pleno/11_mapear_concorrente.py
"""

import time


def mapear(func, itens: list, trabalhadores: int = 4) -> list:
    # seu codigo aqui
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    def lento(numero: int) -> int:
        if numero == 1:
            time.sleep(0.05)
        return numero * 10

    _verificar(mapear(lento, [1, 2, 3], trabalhadores=3) == [10, 20, 30], "ordem da entrada", falhas)
    _verificar(mapear(lento, []) == [], "lista vazia", falhas)

    def pode_falhar(numero: int) -> int:
        if numero in (0, 2):
            raise RuntimeError(f"falha {numero}")
        return numero

    try:
        mapear(pode_falhar, [0, 1, 2])
        _verificar(False, "deveria propagar a excecao", falhas)
    except RuntimeError as erro:
        _verificar(str(erro) == "falha 0", f"erro do menor indice, veio {erro}", falhas)

    try:
        mapear(lento, [1], trabalhadores=0)
        _verificar(False, "zero trabalhadores deveria falhar", falhas)
    except ValueError:
        _verificar(True, "zero trabalhadores levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
