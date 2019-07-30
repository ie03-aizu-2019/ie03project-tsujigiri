import math
inf = float('inf')

from Node import Node
from Point import Point

class The_shortest_path():
    def __init__(self, Graph, points, cpoints, s, d, k):
        self.Graph = Graph
        self.points = points
        self.cpoints = cpoints
        self.s = s
        self.d = d
        self.k = k
        #self.path = build_path(self.Graph, self.points, self.cpoints, self.s, self.d, self.k)

        """
        for point in points:
            print(point.id)
        for cpoint in cpoints:
            print(cpoint.Cid)
            """


def build_path(aGraph, points, cpoints, s, d, k):

    sNodes = []
    eNodes = []
    for i in range(len(k)):
        sNode, eNode = prepare(aGraph.nodes, points, cpoints, s[i], d[i], k[i])

        sNodes.append(sNode)
        eNodes.append(eNode)

    # hukusuu
    print("from", sNodes[0].id, "to", eNodes[0].id)
    DIJKSTRA (aGraph, sNodes[0])
    for i in aGraph.nodes:
        print(i.id,":", i.axis.x, i.axis.y)

    #print(eNodes[0].weight)
    #display(eNodes[0])

def display(node):
    if node.parent != None:

        print(node.parent.id)

        display(node.parent)



def DIJKSTRA (G, s):
    INIT_SS(G, s)

    Q = MIN_PRIORITY_QUEUE(G.nodes)
    #print("33333Q[0].weight)

    for edge in G.edges:
        print(edge.n1.id, edge.n2.id)

    while len(Q) > 0:
        u = EXTRACT_MIN(Q)
        v = Adj(u, G.edges, G.nodes)
        print(u.id, "adj", len(v))
        for i in range(len(v)):
            RELAX(u,v[i], G.edges)
def INIT_SS (G, s):
    u = G.nodes

    for i in range(len(u)):
        u[i].weight = inf
        u[i].parent = None

    s.weight = 0
def MIN_PRIORITY_QUEUE(nodes):
    Q = []

    for i in range(len(nodes)):
        Q.append(nodes[i])

    return Q
def EXTRACT_MIN(Q):
    Min = Q[0].weight
    key = 0

    for i in range(1, len(Q)):
        if Q[i].weight < Min:
            Min = Q[i].weight
            key = i

    return Q.pop(key)
def Adj(u, edges, nodes):
    S = []


    for edge in edges:
        if u.id is edge.n1.id or u.id is edge.n2.id:
            print("ok")
            if u.id is edge.n1.id:
                S.append(edge.n2)

            elif u.id is edge.n2.id:
                S.append(edge.n1)



    """
    for i in range(len(edges)):
        if u.id is edges[i].n1.id:
            for j in range(len(nodes)):
                if nodes[j].id is edges[i].n2.id:
                    break

            S.append(nodes[j])

        elif u.id is edges[i].n2.id:
            for j in range(len(nodes)):
                if nodes[j].id is edges[i].n1.id:
                    break

            S.append(nodes[j])
            """
    return S
def RELAX(u,v,edges):

    T = W(u, v, edges)

    if v.weight > u.weight + T:
        v.weight = u.weight + T
        v.parent = u
def W(u, v, edges): # u, v is a vertex.

    for i in range(len(edges)):
        a = edges[i].n1.id
        b = edges[i].n2.id

        if u.id == a:
            if v.id == b:
                return edges[i].distance


        elif u.id == b:
            if v.id == a:
                return edges[i].distance

    return inf


def prepare(nodes, points, cpoints, s, d, k):
    sNode = None
    eNode = None

    if len(s) > 1 and s[0] == 'C': # cross point
        S = []
        possible = False

        for i in range(1, len(s)):
            S.append(s[i])

        #tmp = list(map(int, input().split()))
        S = ''.join(S)
        num = int(S)

        for i in range(len(cpoints)):
            if cpoints[i].Cid == num:
                possible = True
                target = i
                break

        if possible == True:
            sNode = find_node(cpoints[target], nodes)
        else:
            sNode = Node(Point(None, None))

    else: # general point
        num = int(s[0])


        for i in range(len(points)):
            if points[i].id == num:
                possible = True
                target = i
                break
        if possible == True:
            sNode = find_node(points[target], nodes)
        else:
            sNode = Node(Point(None, None))
    if len(d) > 1 and d[0] == 'C': # cross point
        S = []
        possible = False

        for i in range(1, len(d)):
            S.append(d[i])

        #tmp = list(map(int, input().split()))
        S = ''.join(S)
        num = int(S)

        for i in range(len(cpoints)):
            if cpoints[i].Cid == num:
                possible = True
                target = i
                break

        if possible == True:
            eNode = find_node(cpoints[target], nodes)
        else:
            eNode = Node(Point(None, None))
    else: # general point
        num = int(d[0])

        for i in range(len(points)):
            if points[i].id == num:
                possible = True
                target = i
                break
        if possible == True:
            eNode = find_node(points[target], nodes)
        else:
            eNode = Node(Point(None, None))


    return sNode, eNode


def find_node(point, nodes):
    for node in nodes:
        if (node.axis.x == point.x) and (node.axis.y == point.y):
            return node
