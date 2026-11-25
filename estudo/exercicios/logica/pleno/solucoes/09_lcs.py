"""Solucao de logica/pleno/09_lcs.py. Tente resolver o enunciado antes de abrir."""

def lcs(a: str, b: str) -> int:
    anterior = [0] * (len(b) + 1)
    for ca in a:
        atual = [0]
        for j, cb in enumerate(b, start=1):
            if ca == cb:
                atual.append(anterior[j - 1] + 1)
            else:
                atual.append(max(anterior[j], atual[-1]))
        anterior = atual
    return anterior[-1]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(lcs=lcs)
