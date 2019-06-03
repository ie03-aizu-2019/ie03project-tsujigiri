

import Point
import Line

# ある点（一つでも線の要素となっている点)と複数の線分をいれ、ある点を含む線分をすべて返す。
def search_linesOfPoint(Vi, lines): # argument are Point type, Line[] type
    inLine = []
    for i in range(len(lines)):
        if (Vi == lines[i].p1) or (Vi == lines[i].p2):
            inLine.append(lines[i])


    return inLine
# ある点とその点を含む一本線分をいれ、その点を除く線分上にある交差点（対応する点も含む）をすべて返す。
def intersection_2(Vi, line):
    
    fPoint = Cross_Checks_2()
    fPoint.append(fPoint)

    callpoint = f()

    T.append(callpoint)

    return T

def distance(Vi, W):

    return dist


















if __name__ == '__main__':
    """
    check for search_linesOfPoint
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
