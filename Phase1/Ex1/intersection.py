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

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q+1, r)

    return A
def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r): # p to r-1
        if A[j] <= x:
            i += 1
            # change
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
        # already, devided
    #change
    tmp = A[i+1]
    A[i+1] = A[r]
    A[r] = tmp

    return i+1


class intersection:
    # make the Cross Points
    def intersection(N, M ,lines):
        Cpoints = [] # Cross Points
        for i in range(0, M-1):
            for j in range(i+1, M):
                check = Cross_Checks.Cross_Checks.Cross_Checks(N, lines[i], lines[j])
                if check is None:
                    continue
                Cpoints.append(check) # for assignment 1

        # sort and return
        Cpoints = intersection.sort_cross_points(Cpoints)
        return Cpoints

    # Sort to x orders
    @classmethod
    def sort_cross_points(self, Cpoints):
        # sort by a element x
        Cpoints = intersection.sort_by_X(Cpoints)
        #Cpoints = intersection.sort_by_Y(Cpoints)

        return Cpoints

    # a part of sort_cross_points, sort by x
    @classmethod
    def sort_by_X(self, Cpoints):
        # get x info
        X = []
        for i in range(len(Cpoints)):
            X.append(Cpoints[i].x)

        # sort X
        X = quickSort(X, 0, len(X)-1)

        # adjust X to Cpoints
        fixed_points = []
        for i in range(len(Cpoints)):
            for j in range(len(X)):
                if X[i] == Cpoints[j].x:
                    fixed_points.append(Cpoints[j])

        return fixed_points
    def sort_by_Y(self, Cpoints):
        # get y info
        Y = []
        for i in range(len(Cpoints)):
            Y.append(Cpoints.y)

        for i in range(len(Cpoints)):
            c = False
            if Cpoints[i].x == Cpoints[i+1].x:
                c = True




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


    points = intersection.intersection(N, M, lines)
    for i in range(len(points)):
        print(points[i].x, points[i].y)

        """
