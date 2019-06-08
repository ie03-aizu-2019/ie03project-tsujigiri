import math

import Point
import Line
import Edge
import aLine_inters


""" There is a point, X.
    Search all points next to X, and measure the each distance   """
class residence():
    def __init__(self, aPoint, info_lines):
        self.edges = []

        inLines = search_linesOfPoint(aPoint, info_lines) # all lines, include aPoint as end point
        # test
        for i in range(len(inLines)):
            insec = aLine_inters.aLine_inters(inLines[i], info_lines) # get all intersections

            invPoint = inverse_point(aPoint, inLines[i])
            #print("invPoint = ",invPoint.x, invPoint.y)

            insec.onLine_Points.append(invPoint)

            near = nearPoint(aPoint, insec.onLine_Points)  # near is the point, which is nearest to aPoint
            #print("nearPoint = ",near.x, near.y)
            dis = distance(aPoint, near) # the distance

            aEdge = Edge.Edge(aPoint, near, dis) # build a edge

            self.edges.append(aEdge)



# ある点（一つでも線の要素となっている点)と複数の線分をいれ、ある点を含む線分をすべて返す。
def search_linesOfPoint(Vi, lines): # argument are Point type, Line[] type
    inLine = []
    for i in range(len(lines)):
        if (Vi == lines[i].p1) or (Vi == lines[i].p2):
            inLine.append(lines[i])


    return inLine
    # cmp


# 点p1と点p1,p2によってなる線分を入れ、p2を返す。
def inverse_point(p1, line):
    if p1 is line.p1:
        return line.p2
    return line.p1


def nearPoint(aPoint, Points):

    tmp1 = distance(aPoint, Points[0])
    nearP = 0

    for i in range(1, len(Points)):
        tmp2 = distance(aPoint, Points[i])
        if tmp2 < tmp1:
            nearP = i

    return Points[nearP]


# ２点を入れ、２点間の距離を実数で返す。
def distance(Vi, W): # two Points
    dts = math.sqrt((Vi.y-W.y)**2 + (Vi.x-W.x)**2)
    return dts



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


    A = residence(p5, lines)

    for i in range(len(A.edges)):
        print(i,"; bPoint:(", A.edges[i].sPoint.x, A.edges[i].sPoint.y, ")ePoint:(", A.edges[i].ePoint.x, A.edges[i].ePoint.y,")")


        #A.edges[i].ePoint,":", A.edges[i].value)
