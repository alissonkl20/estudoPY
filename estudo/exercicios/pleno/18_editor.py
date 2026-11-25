"""
Teste tecnico 18 — Editor com desfazer e refazer

Nivel pleno. Cada edicao vira um estado. Desfazer volta. Refazer avanca.
Uma edicao nova apaga o que dava para refazer.

Implemente Editor.

- texto comeca vazio
- inserir(trecho) cola no fim. trecho vazio levanta ValueError
- apagar(n) remove os n ultimos caracteres
- n < 1, bool, ou n maior que o texto: ValueError, texto intacto
- desfazer e refazer sem destino levantam ValueError e nao mudam o texto

Como testar:
    python3 pleno/18_editor.py
"""


class Editor:
    def __init__(self) -> None:
        self.texto = ""

    def inserir(self, trecho: str) -> None:
        return None

    def apagar(self, n: int) -> None:
        return None

    def desfazer(self) -> None:
        return None

    def refazer(self) -> None:
        return None


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    editor = Editor()
    editor.inserir("abc")
    editor.inserir("de")
    _verificar(editor.texto == "abcde", f"inseriu, veio {editor.texto!r}", falhas)
    editor.apagar(2)
    _verificar(editor.texto == "abc", "apagou dois", falhas)
    editor.desfazer()
    _verificar(editor.texto == "abcde", "desfez o apagar", falhas)
    editor.desfazer()
    _verificar(editor.texto == "abc", "desfez a segunda insercao", falhas)
    editor.refazer()
    _verificar(editor.texto == "abcde", "refez", falhas)
    editor.inserir("!")
    _verificar(editor.texto == "abcde!", "edicao nova", falhas)

    try:
        editor.refazer()
        _verificar(False, "refazer depois de editar deveria falhar", falhas)
    except ValueError:
        _verificar(editor.texto == "abcde!", "refazer ilegal nao mexe no texto", falhas)

    vazio = Editor()
    try:
        vazio.desfazer()
        _verificar(False, "desfazer vazio deveria falhar", falhas)
    except ValueError:
        _verificar(vazio.texto == "", "desfazer vazio nao mexe no texto", falhas)

    curto = Editor()
    curto.inserir("abc")
    try:
        curto.apagar(10)
        _verificar(False, "apagar demais deveria falhar", falhas)
    except ValueError:
        _verificar(curto.texto == "abc", "apagar demais nao grava", falhas)

    try:
        curto.apagar(True)  # type: ignore[arg-type]
        _verificar(False, "bool nao e quantidade", falhas)
    except ValueError:
        _verificar(True, "apagar bool levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
