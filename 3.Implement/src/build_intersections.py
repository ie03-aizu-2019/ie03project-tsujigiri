from Point import Point
from Line import Line

from check_aPoint import check_aPoint



class build_intersections():
    def __init__(self, lines):
        self.lines = lines # list
        self.some_crosspoint = self.build_intersections(self.lines)



    @classmethod
    def build_intersections(self, lines):
        M = len(lines)
        Cpoints = [] # Cross Points
        for i in range(0, M-1): # 0 to end-1
            for j in range(i+1, M): # i+1 to end
                tmp = check_aPoint(lines[i], lines[j])
                if tmp.x != None:
                    Cpoints.append(tmp)


        Cpoints = sort_Points(Cpoints)


        return Cpoints



def sort_Points(some_crosspoint):
    points = sorted(some_crosspoint, key=lambda P:(P.x,P.y))

    for i in range(len(points)):
        points[i].Cid = Point.Cid_k
        Point.Cid_k += 1

    return points




def sort_cross_points(self, Cpoints):
    N = len(Cpoints) # N is the number of elements
    add_point = Cpoints[N-1]

    i = 0   # insert point as x
    while Cpoints[i].x < add_point.x:
        i +=1
    if (Cpoints[i].x == add_point.x) and (Cpoints[i].y < add_point.y):
        i +=1


    for j in range(N-i-1): # i to N-1
        Cpoints[N-j-1] = Cpoints[N-j-2]

    Cpoints[i] = add_point


    return Cpoints



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
