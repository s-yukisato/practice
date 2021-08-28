N = int(input())

L = [0] * N
R = [0] * N

for i in range(N):
    t, l, r = map(int, input().split())
    L[i], R[i] = [(l, r), (l, r-0.5), (l+0.5, r), (l+0.5, r-0.5)][t-1]

ans = 0
for i in range(N):
    for j in range(i+1, N):
        ans += (max(L[i], L[j]) <= min(R[i], R[j]))

print(ans)