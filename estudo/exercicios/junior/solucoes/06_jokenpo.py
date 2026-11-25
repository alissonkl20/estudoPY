"""Solucao de junior/06_jokenpo.py. Tente resolver o enunciado antes de abrir."""

_GANHA_DE = {"pedra": "tesoura", "tesoura": "papel", "papel": "pedra"}


def jogar(a: str, b: str) -> str:
    if not isinstance(a, str) or not isinstance(b, str):
        raise ValueError("jogada invalida")
    primeira = a.strip().lower()
    segunda = b.strip().lower()
    if primeira not in _GANHA_DE or segunda not in _GANHA_DE:
        raise ValueError("jogada invalida")
    if primeira == segunda:
        return "empate"
    if _GANHA_DE[primeira] == segunda:
        return "a"
    return "b"


if __name__ == "__main__":
    from _rodar import rodar

    rodar(jogar=jogar)
