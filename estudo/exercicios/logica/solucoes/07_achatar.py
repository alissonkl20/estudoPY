"""Solucao de logica/07_achatar.py. Tente resolver o enunciado antes de abrir."""


def achatar(valor) -> list:
    if isinstance(valor, list):
        saida = []
        for item in valor:
            saida.extend(achatar(item))
        return saida
    return [valor]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(achatar=achatar)
