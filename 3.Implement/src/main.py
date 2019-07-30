from build_information import build_information
from build_intersections import build_intersections


class main():
    def __init__(self):
        main_information = build_information()
        some_crosspoint = build_intersections(main_information.lines)
        display_somecrosspoint(some_crosspoint)


def display_somecrosspoint(some_crosspoint):
    for i in range(len(some_crosspoint)):
        if some_crosspoint[i].x != None:
            print(some_crosspoint[i].x, some_crosspoint[i].y)



if __name__ == '__main__':
    main()
