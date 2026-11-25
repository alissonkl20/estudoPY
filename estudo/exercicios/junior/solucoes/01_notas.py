"""Solucao de junior/01_notas.py. Tente resolver o enunciado antes de abrir."""


def boletim(notas: list) -> dict:
    if not notas:
        raise ValueError("sem notas")
    for nota in notas:
        if isinstance(nota, bool) or not isinstance(nota, (int, float)) or not 0 <= nota <= 10:
            raise ValueError("nota invalida")
    media = round(sum(notas) / len(notas), 2)
    return {
        "media": media,
        "maior": max(notas),
        "menor": min(notas),
        "aprovado": media >= 7,
    }


if __name__ == "__main__":
    from _rodar import rodar

    rodar(boletim=boletim)
