N = int(input())
A = list(map(int, input().split()))

ans = 0

for i in range(N):
    min_val = 10 ** 9
    for j in range(i, N):
        min_val = min(min_val, A[j])
        ans = max(ans, min_val * (j-i+1))

print(ans)