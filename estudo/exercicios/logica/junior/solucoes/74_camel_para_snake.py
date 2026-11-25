"""Solucao de logica/junior/74_camel_para_snake.py. Tente resolver o enunciado antes de abrir."""

def camel_para_snake(nome: str) -> str:
    saida = []
    for i, ch in enumerate(nome):
        if ch.isupper() and i:
            saida.append("_")
        saida.append(ch.lower())
    return "".join(saida)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(camel_para_snake=camel_para_snake)
