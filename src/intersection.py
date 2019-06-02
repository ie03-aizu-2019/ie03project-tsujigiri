"""
    The program to research there are intersections,
    mC2 times research

    modify at ex2:
        Cross_Checks: 1 times -> mC2 times

    status: fin.ex1 - go.ex2

    TODO: not complete sort_by_Y.
                                                        """

import Cross_Checks
# not need
import Point
import Line



class intersection:
    # make the Cross Points
    def intersection(N, line1, line2):
         Cross_Checks.Cross_Checks.Cross_Checks(N, line1, line2)



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

    lines.append(Line.Line(p1, p6)) #2
    lines.append(Line.Line(p3, p5)) #4
    lines.append(Line.Line(p1, p4)) #1
    lines.append(Line.Line(p4, p6)) #5
    lines.append(Line.Line(p2, p5)) #3


    intersection.intersection(N, lines[0], lines[2])
"""
