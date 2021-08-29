# import sys
# input = sys.stdin.readline

def II(): return int(input())
def II_(): return input()
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI_(): return list(input())
def TL(n): return [list(map(int, input().split())) for _ in range(n)]
def TL_(n): return [list(input()) for _ in range(n)]


def yn(judge, yes="Yes", no="No"): print(yes if judge else no)


MOD = 10 ** 9 + 7
INF = float('inf')

from collections import defaultdict

d = defaultdict(int)


N, W = MI()
for _ in range(N):
    s, t, p = MI()
    d[s] += p
    d[t] -= p

l = sorted(list(d.items()))
useL = 0
for time, water in l:
    useL += water
    if useL > W:
        print("No")
        break
else:
    print("Yes")





