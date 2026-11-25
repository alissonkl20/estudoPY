"""Solucao de logica/pleno/16_sudoku_valido.py. Tente resolver o enunciado antes de abrir."""

def sudoku_valido(grade: list[list[int]]) -> bool:
    if len(grade) != 9 or any(len(linha) != 9 for linha in grade):
        raise ValueError("grade invalida")

    def ok(valores) -> bool:
        nums = [v for v in valores if v != 0]
        return len(nums) == len(set(nums)) and all(1 <= v <= 9 for v in nums)

    for i in range(9):
        if not ok(grade[i]) or not ok(grade[r][i] for r in range(9)):
            return False
    for br in range(3):
        for bc in range(3):
            bloco = [
                grade[r][c]
                for r in range(br * 3, br * 3 + 3)
                for c in range(bc * 3, bc * 3 + 3)
            ]
            if not ok(bloco):
                return False
    return True


if __name__ == "__main__":
    from _rodar import rodar

    rodar(sudoku_valido=sudoku_valido)
