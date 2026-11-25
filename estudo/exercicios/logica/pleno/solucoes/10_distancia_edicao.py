"""Solucao de logica/pleno/10_distancia_edicao.py. Tente resolver o enunciado antes de abrir."""

def distancia_edicao(a: str, b: str) -> int:
    anterior = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        atual = [i]
        for j, cb in enumerate(b, start=1):
            troca = 0 if ca == cb else 1
            atual.append(min(atual[-1] + 1, anterior[j] + 1, anterior[j - 1] + troca))
        anterior = atual
    return anterior[-1]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(distancia_edicao=distancia_edicao)
