
import information
import intersection


if __name__ == '__main__':
    info = information.information()
    intersection.intersection(info.N, info.lines[0], info.lines[1])
