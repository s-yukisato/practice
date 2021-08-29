# import sys
# input = sys.stdin.readline
from itertools import permutations
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


N, K = MI()
T = TL(N)

direct = list(permutations(range(1, N)))

cnt = 0

for d in direct:
    tmp = 0
    for i in range(N-1):
        if i == 0:
            tmp += T[0][d[i]]
        else:
            tmp += T[d[i-1]][d[i]]
    else:
        tmp += T[d[i]][0]
    if tmp == K:
        cnt += 1

print(cnt)

