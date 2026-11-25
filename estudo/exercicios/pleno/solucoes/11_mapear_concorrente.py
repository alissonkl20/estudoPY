"""Solucao de pleno/11_mapear_concorrente.py. Tente resolver o enunciado antes de abrir."""

from concurrent.futures import ThreadPoolExecutor, as_completed


def mapear(func, itens: list, trabalhadores: int = 4) -> list:
    if isinstance(trabalhadores, bool) or not isinstance(trabalhadores, int) or trabalhadores < 1:
        raise ValueError("trabalhadores invalido")
    if not itens:
        return []

    resultados = [None] * len(itens)
    erros: dict[int, Exception] = {}
    with ThreadPoolExecutor(max_workers=trabalhadores) as executor:
        futuros = {
            executor.submit(func, item): indice for indice, item in enumerate(itens)
        }
        for futuro in as_completed(futuros):
            indice = futuros[futuro]
            try:
                resultados[indice] = futuro.result()
            except Exception as erro:
                erros[indice] = erro
    if erros:
        raise erros[min(erros)]
    return resultados


if __name__ == "__main__":
    from _rodar import rodar

    rodar(mapear=mapear)
