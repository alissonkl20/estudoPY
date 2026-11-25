"""Solucao de logica/pleno/21_texto_por_frequencia.py. Tente resolver o enunciado antes de abrir."""

def texto_por_frequencia(texto: str) -> str:
    from collections import Counter
    ordenados = sorted(Counter(texto).items(), key=lambda item: (-item[1], item[0]))
    return "".join(ch * qtd for ch, qtd in ordenados)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(texto_por_frequencia=texto_por_frequencia)
