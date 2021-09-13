H, W = map(int, input().split())

fields = [list(input()) for _ in range(H)]

MOD = 10 ** 9 + 7

dp = [[0] * (W+1) for _ in range(H+1)]
dp[H-1][W] = 1

for i in range(H-1, -1, -1):
    for j in range(W-1, -1, -1):
        if fields[i][j] == "#":
            dp[i][j] = 0
        else:
            dp[i][j] = (dp[i+1][j] + dp[i][j+1]) % MOD

print(dp[0][0])