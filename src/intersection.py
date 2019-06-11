"""
    The program to research there are intersections,
    mC2 times research

                                                        """

import Cross_Checks
# not need
import Point
import Line


class intersection:
    def __init__(self, lines):
        self.Cpoints = self.func(lines)

    @classmethod
    def func(self, lines):
        M = len(lines)
        Cpoints = [] # Cross Points
        for i in range(0, M-1): # 0 to end-1
            for j in range(i+1, M): # i+1 to end
                tmp = Cross_Checks.Cross_Checks(lines[i], lines[j])
                if tmp.CrossApoint:
                    Cpoints.append(tmp.CrossApoint) # for assignment 1
                    Cpoints = self.sort_cross_points(Cpoints)

        return Cpoints


"""
if __name__ == '__main__':

    N = 6
    p1 = Point.Point(0, 0)
    p2 = Point.Point(5, 5)
    p3 = Point.Point(0, 5)
    p4 = Point.Point(5, 0)

    p5 = Point.Point(0, 2)
    p6 = Point.Point(7, 2)

    M = 5
    lines = []

    lines.append(Line.Line(p1, p2)) #2
    lines.append(Line.Line(p3, p4)) #4
    lines.append(Line.Line(p5, p6)) #1


    insecs = intersection(lines)
    for i in range(len(insecs.Cpoints)):
        print(insecs.Cpoints[i].x, insecs.Cpoints[i].y)
"""
"""
if __name__ == '__main__':

    N = 6
    p1 = Point.Point(0, 0)
    p2 = Point.Point(2, 5)
    p3 = Point.Point(4, 7)
    p4 = Point.Point(5, 5)
    p5 = Point.Point(7, 1)
    p6 = Point.Point(9, 5)

    M = 5
    lines = []

    lines.append(Line.Line(p1, p4))
    lines.append(Line.Line(p1, p6))
    lines.append(Line.Line(p2, p5))
    lines.append(Line.Line(p3, p5))
    lines.append(Line.Line(p4, p6))


    insecs = intersection(lines)
    for i in range(len(insecs.Cpoints)):
        pass#print(insecs.Cpoints[i].x, insecs.Cpoints[i].y)
        """
