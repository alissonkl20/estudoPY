"""
Teste tecnico 28 — Calculadora de inteiros

Nivel pleno. Interprete a expressao. Multiplicacao acontece antes de
soma e subtracao. Operacoes iguais seguem da esquerda para a direita.
Nao ha divisao nem sinal unario.

Implemente calcular(expressao) -> int.

- numeros inteiros e os operadores + - * ( )
- espacos sao ignorados
- "2 + 3 * 4" vale 14
- "(2 + 3) * 4" vale 20
- "10 - 3 - 2" vale 5
- expressao vazia, parentese aberto, operador sobrando ou caractere
  estranho levanta ValueError

Como testar:
    python3 pleno/28_calculadora.py
"""


def calcular(expressao: str) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(calcular("2 + 3 * 4") == 14, "multiplicacao primeiro", falhas)
    _verificar(calcular("(2 + 3) * 4") == 20, "parenteses", falhas)
    _verificar(calcular("10 - 3 - 2") == 5, "esquerda para a direita", falhas)
    _verificar(calcular(" ( 8 - 2 ) * 3 ") == 18, "espacos", falhas)
    _verificar(calcular("((2))") == 2, "parenteses aninhados", falhas)
    _verificar(calcular("2*3+4*5") == 26, "duas multiplicacoes", falhas)

    for ruim in ("", "2 +", "(2+3", "8 / 2", "2 + + 3"):
        try:
            calcular(ruim)
            _verificar(False, f"{ruim!r} deveria falhar", falhas)
        except ValueError:
            _verificar(True, f"{ruim!r} levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
