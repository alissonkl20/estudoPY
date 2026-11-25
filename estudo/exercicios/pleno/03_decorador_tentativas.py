"""
Teste tecnico 03 — Decorador de tentativas

Nivel pleno. O decorador nao conhece a funcao que vai envolver.
Ele so repete a chamada quando a excecao esta na lista permitida.

Implemente tentar(vezes=3, excecoes=(Exception,)).

- vezes < 1 levanta ValueError na hora de decorar
- excecao permitida: tenta de novo, ate `vezes`
- esgotou as tentativas: levanta a ultima excecao
- excecao de fora da lista: propaga na hora, sem gastar as outras tentativas
- preserve __name__ da funcao original (functools.wraps)

Como testar:
    python3 pleno/03_decorador_tentativas.py
"""


def tentar(vezes: int = 3, excecoes: tuple[type[BaseException], ...] = (Exception,)):
    # seu codigo aqui
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    chamadas = {"instavel": 0, "dados": 0, "rede": 0}

    @tentar(vezes=3, excecoes=(TimeoutError,))
    def instavel():
        chamadas["instavel"] += 1
        if chamadas["instavel"] < 3:
            raise TimeoutError("rede")
        return "ok"

    try:
        veio = instavel()
    except Exception as erro:
        _verificar(False, f"sucesso na terceira tentativa, veio erro {erro}", falhas)
    else:
        _verificar(veio == "ok", "sucesso na terceira tentativa", falhas)
        _verificar(chamadas["instavel"] == 3, "chamou tres vezes", falhas)
    _verificar(instavel.__name__ == "instavel", "preserva __name__", falhas)

    @tentar(vezes=4, excecoes=(TimeoutError,))
    def dados_ruins(codigo):
        chamadas["dados"] += 1
        raise ValueError(codigo)

    try:
        dados_ruins("x")
        _verificar(False, "ValueError deveria passar direto", falhas)
    except ValueError:
        _verificar(chamadas["dados"] == 1, "nao repetiu excecao fora da lista", falhas)

    @tentar(vezes=2, excecoes=(TimeoutError,))
    def rede():
        chamadas["rede"] += 1
        raise TimeoutError("caiu")

    try:
        rede()
        _verificar(False, "deveria levantar TimeoutError", falhas)
    except TimeoutError as erro:
        _verificar(chamadas["rede"] == 2 and str(erro) == "caiu", "ultima excecao", falhas)

    try:

        @tentar(vezes=0)
        def nunca():
            return 1

        _verificar(False, "vezes 0 deveria levantar ValueError", falhas)
    except ValueError:
        _verificar(True, "vezes 0 levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
