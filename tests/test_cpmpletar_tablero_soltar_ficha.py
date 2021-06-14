from src.four_line import soltarFichaEnColumna, completarTableroEnOrden

def test_soltar_ficha_en_columna():
  tablero = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            ]
  secuencia = [2,1,6,7,6,3]

  assert [
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0],
         [2, 1, 2, 0, 0, 1, 2],
         ] == completarTableroEnOrden(secuencia, tablero)
