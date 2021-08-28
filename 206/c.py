from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)

cnt = 0
for i in range(N):
    c[A[i]] -= 1
    cnt += N-(i+1)-c[A[i]]

print(cnt)