"""Solucao de logica/pleno/55_busca_rotacionada.py. Tente resolver o enunciado antes de abrir."""

def busca_rotacionada(nums: list[int], alvo: int) -> int:
    inicio, fim = 0, len(nums) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if nums[meio] == alvo:
            return meio
        if nums[inicio] <= nums[meio]:
            if nums[inicio] <= alvo < nums[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1
        elif nums[meio] < alvo <= nums[fim]:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


if __name__ == "__main__":
    from _rodar import rodar

    rodar(busca_rotacionada=busca_rotacionada)
