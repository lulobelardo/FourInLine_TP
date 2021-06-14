from src.four_line import contenidoFila

def test_contenido_fila():
  tablero = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 1, 2, 0, 0, 0],
            [0, 0, 2, 1, 0, 0, 0],
            [0, 0, 2, 1, 0, 0, 0],
            [0, 0, 1, 1, 2, 0, 0],
            ]
  assert [0, 0, 1, 1, 2, 0, 0] == contenidoFila(6, tablero)