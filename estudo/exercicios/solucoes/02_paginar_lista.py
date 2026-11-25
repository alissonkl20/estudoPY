"""Solucao do exercicio 02. Tente resolver o arquivo em exercicios/ antes de abrir."""


def paginar(itens: list, pagina: int, por_pagina: int) -> dict:
    if por_pagina < 1:
        raise ValueError("por_pagina deve ser >= 1")

    total = len(itens)
    total_paginas = (total + por_pagina - 1) // por_pagina if total else 0
    if pagina < 1:
        dados: list = []
    else:
        inicio = (pagina - 1) * por_pagina
        dados = itens[inicio : inicio + por_pagina]

    return {
        "dados": dados,
        "pagina": pagina,
        "por_pagina": por_pagina,
        "total": total,
        "total_paginas": total_paginas,
    }


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    itens = list(range(10))

    pagina1 = paginar(itens, 1, 3)
    _verificar(
        pagina1
        == {
            "dados": [0, 1, 2],
            "pagina": 1,
            "por_pagina": 3,
            "total": 10,
            "total_paginas": 4,
        },
        f"primeira pagina, veio {pagina1}",
        falhas,
    )

    ultima = paginar(itens, 4, 3)
    _verificar(ultima["dados"] == [9], f"ultima pagina, veio {ultima['dados']}", falhas)
    _verificar(ultima["total_paginas"] == 4, "total de paginas continua 4", falhas)

    alem = paginar(itens, 5, 3)
    _verificar(alem["dados"] == [] and alem["total"] == 10, "pagina alem do fim", falhas)

    _verificar(paginar(itens, 0, 3)["dados"] == [], "pagina 0 nao devolve dados", falhas)
    _verificar(paginar([], 1, 10)["total_paginas"] == 0, "lista vazia tem 0 paginas", falhas)
    _verificar(itens == list(range(10)), "lista original intacta", falhas)

    try:
        paginar(itens, 1, 0)
        _verificar(False, "por_pagina 0 deveria levantar ValueError", falhas)
    except ValueError:
        _verificar(True, "por_pagina 0 levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
