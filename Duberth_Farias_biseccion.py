import math
"""
Nombre y Apellidos: <Duberth Farias>
Cédula: <28345088>
"""

def comprobar(fx, value):
    val = fx(value)
    
    if val < 0:
        return ("(-)")
    else:
        return ("(+)")
    
def error_relativo(vact, vant):
    rel_er = 0
    if vact != 0:
        rel_er = math.fabs((vact-vant)/vact)
        return rel_er
    else:
        return None


def biseccion(fx, inter, er, n):
    i = 0
    vincial = inter[0]
    vfinal = inter[1]
    a = fx(inter[0])
    b = fx(inter[1])

    if a * b < 0:

        while i < n:

            print("iteracion ", i+1, ":")

            medio = float(vincial + vfinal) / 2

            print ("-Inicio: ", comprobar(fx, vincial), vincial, " medio: ", \
                comprobar(fx, medio), medio, " final: ", comprobar(fx, vfinal), \
                vfinal, " error: ", error_relativo(vincial, vfinal), "\n")

            if fx(vincial) * fx(medio) < 0:
                vfinal = float(medio) 
            else: 
                vincial = float(medio)
            
            input("Enter para continuar\n")
            
            if error_relativo(vincial, vfinal) < er:
                value = str.format("F({0}) = {1}",medio,fx(medio))
                return value
            
            i += 1


if __name__ == "__main__":
    # Testing.

    # Datos.
    fx = lambda x: (x - 2)**2 - math.log(x)
    inter = (1, 2)
    er = 0.02
    n = 50

    print(biseccion(fx, inter, er, n))
