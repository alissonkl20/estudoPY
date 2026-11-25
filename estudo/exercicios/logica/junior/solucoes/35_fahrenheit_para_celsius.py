"""Solucao de logica/junior/35_fahrenheit_para_celsius.py. Tente resolver o enunciado antes de abrir."""

def fahrenheit_para_celsius(fahrenheit: float) -> float:
    return round((fahrenheit - 32) * 5 / 9, 2)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(fahrenheit_para_celsius=fahrenheit_para_celsius)
