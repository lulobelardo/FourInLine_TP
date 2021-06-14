from src.four_line import filasTablero

def test_filas_tablero():
  tablero = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 1, 2, 0, 0, 0],
            [0, 0, 2, 1, 0, 0, 0],
            [0, 0, 2, 1, 0, 0, 0],
            [0, 0, 1, 1, 2, 0, 0],
            ]
  assert tablero == filasTablero(tablero)