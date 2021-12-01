N = int(input())
H = W =1001

fields = [[0] * H for _ in range(W)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    fields[ly][lx] += 1
    fields[ry][rx] += 1
    fields[ly][rx] -= 1
    fields[ry][lx] -= 1

for i in range(H):
    for j in range(1, W):
        fields[i][j] += fields[i][j-1]

for j in range(W):
    for i in range(1, H):
        fields[i][j] += fields[i-1][j]

ans = [0] * (N+1)
for i in range(H):
    for j in range(W):
        ans[fields[i][j]] += 1

print(*ans[1:], sep="\n")
