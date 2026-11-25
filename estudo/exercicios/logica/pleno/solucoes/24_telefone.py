"""Solucao de logica/pleno/24_telefone.py. Tente resolver o enunciado antes de abrir."""

def telefone(digitos: str) -> list[str]:
    if digitos == "":
        return []
    mapa = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
    }
    if any(d not in mapa for d in digitos):
        raise ValueError("digito invalido")
    saida = [""]
    for digito in digitos:
        saida = [prefixo + letra for prefixo in saida for letra in mapa[digito]]
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(telefone=telefone)
