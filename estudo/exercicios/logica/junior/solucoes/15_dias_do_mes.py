"""Solucao de logica/junior/15_dias_do_mes.py. Tente resolver o enunciado antes de abrir."""

def dias_do_mes(mes: int, ano: int) -> int:
    if mes < 1 or mes > 12 or ano < 1:
        raise ValueError("data invalida")
    if mes == 2:
        bissexto = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
        return 29 if bissexto else 28
    if mes in (4, 6, 9, 11):
        return 30
    return 31


if __name__ == "__main__":
    from _rodar import rodar

    rodar(dias_do_mes=dias_do_mes)
