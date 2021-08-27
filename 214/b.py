s, t = map(int, input().split())

cnt = 0
for i in range(s+1):
    for j in range(s-i+1):
        for k in range(s-i-j+1):
            if i*j*k <= t:
                cnt += 1

print(cnt)