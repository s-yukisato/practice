N, D = map(int, input().split())
M = 998244353

memo = [pow(2, i, M) for i in range(10 ** 6)]
print(memo)

cnt = 0

for i in range(D+1):
    if max(1, D-i) > N:
        continue

    numl = memo[i-1] if i > 0 else 1
    numr = memo[D-i-1] if i < D else 1
    maxD = N-1-max(i, D-i)

    cnt += (memo[maxD+1] -1) * numl * numr
    cnt %= M

cnt *= 2
cnt %= M
print(cnt)
