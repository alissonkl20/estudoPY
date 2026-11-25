"""
Logica junior 05 — Contar ocorrencias

Conte quantas vezes alvo aparece. Zero se nao aparecer.

Como testar:
    python3 logica/junior/05_contar_ocorrencias.py
"""

def contar_ocorrencias(itens: list, alvo) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = contar_ocorrencias([1, 2, 1, 1], 1)
    _verificar(veio == 3, f"contar_ocorrencias([1, 2, 1, 1], 1) -> 3, veio {veio!r}", falhas)
    veio = contar_ocorrencias(['a', 'b'], 'a')
    _verificar(veio == 1, f"contar_ocorrencias(['a', 'b'], 'a') -> 1, veio {veio!r}", falhas)
    veio = contar_ocorrencias([], 1)
    _verificar(veio == 0, f"contar_ocorrencias([], 1) -> 0, veio {veio!r}", falhas)
    veio = contar_ocorrencias([1, 2], 9)
    _verificar(veio == 0, f"contar_ocorrencias([1, 2], 9) -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

