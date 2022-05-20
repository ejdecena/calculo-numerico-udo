import math

"""
Nombre y Apellidos: <Ulises Hernandez Mora>
Cédula: <29.582.637>
"""


def error_relativo(vact, vant):
    """Implementación del error relativo.

    vact: valor actual.
    vant: valor anterior.

    return el error relativo de vact y vant.
    """
    return abs(((vact - vant) / vact)) #implementacion del error relativo con m1 - m2 / m2


def biseccion(fx, inter, er, n):
    """Implementación del método de biseccion.

    fx: una función.
    inter: es la tupla del intervalo de fx.
    er: es la cota del error relativo.
    n: número máximo de iteraciones.

    Debe mostrar por teclado una a una las iteraciones del algoritmo de
    bisección,  hacer la comprobación. y retornar el último punto medio (m)
    """
    Iteraciones = 1  # Este es el contador de iteraciones
    Ea = 1  # Valor del Error Aproximado
    Intera = inter[0]  # Tupla en la posicion 0 (1)
    Interb = inter[1]  # Tupla en la posicion 1 (2)
    PuntoMedioActual = 0  # Aqui guardamos el punto medio actual
    PuntoMedioPrevio = 0  # Aqui el punto medio anterior

    while Iteraciones < n and Ea > er:
        PuntoMedioPrevio = PuntoMedioActual # en cada iteracion pasamos el punto medio a vovlerse previo
        PuntoMedioActual = (Intera + Interb) / 2 # a + b entre 2 para sacar el punto medio

        if fx(PuntoMedioActual) * fx(Interb) < 0: # f(a) x f(b) sea menor a 0
            Intera = PuntoMedioActual
        else:
            Interb = PuntoMedioActual

        if Iteraciones > 1:
            Ea = error_relativo(PuntoMedioActual, PuntoMedioPrevio)

        print("\n")
        print("Iteracion Nro:", Iteraciones)
        print("Punto Medio Actual:", PuntoMedioActual)
        print("Error Aproximado:", Ea)

        Iteraciones += 1
    return PuntoMedioActual


if __name__ == "__main__":
    # Testing.

    # Datos.
    fx = lambda x: (x - 2) ** 2 - math.log(x)
    inter = (1, 2)
    er = 0.02
    n = 50

    biseccion(fx, inter, er, n)
