"""Solucao do exercicio 01. Tente resolver o arquivo em exercicios/ antes de abrir."""


def validar_cadastro(dados: dict) -> list[str]:
    erros: list[str] = []

    nome = dados.get("nome")
    if not isinstance(nome, str) or len(nome.strip()) < 2:
        erros.append("nome invalido")

    email = dados.get("email")
    if not _email_valido(email):
        erros.append("email invalido")

    senha = dados.get("senha")
    if not isinstance(senha, str) or len(senha) < 8 or not any(c.isdigit() for c in senha):
        erros.append("senha invalida")

    idade = dados.get("idade")
    if type(idade) is not int or not 18 <= idade <= 120:
        erros.append("idade invalida")

    return erros


def _email_valido(email: object) -> bool:
    if not isinstance(email, str) or email.count("@") != 1:
        return False
    local, dominio = email.split("@")
    return bool(local) and "." in dominio


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    valido = validar_cadastro(
        {
            "nome": " Ana ",
            "email": "ana@email.com",
            "senha": "abcd1234",
            "idade": 18,
        }
    )
    _verificar(valido == [], f"cadastro valido, veio {valido}", falhas)

    _verificar(
        validar_cadastro(
            {"nome": " a ", "email": "ana@email.com", "senha": "abcd1234", "idade": 30}
        )
        == ["nome invalido"],
        "nome curto depois do strip",
        falhas,
    )
    _verificar(
        validar_cadastro(
            {"nome": "Ana", "email": "ana@email", "senha": "abcd1234", "idade": 30}
        )
        == ["email invalido"],
        "email sem ponto no dominio",
        falhas,
    )
    _verificar(
        validar_cadastro(
            {"nome": "Ana", "email": "ana@@email.com", "senha": "abcd1234", "idade": 30}
        )
        == ["email invalido"],
        "email com dois @",
        falhas,
    )
    _verificar(
        validar_cadastro(
            {"nome": "Ana", "email": "ana@email.com", "senha": "abcdefgh", "idade": 30}
        )
        == ["senha invalida"],
        "senha sem digito",
        falhas,
    )
    _verificar(
        validar_cadastro(
            {"nome": "Ana", "email": "ana@email.com", "senha": "abc123", "idade": 30}
        )
        == ["senha invalida"],
        "senha curta",
        falhas,
    )
    _verificar(
        validar_cadastro(
            {"nome": "Ana", "email": "ana@email.com", "senha": "abcd1234", "idade": 17}
        )
        == ["idade invalida"],
        "menor de idade",
        falhas,
    )
    _verificar(
        validar_cadastro(
            {"nome": "Ana", "email": "ana@email.com", "senha": "abcd1234", "idade": True}
        )
        == ["idade invalida"],
        "bool nao e idade",
        falhas,
    )
    _verificar(
        validar_cadastro({})
        == ["nome invalido", "email invalido", "senha invalida", "idade invalida"],
        "todos os campos ausentes",
        falhas,
    )
    _verificar(
        validar_cadastro(
            {"nome": "Lia", "email": "lia@site.com", "senha": "senha123", "idade": 120}
        )
        == [],
        "idade no limite de 120",
        falhas,
    )

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
