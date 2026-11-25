"""Solucao de junior/10_senha.py. Tente resolver o enunciado antes de abrir."""


def validar_senha(senha: str) -> list[str]:
    if not isinstance(senha, str):
        raise ValueError("senha invalida")
    erros = []
    if len(senha) < 6:
        erros.append("curta")
    if not any(caractere.isalpha() for caractere in senha):
        erros.append("sem letra")
    if not any(caractere.isdigit() for caractere in senha):
        erros.append("sem numero")
    return erros


if __name__ == "__main__":
    from _rodar import rodar

    rodar(validar_senha=validar_senha)
