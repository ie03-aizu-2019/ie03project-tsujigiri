from Point import Point
from Line import Line

def check_aPoint(line1, line2): # A two lines, twolines.
    # line1 check
    s1 = signed_tri(line1, line2.p1)
    s2 = signed_tri(line1, line2.p2)
    s3 = signed_tri(line2, line1.p1)
    s4 = signed_tri(line2, line1.p2)

    if s1*s2*s3*s4 > 0: # cross check
        cPoint = cross_point(line1, line2)
        return cPoint


    return Point(None, None)


def signed_tri(line, aPoint):
    pa = line.p1
    pb = line.p2
    pc = aPoint

    S = (pa.x*pb.y + pb.x*pc.y + pc.x*pa.y) - (pa.y*pb.x + pb.y*pc.x + pc.y*pa.x) # signed triangle * 2

    return S

def cross_point(line1, line2):
    A = ((line1.p2.x-line1.p1.x)*(line2.p1.y-line2.p2.y)) + ((line2.p2.x-line2.p1.x)*(line1.p2.y-line1.p1.y)) # determinant must not be 0.
    B = [[line2.p1.y-line2.p2.y, line2.p2.x-line2.p1.x], [line1.p1.y-line1.p2.y, line1.p2.x-line1.p1.x]]
    C = [line2.p1.x-line1.p1.x, line2.p1.y-line1.p1.y]
    s = float(B[0][0]*C[0] + B[0][1]*C[1])/A

    x = line1.p1.x + (line1.p2.x - line1.p1.x)*s
    y = line1.p1.y + (line1.p2.y - line1.p1.y)*s

    cpoint = Point(x, y)

    return cpoint

if __name__ == '__main__':

    N = 6
    p1 = Point(0, 0)
    p2 = Point(2, 5)
    p3 = Point(4, 7)
    p4 = Point(5, 5)
    p5 = Point(0, 1)
    p6 = Point(3, 5)

    M = 5
    lines = []

    lines.append(Line(p1, p4))
    lines.append(Line(p1, p6))
    lines.append(Line(p2, p5))

    lines.append(Line(p1, p5))
    lines.append(Line(p2, p6))

    insecs = check_aPoint(lines[2], lines[2])
