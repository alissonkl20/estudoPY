"""
Logica junior 33 — Tipo de triangulo

Devolva "equilatero", "isosceles" ou "escaleno". Lados que nao formam triangulo levantam ValueError.

Como testar:
    python3 logica/junior/33_tipo_triangulo.py
"""

def tipo_triangulo(a: int, b: int, c: int) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = tipo_triangulo(3, 3, 3)
    _verificar(veio == 'equilatero', f"tipo_triangulo(3, 3, 3) -> 'equilatero', veio {veio!r}", falhas)
    veio = tipo_triangulo(3, 3, 4)
    _verificar(veio == 'isosceles', f"tipo_triangulo(3, 3, 4) -> 'isosceles', veio {veio!r}", falhas)
    veio = tipo_triangulo(3, 4, 5)
    _verificar(veio == 'escaleno', f"tipo_triangulo(3, 4, 5) -> 'escaleno', veio {veio!r}", falhas)
    try:
        tipo_triangulo(1, 2, 3)
        _verificar(False, "tipo_triangulo(1, 2, 3) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "tipo_triangulo(1, 2, 3) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

