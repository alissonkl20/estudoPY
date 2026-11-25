"""Solucao de logica/pleno/14_soma_caminho.py. Tente resolver o enunciado antes de abrir."""

def soma_caminho(grade: list[list[int]]) -> int:
    if not grade or not grade[0]:
        raise ValueError("grade vazia")
    linhas, colunas = len(grade), len(grade[0])
    dp = [0] * colunas
    for r in range(linhas):
        for c in range(colunas):
            if r == 0 and c == 0:
                dp[c] = grade[r][c]
            elif r == 0:
                dp[c] = dp[c - 1] + grade[r][c]
            elif c == 0:
                dp[c] = dp[c] + grade[r][c]
            else:
                dp[c] = min(dp[c], dp[c - 1]) + grade[r][c]
    return dp[-1]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(soma_caminho=soma_caminho)
