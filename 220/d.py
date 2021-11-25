N = int(input())

A = list(map(int, input().split()))

MOD = 998244353

dp = [[0] * 10 for _ in range(N+1)]
print(dp)
dp[1][A[1]] = 1

for i in range(1, len(A)-1):
    for j in range(10):
        dp[i+1][(j + A[i+1])%10] += dp[i][j] 
        dp[i+1][(j * A[i+1])%10] += dp[i][j]
    print(dp)

for i in range(10):
    print(dp[N-1][i]%MOD)
