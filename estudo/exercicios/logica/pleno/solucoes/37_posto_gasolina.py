"""Solucao de logica/pleno/37_posto_gasolina.py. Tente resolver o enunciado antes de abrir."""

def posto_gasolina(gas: list[int], custo: list[int]) -> int:
    if not gas or len(gas) != len(custo):
        return -1
    total = tanque = inicio = 0
    for i in range(len(gas)):
        total += gas[i] - custo[i]
        tanque += gas[i] - custo[i]
        if tanque < 0:
            inicio = i + 1
            tanque = 0
    if total < 0 or inicio == len(gas):
        return -1
    return inicio


if __name__ == "__main__":
    from _rodar import rodar

    rodar(posto_gasolina=posto_gasolina)
