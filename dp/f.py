S = list(input())
N = len(S)
T = list(input())
M = len(T)

dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        if S[i] == T[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

sna = ""

while N and M:
    if dp[N][M] == dp[N-1][M]:
        N -= 1
    elif dp[N][M] == dp[N][M-1]:
        M -= 1
    else:
        sna += S[N-1]
        N -=1
        M -= 1

print(sna[::-1])