N = int(input())

P = list(map(float,input().split()))

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(1, N):
    for j in range(i):
        dp[i][j] = dp[i-1][j-1] * P[i] + dp[i-1][j] * (1-P[i])

ans = 0
for i in range(N):
    if i > N-i:
        ans += dp[N-1][i]
print(dp)
print(ans)