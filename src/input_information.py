class input_information:
    def __init__(self):
        self.N, self.M, self.P, self.Q = self.main_info()
        self.x_b, self.y_b = self.points_info(self.N)
        self.b, self.e = self.line_info(self.N, self.M)
        self.s, self.d, self.k = self.distance_info(self.Q)
        # c_s is "s", but cross point

    @classmethod
    def main_info(self):
        print("input main information")
        while(True): # loop for regulation check
            tmp = list(map(int, input().split()))
            N = tmp[0]
            M = tmp[1]
            P = tmp[2]
            Q = tmp[3]

            # regulation checks(3)
            if (2 <= N) and (N <= 1000):
                if (1 <= M) and (M <= 500):
                    if(P == 0):
                        if (0 <= Q) and (Q <= 100):
                            break

            print("retype")


        return N, M, P, Q

    @classmethod
    def points_info(self, N):
        xArray = []
        yArray = []
        print("input points information")
        for i in range(N):
            while(True): # loop for regulation check
                tmp = list(map(int, input().split()))
                x = tmp[0]
                y = tmp[1]
                # regulation check(3)
                if (0 <= (x or y)) and ((x or y ) <= 1000):
                    break
                print("retype")

            xArray.append(x)
            yArray.append(y)


        return xArray, yArray

    @classmethod
    def line_info(self, N, M):
        bArray = []
        eArray = []
        print("input line information")

        for i in range(M):
            # for regulation check
            tmp = list(map(int, input().split()))

            b = tmp[0]
            e = tmp[1]
            # regulation check
            if ((b or e) < 0 or N < (b or e)):
                print("retype")
                i -= 1
                continue


            bArray.append(b)
            eArray.append(e)

        return bArray, eArray

    @classmethod
    def distance_info(self, Q):
        s = []
        d = []
        k = []

        print("input discance information")
        for i in range(Q):
            tmp = input().split()

            s.append(tmp[0])
            d.append(tmp[1])
            k.append(tmp[2])
        return s, d, k

"""
if __name__ == '__main__':
    #s, d, k = input_information.distance_info(2)
    #input_information.line_info(6,5)
    #print(s)

"""
