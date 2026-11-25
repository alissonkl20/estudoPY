"""Solucao de logica/pleno/65_intersecao_intervalos.py. Tente resolver o enunciado antes de abrir."""

def intersecao_intervalos(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int] | None:
    if a[0] > a[1] or b[0] > b[1]:
        raise ValueError("intervalo invalido")
    inicio = a[0] if a[0] > b[0] else b[0]
    fim = a[1] if a[1] < b[1] else b[1]
    if inicio > fim:
        return None
    return (inicio, fim)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(intersecao_intervalos=intersecao_intervalos)
