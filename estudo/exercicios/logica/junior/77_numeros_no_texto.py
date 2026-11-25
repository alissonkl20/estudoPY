"""
Logica junior 77 — Numeros no texto

Extraia as sequencias de digitos, da esquerda para a direita, como inteiros. 007 vira 7.

Como testar:
    python3 logica/junior/77_numeros_no_texto.py
"""

def numeros_no_texto(texto: str) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = numeros_no_texto('a12b3')
    _verificar(veio == [12, 3], f"numeros_no_texto('a12b3') -> [12, 3], veio {veio!r}", falhas)
    veio = numeros_no_texto('x')
    _verificar(veio == [], f"numeros_no_texto('x') -> [], veio {veio!r}", falhas)
    veio = numeros_no_texto('007')
    _verificar(veio == [7], f"numeros_no_texto('007') -> [7], veio {veio!r}", falhas)
    veio = numeros_no_texto('1 20')
    _verificar(veio == [1, 20], f"numeros_no_texto('1 20') -> [1, 20], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

