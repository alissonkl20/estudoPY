"""Solucao de logica/pleno/48_menor_numero.py. Tente resolver o enunciado antes de abrir."""

def menor_numero(numero: str, k: int) -> str:
    if k < 0 or k > len(numero) or not numero.isdigit():
        raise ValueError("entrada invalida")
    pilha = []
    for digito in numero:
        while k and pilha and pilha[-1] > digito:
            pilha.pop()
            k -= 1
        pilha.append(digito)
    while k:
        pilha.pop()
        k -= 1
    return "".join(pilha).lstrip("0") or "0"


if __name__ == "__main__":
    from _rodar import rodar

    rodar(menor_numero=menor_numero)
