"""Solucao de logica/junior/34_celsius_para_fahrenheit.py. Tente resolver o enunciado antes de abrir."""

def celsius_para_fahrenheit(celsius: float) -> float:
    return round(celsius * 9 / 5 + 32, 2)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(celsius_para_fahrenheit=celsius_para_fahrenheit)
