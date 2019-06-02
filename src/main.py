import information
import intersection

def Display_Intersection(points):
    for i in range(len(points)):
        print(points[i].x, points[i].y)


if __name__ == '__main__':
    info = information.information()

    Cross_points = intersection.intersection.intersection(info.N, info.M, info.lines)
    Display_Intersection(Cross_points)
