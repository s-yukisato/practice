# import sys
# input = sys.stdin.readline
from functools import reduce
from operator import mul
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

S = list(input())
T = list(input())

ans = INF

for i in range(len(S)-len(T)+1):
    tmp = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            tmp += 1
    ans = min(ans, tmp)

print(ans)
