"""Solucao de logica/junior/56_par_ou_impar.py. Tente resolver o enunciado antes de abrir."""

def par_ou_impar(n: int) -> str:
    if n % 2 == 0:
        return "par"
    return "impar"


if __name__ == "__main__":
    from _rodar import rodar

    rodar(par_ou_impar=par_ou_impar)
