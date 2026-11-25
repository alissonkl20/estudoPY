"""Solucao de pleno/23_disjuntor.py. Tente resolver o enunciado antes de abrir."""


class DisjuntorAberto(Exception):
    pass


class Disjuntor:
    def __init__(self, falhas_para_abrir: int, janela_aberto: int):
        if (
            isinstance(falhas_para_abrir, bool)
            or not isinstance(falhas_para_abrir, int)
            or falhas_para_abrir < 1
        ):
            raise ValueError("limite invalido")
        if isinstance(janela_aberto, bool) or not isinstance(janela_aberto, int) or janela_aberto < 1:
            raise ValueError("janela invalida")
        self.falhas_para_abrir = falhas_para_abrir
        self.janela_aberto = janela_aberto
        self._falhas = 0
        self._aberto_ate: int | None = None

    def executar(self, func, agora: int):
        if isinstance(agora, bool) or not isinstance(agora, int):
            raise ValueError("instante invalido")
        if self._aberto_ate is not None and agora < self._aberto_ate:
            raise DisjuntorAberto("aberto")
        meio_aberto = self._aberto_ate is not None
        try:
            resultado = func()
        except Exception:
            self._falhas += 1
            if self._falhas >= self.falhas_para_abrir or meio_aberto:
                self._aberto_ate = agora + self.janela_aberto
            raise
        self._falhas = 0
        self._aberto_ate = None
        return resultado


if __name__ == "__main__":
    from _rodar import rodar

    rodar(DisjuntorAberto=DisjuntorAberto, Disjuntor=Disjuntor)
