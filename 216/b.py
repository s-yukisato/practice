# import sys
# input = sys.stdin.readline
# from functools import reduce
# from operator import add, mul, sub
from collections import defaultdict, deque
import math
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


N = II()
ans = "No"

S = set()


for _ in range(N):
    s, t = input().split()
    if (s, t) in S:
        ans = "Yes"
    S.add((s,t))

print(ans)