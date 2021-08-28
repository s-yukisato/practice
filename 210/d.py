H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

INF = 10 ** 18
ans = INF

for _ in range(2):
    dp = [[INF] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1])
            ans = min(ans, A[i][j] + C*(i+j) + dp[i][j])
            dp[i][j] = min(dp[i][j], A[i][j] - C*(i+j))
    
    A.reverse()

print(ans)
