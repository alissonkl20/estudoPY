"""
Logica pleno 24 — Letras do telefone

2=abc, 3=def, 4=ghi, 5=jkl, 6=mno, 7=pqrs, 8=tuv, 9=wxyz. Devolva as combinacoes em ordem. Vazio devolve []. 0 ou 1 levanta ValueError.

Como testar:
    python3 logica/pleno/24_telefone.py
"""

def telefone(digitos: str) -> list[str]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = telefone('2')
    _verificar(veio == ['a', 'b', 'c'], f"telefone('2') -> ['a', 'b', 'c'], veio {veio!r}", falhas)
    veio = telefone('23')
    _verificar(veio == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'], f"telefone('23') -> ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'], veio {veio!r}", falhas)
    veio = telefone('')
    _verificar(veio == [], f"telefone('') -> [], veio {veio!r}", falhas)
    try:
        telefone('1')
        _verificar(False, "telefone('1') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "telefone('1') levanta ValueError", falhas)
    try:
        telefone('20')
        _verificar(False, "telefone('20') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "telefone('20') levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

