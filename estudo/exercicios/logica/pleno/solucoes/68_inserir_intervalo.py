"""Solucao de logica/pleno/68_inserir_intervalo.py. Tente resolver o enunciado antes de abrir."""

def inserir_intervalo(intervalos: list[tuple[int, int]], novo: tuple[int, int]) -> list[tuple[int, int]]:
    inicio, fim = novo
    if inicio > fim:
        raise ValueError("intervalo invalido")
    saida = []
    i = 0
    while i < len(intervalos) and intervalos[i][1] < inicio:
        saida.append(intervalos[i])
        i += 1
    while i < len(intervalos) and intervalos[i][0] <= fim:
        inicio = min(inicio, intervalos[i][0])
        fim = max(fim, intervalos[i][1])
        i += 1
    saida.append((inicio, fim))
    saida.extend(intervalos[i:])
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(inserir_intervalo=inserir_intervalo)
