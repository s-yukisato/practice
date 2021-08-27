import heapq

n = int(input())

hp = []
addis = 0


for _ in range(n):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(hp, query[1] - addis)
    elif query[0] == 2:
        addis += query[1]
    else:
        print(heapq.heappop(hp)+addis)
