"""Solucao de logica/pleno/36_saltos_minimos.py. Tente resolver o enunciado antes de abrir."""

def saltos_minimos(nums: list[int]) -> int:
    if not nums:
        raise ValueError("sem caminho")
    if len(nums) == 1:
        return 0
    fim = alcance = pulos = 0
    for i in range(len(nums)):
        alcance = max(alcance, i + nums[i])
        if i == fim:
            pulos += 1
            fim = alcance
            if fim >= len(nums) - 1:
                return pulos
            if fim == i:
                break
    raise ValueError("sem caminho")


if __name__ == "__main__":
    from _rodar import rodar

    rodar(saltos_minimos=saltos_minimos)
