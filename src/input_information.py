class input_information:
    def __init__(self):
        self.N, self.M, self.P, self.Q = self.main_info()
        self.x_b, self.y_b = self.points_info(self.N)
        self.b, self.e = self.line_info(self.N, self.M)
        self.s, self.d, self.k, self.c_s, self.c_d = self.discance_info(self.Q)


    @classmethod
    def main_info(self):
        print("input main information")
        while(True): # loop for regulation check
            tmp = list(map(int, input().split()))
            N = tmp[0]
            M = tmp[1]
            P = tmp[2]
            Q = tmp[3]

            # regulation checks
            if (2 <= N) and (N <= 200):
                if (1 <= M) and (M <= 100):
                    if(P == 0) and (Q == 0):
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
                # regulation check
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
            while(True): # for regulation check
                tmp = list(map(int, input().split()))
                b = tmp[0]
                e = tmp[1]
                # regulation check
                if (0 <= (b or e)) and ((b or e) <= N):
                    break

                print("retype")


            bArray.append(b)
            eArray.append(e)

        return bArray, eArray

    @classmethod
    def distance_info(self, Q):
        s = []
        d = []
        k = []
        c_s = [] # the number cross in s
        c_d = [] # the number cross in d
        print("input discance information")
        for i in range(Q):
            tmp = input().split()
            # check "C", cross points input
                # if the first char in s is "C"
            if tmp[0][0] == "C":
                c_s.append(i)
                tmp[0] = int(tmp[0][1])
                # if the first char in d is "C"
            if tmp[1][0] == "C":
                c_d.append(i)
                tmp[1] = int(tmp[1][1])

            tmp[2] = int(tmp[2])




            # regulation check



            s.append(tmp[0])
            d.append(tmp[1])
            k.append(tmp[2])
        return s, d, k, c_s, c_d


if __name__ == '__main__':
    s, d, k = input_information.distance_info(2)
    print(s)
