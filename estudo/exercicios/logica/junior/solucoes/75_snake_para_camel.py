"""Solucao de logica/junior/75_snake_para_camel.py. Tente resolver o enunciado antes de abrir."""

def snake_para_camel(nome: str) -> str:
    partes = [parte for parte in nome.split("_") if parte]
    if not partes:
        return ""
    return partes[0].lower() + "".join(parte.capitalize() for parte in partes[1:])


if __name__ == "__main__":
    from _rodar import rodar

    rodar(snake_para_camel=snake_para_camel)
