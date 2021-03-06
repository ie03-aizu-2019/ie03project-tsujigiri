import Point
import Line


# mode: 0 -> only line to line
# mode: 1 -> above but also, line to point
class Cross_Checks():
    def __init__(self, l1, l2, mode):
        if mode == 0:
            self.CrossApoint = self.Mode0(l1, l2)
        elif mode == 1:
            self.CrossApoint = self.Mode1(l1, l2)

    @classmethod
    def Mode0(self, l1, l2):
        A = Step1(l1, l2)
        if A != 0: # if not, no intersection

            s, t = Step2(A, l1, l2)
            if ((0 < s) and (s < 1)) and ((0 < t) and (t < 1)):  # only line to line
                if Step3(s, t):
                    x, y = Step4(l1, l2, s, t)
                    cPoint = Point.Point(x, y)

                    return cPoint

        return False

    @classmethod
    def Mode1(self, l1, l2):
        A = Step1(l1, l2) # A is determinant

        if A != 0: # devide 2 case, (1) if A is 0, right then no intersection. (2) if A is not 0, then coninue
            s, t = Step2(A, l1, l2) # s, t are each palameter set
            if (((0 <= s) and (s <= 1)) and ((0 < t) and (t < 1))) or (((0 < s) and (s < 1)) and ((0 <= t) and (t <= 1))): # only line to line or line to point
                if Step3(s, t):
                    x, y = Step4(l1, l2, s, t)
                    cPoint = Point.Point(x, y)
                    return cPoint

        return False







def Step1(l1, l2):
    A = ((l1.p2.x-l1.p1.x)*(l2.p1.y-l2.p2.y)) + ((l2.p2.x-l2.p1.x)*(l1.p2.y-l1.p1.y))
    return A

def Step2(A, l1, l2):

    B = [[l2.p1.y-l2.p2.y, l2.p2.x-l2.p1.x], [l1.p1.y-l1.p2.y, l1.p2.x-l1.p1.x]]


    C = [l2.p1.x-l1.p1.x, l2.p1.y-l1.p1.y]


    s = (B[0][0]*C[0] + B[0][1]*C[1])/A
    t = (B[1][0]*C[0] + B[1][1]*C[1])/A

    return s, t

def Step3(s, t):

    if ((0 <= s) and (s <= 1)) and ((0 <= t) and (t <= 1)):
        return True
    else:
        return False

def Step4(l1, l2, s, t):
    x = l1.p1.x + (l1.p2.x - l1.p1.x)*s
    y = l1.p1.y + (l1.p2.y - l1.p1.y)*s

    return x, y


if __name__ == '__main__':

    p1 = Point.Point(0, 0)
    q1 = Point.Point(5, 5)
    p2 = Point.Point(2, 5)
    q2 = Point.Point(7, 1)

    l1 = Line.Line(p1, q1)
    l2 = Line.Line(p2, q2)


    point = Cross_Checks(l1, l2, 0)
    if point.CrossApoint:
        print(point.CrossApoint.x, point.CrossApoint.y)


"""
# ex2, example
p1 = Point.Point(0, 0)
p2 = Point.Point(2, 5)
p3 = Point.Point(4, 7)
p4 = Point.Point(5, 5)
p5 = Point.Point(7, 1)
p6 = Point.Point(9, 5)


l1 = Line.Line(p1, p4)
l2 = Line.Line(p3, p5)

point = Cross_Checks(l1, l2, 0)
if point.CrossApoint:
    print(point.CrossApoint.x, point.CrossApoint.y)
    """
