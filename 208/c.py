N, K = map(int, input().split())
A = list(map(int, input().split()))

sortA = sorted(A)

eq = K // N
md = K % N

border = sortA[md]

for a in A:
    if a < border:
        print(eq + 1)
    else:
        print(eq)