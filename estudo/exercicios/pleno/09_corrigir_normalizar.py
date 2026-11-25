"""
Teste tecnico 09 — Corrigir normalizacao de usuarios

Nivel pleno. O codigo abaixo roda, mas o resultado esta errado.
Os testes sao o contrato. Corrija a funcao sem mudar os testes.

Contrato de normalizar_usuarios(usuarios) -> list[dict]:
- devolve uma lista nova
- nao altera a lista recebida nem os dicionarios dela
- a saida so tem as chaves nome, email e ativo
- email: strip e minusculo; sem "@" o usuario e descartado
- nome: strip, espacos repetidos viram um, cada palavra comeca maiuscula
- ativo aceita bool, 1, 0 e os textos "true" e "false" em qualquer caixa
- outro ativo descarta o usuario
- email repetido, depois de normalizar, fica so a primeira ocorrencia
- a ordem dos usuarios mantidos e a ordem de entrada
- nome ou email que nao sejam str descartam o usuario

Como testar:
    python3 pleno/09_corrigir_normalizar.py
"""

import copy


def normalizar_usuarios(usuarios: list[dict]) -> list[dict]:
    # Este codigo tem defeitos de proposito. Faca os testes passarem.
    saida = []
    for usuario in usuarios:
        email = str(usuario.get("email", "")).lower()
        nome = str(usuario.get("nome", "")).title()
        if "@" in email:
            usuario["email"] = email
            usuario["nome"] = nome
            saida.append(usuario)
    return saida


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    originais = [
        {"nome": " ana silva ", "email": " Ana@Email.com ", "ativo": "TRUE", "extra": 1},
        {"nome": "Bruno", "email": "bruno@email.com", "ativo": 1},
        {"nome": "Caio", "email": "sem-email", "ativo": True},
        {"nome": "Ana", "email": "ana@email.com", "ativo": False},
        {"nome": "Duda", "email": "duda@email.com", "ativo": "sim"},
        {"nome": "Eva", "email": "eva@email.com", "ativo": 0},
        {"email": "sem-nome@email.com", "ativo": True},
        {"nome": "Lia", "email": "lia@email.com", "ativo": False},
        {"nome": 10, "email": "num@email.com", "ativo": True},
    ]
    copia = copy.deepcopy(originais)
    resultado = normalizar_usuarios(originais)

    _verificar(originais == copia, "entrada original intacta", falhas)
    _verificar(
        resultado
        == [
            {"nome": "Ana Silva", "email": "ana@email.com", "ativo": True},
            {"nome": "Bruno", "email": "bruno@email.com", "ativo": True},
            {"nome": "Eva", "email": "eva@email.com", "ativo": False},
            {"nome": "Lia", "email": "lia@email.com", "ativo": False},
        ],
        f"normalizados, veio {resultado}",
        falhas,
    )
    _verificar(
        all(set(usuario) == {"nome", "email", "ativo"} for usuario in resultado),
        "so os tres campos",
        falhas,
    )
    _verificar(normalizar_usuarios([]) == [], "lista vazia", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
