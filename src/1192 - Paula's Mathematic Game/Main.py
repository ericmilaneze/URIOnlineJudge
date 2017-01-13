q = int(input())

i = 0
nums = []

while i < q:
    i = i + 1

    v = input()

    d1, c, d2 = int(v[0]), v[1], int(v[2])

    if d1 == d2:
        print(d1 * d2)
        continue

    if ord(c) >= 97 and ord(c) <= 122:
        print(d1 + d2)
        continue

    print(d2 - d1)
