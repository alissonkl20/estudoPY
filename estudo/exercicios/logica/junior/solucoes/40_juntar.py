"""Solucao de logica/junior/40_juntar.py. Tente resolver o enunciado antes de abrir."""

def juntar(itens: list[str], separador: str) -> str:
    for item in itens:
        if not isinstance(item, str):
            raise ValueError("item invalido")
    return separador.join(itens)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(juntar=juntar)
