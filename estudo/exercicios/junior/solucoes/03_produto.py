"""Solucao de junior/03_produto.py. Tente resolver o enunciado antes de abrir."""


class Produto:
    def __init__(self, nome: str, preco: float):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("nome invalido")
        if isinstance(preco, bool) or not isinstance(preco, (int, float)) or preco <= 0:
            raise ValueError("preco invalido")
        self.nome = nome.strip()
        self.preco = preco

    def aplicar_desconto(self, percentual: int) -> float:
        if isinstance(percentual, bool) or not isinstance(percentual, int) or not 0 <= percentual <= 50:
            raise ValueError("percentual invalido")
        return round(self.preco * (1 - percentual / 100), 2)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(Produto=Produto)
