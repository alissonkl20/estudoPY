"""Solucao de logica/junior/11_primos_ate.py. Tente resolver o enunciado antes de abrir."""

def primos_ate(n: int) -> list[int]:
    saida = []
    for candidato in range(2, n + 1):
        primo = True
        i = 2
        while i * i <= candidato:
            if candidato % i == 0:
                primo = False
                break
            i += 1
        if primo:
            saida.append(candidato)
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(primos_ate=primos_ate)
