N = int(input())

A = list(map(int, input().split()))

dp = [[0, 0] for _ in range(N+1)]
dp[0] = [1, 1]

for i in range(1, N+1):
    dp[i][0] += dp[i-1][0] + dp[i-1][1]
    dp[i][1] += dp[i-1][0]

print(dp[N][0] * dp[N][1])
