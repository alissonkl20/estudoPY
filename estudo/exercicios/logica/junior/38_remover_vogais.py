"""
Logica junior 38 — Remover vogais

Tire a, e, i, o, u sem diferenciar maiusculas. O resto permanece, inclusive espacos.

Como testar:
    python3 logica/junior/38_remover_vogais.py
"""

def remover_vogais(texto: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = remover_vogais('Banana')
    _verificar(veio == 'Bnn', f"remover_vogais('Banana') -> 'Bnn', veio {veio!r}", falhas)
    veio = remover_vogais('Aeiou')
    _verificar(veio == '', f"remover_vogais('Aeiou') -> '', veio {veio!r}", falhas)
    veio = remover_vogais('a b')
    _verificar(veio == ' b', f"remover_vogais('a b') -> ' b', veio {veio!r}", falhas)
    veio = remover_vogais('')
    _verificar(veio == '', f"remover_vogais('') -> '', veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

