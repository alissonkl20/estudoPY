"""Solucao de logica/pleno/39_indices_anagrama.py. Tente resolver o enunciado antes de abrir."""

def indices_anagrama(texto: str, padrao: str) -> list[int]:
    if not padrao or len(padrao) > len(texto):
        return []
    from collections import Counter
    falta = Counter(padrao)
    diferentes = len(falta)
    saida = []
    for i, ch in enumerate(texto):
        if ch in falta:
            falta[ch] -= 1
            if falta[ch] == 0:
                diferentes -= 1
        if i >= len(padrao):
            saiu = texto[i - len(padrao)]
            if saiu in falta:
                if falta[saiu] == 0:
                    diferentes += 1
                falta[saiu] += 1
        if i >= len(padrao) - 1 and diferentes == 0:
            saida.append(i - len(padrao) + 1)
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(indices_anagrama=indices_anagrama)
