"""
Logica junior 14 — Ano bissexto

Multiplo de 4 e bissexto, exceto os multiplos de 100 que nao sao multiplos de 400. Ano menor que 1 levanta ValueError.

Como testar:
    python3 logica/junior/14_bissexto.py
"""

def bissexto(ano: int) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = bissexto(2024)
    _verificar(veio == True, f"bissexto(2024) -> True, veio {veio!r}", falhas)
    veio = bissexto(2023)
    _verificar(veio == False, f"bissexto(2023) -> False, veio {veio!r}", falhas)
    veio = bissexto(1900)
    _verificar(veio == False, f"bissexto(1900) -> False, veio {veio!r}", falhas)
    veio = bissexto(2000)
    _verificar(veio == True, f"bissexto(2000) -> True, veio {veio!r}", falhas)
    try:
        bissexto(0)
        _verificar(False, "bissexto(0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "bissexto(0) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

