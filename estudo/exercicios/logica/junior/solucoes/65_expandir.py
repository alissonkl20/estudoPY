"""Solucao de logica/junior/65_expandir.py. Tente resolver o enunciado antes de abrir."""

def expandir(partes: list) -> str:
    saida = []
    for par in partes:
        if not isinstance(par, (list, tuple)) or len(par) != 2:
            raise ValueError("grupo invalido")
        caractere, quantidade = par
        if not isinstance(caractere, str) or len(caractere) != 1:
            raise ValueError("caractere invalido")
        if isinstance(quantidade, bool) or not isinstance(quantidade, int) or quantidade < 1:
            raise ValueError("quantidade invalida")
        saida.append(caractere * quantidade)
    return "".join(saida)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(expandir=expandir)
