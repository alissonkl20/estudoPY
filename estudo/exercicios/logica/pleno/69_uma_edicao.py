"""
Logica pleno 69 — Uma edicao de distancia

Verdadeiro se os textos sao iguais ou se uma insercao, remocao ou troca transforma um no outro.

Como testar:
    python3 logica/pleno/69_uma_edicao.py
"""

def uma_edicao(a: str, b: str) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = uma_edicao('pale', 'ple')
    _verificar(veio == True, f"uma_edicao('pale', 'ple') -> True, veio {veio!r}", falhas)
    veio = uma_edicao('pales', 'pale')
    _verificar(veio == True, f"uma_edicao('pales', 'pale') -> True, veio {veio!r}", falhas)
    veio = uma_edicao('pale', 'bale')
    _verificar(veio == True, f"uma_edicao('pale', 'bale') -> True, veio {veio!r}", falhas)
    veio = uma_edicao('pale', 'bake')
    _verificar(veio == False, f"uma_edicao('pale', 'bake') -> False, veio {veio!r}", falhas)
    veio = uma_edicao('a', 'a')
    _verificar(veio == True, f"uma_edicao('a', 'a') -> True, veio {veio!r}", falhas)
    veio = uma_edicao('', 'a')
    _verificar(veio == True, f"uma_edicao('', 'a') -> True, veio {veio!r}", falhas)
    veio = uma_edicao('', 'ab')
    _verificar(veio == False, f"uma_edicao('', 'ab') -> False, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

