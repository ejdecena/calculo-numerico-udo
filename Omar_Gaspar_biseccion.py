import math
"""
Nombre y Apellidos: Omar Gaspar
Cédula: 28.593.179
"""

def error_relativo(vact, vant):
    """Implementación del error relativo.

    vact: valor actual.
    vant: valor anterior.

    return el error relativo de vact y vant.
    """
    return math.fabs((vact-vant)/vact)

    pass

def biseccion1(fx, inter, er, n, vant, ni):

    if ni > n:
        return False
    else:
        vact = (inter[0]+inter[1])/2
        if fx(vact)*fx(inter[1])<0:
            inter[0] = vact
        else:
            inter[1] = vact
        Error = error_relativo(vact,vant)
        ni = ni+1
        print('Iteracion: '+str(ni))
        print('Valor Actual: '+str(vact))
        print('Error Actual: '+str(Error))
        if Error < er:
            return vact
        else:
            return biseccion1(fx, inter, er, n, vact, ni)
    pass

def biseccion(fx, inter, er, n):
    """Implementación del método de biseccion.

    fx: una función.
    inter: es la tupla del intervalo de fx.
    er: es la cota del error relativo.
    n: número máximo de iteraciones.

    Debe mostrar por teclado una a una las iteraciones del algoritmo de
    bisección,  hacer la comprobación. y retornar el último punto medio (m)
    """

    inter = list(inter)
    vact = (inter[0]+inter[1])/2
    if fx(vact)*fx(inter[1])<0:
        inter[0] = vact
    else:
        inter[1] = vact
    print('Iteracion: 1')
    print('Valor Actual: '+str(vact))
    return biseccion1(fx, inter, er, n, vact, 1)

    pass


if __name__ == "__main__":
    # Testing.

    # Datos.
    fx = lambda x: (x - 2)**2 - math.log(x)
    inter = (2, 1)
    er = 0.02
    n = 50

    biseccion(fx, inter, er, n)
