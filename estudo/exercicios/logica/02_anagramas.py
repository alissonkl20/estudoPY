"""
Exercicio 02 — Anagramas

Duas palavras sao anagramas quando tem as mesmas letras na mesma quantidade.
Maiusculas e espacos nao contam. Pontuacao conta como caractere.

Implemente sao_anagramas(a, b) -> bool e agrupar(palavras) -> list[list[str]].

agrupar:
- junta anagramas na ordem em que cada grupo aparece pela primeira vez
- dentro do grupo, mantem a ordem original das palavras
- devolve uma lista nova
- nao altera a lista recebida

Como testar:
    python3 logica/02_anagramas.py
"""


def sao_anagramas(a: str, b: str) -> bool:
    # seu codigo aqui
    return False


def agrupar(palavras: list[str]) -> list[list[str]]:
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

    _verificar(sao_anagramas("Roma", "amor"), "ignora maiusculas", falhas)
    _verificar(sao_anagramas("Amo r", "Roma"), "ignora espacos", falhas)
    _verificar(not sao_anagramas("amor", "amor!"), "pontuacao conta", falhas)
    _verificar(not sao_anagramas("abc", "ab"), "quantidades diferentes", falhas)
    _verificar(sao_anagramas("   ", ""), "so espacos equivale a vazio", falhas)

    palavras = ["amor", "Roma", "casa", "ramo", "Asa", "saca"]
    original = list(palavras)
    grupos = agrupar(palavras)
    _verificar(
        grupos == [["amor", "Roma", "ramo"], ["casa", "saca"], ["Asa"]],
        f"grupos na ordem de aparicao, veio {grupos}",
        falhas,
    )
    _verificar(palavras == original, "lista original intacta", falhas)
    _verificar(agrupar([]) == [], "lista vazia", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
