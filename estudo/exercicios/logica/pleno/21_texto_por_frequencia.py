"""
Logica pleno 21 — Texto por frequencia

Rearranje os caracteres: mais frequente primeiro. Empate fica com a letra que vem antes no alfabeto.

Como testar:
    python3 logica/pleno/21_texto_por_frequencia.py
"""

def texto_por_frequencia(texto: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = texto_por_frequencia('tree')
    _verificar(veio == 'eert', f"texto_por_frequencia('tree') -> 'eert', veio {veio!r}", falhas)
    veio = texto_por_frequencia('cccaaa')
    _verificar(veio == 'aaaccc', f"texto_por_frequencia('cccaaa') -> 'aaaccc', veio {veio!r}", falhas)
    veio = texto_por_frequencia('')
    _verificar(veio == '', f"texto_por_frequencia('') -> '', veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

