"""
Teste tecnico 07 — Cache LRU

Nivel pleno. Capacidade fixa. O item menos usado recentemente sai
quando entra um novo e o cache esta cheio. Nao use functools.lru_cache.

Implemente CacheLRU.

- capacidade < 1, ou que nao seja int, levanta ValueError (bool nao vale)
- get de chave ausente devolve None
- get de chave presente devolve o valor e marca como recente
- put de chave nova, com cache cheio, remove a menos recente
- put de chave que ja existe atualiza o valor, nao aumenta o tamanho
  e marca como recente
- len(cache) e a quantidade de chaves guardadas
- None nao e um valor valido para guardar; get usa None so para "nao achei"

Como testar:
    python3 pleno/07_cache_lru.py
"""


class CacheLRU:
    def __init__(self, capacidade: int):
        # seu codigo aqui
        self.capacidade = capacidade

    def get(self, chave):
        # seu codigo aqui
        return None

    def put(self, chave, valor) -> None:
        # seu codigo aqui
        return None

    def __len__(self) -> int:
        # seu codigo aqui
        return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    try:
        CacheLRU(0)
        _verificar(False, "capacidade 0 deveria falhar", falhas)
    except ValueError:
        _verificar(True, "capacidade 0 levanta ValueError", falhas)

    try:
        CacheLRU(True)  # type: ignore[arg-type]
        _verificar(False, "bool nao e capacidade", falhas)
    except ValueError:
        _verificar(True, "capacidade bool levanta ValueError", falhas)

    cache = CacheLRU(2)
    cache.put("a", 1)
    cache.put("b", 2)
    _verificar(cache.get("a") == 1, "get devolve o valor", falhas)
    cache.put("c", 3)
    _verificar(cache.get("b") is None, "b saiu porque era o menos recente", falhas)
    _verificar(cache.get("a") == 1 and cache.get("c") == 3, "a e c ficaram", falhas)
    _verificar(len(cache) == 2, f"tamanho 2, veio {len(cache)}", falhas)

    cache.put("a", 9)
    _verificar(cache.get("a") == 9 and len(cache) == 2, "atualizar nao cresce", falhas)
    cache.put("d", 4)
    _verificar(cache.get("c") is None, "c saiu depois que a foi renovada", falhas)
    _verificar(cache.get("d") == 4, "d entrou", falhas)

    unico = CacheLRU(1)
    unico.put("x", 1)
    unico.put("y", 2)
    _verificar(unico.get("x") is None and unico.get("y") == 2, "capacidade 1", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
