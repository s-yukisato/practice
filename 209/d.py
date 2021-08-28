from collections import deque

N ,Q = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)

que = deque()
color = [-1]*N
color[0] = 0
que.append(0)

while que:
    t = que.pop()
    for i in G[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.appendleft(i)

for i in range(Q):
    a, b = map(lambda x: int(x)-1, input().split())
    print("Town" if color[a] == color[b] else "Road")