"""
    option -t : user types inputs

    """

class input_information:
    def __init__(self):
        self.N, self.M, self.P, self.Q = main_info()    # self.N, self.M, self.P, self.Q = 4, 2, 0, 0
        self.x_1, self.y_1 = point1_info(self.N)
        self.b, self.e = line_info(self.N, self.M)
        self.x_2, self.y_2 = point2_info(self.P)
        self.s, self.d, self.k = route_info(self.Q)

def main_info():

    while(True): # loop for regulation check
        tmp = list(map(int, input().split()))
        if len(tmp) != 4:
            print("retype")
            continue

        N = tmp[0]
        M = tmp[1]
        P = tmp[2]
        Q = tmp[3]
        # regulation checks(3)
        if (2 <= N) and (N <= 200):
            if (1 <= M) and (M <= 100):
                if(P == 0):
                    if (0 <= Q) and (Q <= 0):
                        break
        print("retype")

    return N, M, P, Q
def point1_info(N):

    return points_info(N)
def line_info(N, M):
    bArray = []
    eArray = []

    for i in range(M):

        while True:
            # for regulation check
            tmp = list(map(int, input().split()))


            b = tmp[0]
            e = tmp[1]
            # regulation check
            if (1 <= b <= N) and  (1 <= e <= N):
                break


        bArray.append(b)
        eArray.append(e)


    return bArray, eArray
def point2_info(P):

    return points_info(P)
def route_info(Q):
        s = []
        d = []
        k = []
        c_s = [] # the number cross in s
        c_d = [] # the number cross in d


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
        return s, d, k
def points_info(Num):
    xArray = []
    yArray = []
    for i in range(Num):

        while(True): # loop for regulation check
            tmp = list(map(int, input().split()))

            x = tmp[0]
            y = tmp[1]
            # regulation check(3)
            if (0 <= x and x <= 1000) and (0 <= y and y <= 1000):
                break


        xArray.append(x)
        yArray.append(y)


    return xArray, yArray



if __name__ == '__main__':
   test = input_information()
   print(test.x_1[0])
