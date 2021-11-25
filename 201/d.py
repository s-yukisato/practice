import sys
sys.setrecursionlimit(10**6)
INF = float('inf')
MOD = 10 ** 9+7

input = lambda: sys.stdin.readline().rstrip()


H, W = map(int, input().split())

A = [list(input()) for _ in range(H)]

dp = [[0] * (W+1) for _ in range(H+1)]

for i in range(H)[::-1]:
    x = 1 if A[i][W-1] == "+" else -1
    if (W-1+i) % 2 == 0:
        x *= -1
    dp[i][W-1] = dp[i+1][W-1] + x

for i in range(W)[::-1]:
    x = 1 if A[H-1][i] == '+' else -1
    if (H - 1 + i) % 2 == 0:
        x *= -1
    dp[H-1][i] = dp[H-1][i+1] + x

for i in range(H-1)[::-1]:
    for j in range(W-1)[::-1]:
        x = 1 if A[i][j] == '+' else -1
        if (i + j) % 2 == 0:
            x *= -1
            dp[i][j] = max(dp[i+1][j], dp[i][j+1]) + x
        else:
            dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + x

if H > 1 and W > 1:
    ans = max(dp[0][1], dp[1][0])
elif H > 1:
    ans = dp[1][0]
else:
    ans = dp[0][1]
if ans > 0:
    print('Takahashi')
elif ans < 0:
    print('Aoki')
else:
    print('Draw')