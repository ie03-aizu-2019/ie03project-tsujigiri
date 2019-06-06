import math

import Point
import Line
import intersection2


""" There is a point, X.
    Search all points next to X, and measure the each distance   """
class residence(aPoint):
    edges = []

    inLine = search_linesOfPoint(apoint) # all lines against aPoint
    for i in range(len(inLine)):
        insec = intersection2.intersection2(inLine[i]) # get all intersections
        invPoint = inverse_point()
        insec.append(invPoint)
        near = nearPoint()  # near is the point, which is nearest to aPoint
        dis = distance(aPoint, near) # the distance

        aEdge = Edge.Edge(aPoint, near, dis) # build a edge



# ある点（一つでも線の要素となっている点)と複数の線分をいれ、ある点を含む線分をすべて返す。
def search_linesOfPoint(Vi, lines): # argument are Point type, Line[] type
    inLine = []
    for i in range(len(lines)):
        if (Vi == lines[i].p1) or (Vi == lines[i].p2):
            inLine.append(lines[i])


    return inLine
    # cmp


def nextTo(Vi, aLine, lines):

    onLine_Points = intersections2(aLine, lines)
    callpoint = inverse_point(Vi, aLine)
    onLine_Points.append(callpoint)

    return onLIne_Points

#　第一引数の線分の上の交差地点を全て返す。

# 点p1と点p1,p2によってなる線分を入れ、p2を返す。
def inverse_point(p1, line):
    return p2



# ２点を入れ、２点間の距離を実数で返す。
def distance(Vi, W): # two Points
    dts = math.sqrt((Vi.y-W.y)**2 + (Vi.x-W.x)**2)
    return dts




"""

    p1 = Point.Point(1,2)
    p2 = Point.Point(3,4)
    q1 = Point.Point(5,6)
    q2 = Point.Point(7,8)

    l1 = Line.Line(p1,p2)
    l2 = Line.Line(q1,q1)

    line = []
    line.append(l1)
    line.append(l2)

    inLine = search_linesOfPoint(p1, line)

    for i in range(len(inLine)):
        print(inLine[i].p1.y)
"""
"""
if __name__ == '__main__':
    p1 = Point.Point(1,2)
    p2 = Point.Point(3,4)

    dts = distance(p1,p2)
    print(dts)
    """
