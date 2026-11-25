"""Solucao de logica/pleno/07_maior_trecho.py. Tente resolver o enunciado antes de abrir."""

def maior_trecho(texto: str) -> int:
    inicio = 0
    melhor = 0
    ultimo = {}
    for i, ch in enumerate(texto):
        if ch in ultimo and ultimo[ch] >= inicio:
            inicio = ultimo[ch] + 1
        ultimo[ch] = i
        melhor = max(melhor, i - inicio + 1)
    return melhor


if __name__ == "__main__":
    from _rodar import rodar

    rodar(maior_trecho=maior_trecho)
