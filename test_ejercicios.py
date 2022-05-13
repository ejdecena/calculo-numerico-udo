import math
from unittest import TestCase


from . ejercicio_biseccion import biseccion as profe_biseccion
from . jeremy_gonzalez_biseccion import biseccion as jeremy_gonzalez_biseccion 



class TestEjercicios(TestCase):

    def setUpClass(self):
        self.fx = lambda x: (x - 2)**2 - math.log(x)
        self.inter = (1, 2)
        self.er = 0.02
        self.n = 50


if __name__ == "__main__":
    # Testing.
    pass
  