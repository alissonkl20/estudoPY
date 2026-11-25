"""Exercicio 01 — Validar cadastro

No backend, o corpo de uma requisicao chega como dicionario.
Antes de gravar, a API devolve a lista de erros. Lista vazia significa valido.

Implemente validar_cadastro(dados) -> list[str].

Regras, nesta ordem. Cada regra quebrada acrescenta exatamente uma mensagem:

1. nome: str com pelo menos 2 caracteres depois de remover espacos nas pontas
   mensagem: "nome invalido"
2. email: str com exatamente um "@", parte local e dominio nao vazios,
   e um ponto dentro do dominio
   mensagem: "email invalido"
3. senha: str com pelo menos 8 caracteres e pelo menos um digito
   mensagem: "senha invalida"
4. idade: int de verdade (bool nao vale) entre 18 e 120, inclusive
   mensagem: "idade invalida"

Como testar:
    python3 exercicios/01_validar_cadastro.py
"""
        #class formulario (object):

    

def validar_cadastro(dados: dict) -> list[str]:
    erros: list[str] = []
    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")
    idade = dados.get("idade")

    email_valido = False
    if isinstance(email, str) and email.count("@") == 1:
        parte_local, dominio = email.split("@")
        email_valido = bool(parte_local and dominio and "." in dominio)

    params = {
        "nome": isinstance(nome, str) and len(nome.strip()) >= 2,
        "email": email_valido,
        "senha": (
            isinstance(senha, str)
            and len(senha) >= 8
            and any(caractere.isdigit() for caractere in senha)
        ),
        "idade": (
            isinstance(idade, int)
            and not isinstance(idade, bool)
            and 18 <= idade <= 120
        ),
    }
    mensagens = {
        "nome": "nome invalido",
        "email": "email invalido",
        "senha": "senha invalida",
        "idade": "idade invalida",
    }

    for campo, valido in params.items():
        if not valido:
            erros.append(mensagens[campo])

    return erros


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
