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

Sx, Sy, Gx, Gy = MI()
print((Sx*Gy + Gx* Sy)/(Sy+Gy))
