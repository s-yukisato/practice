import heapq
from collections import defaultdict

INF = float('inf')


def solve():
    n = int(input())
    # 開始位置が同じものをまとめる
    d = defaultdict(list)
    for _ in range(n):
        l, r = map(int, input().split())
        d[l].append(r)
    # 開始位置の速い順にする
    left_list = [key for key in d]
    left_list.sort()
    # 最後のnext_left用
    left_list.append(INF)

    # 現在位置
    now = 1
    # 締め切り(r)の近いものを順に格納する
    hp = []
    for i in range(len(left_list)-1):
        # 開始位置
        l = left_list[i]
        # hp追加のタイミング
        next_l = left_list[i+1]
        # 無駄な探索をしない
        now = max(now, l)
        for r in d[l]:
            heapq.heappush(hp, r)

        # 全ての球を箱詰めするか、更新のタイミングを迎えるか
        while hp and now < next_l:
            r = heapq.heappop(hp)
            # 現在位置が締め切りを超えていた（箱詰め不可）
            if now > r:
                print("No")
                return
            now += 1
    print("Yes")
    return


t = int(input())
for _ in range(t):
    solve()
