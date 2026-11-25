"""Solucao de junior/05_formatar_nome.py. Tente resolver o enunciado antes de abrir."""


def formatar_nome(nome: str) -> str:
    if not isinstance(nome, str):
        raise ValueError("nome invalido")
    partes = nome.split()
    if not partes:
        raise ValueError("nome invalido")
    return " ".join(parte.capitalize() for parte in partes)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(formatar_nome=formatar_nome)
