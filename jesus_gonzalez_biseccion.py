import math
"""
Nombre y Apellidos: Jesús Raziel González Sosa
Cédula: 28.074.361
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
    if (inter[0] > inter[1]):
        print("Limite inferior no puede ser mayor que limite inferior")
        return None
    fa = fx(inter[0]) # Función evaluada en el punto a.
    fb = fx(inter[1]) # Función evaluada en el punto b.
    if not (fa*fb) <= 0: 
        print("No existen raices en el intervalo especificado.")
        return None
    m = (inter[0]+inter[1])/2 # Punto medio.
    fm = fx(m)
    print(
     "|---------------------------------------|\n"
    f"| Iteracion 1:\n"
     "|---------------------------------------|\n"
    f"| a = {inter[0]}\n"
    f"| (a) = {fa}\n"
     "|---------------------------------------|\n"
    f"| b = {inter[1]}\n"
    f"| f(b) = {fb}\n"
     "|---------------------------------------|\n"
    f"| m1 = {m}\n"
    f"| f(m1) = {fm}\n"
     "|---------------------------------------|\n")
    
    if (fm*fa) < 0: # Caso 1
        print(f"Intervalo para proxima iteracion: [{inter[0]},{m}]\n")
        inter_iter = (inter[0],m)
    elif (fa*fm) > 0: # Caso 2
        print(f"Intervalo para proxima iteracion: [{m},{inter[1]}]\n")
        inter_iter = (m,inter[1])
    else:
        if fa == 0: # Caso 3
            print(f"Raiz encontrada en limites del intervalo: {iter[0]}")
            return iter[0]
        else:
            print(f"Raiz encontrada en limites del intervalo: {iter[1]}")
            return iter[1]
        return

    for i in range(1,n): # Proceso iterativo.
        vant = m # Aproximación anterior.
        fa = fx(inter_iter[0]) # Funcion evaluada en el limite inferior.
        fb = fx(inter_iter[1]) # Funcion evaluada en el limite superior.
        m = (inter_iter[0]+inter_iter[1])/2 # Punto medio.
        fm = fx(m) #Funcion evaluada en el punto mdio.
        err_relativo = error_relativo(m,vant) #Calculo del error relativo.
        print(
         "|---------------------------------------|\n"
        f"| Iteracion {i+1}:\n"
         "|---------------------------------------|\n"
        f"| a = {inter_iter[0]}\n"
        f"| f(a) = {fa}\n"
         "|---------------------------------------|\n"
        f"| b = {inter_iter[1]}\n"
        f"| f(b) = {fb}\n"
         "|---------------------------------------|\n"
        f"| Aproximacion anterior = {vant}\n"
        f"| m{i+1} = {m}\n"
        f"| Error relativo: {err_relativo}\n"
         "|---------------------------------------|\n"
        f"| f(m{i+1}) = {fm}\n"
         "|---------------------------------------|\n")
        if (err_relativo < er): # Condición de salida.
            print(f"Error relativo menor que cota. Raiz aproximada: {m}")
            return m

        if (fm*fa) < 0: # Caso 1
            print(f"Intervalo para proxima iteracion: [{inter_iter[0]},{m}]\n")
            inter_iter = (inter_iter[0],m)
        elif (fa*fm) > 0: # Caso 2
            print(f"Intervalo para proxima iteracion: [{m},{inter_iter[1]}]\n")
            inter_iter = (m,inter_iter[1])
        else: # Caso 3
            if fa == 0:
                print(f"Raiz encontrada en limites del intervalo: {inter_iter[0]}")
                return inter_iter[0]
            else:
                print(f"Raiz encontrada en limites del intervalo: {inter_iter[1]}")
                return inter_iter[1]
    print(f"Limite de iteraciones alcanzado. Raiz aproximada: {m}") #Limite de iteraciones alcanzado.
    return m


if __name__ == "__main__":
    # Testing.

    # Datos.
    fx = lambda x: (x - 2)**2 - math.log(x)
    inter = (1,2)
    er = 0.02
    n = 50

    biseccion(fx, inter, er, n)
