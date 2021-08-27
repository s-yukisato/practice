from bisect import bisect_right

INF = 10**12

n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split())) + [-INF, INF]

B.sort()

ans = INF

for a in A:
    idx = bisect_right(B, a)
    ans = min(ans, abs(B[idx-1]-a))
    ans = min(ans, abs(B[idx]-a))

print(ans)


