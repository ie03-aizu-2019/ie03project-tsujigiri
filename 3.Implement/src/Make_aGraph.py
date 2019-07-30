import copy
import numpy

from Graph import Graph
from Point import Point
from Node import Node
from Edge import Edge

from check_aPoint import signed_tri, cross_point
from build_intersections import sort_Points

# from main import main

class Make_aGraph():
    def __init__(self, lines, points):
        self.lines = lines
        self.points = points
        self.aGraph = self.Make_aGraph(self.lines, self.points)

        print(len(self.aGraph.edges))
        for i in self.aGraph.edges:
            print(i.n1.id, i.n2.id)


    def Make_aGraph(self, lines, points):
        aGraph = Graph()

        another_cpoints = build_intersections(lines)
        nodes = build_nodes(another_cpoints, points)
        edges = build_edges(nodes, lines)

        aGraph.nodes += nodes
        aGraph.edges += edges


        return aGraph


def build_intersections(lines):
    M = len(lines)
    Cpoints = [] # Cross Points
    for i in range(0, M-1): # 0 to end-1
        for j in range(i+1, M): # i+1 to end
            tmp = check_aPoint(lines[i], lines[j])
            if tmp.x != None:
                Cpoints.append(tmp)


    Cpoints = sort_Points(Cpoints)


    return Cpoints
def check_aPoint(line1, line2): # A two lines, twolines.
    # line1 check
    s1 = signed_tri(line1, line2.p1)
    s2 = signed_tri(line1, line2.p2)
    s3 = signed_tri(line2, line1.p1)
    s4 = signed_tri(line2, line1.p2)

    a = s1*s2
    b = s3*s4

    if (a == 0 and b < 0) or (a < 0 and b == 0):
        if s1 == 0:
            return line2.p1
        elif s2 == 0:
            return line2.p2
        elif s3 == 0:
            return line1.p1
        elif s4 == 0:
            return line1.p2


    if (s1*s2 < 0) and (s3*s4 < 0): # cross check
        cPoint = cross_point(line1, line2)
        return cPoint


    return Point(None, None)
def build_nodes(cpoints, points):
    nodes = []
    POINTS = points+cpoints

    for i in range(len(POINTS)):
        add_node(POINTS[i], nodes)


    return nodes
def build_edges(nodes, lines):
    edges = []

    for line in lines:
        edges += online_node(line, nodes)


    return edges
def add_node(point, nodes):

    i = 0
    while i < len(nodes):
        if nodes[i].axis == point:
            nodes[i].points.append(point)
            return None
        i += 1


    nodes.append(Node(point))




    nodes[Node.k-1].id = Node.k
    nodes[Node.k-1].points.append(point)
    Node.k += 1

    return None
def find_node(point, nodes):
    for node in nodes:
        if node.axis is point:
            return node
def online_node(line, nodes):
    edges = []

    dx = line.p2.x - line.p1.x # if dx>0, p2 is right
    dy = line.p2.y - line.p1.y # if dy>0, p2 is above

    if dx > 0:
        SORTS = sorted(nodes, key=lambda P:P.axis.x)

        t1 = find_node(line.p1, nodes)
        flg = False
        for node in SORTS:
            if (line.p1.x < node.axis.x and node.axis.x < line.p2.x) and (aboveLine(line, node) == 0):
                flg = True
                t2 = find_node(node.axis, nodes)
                edges.append(Edge(t1, t2))

                t1 = copy.deepcopy(t2)

        if flg == False:
            t2 = find_node(line.p2, nodes)
            edges.append(Edge(t1, t2))

    elif dx < 0:
        SORTS = sorted(nodes, key=lambda P:P.axis.x)

        t1 = find_node(line.p2, nodes)
        flg = False
        for node in SORTS:
            if (line.p2.x < node.axis.x and node.axis.x < line.p1.x) and (aboveLine(line, node) == 0):
                flg = True
                t2 = find_node(node.axis, nodes)
                edges.append(Edge(t1, t2))
                t1 = copy.deepcopy(t2)

        if flg == False:
            t2 = find_node(line.p1, nodes)
            edges.append(Edge(t1, t2))
    else:
        if dy > 0:
            SORTS = sorted(nodes, key=lambda P:P.axis.y)

            t1 = find_node(line.p1, nodes)
            flg = False
            for node in SORTS:
                if line.p1.y < node.axis.y and node.axis.y < line.p2.y:
                    flg = True
                    t2 = find_node(node.axis, nodes)
                    edges.append(Edge(t1, t2))
                    t1 = copy.deepcopy(t2)

            if flg == False:
                t2 = find_node(line.p2, nodes)
                edges.append(Edge(t1, t2))


        elif dy < 0:
            SORTS = sorted(nodes, key=lambda P:P.axis.y)

            t1 = find_node(line.p2, nodes)
            flg = False
            for node in SORTS:
                if (line.p2.y < node.axis.y and node.axis.y < line.p1.y) and (aboveLine(line, node) == 0):
                    flg = True
                    t2 = find_node(node.axis, nodes)
                    edges.append(Edge(t1, t2))
                    t1 = copy.deepcopy(t2)


            if flg == False:
                t2 = find_node(line.p1, nodes)
                edges.append(Edge(t1, t2))

    return edges



def aboveLine(line, node):
    px = node.axis.x
    py = node.axis.y
    x1 = line.p1.x
    y1 = line.p1.y
    x2 = line.p2.x
    y2 = line.p2.y


    a = x2 - x1
    b = y2 - y1
    a2 = a * a
    b2 = b * b
    r2 = a2 + b2
    tt = -(a * (x1 - px) + b * (y1 - py))
    if tt < 0:
        return (x1 - px) * (x1 - px) + (y1 - py) * (y1 - py)
    if tt > r2:
        return (x2 - px) * (x2 - px) + (y2 - py) * (y2 - py)

    f1 = a * (y1 - py) - b * (x1 - px)
    return f1 * f1 / r2





if __name__ == '__main__':
    main = main()

    aGraph = Make_aGraph(main.main_information.lines, main.main_information.points).aGraph

    print(len(aGraph.nodes))
    print(len(aGraph.edges))
