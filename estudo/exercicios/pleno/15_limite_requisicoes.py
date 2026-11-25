"""
Teste tecnico 15 — Limite de requisicoes

Nivel pleno. Uma janela deslizante: no instante `agora`, contam as
requisicoes t em que agora - t < janela. Estouro nao grava a tentativa.

Implemente LimiteRequisicoes(maximo, janela).

- maximo e janela: int >= 1 (bool nao vale); senao ValueError
- permitir(agora) -> bool
- True grava a requisicao; False nao grava
- agora precisa ser int (bool nao vale)

Como testar:
    python3 pleno/15_limite_requisicoes.py
"""


class LimiteRequisicoes:
    def __init__(self, maximo: int, janela: int):
        self.maximo = maximo
        self.janela = janela

    def permitir(self, agora: int) -> bool:
        return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    try:
        LimiteRequisicoes(0, 10)
        _verificar(False, "maximo 0 deveria falhar", falhas)
    except ValueError:
        _verificar(True, "maximo 0 levanta ValueError", falhas)

    try:
        LimiteRequisicoes(True, 10)  # type: ignore[arg-type]
        _verificar(False, "bool nao e maximo", falhas)
    except ValueError:
        _verificar(True, "maximo bool levanta ValueError", falhas)

    limite = LimiteRequisicoes(2, 10)
    _verificar(limite.permitir(0), "primeira entra", falhas)
    _verificar(limite.permitir(1), "segunda entra", falhas)
    _verificar(not limite.permitir(2), "terceira estoura", falhas)
    _verificar(limite.permitir(10), "a do instante 0 saiu da janela", falhas)
    _verificar(not limite.permitir(10), "recusa nao ocupa vaga", falhas)

    try:
        limite.permitir(True)  # type: ignore[arg-type]
        _verificar(False, "bool nao e instante", falhas)
    except ValueError:
        _verificar(True, "instante bool levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
