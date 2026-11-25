"""
Logica junior 74 — Camel para snake

Coloque "_" antes de cada maiuscula, exceto no inicio, e deixe tudo minusculo.

Como testar:
    python3 logica/junior/74_camel_para_snake.py
"""

def camel_para_snake(nome: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = camel_para_snake('somaTotal')
    _verificar(veio == 'soma_total', f"camel_para_snake('somaTotal') -> 'soma_total', veio {veio!r}", falhas)
    veio = camel_para_snake('A')
    _verificar(veio == 'a', f"camel_para_snake('A') -> 'a', veio {veio!r}", falhas)
    veio = camel_para_snake('jaFoiLa')
    _verificar(veio == 'ja_foi_la', f"camel_para_snake('jaFoiLa') -> 'ja_foi_la', veio {veio!r}", falhas)
    veio = camel_para_snake('ja')
    _verificar(veio == 'ja', f"camel_para_snake('ja') -> 'ja', veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

