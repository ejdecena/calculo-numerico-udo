import math
from unittest import TestCase

#from . ejercicio_biseccion import biseccion as profe_biseccion
# INCLUIR ABAJO SU IMPORT
from . Duberth_Farias_biseccion import biseccion as pedro_perez_biseccion


class TestEjercicios(TestCase):

    def setUpClass(self):
        self.fx = lambda x: (x - 2)**2 - math.log(x)
        self.inter = (1, 2)
        self.er = 0.02
        self.n = 50

if __name__ == "__main__":
    # Testing.
    pass
