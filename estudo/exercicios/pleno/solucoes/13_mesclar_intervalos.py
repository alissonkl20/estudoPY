"""Solucao de pleno/13_mesclar_intervalos.py. Tente resolver o enunciado antes de abrir."""


def mesclar(intervalos: list[tuple[int, int]]) -> list[tuple[int, int]]:
    normalizados: list[tuple[int, int]] = []
    for par in intervalos:
        if not isinstance(par, tuple) or len(par) != 2:
            raise ValueError("intervalo invalido")
        inicio, fim = par
        if (
            isinstance(inicio, bool)
            or isinstance(fim, bool)
            or not isinstance(inicio, int)
            or not isinstance(fim, int)
            or inicio > fim
        ):
            raise ValueError("intervalo invalido")
        normalizados.append((inicio, fim))
    normalizados.sort()
    if not normalizados:
        return []
    saida = [normalizados[0]]
    for inicio, fim in normalizados[1:]:
        atual_inicio, atual_fim = saida[-1]
        if inicio <= atual_fim:
            saida[-1] = (atual_inicio, max(atual_fim, fim))
        else:
            saida.append((inicio, fim))
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(mesclar=mesclar)
