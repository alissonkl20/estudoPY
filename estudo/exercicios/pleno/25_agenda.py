"""
Teste tecnico 25 — Agenda de salas

Nivel pleno. Duas reservas da mesma sala conflitam quando os intervalos
se cruzam. Encostar e permitido: uma termina no instante em que a outra
comeca. Salas diferentes nao se enxergam.

Implemente Conflito e Agenda.

marcar(sala, inicio, fim, titulo)
- fim <= inicio levanta ValueError e nao grava
- bool nao vale como horario
- titulo vazio, depois do strip, levanta ValueError
- conflito levanta Conflito e nao grava
- listar(sala) devolve copias, ordenadas pelo inicio
- sala sem reserva devolve []

Como testar:
    python3 pleno/25_agenda.py
"""


class Conflito(Exception):
    pass


class Agenda:
    def marcar(self, sala: str, inicio: int, fim: int, titulo: str) -> None:
        return None

    def listar(self, sala: str) -> list[dict]:
        return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    agenda = Agenda()
    agenda.marcar("a", 1, 3, "daily")
    agenda.marcar("a", 3, 4, "depois")
    agenda.marcar("b", 1, 3, "outra")
    lista = agenda.listar("a")
    _verificar(
        lista
        == [
            {"titulo": "daily", "inicio": 1, "fim": 3},
            {"titulo": "depois", "inicio": 3, "fim": 4},
        ],
        f"encostar e permitido, veio {lista}",
        falhas,
    )
    _verificar(len(agenda.listar("b")) == 1, "outra sala nao conflita", falhas)
    if lista:
        copia = agenda.listar("a")
        copia[0]["titulo"] = "hack"
        _verificar(agenda.listar("a")[0]["titulo"] == "daily", "listar devolve copia", falhas)
    else:
        _verificar(False, "listar devolve copia", falhas)

    agenda.marcar("c", 10, 12, "tarde")
    agenda.marcar("c", 1, 2, "cedo")
    _verificar(
        [evento["titulo"] for evento in agenda.listar("c")] == ["cedo", "tarde"],
        "ordena pelo inicio",
        falhas,
    )

    try:
        agenda.marcar("a", 2, 5, "choque")
        _verificar(False, "sobreposicao deveria falhar", falhas)
    except Conflito:
        _verificar(len(agenda.listar("a")) == 2, "conflito nao grava", falhas)

    try:
        agenda.marcar("a", 5, 5, "ponto")
        _verificar(False, "fim igual ao inicio deveria falhar", falhas)
    except ValueError:
        _verificar(True, "intervalo vazio levanta ValueError", falhas)

    try:
        agenda.marcar("a", True, 2, "x")  # type: ignore[arg-type]
        _verificar(False, "bool nao e horario", falhas)
    except ValueError:
        _verificar(True, "horario bool levanta ValueError", falhas)

    _verificar(agenda.listar("vazia") == [], "sala sem reserva", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
