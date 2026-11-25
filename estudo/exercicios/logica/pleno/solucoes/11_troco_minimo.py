"""Solucao de logica/pleno/11_troco_minimo.py. Tente resolver o enunciado antes de abrir."""

def troco_minimo(moedas: list[int], valor: int) -> int:
    if valor < 0:
        raise ValueError("valor invalido")
    grande = valor + 1
    dp = [0] + [grande] * valor
    for atual in range(1, valor + 1):
        for moeda in moedas:
            if 0 < moeda <= atual:
                dp[atual] = min(dp[atual], dp[atual - moeda] + 1)
    return -1 if dp[valor] == grande else dp[valor]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(troco_minimo=troco_minimo)
