"""
Logica junior 19 — Contar vogais

Conte a, e, i, o, u, sem diferenciar maiusculas. Outros caracteres nao contam.

Como testar:
    python3 logica/junior/19_vogais.py
"""

def vogais(texto: str) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = vogais('AeIoU')
    _verificar(veio == 5, f"vogais('AeIoU') -> 5, veio {veio!r}", falhas)
    veio = vogais('xyz')
    _verificar(veio == 0, f"vogais('xyz') -> 0, veio {veio!r}", falhas)
    veio = vogais('Banana')
    _verificar(veio == 3, f"vogais('Banana') -> 3, veio {veio!r}", falhas)
    veio = vogais('')
    _verificar(veio == 0, f"vogais('') -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

