"""
Teste tecnico 27 — Slugs unicos

Nivel pleno. Um slug e estavel, minusculo, sem acento e sem pontuacao.
Quando dois textos caem no mesmo slug, o segundo ganha sufixo -2, -3...

Implemente slugificar(texto) -> str e slugs_unicos(textos) -> list[str].

slugificar:
- minusculas
- acentos comuns do portugues viram a letra sem acento (ç vira c)
- o que nao e letra nem numero vira hifen
- hifens repetidos viram um; hifen na ponta sai
- texto que nao e str levanta ValueError

slugs_unicos:
- aplica slugificar em ordem
- slug vazio vira "item"
- o primeiro de cada base fica sem sufixo
- o proximo vira base-2, depois base-3
- devolve lista nova

Como testar:
    python3 pleno/27_slugs.py
"""


def slugificar(texto: str) -> str:
    return ""


def slugs_unicos(textos: list[str]) -> list[str]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(slugificar("São Paulo!") == "sao-paulo", "acento e pontuacao", falhas)
    _verificar(slugificar("  Olá, Mundo  ") == "ola-mundo", "espaco e virgula", falhas)
    _verificar(slugificar("Açaí") == "acai", "cedilha", falhas)
    _verificar(
        slugs_unicos(["Ana", "ana", "Ana!"]) == ["ana", "ana-2", "ana-3"],
        "sufixo nas repeticoes",
        falhas,
    )
    _verificar(
        slugs_unicos(["São Paulo", "!!!", "!!!"]) == ["sao-paulo", "item", "item-2"],
        "slug vazio vira item",
        falhas,
    )
    _verificar(slugs_unicos([]) == [], "lista vazia", falhas)

    try:
        slugificar(10)  # type: ignore[arg-type]
        _verificar(False, "numero deveria falhar", falhas)
    except ValueError:
        _verificar(True, "texto que nao e str levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
