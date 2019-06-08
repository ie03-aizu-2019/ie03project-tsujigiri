"""
    This function, build all edges in order to create a graph.
    just using lines got in first, all edges can be created.

    lines, made of input information -> all Edges


    """
import Point
import Line

import residence


class Collect_Edges():
    def __init__(self, info_lines):
        self.edges = [] # the value, which is returned at the end.
        self.V = self.input_pointsOflines(info_lines) # lines -> all points except for all intersections.

        for i in range(len(self.V)):   # all points
            tmp = residence.residence(self.V[i], info_lines) # get edges against one point.

            self.edges += tmp.edges # store to array


    # collect all node, without duplicates
    def input_pointsOflines(self, lines):
        V = []
        for i in range(len(lines)):
            dup = Collect_Edges.search_duplicates(V, lines[i].p1)
            if not(dup): # no duplicates
                V.append(lines[i].p1)
            dup = Collect_Edges.search_duplicates(V, lines[i].p2)
            if not(dup): # no duplicates
                V.append(lines[i].p2)


        return V
        # cmp
    # if there is a duplicate, return True
    def search_duplicates(V, P):
        Fd = False
        for i in range(len(V)): # search duplicates
            if P is V[i]:
                Fd = True
                return Fd

        return Fd
        # cmp


if __name__ == '__main__':
    p1 = Point.Point(0,0)
    p2 = Point.Point(1,1)
    p3 = Point.Point(2,2)
    p4 = Point.Point(3,3)
    lines = []
    l1 = Line.Line(p1,p1)
    l2 = Line.Line(p3,p4)
    lines.append(l1)
    lines.append(l2)


    V = Collect_Edges(lines)
    for i in range(len(V.edges)):
        print(i,"; bPoint:(", V.edges[i].sPoint.x, V.edges[i].sPoint.y, ")", end = "")
        print("ePoint:(", V.edges[i].ePoint.x, V.edges[i].ePoint.y,")", end = "")
        print("value: ", V.edges[i].value)
