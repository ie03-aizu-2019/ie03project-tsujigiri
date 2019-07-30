from build_information import build_information
from check_aPoint import check_aPoint


class main():
    def __init__(self):
        main_information = build_information()
        A_crosspoint = check_aPoint(main_information.lines[0], main_information.lines[1])
        display_Acrosspoint(A_crosspoint)



def display_Acrosspoint(A_crosspoint):
    if A_crosspoint.x == None:
        print("NA")
    else:
        print(A_crosspoint.x, A_crosspoint.y)


        #Print(insecs.Cpoints[0].CrossApoint.x, insecs.Cpoints[0].CrossApoint.y)
        #intersection2.intersection2(info.lines[0], info.lines)


if __name__ == '__main__':
    main()
