"""Solucao de pleno/03_decorador_tentativas.py. Tente resolver o enunciado antes de abrir."""

import functools


def tentar(vezes: int = 3, excecoes: tuple[type[BaseException], ...] = (Exception,)):
    if vezes < 1:
        raise ValueError("vezes invalido")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ultimo: BaseException | None = None
            for _ in range(vezes):
                try:
                    return func(*args, **kwargs)
                except excecoes as erro:
                    ultimo = erro
            if ultimo is None:
                raise RuntimeError("nenhuma tentativa executada")
            raise ultimo

        return wrapper

    return decorator


if __name__ == "__main__":
    from _rodar import rodar

    rodar(tentar=tentar)
