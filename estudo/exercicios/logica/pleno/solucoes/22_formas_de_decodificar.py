"""Solucao de logica/pleno/22_formas_de_decodificar.py. Tente resolver o enunciado antes de abrir."""

def formas_de_decodificar(texto: str) -> int:
    if not texto or not texto.isdigit():
        raise ValueError("texto invalido")
    dp = [1] + [0] * len(texto)
    for i in range(1, len(texto) + 1):
        if texto[i - 1] != "0":
            dp[i] += dp[i - 1]
        if i >= 2 and texto[i - 2] != "0" and 10 <= int(texto[i - 2 : i]) <= 26:
            dp[i] += dp[i - 2]
    return dp[-1]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(formas_de_decodificar=formas_de_decodificar)
