import math
from unittest import TestCase

from ejercicio_biseccion import biseccion as profe_biseccion
from kevin_rojas_biseccion import biseccion as kevin_rojas_biseccion
# INCLUIR ABAJO SU IMPORT
<<<<<<< HEAD
# from pedro_perez_biseccion import biseccion as pedro_perez_biseccion
from jesus_gonzalez_biseccion import biseccion as jesus_gonzalez_biseccion
from cesar_albornoz_biseccion import biseccion as cesar_albornoz_biseccion
=======
# from . pedro_perez_biseccion import biseccion as pedro_perez_biseccion
from cesar_zabala_biseccion import biseccion as cesar_zabala_biseccion

>>>>>>> f1413f1 (Mi algoritmo de biseccion. Por favor que esto funcione x_x)

class TestEjercicios(TestCase):

    def setUpClass(self):
        self.fx = lambda x: (x - 2)**2 - math.log(x)
        self.inter = (1, 2)
        self.er = 0.02
        self.n = 50


if __name__ == "__main__":
    # Testing.
    pass
