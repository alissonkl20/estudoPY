"""
Teste tecnico 22 — Sobrepor configuracao

Nivel pleno. Junte dicionarios em profundidade. Dict aninha. Qualquer
outro valor, inclusive list e None, e trocado pela camada de cima.
Nao altere os dicionarios recebidos, nem os dicts internos deles.

Implemente sobrepor(base, *camadas) -> dict.

Como testar:
    python3 pleno/22_sobrepor_config.py
"""

def sobrepor(base: dict, *camadas: dict) -> dict:
    return {}


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    base = {"a": 1, "b": {"c": 2, "d": 3}, "e": [1]}
    camada = {"b": {"c": 9}, "e": [2, 3], "f": None}
    resultado = sobrepor(base, camada)
    esperado = {"a": 1, "b": {"c": 9, "d": 3}, "e": [2, 3], "f": None}
    _verificar(resultado == esperado, f"merge, veio {resultado}", falhas)
    if resultado == esperado:
        resultado["b"]["d"] = 0
        resultado["e"].append(9)
        _verificar(base["b"]["d"] == 3 and base["e"] == [1], "copia profunda", falhas)
        _verificar(camada["b"]["c"] == 9, "camada original intacta", falhas)
    else:
        _verificar(False, "copia profunda", falhas)
        _verificar(False, "camada original intacta", falhas)

    segunda = {"b": {"d": 7}, "a": 4}
    coberto = sobrepor(base, camada, segunda)
    _verificar(
        isinstance(coberto, dict) and coberto.get("b") == {"c": 9, "d": 7},
        "terceira camada cobre a segunda",
        falhas,
    )
    _verificar(sobrepor({"a": 1}) == {"a": 1}, "sem camada devolve copia", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
