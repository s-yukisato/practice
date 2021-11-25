from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

MOD = 998244353
inv2 = (MOD+1)//2

bit = [0] * 330000

def add(pos, val):
    pos += 1
    while pos < len(bit):
        bit[pos] += val
        pos += pos & -pos

def get(pos):
    pos += 1
    ans = 0
    while pos:
        ans += bit[pos]
        ans %= MOD
        pos -= pos & -pos
    return ans

numbers = sorted(list(set(A)))

for i in range(N):
    A[i] = bisect_left(numbers, A[i])
    print(A)

ans = 0

for i in range(N):
    val = A[i]
    print(get(val))
    ans += pow(2, i, MOD) * get(val) % MOD
    ans %= MOD
    add(val, pow(inv2, i+1, MOD))

print(ans)

