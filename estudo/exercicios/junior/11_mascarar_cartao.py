"""
Teste tecnico 11 — Mascarar cartao

Nivel junior. Mostre so os quatro ultimos digitos. O resto vira asterisco,
em grupos de quatro.

Implemente mascarar_cartao(numero) -> str.

- numero precisa ser str
- espacos e hifens podem aparecer e sao ignorados
- depois disso, precisam sobrar exatamente 16 digitos
- qualquer outro caractere, ou quantidade diferente, levanta ValueError
- a resposta tem o formato "**** **** **** 3456"

Como testar:
    python3 junior/11_mascarar_cartao.py
"""


def mascarar_cartao(numero: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    esperado = "**** **** **** 3456"
    _verificar(mascarar_cartao("1234567890123456") == esperado, "16 digitos seguidos", falhas)
    _verificar(mascarar_cartao("1234-5678-9012-3456") == esperado, "com hifens", falhas)
    _verificar(mascarar_cartao("1234 5678 9012 3456") == esperado, "com espacos", falhas)

    for ruim in ("123", "123456789012345", "12345678901234567", "123456789012345a", 1234567890123456):
        try:
            mascarar_cartao(ruim)  # type: ignore[arg-type]
            _verificar(False, f"{ruim!r} deveria falhar", falhas)
        except ValueError:
            _verificar(True, f"{ruim!r} levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
