import math
"""
Nombre y Apellidos: César Augusto Zabala De Freitas Barboza
Cédula: 30.008.042
"""

def error_relativo(vact, vant):
    """Implementación del error relativo.

    vact: valor actual.
    vant: valor anterior.

    return el error relativo de vact y vant.
    """
    return abs((vact - vant) / vact)


def biseccion(fx, inter, er, n):
    """Implementación del método de biseccion.

    fx: una función.
    inter: es la tupla del intervalo de fx.
    er: es la cota del error relativo.
    n: número máximo de iteraciones.

    Debe mostrar por teclado una a una las iteraciones del algoritmo de
    bisección,  hacer la comprobación. y retornar el último punto medio (m)
    """
    a = inter[0]  # / Valores del parametro
    b = inter[1]  # \
    a_er = 100     # Actual error relativo (Al principio como no hay valor inicia en 100)
    m = 0  # Punto medio actual
    m_previo = 0  # Punto medio previo
    i = 1         # Acumulador de # de iteraciones

    if a > b:
        print("Error: El primer valor es mayor que el segundo")
        return

    while i < n and a_er > er:
        m_previo = m
        m = (a + b) / 2
        
        print("----------------")
        print(f">>> ITERACION #{i}:")
        print(f"> a = {a} ; b = {b}")
        print(f"> m{i} = {m}")
        print(f"f(a) = {fx(a)}")
        print(f"f(b) = {fx(b)}")
        print(f"f(m{i}) = {fx(m)}")
            
        
        # Calcular donde ocurre el cambio de signo (El resultado que no cambie de signo sera reemplazado)
        if fx(m) * fx(b) < 0: 
            a = m
        else:
            b = m

        # A partir de la 2da iteracion, calcular el error relativo
        if i > 1: 
            a_er = error_relativo(m, m_previo)
            print(f"> ERROR RELATIVO (er) = {a_er}")
        i = i + 1
    print("----------------")
    if i == n:
        print("SE HA ALCANZADO EL LIMITE DE ITERACIONES")
    elif a_er < er:
        print("SE HA CUMPLIDO LA COTA DEL ERROR RELATIVO")
    # Imprimir ultimos resultados
    print(f"> Raiz aproximada ^p = {m}")
    print(f"> Error relativo = {a_er}")
    print(f"> Iteraciones = {i-1}")
    print("----------------")
    return m

if __name__ == "__main__":
    # Testing.

    # Datos.
    fx = lambda x: (x - 2)**2 - math.log(x)
    inter = (1, 2)
    er = 0.02
    n = 50

    biseccion(fx, inter, er, n)
