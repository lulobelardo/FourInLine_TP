def tableroVacio():
  return [
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          ]

def soltarFichaEnColumna(ficha, columna, tablero):
  for fila in range(6, 0, -1):
    if tablero[fila - 1][columna - 1] == 0:
      tablero[fila - 1][columna - 1] = ficha
      return

def completarTableroEnOrden(secuencia, tablero):
  for ficha in range(len(secuencia)):
    if (ficha % 2 == 0):
      soltarFichaEnColumna(1,secuencia[ficha],tablero)
    else:
      soltarFichaEnColumna(2,secuencia[ficha],tablero)
  return tablero

def dibujarTablero(tablero):
  for fila in range(0, 6):
    for casilla in range(0, 7):
      print(str(tablero[fila][casilla]).replace('0',' '), end='  ')
    print()


secuencia = [1, 2, 3, 1, 5, 6, 3]

dibujarTablero(
        completarTableroEnOrden(
                secuencia, tableroVacio()
        )
)

