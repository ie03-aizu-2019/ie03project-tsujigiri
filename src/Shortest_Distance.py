import Graph

f_inf = float('inf')

class Shortest_Distance:
    def __init__(self, info_lines, info_points, info_s, info_d, Cpoints):

        self.solutions = self.solution(info_lines, info_points, info_s, info_d, Cpoints) # type : double[]

        #for_test(self.G)

    @classmethod
    def solution(self, lines, points, s, d, Cpoints):
        solutions = []

        G = Graph.Graph(lines, points) # Graph type
        N = len(s)

        aSolution = Shortest_roots_problem(G, s[4], d[4], points, Cpoints)
        solutions.append(aSolution)



        return solutions



def Shortest_roots_problem(G, s, d, points, Cpoints):

    start, end = decide_SandE(G, s, d, points, Cpoints)
    Nodes = G.vertexes


#1:
    center = Nodes[start]
    id = [] # each all points has id
    for i in range(len(Nodes)):
        if Nodes[i] == center

        else
            


    return 0

def decide_SandE(G, s, d, points, Cpoints): # which the element
    # divide 2 cases, s is cross or not cross.
    regulation = len(Cpoints)

    if s[0] is 'C':
        s = int(s[1])-1
        if s > regulation:
            return None
        sPoint = Cpoints[s]
    else:
        s = int(s[0])-1
        if s > regulation:
            return None
        sPoint = points[s]

    if d[0] is 'C':
        d = int(d[1])-1
        if d > regulation:
            return None
        dPoint = Cpoints[d]
    else:
        d = int(d[0])
        if d > regulation:
            return None
        dPoint = points[d-1]

    # got sPoint, dPoint
    # get the relations to Graph
    for i in range(len(G.vertexes)):
        if G.vertexes[i] is sPoint:
            start = i
        if G.vertexes[i] is ePoint:
            end = i


    return start, end



"""
def for_test(G):
    for i in range(len(G.vertexes)):
        print(G.vertexes[i].x, G.vertexes[i].y)
        """
