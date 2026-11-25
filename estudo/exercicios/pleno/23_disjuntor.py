"""
Teste tecnico 23 — Disjuntor

Nivel pleno. Depois de falhas demais, o disjuntor abre e para de chamar
a funcao por uma janela de tempo. O tempo e o int `agora`, nao o relogio.

Implemente DisjuntorAberto e Disjuntor(falhas_para_abrir, janela_aberto).

- os dois numeros sao int >= 1 (bool nao vale)
- executar(func, agora) chama func sem argumentos
- sucesso zera o contador e fecha o disjuntor
- excecao de func sobe depois de contar
- ao atingir falhas_para_abrir, abre ate agora + janela_aberto
- aberto e agora ainda nao chegou: levanta DisjuntorAberto e nao chama func
- agora >= liberacao: deixa uma chamada passar
- sucesso nessa chamada fecha
- falha nessa chamada abre de novo, a partir desse agora

Como testar:
    python3 pleno/23_disjuntor.py
"""


class DisjuntorAberto(Exception):
    pass


class Disjuntor:
    def __init__(self, falhas_para_abrir: int, janela_aberto: int):
        self.falhas_para_abrir = falhas_para_abrir
        self.janela_aberto = janela_aberto

    def executar(self, func, agora: int):
        return func()


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    chamadas = {"n": 0}

    def ok():
        chamadas["n"] += 1
        return "ok"

    def ruim():
        chamadas["n"] += 1
        raise RuntimeError("falhou")

    try:
        Disjuntor(0, 10)
        _verificar(False, "limite 0 deveria falhar", falhas)
    except ValueError:
        _verificar(True, "limite 0 levanta ValueError", falhas)

    disjuntor = Disjuntor(2, 10)
    _verificar(disjuntor.executar(ok, 0) == "ok", "fechado chama a funcao", falhas)
    try:
        disjuntor.executar(ruim, 1)
        _verificar(False, "falha da funcao deveria subir", falhas)
    except RuntimeError:
        _verificar(True, "primeira falha sobe", falhas)
    try:
        disjuntor.executar(ruim, 2)
        _verificar(False, "segunda falha deveria subir", falhas)
    except RuntimeError:
        _verificar(True, "segunda falha abre", falhas)

    antes = chamadas["n"]
    try:
        disjuntor.executar(ok, 5)
        _verificar(False, "aberto nao deveria chamar", falhas)
    except DisjuntorAberto:
        _verificar(chamadas["n"] == antes, "aberto nao chama a funcao", falhas)

    _verificar(disjuntor.executar(ok, 12) == "ok", "depois da janela uma chamada passa", falhas)
    _verificar(disjuntor.executar(ok, 13) == "ok", "sucesso fecha de vez", falhas)

    outro = Disjuntor(1, 10)
    try:
        outro.executar(ruim, 0)
    except RuntimeError:
        pass
    try:
        outro.executar(ruim, 10)
    except RuntimeError:
        pass
    antes = chamadas["n"]
    try:
        outro.executar(ok, 15)
        _verificar(False, "falha no meio aberto deveria reabrir", falhas)
    except DisjuntorAberto:
        _verificar(chamadas["n"] == antes, "reabriu e nao chamou", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
