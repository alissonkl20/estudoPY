"""
Logica junior 48 — Filtrar positivos

Fique so com os numeros maiores que zero, na ordem original. Zero sai.

Como testar:
    python3 logica/junior/48_filtrar_positivos.py
"""

def filtrar_positivos(nums: list[int]) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = filtrar_positivos([0, -1, 2, 3])
    _verificar(veio == [2, 3], f"filtrar_positivos([0, -1, 2, 3]) -> [2, 3], veio {veio!r}", falhas)
    veio = filtrar_positivos([])
    _verificar(veio == [], f"filtrar_positivos([]) -> [], veio {veio!r}", falhas)
    veio = filtrar_positivos([-5])
    _verificar(veio == [], f"filtrar_positivos([-5]) -> [], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

