from Point import Point
from Line import Line

from check_aPoint import check_aPoint



class build_intersections():
    def __init__(self, lines):
        self.lines = lines # list
        self.some_crosspoint = build_intersections(self.lines)


def build_intersections(lines):
    M = len(lines)
    Cpoints = [] # Cross Points
    for i in range(0, M-1): # 0 to end-1
        for j in range(i+1, M): # i+1 to end
            tmp = check_aPoint(lines[i], lines[j])
            Cpoints.append(tmp)

    return Cpoints



def sort_Points(some_crospoint):


    return points


if __name__ == '__main__':
    N = 6
    p1 = Point(0, 0)
    p2 = Point(2, 5)
    p3 = Point(4, 7)
    p4 = Point(5, 5)
    p5 = Point(7, 1)
    p6 = Point(9, 5)

    M = 5
    lines = []
    lines.append(Line(p1, p4))
    lines.append(Line(p1, p6))
    lines.append(Line(p2, p5))
    lines.append(Line(p3, p5))
    lines.append(Line(p4, p6))



    ins = build_intersections(lines)

    print(len(ins))
