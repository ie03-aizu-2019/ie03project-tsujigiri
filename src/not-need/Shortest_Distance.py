import build_Graph

f_inf = float('inf')

class Shortest_Distance:
    def __init__(self, info_lines, info_points, info_s, info_d, Cpoints):

        self.solutions = self.solution(info_lines, info_points, info_s, info_d, Cpoints) # type : double[]

        #for_test(self.G)

    @classmethod
    def solution(self, lines, points, s, d, Cpoints):
        solutions = []

        G = build_Graph.build_Graph(lines, points) # Graph type
        N = len(s)

        aSolution = Shortest_roots_problem(G, s[4], d[4], points, Cpoints)
        solutions.append(aSolution)



        return solutions



def Shortest_roots_problem(G, s, d, points, Cpoints):
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


    """
    implementation
    



    return 0

def for_test(G):
    for i in range(len(G.vertexes)):
        print(G.vertexes[i].x, G.vertexes[i].y)
