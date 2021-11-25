from itertools import accumulate

N = int(input())

scheduled  = [[0] * (48+1) for _ in range(10**5+1)]

maxDay = 0
for _ in range(N):
    d, s, t = map(int, input().split())
    d -= 1
    s *= 2
    t = t * 2 - 1
    scheduled[d][s] += 1
    scheduled[d][t] -= 1
    maxDay = max(maxDay,d)

for d in range(maxDay+1):
    u = list(accumulate(scheduled[d]))
    if max(u) >= 2:
        print("Yes")
        exit()

print("No")

