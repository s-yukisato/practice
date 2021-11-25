

N, M = map(int, input().split())

left = set()
right = set()

for _ in range(M):
    L, R = map(int, input().split())
    if L == 1:
        left.add(R)
    if R == N:
        right.add(L)

for l in left:
    if l in right:
        print("POSSIBLE")
        exit()

print("IMPOSSIBLE")
