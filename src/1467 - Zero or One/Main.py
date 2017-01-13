import sys

for line in sys.stdin:
    a, b, c = [i for i in line.split()]

    if [a, b, c] in [["0", "0", "0"], ["1", "1", "1"]]:
        print("*")
        continue

    if a not in [b, c]:
        print("A")
        continue
        
    if b not in [a, c]:
        print("B")
        continue
        
    if c not in [a, b]:
        print("C")
        continue
