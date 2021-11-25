import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs(cur, prev, dist):
    ans[0] += dist
    for to in info[cur]:
        if to == prev:
            continue
        dfs(to, cur, dist+1)
        sub[cur] += sub[to]


if __name__ == '__main__':
    N = int(input())
    info = defaultdict(list)
    for _ in range(N - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        info[u].append(v)
        info[v].append(u)

    ans, sub = [0] * N, [1] * N
    dfs(0, -1, 0)
    que = deque([0])
    while que:
        cur = que.popleft()
        for to in info[cur]:
            if ans[to]:
                continue
            ans[to] = ans[cur] - sub[to] + (N - sub[to])
            que.append(to)
    print(ans)
    print(sub)
    for a in ans:
        print(a)
