"""
Teste tecnico 02 — Tirar repetidos

Nivel junior. Percorra a lista uma vez e fique com a primeira vez
que cada valor aparece.

Implemente unicos(itens) -> list.

- [1, 2, 2, 1, 3] devolve [1, 2, 3]
- "A" e "a" sao valores diferentes
- lista vazia devolve []
- nao altere a lista recebida

Como testar:
    python3 junior/02_unicos.py
"""


from unittest import result

def unicos(itens: list) -> list:
    # Cria um conjunto vazio para armazenar os valores
    # que já foram encontrados.
    vistos = set()

    # Cria uma lista vazia para guardar os valores únicos,
    # mantendo a ordem em que aparecem na lista original.
    resultado = []

    # Percorre cada elemento da lista recebida pela função.
    for item in itens:

        # Verifica se o elemento atual ainda não está
        # no conjunto 'vistos'.
        if item not in vistos:

            # Adiciona o elemento ao conjunto,
            # para sabermos que já foi encontrado.
            vistos.add(item)

            # Adiciona o elemento à lista final.
            resultado.append(item)

    # Devolve a lista com os elementos únicos.
    return resultado



def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    dados = [1, 2, 2, 1, 3]
    copia = list(dados)
    _verificar(unicos(dados) == [1, 2, 3], "mantem a primeira ocorrencia", falhas)
    _verificar(dados == copia, "lista original intacta", falhas)
    _verificar(unicos(["A", "a", "A"]) == ["A", "a"], "maiuscula e minuscula", falhas)
    _verificar(unicos([]) == [], "lista vazia", falhas)
    _verificar(unicos(["ana", "ana"]) == ["ana"], "texto repetido", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
