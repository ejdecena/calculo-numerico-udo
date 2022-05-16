import math

#Nestor Aguilar
#C.I : 28.316.308

#Error relativo (no porcentual)
def error_relativo(vact, vant):
    return abs((vact - vant)/vact)

#Teorema de Valor Intermedio
def TVI(fx, a, b):
    return fx(a)*fx(b) < 0

def biseccion(fx, inter, er, n):
    mact = 0        #aproximación actual
    mant = 0        #aproximación anterio
    a = inter[0]    #límite inferior del intervalo
    b = inter[1]    #límite superior del intervalo
    er_actual = 1   #error relativo de la aproximación actual
    i = 0           #número de iteraciones

    #se verifica el teorema de valor intermedio
    if(TVI(fx, a, b)):
        #en dado caso, se realiza la bisección
        while er_actual > er and i < n:
            mant = mact
            mact = (a + b)/2

            if(TVI(fx, mact, b)):
                a = mact
            else:
                b = mact

            er_actual = error_relativo(mact, mant)
            
            print(f"------------ Iteración {i} ------------")
            print(f"m{i}: {mact}")
            print(f"er: {er_actual}")
            i += 1
    #en caso contrario, no se realiza la biseccion
    else:
        print("No hay corte en este intervalo")
    return


fx = lambda x: (x - 2)**2 - math.log(x)
intervalo = (1,2)
error = 0.02
iteraciones = 50

biseccion(fx, intervalo, error, iteraciones)