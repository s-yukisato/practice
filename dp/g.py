import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())

edges = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    edges[u-1].append(v-1)

memo = [-1] * N

def dp(v):
    if memo[v] != -1:
        return memo[v]
    res = 0
    for to in edges[v]:
        res = max(res, dp(to) + 1)
    memo[v] = res
    return res


ans = 0
for v in range(N):
    ans = max(ans, dp(v))

print(ans)