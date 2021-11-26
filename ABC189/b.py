N, X = map(int, input().split())
X *= 100

now = 0
ans = -1
for i in range(N):
    v, p = map(int, input().split())
    now += v * p

    if now > X and ans == -1:
        ans = i+1

print(ans)