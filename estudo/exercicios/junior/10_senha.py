"""
Teste tecnico 10 — Senha simples

Nivel junior. Devolva a lista do que faltou. Lista vazia significa senha aceita.
As mensagens saem sempre nesta ordem: curta, sem letra, sem numero.

Implemente validar_senha(senha) -> list[str].

- senha precisa ser str; senao ValueError
- menos de 6 caracteres: "curta"
- nenhuma letra: "sem letra"
- nenhum digito: "sem numero"
- uma senha pode falhar em mais de uma regra

Como testar:
    python3 junior/10_senha.py
"""


def validar_senha(senha: str) -> list[str]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(validar_senha("abc123") == [], "senha aceita", falhas)
    _verificar(validar_senha("abc") == ["curta", "sem numero"], "curta e sem numero", falhas)
    _verificar(validar_senha("123456") == ["sem letra"], "so digitos", falhas)
    _verificar(validar_senha("abcdef") == ["sem numero"], "so letras", falhas)
    _verificar(validar_senha("ab1") == ["curta"], "curta mas tem letra e numero", falhas)
    _verificar(
        validar_senha("") == ["curta", "sem letra", "sem numero"],
        "vazia falha nas tres",
        falhas,
    )

    try:
        validar_senha(123456)  # type: ignore[arg-type]
        _verificar(False, "numero deveria falhar", falhas)
    except ValueError:
        _verificar(True, "senha que nao e str levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
