import math
"""
Nombre y Apellidos: <Cesar Ramon Albornoz Benitez>
Cédula: <26.311.747>
"""

def error_relativo(vact, vant):
    """Implementación del error relativo.
    vact: valor actual.
    vant: valor anterior.
    return el error relativo de vact y vant.
    """
    pass


def biseccion(fx, inter, er, n):
    a=inter[0]
    b=inter[1]
    if fx(a)*fx(b) < 0:
        it=1
        P_Medioactual=0
        P_Medioprevio=0
        e=100;
        while (it<n)&(e>er):
            P_Medioprevio=P_Medioactual
            P_Medioactual=(a+b)/2
            if fx(P_Medioactual)*fx(b)<0:
                a=P_Medioactual
            else:
                b=P_Medioactual
            if it>1:
                e=abs(P_Medioactual-P_Medioprevio/P_Medioactual)
            it=it+1
            print("Iteración:", it, "Punto Medio:", P_Medioactual, "Error:", e)

        return P_Medioactual
    else:
        print ("El intervalo no es valido.")



if __name__ == "__main__":
    # Testing.

    # Datos.
    fx = lambda x: (x - 2)**2 - math.log(x)
    inter = (1, 2)
    er = 0.02
    n = 50

    biseccion(fx, inter, er, n)
