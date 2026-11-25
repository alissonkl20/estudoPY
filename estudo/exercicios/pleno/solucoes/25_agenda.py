"""Solucao de pleno/25_agenda.py. Tente resolver o enunciado antes de abrir."""


class Conflito(Exception):
    pass


class Agenda:
    def __init__(self) -> None:
        self._salas: dict[str, list[dict]] = {}

    def marcar(self, sala: str, inicio: int, fim: int, titulo: str) -> None:
        if (
            isinstance(inicio, bool)
            or isinstance(fim, bool)
            or not isinstance(inicio, int)
            or not isinstance(fim, int)
            or fim <= inicio
        ):
            raise ValueError("horario invalido")
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("titulo invalido")
        eventos = self._salas.setdefault(sala, [])
        for evento in eventos:
            if inicio < evento["fim"] and fim > evento["inicio"]:
                raise Conflito("conflito")
        eventos.append({"titulo": titulo, "inicio": inicio, "fim": fim})
        eventos.sort(key=lambda evento: evento["inicio"])

    def listar(self, sala: str) -> list[dict]:
        return [dict(evento) for evento in self._salas.get(sala, [])]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(Conflito=Conflito, Agenda=Agenda)
