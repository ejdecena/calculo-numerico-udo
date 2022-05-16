import math
"""
Nombre y Apellidos: jeremy gonzalez
Cédula: 27403276
"""

def error_relativo(vact, vant):
    """Implementación del error relativo.
    vact: valor actual.
    vant: valor anterior.
    return el error relativo de vact y vant.
    """
    return abs((vact-vant)/vact)


def biseccion(fx, inter, er, n):
    """Implementación del método de biseccion.
    fx: una función.
    inter: es la tupla del intervalo de fx.
    er: es la cota del error relativo.
    n: número máximo de iteraciones.
    Debe mostrar por teclado una a una las iteraciones del algoritmo de
    bisección,  hacer la comprobación. y retornar el último punto medio (m)
    """
    m = ((inter[0]+inter[1])/2)
    
    for i in range(1,n):
      anterior = m 
      m = ((inter[0]+inter[1])/2) 
      fa=fx(inter[0])
      fb=fx(inter[1])
      fm = fx(m)
      errelativo = error_relativo(m,anterior) 
      if (fb*fa)==0:
          if fa ==0:
            m = inter[0]
            print(f"""la raiz es {m}""")
            return m
          elif  fb ==0:
            m = inter[1]
            print(f"""la raiz es {m}""")
            return m
              

      elif (fb*fa)<0:
        if (errelativo < er)and not(errelativo == 0):
          print(f"""Iteraicon n°: {i}""")     
          print(f"""la raiz es {m}""")
          return m
        elif (fm*fa)<0:
          inter=(inter[0],m)
        elif (fm*fb)<0:
          inter=(m,inter[1])
      print(f"""Iteraicon n°: {i}""")   
    print(f"""la raiz es {m}""")
    return m


if __name__ == "__main__":
    # Testing.

    # Datos.
    fx = lambda x: (x - 2)**2 - math.log(x)
    inter = (1, 2)
    er = 0.02
    n = 50

    biseccion(fx, inter, er, n)