import input_information
from Point import Point
from Line import Line


class build_information(input_information.input_information):
    def __init__(self):
        super().__init__() # for check
        self.points = get_point(self.x_1, self.y_1, self.N)
        self.lines = get_line(self.points, self.b, self.e, self.M)


def get_point(x, y, N):
    points = []
    for i in range(N):
        points.append(Point(x[i], y[i]))
        points[i].id = Point.id_k
        Point.id_k += 1

    return points
def get_line(points, b, e, M):
    lines = []
    for i in range(M):
        lines.append(Line(points[b[i]-1], points[e[i]-1]))

    return lines


if __name__ == '__main__':
    info = build_information()
    print(info.points[0].id)
