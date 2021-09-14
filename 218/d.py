N = int(input())

Z = set(tuple(map(int, input().split())) for _ in range(N))

ans = 0

for z1 in Z:
    for z2 in Z:
        if z2[0] > z1[0] and z2[1] > z1[1]:
            s = (z2[0], z1[1])
            t = (z1[0], z2[1])
            if s in Z and t in Z:
                ans += 1

print(ans)
