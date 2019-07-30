from build_information import build_information
from build_intersections import build_intersections
from Make_aGraph import Make_aGraph
from The_shortest_path import The_shortest_path



class main():
    def __init__(self):
        self.main_information = build_information()
        self.some_crosspoint = build_intersections(self.main_information.lines).some_crosspoint
        self.aGraph = Make_aGraph(self.main_information.lines, self.main_information.points).aGraph
        self.The_shortest_path = The_shortest_path(self.aGraph, self.main_information.points, self.some_crosspoint,self.main_information.s, self.main_information.d, self.main_information.k )


        #display_somecrosspoint(some_crosspoint)
        """
        print(len(self.aGraph.nodes))
        print(len(self.aGraph.edges))
        """

def display_somecrosspoint(some_crosspoint):
    if len(some_crosspoint) == 0:
        print("NA")

    else:
        for i in range(len(some_crosspoint)):
            print(some_crosspoint[i].x, some_crosspoint[i].y)



if __name__ == '__main__':
    main()
