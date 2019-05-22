class input_information:
    def __init__(self):
        self.N, self.M, self.P, self.Q = self.main_info()
        self.x_b, self.y_b = self.points_info(self.N)
        self.b, self.e = self.line_info(self.N, self.M)

    @classmethod
    def main_info(self):
        print("input main information")
        while(True):
            In = input("")
            In = In.split(" ")
            for i in range(len(In)):
                In[i] = int(In[i])
            # regulation checks
            if (2 <= In[0]) and (In[0] <= 200):
                if (1 <= In[1]) and (In[1] <= 100):
                    if (In[2] == 0) and (In[3] == 0):
                        break
            print("retype")
        return In

    @classmethod
    def points_info(self, N):
        x = []
        y = []
        print("input points information")
        for i in range(N):
            while(True):
                In = input("")
                In = In.split(" ")
                for j in range(2):
                    In[j] = int(In[j])

                x.append(In[0])
                y.append(In[1])

                # regulation check
                if ((0 <= x[i]) and (x[i] <= 1000)) and ((0 <= y[i]) and (y[i] <= 1000)):
                    break

                print("retype")

        return x, y

    @classmethod
    def line_info(self, N, M):
        b = []
        e = []
        print("input line information")
        for i in range(M):
            while(True):
                In = input("")
                In = In.split(" ")
                for j in range(2):
                    In[j] = int(In[j])

                b.append(In[0])
                e.append(In[1])

                # regulation check
                if ((0 <= b[i]) and (b[i] <= N)) or ((0 <= e[i]) and (e[i] <= N)):
                    break

                print("retype")

        return b, e

"""
if __name__ == '__main__':
    info = information()
    print(info.N)
    """
