"""Solucao de logica/junior/36_conceito.py. Tente resolver o enunciado antes de abrir."""

def conceito(nota: float) -> str:
    if isinstance(nota, bool) or not isinstance(nota, (int, float)) or not 0 <= nota <= 10:
        raise ValueError("nota invalida")
    if nota >= 9:
        return "A"
    if nota >= 7:
        return "B"
    if nota >= 5:
        return "C"
    if nota >= 3:
        return "D"
    return "F"


if __name__ == "__main__":
    from _rodar import rodar

    rodar(conceito=conceito)
