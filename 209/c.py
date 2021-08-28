n = int(input())
C = list(map(int, input().split()))
C.sort()

MOD = 10 ** 9+7

ans = 1
for i, c in enumerate(C):
    ans *= max(0, c - i)
    ans %= MOD

print(ans)
