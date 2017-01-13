import sys

while True:
    games = int(input())

    if games == 0:
        break

    v = [int(i) for i in input().split()][0:games]

    mary = len([i for i in v if i == 0])
    john = len(v) - mary

    print("Mary won {} times and John won {} times".format(mary, john))
