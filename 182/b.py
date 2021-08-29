N = int(input())
A = list(map(int, input().split()))

maxA = max(A)

ans = 0
cnt = 0
for i in range(2, maxA+1):
    tmp = 0
    for a in A:
        if a % i == 0:
            tmp += 1
    if cnt <= tmp:
        cnt = tmp
        ans = i

print(ans)