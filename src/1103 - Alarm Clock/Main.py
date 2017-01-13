import sys

for line in sys.stdin:
    h1, m1, h2, m2 = [int(i) for i in line.split()]

    if [h1, m1, h2, m2] == [0, 0, 0, 0]:
        break

    minutes1 = h1 * 60 + m1
    minutes2 = h2 * 60 + m2

    print((minutes2 - minutes1 if minutes2 >= minutes1 else minutes2 + 1440 - minutes1))
