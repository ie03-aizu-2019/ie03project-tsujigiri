import Point
import Line
import Cross_Checks


# 線分(aLine)上にある交差点を全て求める（
class aLine_inters():
    def __init__(self, aLine, lines):
        self.onLine_Points = self.func(aLine, lines)

    def func(self, aLine, lines):
        onLine_Points = []


        for i in range(len(lines)):
            crossP = Cross_Checks.Cross_Checks(aLine, lines[i], 1)
            if crossP.CrossApoint:
                onLine_Points.append(crossP.CrossApoint)

        return onLine_Points
"""


if __name__ == '__main__':


    p1 = Point.Point(0, 0)
    p2 = Point.Point(2, 5)
    p3 = Point.Point(4, 7)
    p4 = Point.Point(5, 5)
    p5 = Point.Point(7, 1)
    p6 = Point.Point(9, 5)


    l0 = Line.Line(p1, p4)
    l1 = Line.Line(p1, p6)
    l2 = Line.Line(p2, p5)
    l3 = Line.Line(p3, p5)
    l4 = Line.Line(p6, p4)

    lines = [l0, l1, l2, l3, l4]

    A = aLine_inters(l0, lines)
    for i in range(len(A.onLine_Points)):
        print(A.onLine_Points[i].x, A.onLine_Points[i].y)
        """
