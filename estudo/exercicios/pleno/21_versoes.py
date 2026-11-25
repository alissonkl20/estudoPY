"""
Teste tecnico 21 — Comparar versoes

Nivel pleno. Compare numeros, nao texto: "1.10" e maior que "1.9".
Pedaco que falta vale 0, entao "1.2" e igual a "1.2.0".

Implemente comparar(a, b) -> int e ordenar(versoes) -> list[str].

comparar devolve -1 se a < b, 0 se iguais, 1 se a > b.
ordenar devolve uma lista nova, sem mudar a recebida.
Versao invalida (vazia, letra, sinal, ponto duplo) levanta ValueError.
Zero a esquerda nao muda o numero: "01" vale 1.

Como testar:
    python3 pleno/21_versoes.py
"""


def comparar(a: str, b: str) -> int:
    return 0


def ordenar(versoes: list[str]) -> list[str]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(comparar("1.10", "1.9") == 1, "1.10 > 1.9", falhas)
    _verificar(comparar("1.2", "1.2.0") == 0, "pedaco faltando vale zero", falhas)
    _verificar(comparar("1.0.0", "1.0.1") == -1, "1.0.0 < 1.0.1", falhas)
    _verificar(comparar("01.2", "1.2") == 0, "zero a esquerda", falhas)

    lista = ["1.10", "1.2", "1.9"]
    copia = list(lista)
    _verificar(ordenar(lista) == ["1.2", "1.9", "1.10"], "ordem numerica", falhas)
    _verificar(lista == copia, "lista original intacta", falhas)

    for ruim in ("", "1.a", "1..2", "-1", "1."):
        try:
            comparar(ruim, "1.0")
            _verificar(False, f"{ruim!r} deveria falhar", falhas)
        except ValueError:
            _verificar(True, f"{ruim!r} levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
