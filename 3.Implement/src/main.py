from build_information import build_information
from build_intersections import build_intersections


class main():
    def __init__(self):
        main_information = build_information()
        some_crosspoint = build_intersections(main_information.lines).some_crosspoint
        display_somecrosspoint(some_crosspoint)


def display_somecrosspoint(some_crosspoint):
    if len(some_crosspoint) == 0:
        print("NA")

    else:
        for i in range(len(some_crosspoint)):
            print(some_crosspoint[i].x, some_crosspoint[i].y)



if __name__ == '__main__':
    main()
