N, M = map(int, input().split())

INF = 10 ** 9 + 7

cost = [[INF] * N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    cost[a][b] = c

for i in range(N):
    cost[i][i] = 0

ans = 0
for k in range(N):
    for s in range(N):
        for t in range(N):
            cost[s][t] = min(cost[s][t], cost[s][k] + cost[k][t])
            if cost[s][t] < INF:
                ans += cost[s][t]

print(ans)