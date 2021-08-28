import math

a, b, c, d = map(int, input().split())

diff = d*c-b
ans = -1
if diff > 0:
    ans = math.ceil(a/diff)

print(ans)

