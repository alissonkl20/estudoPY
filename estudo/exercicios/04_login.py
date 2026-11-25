"""
Exercicio 04 — Login sem devolver a senha

O banco guarda o hash da senha, nunca o texto puro.
A rota de login procura o usuario e, se a senha bater, devolve so os dados publicos.

hash_senha ja esta pronta. Implemente autenticar(usuarios, email, senha).

Regras:
- email e comparado exatamente, sem ignorar maiusculas
- senha certa: retorne {"id", "nome", "email"}
- senha errada ou email inexistente: retorne None
- a resposta nao pode conter senha_hash

Como testar:
    python3 exercicios/04_login.py
"""

import hashlib


def hash_senha(senha: str) -> str:
    return hashlib.sha256(senha.encode()).hexdigest()


def autenticar(usuarios: list[dict], email: str, senha: str) -> dict | None:
    # seu codigo aqui
    return None


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    usuarios = [
        {
            "id": 1,
            "nome": "Ana",
            "email": "ana@email.com",
            "senha_hash": hash_senha("senha123"),
        },
        {
            "id": 2,
            "nome": "Bruno",
            "email": "bruno@email.com",
            "senha_hash": hash_senha("abc12345"),
        },
    ]

    ok = autenticar(usuarios, "ana@email.com", "senha123")
    _verificar(
        ok == {"id": 1, "nome": "Ana", "email": "ana@email.com"},
        f"login certo, veio {ok}",
        falhas,
    )
    _verificar(
        autenticar(usuarios, "ana@email.com", "errada") is None,
        "senha errada",
        falhas,
    )
    _verificar(
        autenticar(usuarios, "ninguem@email.com", "senha123") is None,
        "email inexistente",
        falhas,
    )
    _verificar(
        autenticar(usuarios, "ANA@email.com", "senha123") is None,
        "email e case sensitive",
        falhas,
    )
    _verificar(
        autenticar(usuarios, "bruno@email.com", "abc12345")
        == {"id": 2, "nome": "Bruno", "email": "bruno@email.com"},
        "segundo usuario",
        falhas,
    )

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
