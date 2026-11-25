"""Solucao de logica/junior/80_intervalo_soma.py. Tente resolver o enunciado antes de abrir."""

def intervalo_soma(inicio: int, fim: int) -> int:
    if inicio > fim:
        raise ValueError("intervalo invalido")
    return sum(range(inicio, fim + 1))


if __name__ == "__main__":
    from _rodar import rodar

    rodar(intervalo_soma=intervalo_soma)
