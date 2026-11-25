"""
Exercicio 01 — Sequencia com regras

Logica de condicionais. A ordem dos divisores importa: 3, depois 5, depois 7.
Se o numero for multiplo de mais de um, as palavras se juntam.

Implemente classificar(n) -> str e sequencia(ate) -> list[str].

classificar(n):
- multiplo de 3 acrescenta "Fizz"
- multiplo de 5 acrescenta "Buzz"
- multiplo de 7 acrescenta "Pop"
- se nao for multiplo de nenhum, devolve o proprio numero como texto
- 105 e multiplo dos tres: "FizzBuzzPop"

sequencia(ate):
- devolve classificar de 1 ate `ate`, inclusive
- ate < 1 levanta ValueError

Como testar:
    python3 logica/01_sequencia.py
"""


def classificar(n: int) -> str:
    resultado = ""
    if n % 3 == 0:
        resultado += "Fizz"             
    if n % 5 == 0:
        resultado += "Buzz"
    if n % 7 == 0:
        resultado += "Pop"
    return resultado or str(n)


def sequencia(ate: int) -> list[str]:
    if ate < 1:
        raise ValueError("ate deve ser um inteiro positivo")
    return [classificar(i) for i in range(1, ate + 1)]


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    casos = {
        1: "1",
        3: "Fizz",
        5: "Buzz",
        7: "Pop",
        15: "FizzBuzz",
        21: "FizzPop",
        35: "BuzzPop",
        105: "FizzBuzzPop",
    }
    for numero, esperado in casos.items():
        veio = classificar(numero)
        _verificar(veio == esperado, f"{numero} -> {esperado}, veio {veio}", falhas)

    _verificar(
        sequencia(5) == ["1", "2", "Fizz", "4", "Buzz"],
        "sequencia ate 5",
        falhas,
    )
    ate_15 = sequencia(15)
    _verificar(
        ate_15 != [] and ate_15[-1] == "FizzBuzz",
        f"ultimo de 1 a 15, veio {ate_15}",
        falhas,
    )

    try:
        sequencia(0)
        _verificar(False, "ate 0 deveria levantar ValueError", falhas)
    except ValueError:
        _verificar(True, "ate 0 levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
