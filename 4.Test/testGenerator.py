import random

# Regulation
N = [2, 200]
M = [1, 100]
P = [0, 0]
Q = [0, 0]
X = [0, 1000]

def best():
    file = open("./testData/test_best", "w")

    n = N[0]
    m = M[0]
    p = P[0]
    q = Q[0]

    main = str(n)+" "+str(m)+" "+str(p)+" "+str(q)+"\n"

    file.write(main)

    for point in range(n):
        x = random.randint(X[0], X[1])
        y = random.randint(X[0], X[1])

        if point == n:
            cont = str(x)+" "+str(y)
        else:
            cont = str(x)+" "+str(y)+"\n"

        file.write(cont)

    for line in range(m):
        b = random.randint(1, n)
        e = random.randint(1, n)

        cont = str(b)+" "+str(e)

        if line == m-1:
            cont = str(b)+" "+str(e)
        else:
            cont = str(b)+" "+str(e)+"\n"

        file.write(cont)

    file.close()
def worst():
    file = open("./testData/test_worst", "w")

    n = N[1]
    m = M[1]
    p = P[1]
    q = Q[1]

    cont = str(n)+" "+str(m)+" "+str(p)+" "+str(q)+"\n"
    file.write(cont)

    for point in range(n):
        x = random.randint(X[0], X[1])
        y = random.randint(X[0], X[1])

        if point == n:
            cont = str(x)+" "+str(y)
        else:
            cont = str(x)+" "+str(y)+"\n"


        file.write(cont)

    for line in range(m):
        b = random.randint(1, n)
        e = random.randint(1, n)

        if line == m-1:
            cont = str(b)+" "+str(e)
        else:
            cont = str(b)+" "+str(e)+"\n"
        file.write(cont)

    file.close()
def general():
    print("How many test data need?")
    Need = int(input())
    for i in range(Need):
        file = open("./testData/test_"+str(i), "w")

        n = random.randint(N[0], N[1])
        m = random.randint(M[0], M[1])
        p = random.randint(P[0], P[1])
        q = random.randint(Q[0], Q[1])

        cont = str(n)+" "+str(m)+" "+str(p)+" "+str(q)+"\n"
        file.write(cont)

        for point in range(n):
            x = random.randint(X[0], X[1])
            y = random.randint(X[0], X[1])

            if point == n:
                cont = str(x)+" "+str(y)
            else:
                cont = str(x)+" "+str(y)+"\n"


            file.write(cont)

        for line in range(m):
            b = random.randint(1, n)
            e = random.randint(1, n)

            if line == m-1:
                cont = str(b)+" "+str(e)
            else:
                cont = str(b)+" "+str(e)+"\n"
            file.write(cont)


        file.close()

if __name__ == '__main__':
    print("What about attempt?")
    print("1)->best case, 2)->worst case, 3)->general cases")
    case = int(input())

    if case == 1:
        best()
    elif case == 2:
        worst()
    elif case == 3:
        general()
    else:
        exit()
