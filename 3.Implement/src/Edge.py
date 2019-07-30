import math

class Edge():
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.distance = self.calc(self.n1, self.n2)

    @classmethod
    def calc(self, n1, n2):
        x1 = n1.axis.x
        x2 = n2.axis.x
        y1 = n1.axis.y
        y2 = n2.axis.y

        tmp = (x1-x2)**2 + (y1-y2)**2
        tmp = tmp ** 0.5

        return tmp
