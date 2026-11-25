"""
Logica junior 76 — Parenteses simples

So o par () importa. Outros caracteres sao ignorados. Vazio e balanceado.

Como testar:
    python3 logica/junior/76_parenteses_simples.py
"""

def parenteses_simples(texto: str) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = parenteses_simples('()')
    _verificar(veio == True, f"parenteses_simples('()') -> True, veio {veio!r}", falhas)
    veio = parenteses_simples('a(b)c')
    _verificar(veio == True, f"parenteses_simples('a(b)c') -> True, veio {veio!r}", falhas)
    veio = parenteses_simples(')(')
    _verificar(veio == False, f"parenteses_simples(')(') -> False, veio {veio!r}", falhas)
    veio = parenteses_simples('((')
    _verificar(veio == False, f"parenteses_simples('((') -> False, veio {veio!r}", falhas)
    veio = parenteses_simples('')
    _verificar(veio == True, f"parenteses_simples('') -> True, veio {veio!r}", falhas)
    veio = parenteses_simples('(]')
    _verificar(veio == False, f"parenteses_simples('(]') -> False, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

