"""Solucao de junior/11_mascarar_cartao.py. Tente resolver o enunciado antes de abrir."""


def mascarar_cartao(numero: str) -> str:
    if not isinstance(numero, str):
        raise ValueError("numero invalido")
    limpo = numero.replace(" ", "").replace("-", "")
    if not limpo.isdigit() or len(limpo) != 16:
        raise ValueError("numero invalido")
    return f"**** **** **** {limpo[-4:]}"


if __name__ == "__main__":
    from _rodar import rodar

    rodar(mascarar_cartao=mascarar_cartao)
