"""
Teste tecnico 16 — Diff de registros

Nivel pleno. Compare duas listas de dicionarios pela chave id.
Nao altere as listas recebidas.

Implemente diff(antes, depois) -> dict com:
    {"adicionados": [...], "removidos": [...], "alterados": [...]}

Os tres valores sao listas de id.
- adicionados e alterados seguem a ordem de `depois`
- removidos segue a ordem de `antes`
- mesmo id com conteudo diferente entra em alterados
- id repetido na mesma lista levanta ValueError
- registro sem id levanta ValueError

Como testar:
    python3 pleno/16_diff_registros.py
"""


def diff(antes: list[dict], depois: list[dict]) -> dict:
    return {"adicionados": [], "removidos": [], "alterados": []}


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    antes = [
        {"id": 1, "nome": "Ana"},
        {"id": 2, "nome": "Bia"},
        {"id": 4, "nome": "Duda"},
    ]
    depois = [
        {"id": 2, "nome": "Bianca"},
        {"id": 4, "nome": "Duda", "idade": 3},
        {"id": 3, "nome": "Caio"},
    ]
    copia_antes = [dict(item) for item in antes]
    resultado = diff(antes, depois)
    _verificar(
        resultado
        == {"adicionados": [3], "removidos": [1], "alterados": [2, 4]},
        f"diff, veio {resultado}",
        falhas,
    )
    _verificar(antes == copia_antes, "lista original intacta", falhas)
    _verificar(
        diff([{"id": 1, "nome": "Ana"}], [{"id": 1, "nome": "Ana"}])
        == {"adicionados": [], "removidos": [], "alterados": []},
        "iguais nao mudam",
        falhas,
    )

    try:
        diff([{"id": 1}, {"id": 1}], [])
        _verificar(False, "id repetido deveria falhar", falhas)
    except ValueError:
        _verificar(True, "id repetido levanta ValueError", falhas)

    try:
        diff([{"nome": "Ana"}], [])
        _verificar(False, "sem id deveria falhar", falhas)
    except ValueError:
        _verificar(True, "sem id levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
