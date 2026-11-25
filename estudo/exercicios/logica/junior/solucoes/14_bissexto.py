"""Solucao de logica/junior/14_bissexto.py. Tente resolver o enunciado antes de abrir."""

def bissexto(ano: int) -> bool:
    if ano < 1:
        raise ValueError("ano invalido")
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(bissexto=bissexto)
