"""Solucao do exercicio 04. Tente resolver o arquivo em exercicios/ antes de abrir."""

import hashlib


def hash_senha(senha: str) -> str:
    return hashlib.sha256(senha.encode()).hexdigest()


def autenticar(usuarios: list[dict], email: str, senha: str) -> dict | None:
    senha_hash = hash_senha(senha)
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha_hash"] == senha_hash:
            return {
                "id": usuario["id"],
                "nome": usuario["nome"],
                "email": usuario["email"],
            }
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
