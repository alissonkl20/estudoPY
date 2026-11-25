"""Solucao de pleno/09_corrigir_normalizar.py. Tente resolver o enunciado antes de abrir."""


def _ativo(valor):
    if isinstance(valor, bool):
        return valor
    if isinstance(valor, int) and valor in (0, 1):
        return bool(valor)
    if isinstance(valor, str) and valor.strip().lower() in {"true", "false"}:
        return valor.strip().lower() == "true"
    return None


def normalizar_usuarios(usuarios: list[dict]) -> list[dict]:
    vistos: set[str] = set()
    saida: list[dict] = []
    for usuario in usuarios:
        email = usuario.get("email")
        nome = usuario.get("nome")
        if not isinstance(email, str) or not isinstance(nome, str):
            continue
        email_norm = email.strip().lower()
        nome_norm = " ".join(parte.capitalize() for parte in nome.split())
        if "@" not in email_norm or not nome_norm or email_norm in vistos:
            continue
        ativo = _ativo(usuario.get("ativo"))
        if ativo is None:
            continue
        vistos.add(email_norm)
        saida.append({"nome": nome_norm, "email": email_norm, "ativo": ativo})
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(normalizar_usuarios=normalizar_usuarios)
