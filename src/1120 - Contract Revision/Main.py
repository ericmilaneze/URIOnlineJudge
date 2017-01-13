import sys

for line in sys.stdin:
    d, n = [i for i in line.split()]

    if [d, n] == ["0", "0"]:
        break

    print(int(0 if n.replace(d, "") == "" else n.replace(d, "")))
