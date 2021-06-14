def tableroVacio():
  return [
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          ]
#Clase 4
def contenidoColumna(nro_columna, tablero):
  columna = []
  for fila in tablero:
    celda = fila[nro_columna - 1]
    columna.append(celda)
  return columna

#Clase 4
def contenidoFila(nro_fila, tablero):
  for indice, fila in enumerate(tablero):
    if indice == nro_fila - 1:
      return fila

#Clase 4
def filasTablero(tablero):
  return tablero

#Clase 4
def columnasTablero(tablero):
  columnas = []
  for columna in range(1,8):
    columnas.append(contenidoColumna(columna, tablero))
  return columnas

#Clase 2
def secuenciaValida(secuencia):
  for columna in secuencia:
    if columna > 7 or columna < 1:
      return False
  return True

#Clase 1
def soltarFichaEnColumna(ficha, columna, tablero):
  for fila in range(6, 0, -1):
    if tablero[fila - 1][columna - 1] == 0:
      tablero[fila - 1][columna - 1] = ficha
      return
#Clase 1
def completarTableroEnOrden(secuencia, tablero):
  for ficha in range(len(secuencia)):
    if (ficha % 2 == 0):
      soltarFichaEnColumna(1,secuencia[ficha],tablero)
    else:
      soltarFichaEnColumna(2,secuencia[ficha],tablero)
  return tablero

#Clase 1
def dibujarTablero(tablero):
  for fila in range(0, 6):
    print('|', end='  ')
    for casilla in range(0, 7):
      print(str(tablero[fila][casilla]).replace('0',' '), end='  ')
    print('|')
  print('+-----------------------+')

#####

secuencia_texto = input("Ingrese la secuencia de numeros: ")
secuencia = []
for items in secuencia_texto.split(','):
  secuencia.append(int(items))

tablero = []
if secuenciaValida(secuencia):
  tablero = completarTableroEnOrden(secuencia, tableroVacio())
  dibujarTablero(tablero)
else:
  print('Secuencia Invalida')