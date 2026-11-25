"""
Logica junior 71 — Acima da media

Devolva os numeros estritamente maiores que a media, na ordem original. Lista vazia devolve [].

Como testar:
    python3 logica/junior/71_acima_da_media.py
"""

def acima_da_media(nums: list[int]) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = acima_da_media([1, 2, 3])
    _verificar(veio == [3], f"acima_da_media([1, 2, 3]) -> [3], veio {veio!r}", falhas)
    veio = acima_da_media([1, 2, 3, 4])
    _verificar(veio == [3, 4], f"acima_da_media([1, 2, 3, 4]) -> [3, 4], veio {veio!r}", falhas)
    veio = acima_da_media([5, 5])
    _verificar(veio == [], f"acima_da_media([5, 5]) -> [], veio {veio!r}", falhas)
    veio = acima_da_media([])
    _verificar(veio == [], f"acima_da_media([]) -> [], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

