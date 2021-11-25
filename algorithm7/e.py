N = int(input())

for i in range(1, 31):
    x = 1
    for j in range(1, 31):
        x *= 3
        if i == j:
            x += 1
    if x == N:
        print(i)
        exit()

print(-1)