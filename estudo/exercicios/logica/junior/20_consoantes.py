"""
Logica junior 20 — Contar consoantes

Conte letras que nao sao vogais. Espaco, numero e pontuacao nao contam. y conta como consoante.

Como testar:
    python3 logica/junior/20_consoantes.py
"""

def consoantes(texto: str) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = consoantes('Banana')
    _verificar(veio == 3, f"consoantes('Banana') -> 3, veio {veio!r}", falhas)
    veio = consoantes('AeIoU x')
    _verificar(veio == 1, f"consoantes('AeIoU x') -> 1, veio {veio!r}", falhas)
    veio = consoantes('y')
    _verificar(veio == 1, f"consoantes('y') -> 1, veio {veio!r}", falhas)
    veio = consoantes('123')
    _verificar(veio == 0, f"consoantes('123') -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

