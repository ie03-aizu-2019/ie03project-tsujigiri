import Point
import Line

import main

# 線分(aLine)上にある交差点を全て求める（
class intersection2():
    def __init__(self, aLine, lines):

        onLine_Points = []

        for i in range(len(lines)):
            crossP = Cross_Checks2(aLine, lines[i])
            onLine_Points.append(crossP)



# 2線分間の交差点を検出。線と点での交差も含む
def Cross_Checks2(line0, line1):
    if (line0.p1 is line1.p1) or (line0.p1 is line1.p2) or (line0.p2 is line1.p1) or (line0.p2 is line1.p2):
        return None

    intersection = False #judge intersection

    # case 1: x = k and x = l, the two are not intersect absolutely
    if (line0.p1.x == line0.p2.x) and (line1.p1.x == line1.p2.x):
        intersection = False

    # case 2: x = k and y = ax + b
    elif (line0.p1.x == line0.p2.x):
        a2 = (line1.p1.y - line1.p2.y)/(line1.p1.x - line1.p2.x)
        b2 = line1.p1.y - (a2 * line1.p1.x)
        UpDn1 = line0.p1.y - (a2 * line0.p1.x + b2)
        UpDn2 = line0.p2.y - (a2 * line0.p2.x + b2)
        if UpDn1 * UpDn2 <= 0:
            if ((line1.p1.x < line0.p1.x) and (line0.p1.x < line1.p2.x) ) or ((line1.p2.x < line0.p1.x) and (line0.p1.x < line1.p1.x)):
                intersection = True

    # case 3: x = k and y = ax + b, similialy
    elif (line1.p1.x == line1.p2.x):
        a1 = (line0.p1.y - line0.p2.y)/(line0.p1.x - line0.p2.x)
        b1 = line0.p1.y - (a1 * line0.p1.x)
        UpDn1 = line1.p1.y - (a1 * line1.p1.x + b1)
        UpDn2 = line1.p2.y - (a1 * line1.p2.x + b1)
        if UpDn1 * UpDn2 <= 0:
            if ((line0.p1.x < line1.p1.x) and (line1.p1.x < line0.p2.x) ) or ((line0.p2.x < line1.p1.x) and (line1.p1.x < line0.p1.x)):
                    intersection = True

    else: # case4
        # when not vertical
        # y = ax + b
        a1 = (line0.p1.y - line0.p2.y)/(line0.p1.x - line0.p2.x)
        b1 = line0.p1.y - (a1 * line0.p1.x)
        # UpDn > 0 then above, UpDn < 0 then below
        UpDn1 = line1.p1.y - (a1 * line1.p1.x + b1)
        UpDn2 = line1.p2.y - (a1 * line1.p2.x + b1)

        if UpDn1 * UpDn2 <= 0:
            # next judge
            a2 = (line1.p1.y - line1.p2.y)/(line1.p1.x - line1.p2.x)
            b2 = line1.p1.y - (a2 * line1.p1.x)
            # UpDn > 0 then above, UpDn < 0 then below
            UpDn1 = line0.p1.y - (a2 * line0.p1.x + b2)
            UpDn2 = line0.p2.y - (a2 * line0.p2.x + b2)
            if UpDn1 * UpDn2 <=0:
                intersection = True

    if intersection == True:
        # print intersection
        x = -(b1 - b2)/(a1 - a2)
        y = a1 * x + b1

        point = Point.Point(x, y)
        return point

    else:
        return None

if __name__ == '__main__':


    p1 = Point.Point(0, 0)
    p2 = Point.Point(5, 5)
    p3 = Point.Point(2, 5)
    p4 = Point.Point(7, 1)
    p5 = Point.Point(0, 3)
    p6 = Point.Point(0, 2)
    p7 = Point.Point(1, 1)

    line1 = Line.Line(p1, p2)
    line2 = Line.Line(p3, p7)

    point = Cross_Checks2(line1, line2)
    if point != None:
        print(point.x, point.y)
