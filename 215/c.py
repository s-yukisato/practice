from itertools import permutations

s, k = input().split()
k = int(k)

l = set(["".join(s) for s in permutations(s)])

t = sorted(list(l))

print(t[k-1])
