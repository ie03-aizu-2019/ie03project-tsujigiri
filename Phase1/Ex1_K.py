
class segment:
    def __init__(self, s):
        self.P = s[0]
        self.Q = s[1]
        self.contacted = [self.P, self.Q]
        self.P.set_contacted(self)
        self.Q.set_contacted(self)

    def to_str(self):
        info = f"P = ({self.P.x}, {self.P.y})\n"
        info = info + f"Q = ({self.Q.x}, {self.Q.y})"
        return info

    def set_contacted(self, point):
        for i in range(len(self.contacted)):
            if self.contacted[i] is point:
                return False
        self.contacted.append(point)

    def set_index(self, index):
        self.index = index

    def isPoint(self):
        return False
