from src.four_line import secuenciaValida

def test_secuencia_valida():
  secuenciaT = [1, 5, 6, 4, 2, 4, 7]
  assert True == secuenciaValida(secuenciaT)

def test_secuencia_INvalida():
  secuenciaF = [1, 5, 6, 8, 2, 4, 0]
  assert False == secuenciaValida(secuenciaF)