from collections import defaultdict

N, M = map(int ,input().split())
choice = [list(map(int ,input().split())) for _ in range(M)]

K = int(input())
balls = [list(map(int ,input().split())) for _ in range(K)]

for _ in range(K):
    d = defaultdict(int)
    for l in balls:
        for i in range(2):
