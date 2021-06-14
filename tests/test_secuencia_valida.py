from src.four_line import secuenciaValida

def test_secuencia_valida():
  secuenciaF = [1, 5, 6, 8, 2, 4, 0]
  assert False == secuenciaValida(secuenciaF)
  secuenciaT = [1, 5, 6, 4, 2, 4, 7]
  assert True == secuenciaValida(secuenciaT)