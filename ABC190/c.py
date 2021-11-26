N, M = map(int, input().split())

query = [list(map(int, input().split())) for _ in range(M)]

K = int(input())

data = [list(map(int, input().split())) for _ in range(K)]

ans = 0

for bit in range(2 ** K):
    balls = set()
    cnt = 0
    for i in range(K):
        if bit & 1 << i:
            balls.add(data[i][1])
        else:
            balls.add(data[i][0])
    
    for a, b in query:
        if a in balls and b in balls:
            cnt += 1
    ans = max(ans, cnt)

print(ans)