"""
Exercicio 03 — Delimitadores balanceados

Uma pilha resolve este problema. Percorra o texto uma vez.

Implemente balanceado(texto) -> bool.

Regras:
- pares validos: (), [] e {}
- qualquer outro caractere e ignorado
- texto vazio e balanceado
- fecha sem abrir, ou fecha o par errado, e falso
- sobrou abertura no fim: falso

Como testar:
    python3 logica/03_balanceado.py
"""


def balanceado(texto: str) -> bool:
    # seu codigo aqui
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    verdadeiros = ["", "()", "({[]})", "a(b[c]{d})e", "([{}])"]
    for texto in verdadeiros:
        _verificar(balanceado(texto), f"valido: {texto!r}", falhas)

    falsos = ["(", ")", "(]", "([)]", ")(", "(()", "{[}]", "([)]"]
    for texto in falsos:
        _verificar(not balanceado(texto), f"invalido: {texto!r}", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
