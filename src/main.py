
import information
import intersection

# test
import intersection2

class main():
    def __init__(self):
        info = information.information()
        #intersection(info.N, info.lines[0], info.lines[1])
        intersection2.intersection2(info.lines[0], info.lines)


if __name__ == '__main__':
    main()
