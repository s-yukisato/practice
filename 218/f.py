from collections import deque

INF = 10 ** 9 + 7
N, M = map(int, input().split())

G = [[] for _ in range(N)]

dict = [INF] * N

for _ in range(M):
    s, t = map(lambda x: int(x)-1, input().split())
    G[s].append(t)


que = deque([0])
dict[0] = 0
while que:
    now = que.pop()
    nears = G[now]
    for near in nears:
        que.append(near)
        dict[near] = min(dict[near], dict[now] + 1)

print(dict)