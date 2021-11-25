from collections import defaultdict

N = int(input())
A = [int(x)%200 for x in input().split()]

cnt = 0

d = defaultdict(int)

for i in range(N):
    cnt += d[A[i]]
    d[A[i]] += 1

print(cnt)