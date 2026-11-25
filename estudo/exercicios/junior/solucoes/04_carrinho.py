"""Solucao de junior/04_carrinho.py. Tente resolver o enunciado antes de abrir."""


class Carrinho:
    def __init__(self) -> None:
        self._itens: list[dict] = []

    def adicionar(self, nome: str, preco: float, qtd: int = 1) -> None:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("nome invalido")
        if isinstance(preco, bool) or not isinstance(preco, (int, float)) or preco <= 0:
            raise ValueError("preco invalido")
        if isinstance(qtd, bool) or not isinstance(qtd, int) or qtd < 1:
            raise ValueError("quantidade invalida")
        nome = nome.strip()
        preco = float(preco)
        for item in self._itens:
            if item["nome"] == nome:
                if item["preco"] != preco:
                    raise ValueError("preco diferente")
                item["qtd"] += qtd
                return
        self._itens.append({"nome": nome, "preco": preco, "qtd": qtd})

    def total(self) -> float:
        return round(sum(item["preco"] * item["qtd"] for item in self._itens), 2)

    def quantidade(self) -> int:
        return sum(item["qtd"] for item in self._itens)

    def itens(self) -> list[dict]:
        return [dict(item) for item in self._itens]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(Carrinho=Carrinho)
