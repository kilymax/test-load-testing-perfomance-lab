import sys

# вариант решения НЕ работающий при n < m
# def main():
#     n, m = int(sys.argv[1]), int(sys.argv[2])
#     path = [1]
#     while True:
#         path.append(path[-1] + (m-1))
#         if path[-1] > n:
#             path[-1] = path[-1] - n
#         if path[-1] == path[0]:
#             path.pop()
#             break

#     print(''.join(map(str, path)))


def main():
    n, m = int(sys.argv[1]), int(sys.argv[2])
    circle_array = []
    switch = True
    while switch:
        for i in range(1, n+1):
            circle_array.append(i)
            if len(circle_array) % m == 0:
                if i == 1:
                    switch = False
                    break
                circle_array.append(i)
    print(''.join(map(str, circle_array[::m])))



if __name__ == "__main__":
    main()
