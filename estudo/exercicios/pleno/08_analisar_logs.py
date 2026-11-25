"""
Teste tecnico 08 — Analisar logs

Nivel pleno. Cada linha valida tem este formato, separado por espacos:

    2024-03-01T10:00:00 INFO usuario=ana acao=login

- o primeiro campo e o instante
- o segundo e o nivel: INFO, WARN ou ERROR
- o resto sao pares chave=valor, sem espaco dentro do valor
- toda linha valida tem a chave usuario

Implemente analisar(linhas) -> dict:

    {
        "total": int,
        "invalidas": int,
        "por_nivel": {"INFO": int, "WARN": int, "ERROR": int},
        "erros_por_usuario": [("ana", 2), ("bruno", 1)],
    }

- linha vazia ou so com espaco e ignorada
- linha invalida soma em invalidas e nao entra no total
- erros_por_usuario so conta nivel ERROR
- a lista vai do usuario com mais erros para o com menos
- empate desempata pelo nome, em ordem alfabetica

Como testar:
    python3 pleno/08_analisar_logs.py
"""


def analisar(linhas: list[str]) -> dict:
    # seu codigo aqui
    return {
        "total": 0,
        "invalidas": 0,
        "por_nivel": {"INFO": 0, "WARN": 0, "ERROR": 0},
        "erros_por_usuario": [],
    }


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    linhas = [
        "2024-03-01T10:00:00 INFO usuario=ana acao=login",
        "2024-03-01T10:01:00 ERROR usuario=ana codigo=500",
        "2024-03-01T10:02:00 ERROR usuario=bruno codigo=404",
        "2024-03-01T10:03:00 ERROR usuario=ana codigo=500",
        "lixo",
        "",
        "   ",
        "2024-03-01T10:04:00 DEBUG usuario=ana",
        "2024-03-01T10:05:00 WARN usuario=caio fila=cheia",
        "2024-03-01T10:06:00 ERROR codigo=500",
        "2024-03-01T10:07:00 INFO usuario=duda",
    ]
    resultado = analisar(linhas)
    _verificar(
        resultado
        == {
            "total": 6,
            "invalidas": 3,
            "por_nivel": {"INFO": 2, "WARN": 1, "ERROR": 3},
            "erros_por_usuario": [("ana", 2), ("bruno", 1)],
        },
        f"resumo, veio {resultado}",
        falhas,
    )

    empate = analisar(
        [
            "2024-03-01T10:00:00 ERROR usuario=bruno codigo=1",
            "2024-03-01T10:01:00 ERROR usuario=ana codigo=1",
        ]
    )
    _verificar(
        empate["erros_por_usuario"] == [("ana", 1), ("bruno", 1)],
        "empate ordena pelo nome",
        falhas,
    )
    _verificar(analisar([])["total"] == 0, "sem linhas", falhas)
    _verificar(analisar(["", "  "])["invalidas"] == 0, "branco nao e invalida", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
