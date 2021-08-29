N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
 
for i in range(N):
    for j in range(i):
        for k in range(j):
            x1, y1 = P[i]
            x2, y2 = P[j]
            x3, y3 = P[k]
            x1 -= x3
            x2 -= x3
            y1 -= y3
            y2 -= y3
            if x2*y1 == x1*y2:
                print('Yes')
                exit()
 
print("No")