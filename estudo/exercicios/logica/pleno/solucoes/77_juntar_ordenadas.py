"""Solucao de logica/pleno/77_juntar_ordenadas.py. Tente resolver o enunciado antes de abrir."""

def juntar_ordenadas(a: list[int], b: list[int]) -> list[int]:
    i = j = 0
    saida = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            saida.append(a[i])
            i += 1
        else:
            saida.append(b[j])
            j += 1
    saida.extend(a[i:])
    saida.extend(b[j:])
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(juntar_ordenadas=juntar_ordenadas)
