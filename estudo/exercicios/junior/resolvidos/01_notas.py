"""
Teste tecnico 01 — Boletim

Nivel junior. A partir das notas, calcule media, maior, menor e se passou.
A media 7 ja aprova.

Implemente boletim(notas) -> dict:

    {"media": float, "maior": numero, "menor": numero, "aprovado": bool}

- lista vazia levanta ValueError
- cada nota e int ou float de 0 a 10, inclusive (bool nao vale)
- media com 2 casas (round)
- aprovado quando a media e pelo menos 7

Como testar:
    python3 junior/01_notas.py
"""

import statistics
from numpy import mean

import statistics


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

    



def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(
        boletim([8, 7, 9]) == {"media": 8.0, "maior": 9, "menor": 7, "aprovado": True},
        "tres notas aprovadas",
        falhas,
    )
    _verificar(
        boletim([6, 8]) == {"media": 7.0, "maior": 8, "menor": 6, "aprovado": True},
        "media 7 aprova",
        falhas,
    )
    _verificar(
        boletim([0, 10]) == {"media": 5.0, "maior": 10, "menor": 0, "aprovado": False},
        "zero e nota valida",
        falhas,
    )
    _verificar(
        boletim([10, 7.5]) == {"media": 8.75, "maior": 10, "menor": 7.5, "aprovado": True},
        "media com decimal",
        falhas,
    )

    for ruim in ([], [11], [-1], [True], [6, 11]):
        try:
            boletim(ruim)
            _verificar(False, f"{ruim!r} deveria falhar", falhas)
        except ValueError:
            _verificar(True, f"{ruim!r} levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
