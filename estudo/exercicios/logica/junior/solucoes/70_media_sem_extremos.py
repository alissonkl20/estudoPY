"""Solucao de logica/junior/70_media_sem_extremos.py. Tente resolver o enunciado antes de abrir."""

def media_sem_extremos(nums: list[int]) -> float:
    if len(nums) < 3:
        raise ValueError("poucos numeros")
    meio = sorted(nums)[1:-1]
    return round(sum(meio) / len(meio), 2)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(media_sem_extremos=media_sem_extremos)
