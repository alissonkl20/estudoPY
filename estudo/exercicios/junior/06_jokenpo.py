"""
Teste tecnico 06 — Pedra, papel e tesoura

Nivel junior. Compare as duas jogadas e diga quem ganhou.

Implemente jogar(a, b) -> str.

- valores validos: "pedra", "papel" e "tesoura"
- ignore maiusculas e espacos nas pontas
- "a" se a primeira jogada ganha
- "b" se a segunda ganha
- "empate" se forem iguais
- pedra ganha de tesoura, tesoura ganha de papel, papel ganha de pedra
- jogada invalida, ou valor que nao e str, levanta ValueError

Como testar:
    python3 junior/06_jokenpo.py
"""


def jogar(a: str, b: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(jogar("Pedra", "tesoura") == "a", "pedra ganha de tesoura", falhas)
    _verificar(jogar("papel", "pedra") == "a", "papel ganha de pedra", falhas)
    _verificar(jogar("tesoura", "papel") == "a", "tesoura ganha de papel", falhas)
    _verificar(jogar("pedra", "papel") == "b", "a segunda ganha", falhas)
    _verificar(jogar("PEDRA", " pedra ") == "empate", "ignora caixa e espaco", falhas)

    for a, b in (("fogo", "pedra"), ("", "pedra"), (1, "pedra")):
        try:
            jogar(a, b)  # type: ignore[arg-type]
            _verificar(False, f"jogar({a!r}, {b!r}) deveria falhar", falhas)
        except ValueError:
            _verificar(True, f"jogar({a!r}, {b!r}) levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
