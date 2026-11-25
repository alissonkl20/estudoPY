"""Solucao de logica/junior/48_filtrar_positivos.py. Tente resolver o enunciado antes de abrir."""

def filtrar_positivos(nums: list[int]) -> list[int]:
    return [n for n in nums if n > 0]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(filtrar_positivos=filtrar_positivos)
