"""Solucao de pleno/24_permissoes.py. Tente resolver o enunciado antes de abrir."""


class Acesso:
    def __init__(self, papeis: dict[str, list[str]], heranca: dict[str, list[str]]):
        self._perms = {nome: set(permissoes) for nome, permissoes in papeis.items()}
        self._heranca = {nome: list(pais) for nome, pais in heranca.items()}
        for nome, pais in self._heranca.items():
            if nome not in self._perms:
                raise ValueError("papel desconhecido")
            for pai in pais:
                if pai not in self._perms:
                    raise ValueError("papel desconhecido")
        self._fechamento: dict[str, set[str]] = {}
        for nome in self._perms:
            self._fechamento[nome] = self._resolver(nome, set())

    def _resolver(self, nome: str, visitando: set[str]) -> set[str]:
        if nome in self._fechamento:
            return set(self._fechamento[nome])
        if nome in visitando:
            raise ValueError("ciclo")
        visitando.add(nome)
        permissoes = set(self._perms[nome])
        for pai in self._heranca.get(nome, []):
            permissoes |= self._resolver(pai, visitando)
        visitando.remove(nome)
        return permissoes

    def pode(self, papeis_usuario: list[str], permissao: str) -> bool:
        for papel in papeis_usuario:
            if papel not in self._perms:
                raise ValueError("papel desconhecido")
            if permissao in self._fechamento[papel]:
                return True
        return False


if __name__ == "__main__":
    from _rodar import rodar

    rodar(Acesso=Acesso)
