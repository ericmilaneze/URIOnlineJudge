import sys

for line in sys.stdin:
    x1, y1, x2, y2 = [int(i) for i in line.split()]

    if [x1, y1, x2, y2] == [0, 0, 0, 0]:
        break

    if [x1, y1] == [x2, y2]:
        print(0)
        continue

    if x1 == x2 or y1 == y2 or [x2, y2] in [[x1 + i, y1 + i] for i in range(-8, 9)] + [[x1 + i, y1 - i] for i in range(-8, 9)]:
        print(1)
        continue

    print(2)
