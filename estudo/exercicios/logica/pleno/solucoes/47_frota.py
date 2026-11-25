"""Solucao de logica/pleno/47_frota.py. Tente resolver o enunciado antes de abrir."""

def frota(alvo: int, posicao: list[int], velocidade: list[int]) -> int:
    if len(posicao) != len(velocidade):
        raise ValueError("listas diferentes")
    carros = sorted(zip(posicao, velocidade), reverse=True)
    grupos = 0
    limite = -1.0
    for lugar, vel in carros:
        tempo = (alvo - lugar) / vel
        if tempo > limite:
            grupos += 1
            limite = tempo
    return grupos


if __name__ == "__main__":
    from _rodar import rodar

    rodar(frota=frota)
