"""Solucao de logica/pleno/57_ocorrencias.py. Tente resolver o enunciado antes de abrir."""

def ocorrencias(nums: list[int], alvo: int) -> tuple[int, int]:
    def lado(esquerda: bool) -> int:
        inicio, fim = 0, len(nums) - 1
        achou = -1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if nums[meio] == alvo:
                achou = meio
                if esquerda:
                    fim = meio - 1
                else:
                    inicio = meio + 1
            elif nums[meio] < alvo:
                inicio = meio + 1
            else:
                fim = meio - 1
        return achou

    return (lado(True), lado(False))


if __name__ == "__main__":
    from _rodar import rodar

    rodar(ocorrencias=ocorrencias)
