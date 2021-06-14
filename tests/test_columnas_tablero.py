from src.four_line import columnasTablero

def test_columnas_tablero():
  tablero = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 1, 2, 0, 0, 0],
            [0, 0, 2, 1, 0, 0, 0],
            [0, 0, 2, 1, 0, 0, 0],
            [0, 0, 1, 1, 2, 0, 0],
            ]
  assert [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 2, 1, 2, 2, 1], [0, 0, 2, 1, 1, 1], [0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] == columnasTablero(tablero)