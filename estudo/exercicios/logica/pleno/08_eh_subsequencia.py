"""
Logica pleno 08 — E subsequencia

Verdadeiro se da para formar padrao apagando letras de texto, sem mudar a ordem. Padrao vazio e verdadeiro.

Como testar:
    python3 logica/pleno/08_eh_subsequencia.py
"""

def eh_subsequencia(padrao: str, texto: str) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = eh_subsequencia('ace', 'abcde')
    _verificar(veio == True, f"eh_subsequencia('ace', 'abcde') -> True, veio {veio!r}", falhas)
    veio = eh_subsequencia('axc', 'ahbgdc')
    _verificar(veio == False, f"eh_subsequencia('axc', 'ahbgdc') -> False, veio {veio!r}", falhas)
    veio = eh_subsequencia('', 'abc')
    _verificar(veio == True, f"eh_subsequencia('', 'abc') -> True, veio {veio!r}", falhas)
    veio = eh_subsequencia('abc', '')
    _verificar(veio == False, f"eh_subsequencia('abc', '') -> False, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

