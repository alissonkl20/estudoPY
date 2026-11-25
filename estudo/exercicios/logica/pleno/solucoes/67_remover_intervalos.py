"""Solucao de logica/pleno/67_remover_intervalos.py. Tente resolver o enunciado antes de abrir."""

def remover_intervalos(intervalos: list[tuple[int, int]]) -> int:
    if not intervalos:
        return 0
    ordenados = sorted(intervalos, key=lambda item: item[1])
    fim = ordenados[0][1]
    fica = 1
    for inicio, novo_fim in ordenados[1:]:
        if inicio >= fim:
            fica += 1
            fim = novo_fim
    return len(intervalos) - fica


if __name__ == "__main__":
    from _rodar import rodar

    rodar(remover_intervalos=remover_intervalos)
