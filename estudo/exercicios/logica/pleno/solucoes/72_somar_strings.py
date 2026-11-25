"""Solucao de logica/pleno/72_somar_strings.py. Tente resolver o enunciado antes de abrir."""

def somar_strings(a: str, b: str) -> str:
    def validar(texto: str) -> None:
        if not texto.isdigit() or (len(texto) > 1 and texto[0] == "0"):
            raise ValueError("numero invalido")

    validar(a)
    validar(b)
    i, j = len(a) - 1, len(b) - 1
    vai = 0
    saida = []
    while i >= 0 or j >= 0 or vai:
        total = vai
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        saida.append(str(total % 10))
        vai = total // 10
    return "".join(reversed(saida))


if __name__ == "__main__":
    from _rodar import rodar

    rodar(somar_strings=somar_strings)
