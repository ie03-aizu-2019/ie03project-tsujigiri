import information
import intersection
import Shortest_Distance

def display_shortest_roots(solutions):
     N = len(solutions)
     for i in range(N):
         if solutions[i] is None:
             print("NA")
         else:
             print(solutions[i])


class main():
    def __init__(self):
        info = information.information()
        """
        j = 0
        for i in range(len(info.s)):
            if i == info.c_s[j]:
                print(info.s[i])
                j +=1
                """

        insec = intersection.intersection(info.lines)
        sols = Shortest_Distance.Shortest_Distance(info.lines, info.points, info.s, info.d, insec.Cpoints)
        display_shortest_roots(sols.solutions)
        #print(insecs.Cpoints[0].CrossApoint.x, insecs.Cpoints[0].CrossApoint.y)
        #intersection2.intersection2(info.lines[0], info.lines)


if __name__ == '__main__':
    main()
