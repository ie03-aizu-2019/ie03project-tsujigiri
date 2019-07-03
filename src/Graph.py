"""
    This function, build all edges in order to create a graph.
    just using lines got in first, all edges can be created.

    lines, made of input information -> all Edges


    """
import Point
import Line

import residence


class Graph():
    def __init__(self, info_lines, info_points):

        self.edges = self.func(info_lines, info_points) # edges
        self.vertexes = self.get_ver(self.edges) # Point[]


    @classmethod
    def func(self, info_lines, info_points):

        edges = []
        for i in range(len(info_points)):   # all points
            tmp = residence.residence(info_points[i], info_lines) # get edges against one point.

            edges += tmp.edges # store to array

        return edges


        # cmp
    # if there is a duplicate, return True
    @classmethod
    def search_duplicates(self, V, P):
        dupli = False
        for i in range(len(V)): # search duplicates
            if P is V[i]:
                Fd = True
                return Fd

        return dupli
        # cmp

    @classmethod
    def get_ver(self, edges):
        vertexes = [] # type : Point[]

        for i in range(len(edges)):
            vertexes.append(edges[i].sPoint)
            vertexes = self.insert(vertexes)
            vertexes.append(edges[i].ePoint)
            vertexes = self.insert(vertexes)



        return vertexes
    @classmethod
    def insert(self, vertexes):
        N = len(vertexes)
        L = vertexes[N-1] # last element

        for i in range(N-1):
            #if (1.0e-6 < abs(vertexes[i].x - L.x) and abs(vertexes[i].x - L.x) < 1.0e-5) and (1.0e-6 < abs(vertexes[i].y - L.y) and abs(vertexes[i].y - L.y) < 1.0e-5):
            rem = False
            if (vertexes[i].x == L.x) and (vertexes[i].y == L.y):
                rem = True


            a1 = vertexes[i].x * 1e15
            a2 = L.x * 1e15
            A = abs(a1-a2)

            b1 = vertexes[i].y * 1e15
            b2 = L.y * 1e15
            B = abs(b1-b2)
            if (0 < A and A < 10) or (0 < B and B < 10):
                rem = True

            if rem == True:
                vertexes.remove(L)
                return vertexes

        return vertexes



"""

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


    V = Graph(lines)
    for i in range(len(V.edges)):
        print(i,"; bPoint:(", V.edges[i].sPoint.x, V.edges[i].sPoint.y, ")", end = "")
        print("ePoint:(", V.edges[i].ePoint.x, V.edges[i].ePoint.y,")", end = "")
        print("value: ", V.edges[i].value)
        """
