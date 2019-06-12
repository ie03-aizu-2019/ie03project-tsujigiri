import information
import intersection


def Display_Intersection(points):
     for i in range(len(points)):
          print(points[i].x,points[i].y)


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
        Display_Intersection(insec.Cpoints)


        
        #print(insecs.Cpoints[0].CrossApoint.x, insecs.Cpoints[0].CrossApoint.y)
        #intersection2.intersection2(info.lines[0], info.lines)


if __name__ == '__main__':
    main()
