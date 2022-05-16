import math
"""
Nombre y Apellidos: Kevin David Rojas Noriega
Cédula: 29.582.382
"""

def error_relativo(vact, vant):
    """Implementación del error relativo.
    vact: valor actual.
    vant: valor anterior.
    return el error relativo de vact y vant.
    """
    return abs(((vact - vant) / vact))


def biseccion(fx, inter, er, n):
    """Implementación del método de biseccion.
    fx: una función.
    inter: es la tupla del intervalo de fx.
    er: es la cota del error relativo.
    n: número máximo de iteraciones.
    Debe mostrar por teclado una a una las iteraciones del algoritmo de
    bisección,  hacer la comprobación. y retornar el último punto medio (m)
    """
    err_rel = 100 # Error aproximado
    iter_act = 1 # Contador del número de iteraciones
    m_actual = 0 # Punto medio actual
    m_previo = 0 # Punto medio previo
    a = inter[0]
    b = inter[1]
    while iter_act < n and err_rel > er:
        m_previo = m_actual
        m_actual = (a + b) / 2

        if fx(m_actual) * fx(b) < 0:
            a = m_actual
        else:
            b = m_actual
        
        if iter_act > 1:
            err_rel = error_relativo(m_actual, m_previo)
        
        print(f"""===============Iteración {iter_act}===================
Valor actual: {m_actual}
Error aproximado: {err_rel}""")
        iter_act += 1
    return m_actual


if __name__ == "__main__":
    # Testing.

    # Datos.
    fx = lambda x: (x - 2)**2 - math.log(x)
    inter = (1, 2)
    er = 0.02
    n = 50

    biseccion(fx, inter, er, n)
