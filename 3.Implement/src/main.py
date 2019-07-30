from build_information import build_information
from build_intersections import build_intersections


class main():
    def __init__(self):
        main_information = build_information()
        some_crosspoint = build_intersections(main_information.lines)
        display_somecrosspoint(some_crosspoint)



def display_somecrosspoint(some_crosspoint):
    for i in range(len(some_crosspoint)):
        
        if some_crosspoint.x == None:
            print("NA")
        else:
            print(some_crosspoint.x, some_crosspoint.y)


        #Print(insecs.Cpoints[0].CrossApoint.x, insecs.Cpoints[0].CrossApoint.y)
        #intersection2.intersection2(info.lines[0], info.lines)


if __name__ == '__main__':
    main()
