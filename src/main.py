import sys
import information
import intersection

args = sys.argv

if __name__ == '__main__':
    info = information.information()
    intersection.intersection(info.N, info.lines[0], info.lines[1])
