import math
import sys

def main():
    circle = open(sys.argv[1]).readlines()
    cx, cy = map(float, circle[0].replace('\n', '').split(' '))
    r = float(circle[1].replace('\n', ''))
    dots = open(sys.argv[2]).readlines()
    for dot in dots:
        dx, dy = map(float, dot.replace('\n', '').split(' '))
        katet = math.sqrt(pow(cx - dx, 2) + pow(cy - dy, 2))
        if katet == r:
            print(0)
        elif katet < r:
            print(1)
        else:
            print(2)

if __name__ == "__main__":
    main()