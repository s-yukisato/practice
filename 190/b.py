N, S, D = map(int, input().split())

ans = "No"

for _ in range(N):
    x, y = map(int, input().split())
    if x < S and y > D:
        ans = "Yes"

print(ans)