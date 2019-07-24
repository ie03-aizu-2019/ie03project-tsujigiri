import information
import intersection


class main():
    def __init__(self):
        info = information.information()
        insecs = intersection.intersection(info.lines)
        display_a_intersectionPoint(insecs.Cpoints)



        #Print(insecs.Cpoints[0].CrossApoint.x, insecs.Cpoints[0].CrossApoint.y)
        #intersection2.intersection2(info.lines[0], info.lines)


if __name__ == '__main__':
    main()
