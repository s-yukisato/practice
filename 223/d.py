from heapq import heappush, heappop

N, M = map(int, input().split())
edge = [[] for i in range(N+1)]

indeg = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    indeg[b] += 1

q = []

for i in range(1, N+1):
    if indeg[i] == 0:
        heappush(q, i)

ans = []

while q:
    v = heappop(q)
    print(v)
    ans.append(v)
    for to in edge[v]:
        indeg[to] -= 1
        if indeg[to] == 0:
            heappush(q, to)

if len(ans) == N:
    print(*ans)
else:
    print(-1)