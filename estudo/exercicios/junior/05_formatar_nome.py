"""
Teste tecnico 05 — Formatar nome

Nivel junior. Limpe o texto e deixe cada palavra com a inicial maiuscula.
"de" tambem vira "De": a regra e a mesma para todas as palavras.

Implemente formatar_nome(nome) -> str.

- tire espacos das pontas e junte espacos repetidos em um
- cada palavra comeca com maiuscula e o resto fica minusculo
- str vazia, ou so com espaco, levanta ValueError
- valor que nao e str levanta ValueError

Como testar:
    python3 junior/05_formatar_nome.py
"""


def formatar_nome(nome: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(formatar_nome("  ana   SILVA ") == "Ana Silva", "espacos e caixa", falhas)
    _verificar(formatar_nome("maria de souza") == "Maria De Souza", "cada palavra", falhas)
    _verificar(formatar_nome("joao") == "Joao", "uma palavra", falhas)

    for ruim in ("", "   ", 10):
        try:
            formatar_nome(ruim)  # type: ignore[arg-type]
            _verificar(False, f"{ruim!r} deveria falhar", falhas)
        except ValueError:
            _verificar(True, f"{ruim!r} levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
