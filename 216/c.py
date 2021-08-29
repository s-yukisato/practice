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

if N == 1:
    print("A")
    exit()

ans = ""
cnt = 0
box = 2
flg = False

while True:
    cnt = 0
    while N % 2 == 0:
        N //= 2
        cnt += 1

    if N != 1:
        ans += "".join("B" * cnt)
    else:
        ans += "".join("B" * (cnt-1))
    if N == 1:
        break
    N -= 1
    ans += "A"

print("AA" + ans[::-1])