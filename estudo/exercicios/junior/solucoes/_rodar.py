"""Carrega o enunciado e troca as funcoes pela solucao antes de testar."""

import importlib.util
import inspect
from pathlib import Path


def rodar(**funcoes) -> None:
    origem = Path(inspect.stack()[1].filename).resolve()
    exercicio = origem.parents[1] / origem.name
    spec = importlib.util.spec_from_file_location(f"exercicio_{origem.stem}", exercicio)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"nao achei {exercicio}")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    for nome, funcao in funcoes.items():
        setattr(modulo, nome, funcao)
    modulo.testar()
