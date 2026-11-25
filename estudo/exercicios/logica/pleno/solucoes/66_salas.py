"""Solucao de logica/pleno/66_salas.py. Tente resolver o enunciado antes de abrir."""

def salas(reservas: list[tuple[int, int]]) -> int:
    eventos = []
    for inicio, fim in reservas:
        if fim <= inicio:
            raise ValueError("reserva invalida")
        eventos.append((inicio, 1))
        eventos.append((fim, -1))
    atual = melhor = 0
    for _, delta in sorted(eventos):
        atual += delta
        if atual > melhor:
            melhor = atual
    return melhor


if __name__ == "__main__":
    from _rodar import rodar

    rodar(salas=salas)
