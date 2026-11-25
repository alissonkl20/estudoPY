"""Solucao de logica/pleno/28_somas_alvo.py. Tente resolver o enunciado antes de abrir."""

def somas_alvo(nums: list[int], alvo: int) -> list[list[int]]:
    ordenados = sorted(nums)
    saida = []

    def buscar(inicio: int, falta: int, atual: list[int]) -> None:
        if falta == 0:
            saida.append(atual)
            return
        for i in range(inicio, len(ordenados)):
            if ordenados[i] > falta:
                break
            buscar(i + 1, falta - ordenados[i], atual + [ordenados[i]])

    buscar(0, alvo, [])
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(somas_alvo=somas_alvo)
