"""
Teste tecnico 06 — Resumo de vendas

Nivel pleno. O mesmo tipo de conta que um GROUP BY faria no banco,
feito em memoria, sem alterar a lista recebida.

Implemente resumir(vendas) -> list[dict].

Cada venda: {"vendedor": str, "valor": numero, "status": str}

- so entra status == "paga"
- valor: int ou float >= 0 (bool nao vale); senao ValueError
- agrupe por vendedor
- cada grupo: vendedor, total, quantidade, ticket_medio
- total e ticket_medio com 2 casas (round no fim, nao a cada soma)
- ticket_medio = total / quantidade
- ordene por total decrescente; empate desempata pelo nome do vendedor
- nenhuma paga: lista vazia

Como testar:
    python3 pleno/06_resumir_vendas.py
"""


def resumir(vendas: list[dict]) -> list[dict]:
    # seu codigo aqui
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    vendas = [
        {"vendedor": "Ana", "valor": 10, "status": "paga"},
        {"vendedor": "Ana", "valor": 20.5, "status": "paga"},
        {"vendedor": "Bruno", "valor": 40, "status": "paga"},
        {"vendedor": "Ana", "valor": 5, "status": "cancelada"},
        {"vendedor": "Caio", "valor": 40, "status": "paga"},
    ]
    copia = [dict(venda) for venda in vendas]
    resultado = resumir(vendas)
    _verificar(
        resultado
        == [
            {"vendedor": "Bruno", "total": 40.0, "quantidade": 1, "ticket_medio": 40.0},
            {"vendedor": "Caio", "total": 40.0, "quantidade": 1, "ticket_medio": 40.0},
            {"vendedor": "Ana", "total": 30.5, "quantidade": 2, "ticket_medio": 15.25},
        ],
        f"resumo ordenado, veio {resultado}",
        falhas,
    )
    _verificar(vendas == copia, "lista original intacta", falhas)
    _verificar(resumir([]) == [], "sem vendas", falhas)
    _verificar(
        resumir([{"vendedor": "Ana", "valor": 10, "status": "aberta"}]) == [],
        "ignora status que nao e paga",
        falhas,
    )

    try:
        resumir([{"vendedor": "Ana", "valor": True, "status": "paga"}])
        _verificar(False, "bool deveria levantar ValueError", falhas)
    except ValueError:
        _verificar(True, "valor bool levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
