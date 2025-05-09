import sys
import json

def main():
    numbers = list(map(int, open(sys.argv[1]).readlines()))
    steps = 0
    mean = int(sum(numbers) / len(numbers))
    switch = True
    while switch:
        switch = False
        for i in range(len(numbers)):
            if numbers[i] < mean:
                numbers[i] += 1
                steps += 1
                switch = True
            if numbers[i] > mean:
                numbers[i] -= 1
                steps += 1
                switch = True
    print(steps)
            


if __name__ == "__main__":
    main()