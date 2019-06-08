
import information
import intersection

# test
import intersection2

class main():
    def __init__(self):
        info = information.information()
        insecs = intersection.intersection(info.lines)

        for i in range(len(insecs.Cpoints)):
            print(insecs.Cpoints[i].x, insecs.Cpoints[i].y)


        #print(insecs.Cpoints[0].CrossApoint.x, insecs.Cpoints[0].CrossApoint.y)
        #intersection2.intersection2(info.lines[0], info.lines)


if __name__ == '__main__':
    main()
