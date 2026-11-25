"""
Logica junior 70 — Media sem extremos

Descarte um menor e um maior e tire a media do resto, com 2 casas. Menos de 3 numeros levanta ValueError.

Como testar:
    python3 logica/junior/70_media_sem_extremos.py
"""

def media_sem_extremos(nums: list[int]) -> float:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = media_sem_extremos([1, 2, 3, 4])
    _verificar(veio == 2.5, f"media_sem_extremos([1, 2, 3, 4]) -> 2.5, veio {veio!r}", falhas)
    veio = media_sem_extremos([1, 100, 2, 3])
    _verificar(veio == 2.5, f"media_sem_extremos([1, 100, 2, 3]) -> 2.5, veio {veio!r}", falhas)
    veio = media_sem_extremos([5, 5, 5])
    _verificar(veio == 5.0, f"media_sem_extremos([5, 5, 5]) -> 5.0, veio {veio!r}", falhas)
    try:
        media_sem_extremos([1, 2])
        _verificar(False, "media_sem_extremos([1, 2]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "media_sem_extremos([1, 2]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

