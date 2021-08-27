from collections import deque

MOD = 10**9+7

n, m = map(int, input().split())

connect = [[] for _ in range(n)]
# 頂点1からの最短距離
dist = [None] * n
# 最短距離でそこまでの頂点に到達できる組み合わせ
cnt = [0] * n

for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    connect[a].append(b)
    connect[b].append(a)

que = deque()
# スタート地点
que.append(0)
dist[0] = 0
cnt[0] = 1

while que:
    now = que.pop()
    for near in connect[now]:
        if dist[near] is None:
            dist[near] = dist[now] + 1
            que.appendleft(near)
            cnt[near]=cnt[now]
        elif dist[near] == dist[now] + 1: # 別の経路で同じ距離
            cnt[near] += cnt[now]
            cnt[near] %= MOD

print(cnt[n-1])