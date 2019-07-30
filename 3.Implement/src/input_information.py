"""
    option -t : user types inputs

    """


import sys
args = sys.argv

class input_information:
    def __init__(self):
        self.N, self.M, self.P, self.Q = main_info()    # self.N, self.M, self.P, self.Q = 4, 2, 0, 0
        self.x_1, self.y_1 = point1_info(self.N)
        self.b, self.e = line_info(self.N, self.M)
        self.x_2, self.y_2 = point2_info(self.P)
        self.s, self.d, self.k = route_info(self.Q)

def main_info():

    if(len(args) == 2):     # Check manual mode
        if( args[1] == "-t" ):
            try:
                raise TestError
            except:
                print("input main information")

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
        if (2 <= N) and (N <= 1000):
            if (1 <= M) and (M <= 500):
                if(P == 0):
                    if (0 <= Q) and (Q <= 100):
                        break
        print("retype")

    return N, M, P, Q
def point1_info(N):
    if(len(args) == 2):     # Check manual mode
        if( args[1] == "-t" ):
            try:
                raise TestError
            except:
                print("input point1 information")

    return points_info(N)
def line_info(N, M):
    bArray = []
    eArray = []

    if(len(args) == 2):     # Check manual mode
        if( args[1] == "-t" ):
            try:
                raise TestError
            except:
                print("input line information")

    for i in range(M):
        if(len(args) == 2):     # Check manual mode
            if( args[1] == "-t" ):
                try:
                    raise TestError
                except:
                    print("No.",i+1, end=" ")

        while True:
            # for regulation check
            tmp = list(map(int, input().split()))
            if len(tmp) != 2:
                print("No.",i+1, end=" ")
                continue

            b = tmp[0]
            e = tmp[1]
            # regulation check
            if (1 <= b <= N) and  (1 <= e <= N):
                break
            print("No.",i+1, end=" ")

        bArray.append(b)
        eArray.append(e)

    if(len(args) == 2):     # Check manual mode
        if( args[1] == "-t" ):
            try:
                raise TestError
            except:
                print("")

    return bArray, eArray
def point2_info(P):

    if(len(args) == 2):     # Check manual mode
        if( args[1] == "-t" ):
            try:
                raise TestError
            except:
                print("input point2 information")

    return points_info(P)
def route_info(Q):
        s = []
        d = []
        k = []

        for i in range(Q):
            tmp = input().split()

            # regulation check
            s.append(tmp[0])
            d.append(tmp[1])
            k.append(int(tmp[2]))

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
            if (0 <= x and x <= 10000) and (0 <= y and y <= 10000):
                break


        xArray.append(x)
        yArray.append(y)

    if(len(args) == 2):     # Check manual mode
        if( args[1] == "-t" ):
            try:
                raise TestError
            except:
                print("")

    return xArray, yArray



if __name__ == '__main__':
   test = input_information()
   #print(test.x_1[0])
