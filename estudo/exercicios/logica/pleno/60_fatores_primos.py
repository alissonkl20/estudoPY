"""
Logica pleno 60 — Fatores primos

Devolva os fatores primos do menor para o maior, com repeticao. 1 devolve []. n menor que 1 levanta ValueError.

Como testar:
    python3 logica/pleno/60_fatores_primos.py
"""

def fatores_primos(n: int) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = fatores_primos(12)
    _verificar(veio == [2, 2, 3], f"fatores_primos(12) -> [2, 2, 3], veio {veio!r}", falhas)
    veio = fatores_primos(1)
    _verificar(veio == [], f"fatores_primos(1) -> [], veio {veio!r}", falhas)
    veio = fatores_primos(17)
    _verificar(veio == [17], f"fatores_primos(17) -> [17], veio {veio!r}", falhas)
    veio = fatores_primos(8)
    _verificar(veio == [2, 2, 2], f"fatores_primos(8) -> [2, 2, 2], veio {veio!r}", falhas)
    try:
        fatores_primos(0)
        _verificar(False, "fatores_primos(0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "fatores_primos(0) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

