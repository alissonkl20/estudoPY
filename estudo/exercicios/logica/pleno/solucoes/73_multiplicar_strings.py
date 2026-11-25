"""Solucao de logica/pleno/73_multiplicar_strings.py. Tente resolver o enunciado antes de abrir."""

def multiplicar_strings(a: str, b: str) -> str:
    def validar(texto: str) -> None:
        if not texto.isdigit() or (len(texto) > 1 and texto[0] == "0"):
            raise ValueError("numero invalido")

    validar(a)
    validar(b)
    if a == "0" or b == "0":
        return "0"
    res = [0] * (len(a) + len(b))
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            soma = int(a[i]) * int(b[j]) + res[i + j + 1]
            res[i + j + 1] = soma % 10
            res[i + j] += soma // 10
    return "".join(str(d) for d in res).lstrip("0")


if __name__ == "__main__":
    from _rodar import rodar

    rodar(multiplicar_strings=multiplicar_strings)
