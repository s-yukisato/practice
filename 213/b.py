n = int(input())
a = list(map(int, input().split()))


b = sorted(a, reverse=True)
ans = b[1]

print(a.index(ans)+1)
