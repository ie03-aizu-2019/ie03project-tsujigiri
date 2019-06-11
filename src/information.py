import input_information
import Point
import Line


class information(input_information.input_information):
    def __init__(self):

        super(information, self).__init__() # for check
        self.points = self.get_point(self.x_b, self.y_b, self.N)
        self.lines = self.get_line(self.points, self.b, self.e, self.M)

    @classmethod
    def get_point(self, x, y, N):
        points = []
        for i in range(N):
            points.append(Point.Point(x[i], y[i]))

        return points

    @classmethod
    def get_line(self, points, b, e, M):
        lines = []
        for i in range(M):
            lines.append(Line.Line(points[b[i]-1], points[e[i]-1]))

        return lines


if __name__ == '__main__':
    info = information()
    print(info.lines[1].p2.y)
