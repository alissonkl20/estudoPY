"""Solucao de logica/junior/71_acima_da_media.py. Tente resolver o enunciado antes de abrir."""

def acima_da_media(nums: list[int]) -> list[int]:
    if not nums:
        return []
    media = sum(nums) / len(nums)
    return [n for n in nums if n > media]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(acima_da_media=acima_da_media)
