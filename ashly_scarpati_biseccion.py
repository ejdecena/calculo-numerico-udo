import math
"""
Nombre y Apellidos: <Ashly  Scarpati>
Cédula: <27.424.492>
"""
def biseccion(f, inter, er, n):
    a=inter[0]
    b=inter[1]
    err=100     #Error relativo aproximado 
    i=1        #Contador de iteraciones
    m_Act=0     #Punto medio actual
    m_Ant=0     #punto medio anterior

    if(fx(a)*fx(b)<0):

        while (err>er) and (i<n):

            m_Ant = m_Act
            m_Act = (a + b)/2

            if (fx(m_Act) * fx(a) < 0):
                b = m_Act
            else:
                a = m_Act

            if(i > 1):
                err=abs((m_Act-m_Ant)/m_Act)

            print("Iteración:", i, "Punto Medio:", m_Act, "Error:", err)

            i+=1

    else:
        print("Esta funcón o los puntos a y b, no cumple con el teorema del valor intermedio")

    return m_Act

pass


if __name__ == "__main__":
    # Testing.

    # Datos.
    fx = lambda x: (x - 2)**2 - math.log(x)
    inter = (1, 2)
    er = 0.02
    n = 50

    biseccion(fx, inter, er, n)