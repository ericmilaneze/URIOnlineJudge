import sys

for line in sys.stdin:
    l, r = [int(i) for i in line.split()]

    if [l, r] == [0, 0]:
        break

    print(l + r)
