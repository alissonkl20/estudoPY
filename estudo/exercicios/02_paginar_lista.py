"""
Exercicio 02 — Paginar uma lista

Listagens de API quase nunca devolvem a tabela inteira.
O cliente pede pagina e tamanho, e a API responde com um recorte e o total.

Implemente paginar(itens, pagina, por_pagina) -> dict.

Contrato:
- pagina comeca em 1
- por_pagina < 1 levanta ValueError
- pagina < 1 devolve "dados" vazio, sem erro
- pagina alem do fim tambem devolve "dados" vazio
- lista vazia tem total_paginas 0
- nao altere a lista original

Formato:
{
    "dados": [...],
    "pagina": pagina,
    "por_pagina": por_pagina,
    "total": quantidade de itens,
    "total_paginas": teto de total / por_pagina, ou 0 se nao houver itens,
}

Como testar:
    python3 exercicios/02_paginar_lista.py
"""


def paginar(itens: list, pagina: int, por_pagina: int) -> dict:
    # seu codigo aqui
    return {}


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
