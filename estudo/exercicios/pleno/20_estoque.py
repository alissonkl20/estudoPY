"""
Teste tecnico 20 — Reserva de estoque

Nivel pleno. Reservar ja tira do disponivel, para duas reservas nao
venderem a mesma unidade. Confirmar encerra a reserva. Cancelar devolve.

Implemente Estoque(saldo).

- saldo e copiado; o dict recebido nao muda
- quantidade negativa no construtor, ou bool, levanta ValueError
- reservar(sku, qtd) -> id "r1", "r2", ... na ordem das reservas
- qtd < 1 ou bool: ValueError
- sku desconhecido ou quantidade acima do disponivel: ValueError, nada muda
- confirmar(id) so esquece a reserva; o disponivel continua igual
- cancelar(id) devolve a quantidade
- id inexistente, ou ja confirmado/cancelado, levanta ValueError
- disponivel(sku) devolve o que ainda pode ser reservado

Como testar:
    python3 pleno/20_estoque.py
"""


class Estoque:
    def __init__(self, saldo: dict[str, int]):
        self.saldo = saldo

    def disponivel(self, sku: str) -> int:
        return 0

    def reservar(self, sku: str, qtd: int) -> str:
        return ""

    def confirmar(self, reserva_id: str) -> None:
        return None

    def cancelar(self, reserva_id: str) -> None:
        return None


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    saldo = {"caneta": 10, "lapis": 2}
    estoque = Estoque(saldo)
    primeira = estoque.reservar("caneta", 4)
    segunda = estoque.reservar("lapis", 1)
    _verificar(primeira == "r1" and segunda == "r2", f"ids, veio {primeira}, {segunda}", falhas)
    _verificar(saldo == {"caneta": 10, "lapis": 2}, "dict original intacto", falhas)
    _verificar(estoque.disponivel("caneta") == 6, "reserva ja desconta", falhas)

    try:
        estoque.reservar("caneta", 7)
        _verificar(False, "estoque curto deveria falhar", falhas)
    except ValueError:
        _verificar(estoque.disponivel("caneta") == 6, "falha nao desconta", falhas)

    estoque.confirmar(primeira)
    _verificar(estoque.disponivel("caneta") == 6, "confirmar nao devolve", falhas)
    try:
        estoque.cancelar(primeira)
        _verificar(False, "cancelar confirmada deveria falhar", falhas)
    except ValueError:
        _verificar(estoque.disponivel("caneta") == 6, "confirmada nao volta", falhas)

    estoque.cancelar(segunda)
    _verificar(estoque.disponivel("lapis") == 2, "cancelar devolve", falhas)

    try:
        estoque.reservar("caneta", True)  # type: ignore[arg-type]
        _verificar(False, "bool nao e quantidade", falhas)
    except ValueError:
        _verificar(True, "quantidade bool levanta ValueError", falhas)

    try:
        estoque.disponivel("borracha")
        _verificar(False, "sku ausente deveria falhar", falhas)
    except ValueError:
        _verificar(True, "sku ausente levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
