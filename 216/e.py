from bisect import bisect_left
def II(): return int(input())
def II_(): return input()
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

INF = float('inf')


N, K = MI()
L = LI()
L.sort()

ans = 0
for i in reversed(range(L[-1]+1)):
    idx = bisect_left(L, i)
    quantity = N - idx
    if K - quantity >= 0:
        K -= quantity
        ans += i * quantity
    else:
        ans += i * K
        break
    

print(ans)

