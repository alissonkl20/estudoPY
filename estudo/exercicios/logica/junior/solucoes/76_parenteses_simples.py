"""Solucao de logica/junior/76_parenteses_simples.py. Tente resolver o enunciado antes de abrir."""

def parenteses_simples(texto: str) -> bool:
    saldo = 0
    for ch in texto:
        if ch == "(":
            saldo += 1
        elif ch == ")":
            saldo -= 1
            if saldo < 0:
                return False
    return saldo == 0


if __name__ == "__main__":
    from _rodar import rodar

    rodar(parenteses_simples=parenteses_simples)
