q = int(input())

i = 0
nums = []

while i < q:
    i = i + 1

    nums.append(int(input()))

for n in sorted(set(nums)):
    print("{} aparece {} vez(es)".format(n, len([i for i in nums if i == n])))
