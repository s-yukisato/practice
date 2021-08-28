from math import gcd
N, M = map(int, input().split())
op = [list(map(int, input().split())) for _ in range(M)]

op.sort(key=lambda x: x[1])

ans = 0
n = N
for a, c in op:
    g = gcd(n, a)
    ans += (n -g) *c
    n = g

print(ans if n == 1 else -1)