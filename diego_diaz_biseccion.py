import math
"""
Nombre y Apellidos: Diego Diaz
Cédula: 27.352.609
"""

def error_relativo(vact, vant):
    """Implementación del error relativo.

    vact: valor actual.
    vant: valor anterior.

    return el error relativo de vact y vant.
    """
    return math.fabs((vact-vant)/vact)

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

    vact = 0
    vant = 0
    ni = 0
    error_act = 100
    intervalo = [inter[0],inter[1]]

    while ni < n and error_act >= er:
        vant = vact
        vact = (intervalo[0]+intervalo[1])/2

        if fx(vact)*fx(intervalo[1])<0:
            intervalo[0] = vact
        else:
            intervalo[1] = vact
        if ni>1:
            error_act = error_relativo(vact,vant)
        ni = ni + 1
        print('Iteracion: '+str(ni))
        print('Valor Actual: '+str(vact))
        print('Error Actual: '+str(error_act))
    return vact
    pass


if __name__ == "__main__":
    # Testing.

    # Datos.
    fx = lambda x: (x - 2)**2 - math.log(x)
    inter = (2, 1)
    er = 0.02
    n = 50

    biseccion(fx, inter, er, n)
