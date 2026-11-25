"""
Logica junior 75 — Snake para camel

A primeira palavra fica minuscula. As seguintes comecam com maiuscula. Separador e um underscore.

Como testar:
    python3 logica/junior/75_snake_para_camel.py
"""

def snake_para_camel(nome: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = snake_para_camel('ja_foi')
    _verificar(veio == 'jaFoi', f"snake_para_camel('ja_foi') -> 'jaFoi', veio {veio!r}", falhas)
    veio = snake_para_camel('ja')
    _verificar(veio == 'ja', f"snake_para_camel('ja') -> 'ja', veio {veio!r}", falhas)
    veio = snake_para_camel('a_b_c')
    _verificar(veio == 'aBC', f"snake_para_camel('a_b_c') -> 'aBC', veio {veio!r}", falhas)
    veio = snake_para_camel('')
    _verificar(veio == '', f"snake_para_camel('') -> '', veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

