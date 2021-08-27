n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

INF = 10 ** 11
ans = [INF] * n

for i in range(2*n):
    ans[i%n] = min(ans[i%n], t[i%n], ans[(i-1)%n] + s[(i-1)%n])

print(*ans, sep="\n")