"""
    Status = complete

    The program, only judge that 2 lines,
        line0 and line1 intersect or not
                                            """
import Line
# only for debug
import Point

class Cross_Checks:
    def Cross_Checks(N, line0, line1):
            intersection = False #judge intersection
            if N == 3: # when N = 3, no intersection
                return None
            else: # N == 4
                """ we should devide to 4 cases:
                    case1: no slope * no slope
                    case2: slope * no slope
                    case3: no slope * slope
                    case4: slope * slope    """
                if (line0.p1.x == line0.p2.x) and (line1.p1.x == line1.p2.x): # case1
                    intersection = False
                elif (line0.p1.x == line0.p2.x): # case2
                    a2 = (line1.p1.y - line1.p2.y)/(line1.p1.x - line1.p2.x)
                    b2 = line1.p1.y - (a2 * line1.p1.x)
                    tmp1 = line0.p1.y - (a2 * line0.p1.x + b2)
                    tmp2 = line0.p2.y - (a2 * line0.p2.x + b2)
                    if tmp1 * tmp2 < 0:
                        if ((line1.p1.x < line0.p1.x) and (line0.p1.x < line1.p2.x) ) or ((line1.p2.x < line0.p1.x) and (line0.p1.x < line1.p1.x)):
                            intersection = True
                elif (line1.p1.x == line1.p2.x): # case3
                    a1 = (line0.p1.y - line0.p2.y)/(line0.p1.x - line0.p2.x)
                    b1 = line0.p1.y - (a1 * line0.p1.x)
                    tmp1 = line1.p1.y - (a1 * line1.p1.x + b1)
                    tmp2 = line1.p2.y - (a1 * line1.p2.x + b1)
                    if tmp1 * tmp2 < 0:
                        if ((line0.p1.x < line1.p1.x) and (line1.p1.x < line0.p2.x) ) or ((line0.p2.x < line1.p1.x) and (line1.p1.x < line0.p1.x)):
                            intersection = True

                else: # case4
                    # when not vertical
                    # y = ax + b
                    a1 = (line0.p1.y - line0.p2.y)/(line0.p1.x - line0.p2.x)
                    b1 = line0.p1.y - (a1 * line0.p1.x)
                    # tmp > 0 then above, tmp < 0 then below
                    tmp1 = line1.p1.y - (a1 * line1.p1.x + b1)
                    tmp2 = line1.p2.y - (a1 * line1.p2.x + b1)

                    if tmp1 * tmp2 < 0:
                        # next judge
                        a2 = (line1.p1.y - line1.p2.y)/(line1.p1.x - line1.p2.x)
                        b2 = line1.p1.y - (a2 * line1.p1.x)
                        # tmp > 0 then above, tmp < 0 then below
                        tmp1 = line0.p1.y - (a2 * line0.p1.x + b2)
                        tmp2 = line0.p2.y - (a2 * line0.p2.x + b2)
                        if tmp1 * tmp2 < 0:
                            intersection = True

                if intersection == True:
                    # print intersection
                    x = -(b1 - b2)/(a1 - a2)
                    y = a1 * x + b1
                    a_cross_point = Point.Point(x, y)

                    return a_cross_point
                else:
                    return None


if __name__ == '__main__':

    N = 4
    p1 = Point.Point(0, 0)
    p2 = Point.Point(5, 5)
    p3 = Point.Point(2, 5)
    p4 = Point.Point(7, 1)

    line1 = Line.Line(p1, p2)
    line2 = Line.Line(p3, p4)

    a_cross_point = Cross_Checks.Cross_Checks(N, line1, line2)

    print(a_cross_point.x, a_cross_point.y)
