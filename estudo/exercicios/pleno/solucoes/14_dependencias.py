"""Solucao de pleno/14_dependencias.py. Tente resolver o enunciado antes de abrir."""


def ordenar(tarefas: dict[str, list[str]]) -> list[str]:
    restantes = {nome: set(pre) for nome, pre in tarefas.items()}
    for nome, pre in restantes.items():
        for item in pre:
            if item not in restantes:
                raise ValueError("dependencia desconhecida")
    saida: list[str] = []
    while restantes:
        prontas = sorted(nome for nome, pre in restantes.items() if not pre)
        if not prontas:
            raise ValueError("ciclo")
        escolhida = prontas[0]
        saida.append(escolhida)
        del restantes[escolhida]
        for pre in restantes.values():
            pre.discard(escolhida)
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(ordenar=ordenar)
