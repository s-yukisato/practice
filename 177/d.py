# import sys
# input = sys.stdin.readline
from operator import add
from functools import reduce

def II(): return int(input())
def II_(): return input()
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI_(): return list(input())
def TL(n): return [list(map(int, input().split())) for _ in range(n)]
def TL_(n): return [list(input()) for _ in range(n)]


def yn(judge, yes="Yes", no="No"): print(yes if judge else no)


from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

MOD = 10 ** 9 + 7
INF = float('inf')
N, M = MI()

UF = UnionFind(N)

for _ in range(M):
    a, b = MI()
    a-= 1
    b-= 1
    UF.union(a, b)


ans = 0
for i in range(N):
    friends = UF.size(i)
    ans = max(ans, friends)

print(ans)



