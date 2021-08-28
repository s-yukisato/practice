from collections import defaultdict
from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
c = list(map(int, input().split()))

d = defaultdict(int)

for i in range(k):
    d[c[i]] += 1

ans = len(d)

for i, j in enumerate(range(k, n)):
    d[c[i]] -= 1
    d[c[j]] += 1
    if d[c[i]] == 0:
        del d[c[i]]
    ans = max(ans, len(d))

print(ans)
