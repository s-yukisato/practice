N, W = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

INF = 10**18
dp = [[0] * (10**5+1) for _ in range(N+1)]
for i in range(1, 10**5+1):
    dp[0][i] = INF


for i in range(1, N+1):
    w, v = items[i-1]
    for j in range(10**5+1):
        if j - v < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-v] + w)
ans = 0
for i in range(10**5+1):
    if dp[N][i] <= W:
        ans = max(ans, i)

print(ans)
