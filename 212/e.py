n, m, k = map(int, input().split())
G = [[] for _ in range(n)]

mod = 998_244_353

for _ in range(m):
    u, v = map(int, input().split())
    u -=1 
    v -= 1
    G[u].append(v)
    G[v].append(u)

dp = [[0]* n for _ in range(k+1)]
dp[0][0] = 1

for i in range(k):
    s = 0
    for j in range(n):
        s += dp[i][j]
    for j in range(n):
        dp[i+1][j] = s - dp[i][j]
        for l in G[j]:
            dp[i+1][j] -= dp[i][l]
        dp[i+1][j] %= mod

print(dp[k][0])