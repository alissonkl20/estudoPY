"""Solucao de pleno/08_analisar_logs.py. Tente resolver o enunciado antes de abrir."""

NIVEIS = ("INFO", "WARN", "ERROR")


def analisar(linhas: list[str]) -> dict:
    por_nivel = {nivel: 0 for nivel in NIVEIS}
    erros: dict[str, int] = {}
    total = 0
    invalidas = 0
    for linha in linhas:
        if not linha.strip():
            continue
        partes = linha.split()
        if len(partes) < 3:
            invalidas += 1
            continue
        _instante, nivel, *resto = partes
        if nivel not in por_nivel:
            invalidas += 1
            continue
        campos: dict[str, str] = {}
        valido = True
        for token in resto:
            if token.count("=") != 1:
                valido = False
                break
            chave, valor = token.split("=", 1)
            if not chave or valor == "":
                valido = False
                break
            campos[chave] = valor
        if not valido or "usuario" not in campos:
            invalidas += 1
            continue
        total += 1
        por_nivel[nivel] += 1
        if nivel == "ERROR":
            usuario = campos["usuario"]
            erros[usuario] = erros.get(usuario, 0) + 1
    return {
        "total": total,
        "invalidas": invalidas,
        "por_nivel": por_nivel,
        "erros_por_usuario": sorted(erros.items(), key=lambda item: (-item[1], item[0])),
    }


if __name__ == "__main__":
    from _rodar import rodar

    rodar(analisar=analisar)
