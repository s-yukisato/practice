p = int(input())

k = [0] * 11
k[0] = 1
for i in range(1, 10+1):
    k[i] = k[i-1] * i

cnt = 0
for i in reversed(k):
    cnt += p// i
    p %= i

print(cnt)