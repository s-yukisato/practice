N = int(input())

total_time = 0
ab = []

for _ in range(N):
    a, b = map(int, input().split())
    total_time += a / b
    ab.append((a, b))


rest = total_time / 2
length = 0

for i in range(N):
    a, b = ab[i]
    time = a / b
    if time <= rest:
        length += a
        rest -= time
    else:
        length += rest * b
        rest = 0

print(length)

