"""Solucao de logica/pleno/12_mochila.py. Tente resolver o enunciado antes de abrir."""

def mochila(pesos: list[int], valores: list[int], capacidade: int) -> int:
    if len(pesos) != len(valores) or capacidade < 0:
        raise ValueError("entrada invalida")
    dp = [0] * (capacidade + 1)
    for peso, valor in zip(pesos, valores):
        for cap in range(capacidade, peso - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - peso] + valor)
    return dp[capacidade]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(mochila=mochila)
