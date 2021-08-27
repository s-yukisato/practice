n, m = map(int, input().split())
A = list(map(int, input().split()))

maxA = max(max(A), m)

exclude = [False] * (maxA+1)
isPrime = [True] * (maxA+1)
donotUsePrime = []

for a in A:
    exclude[a] = True

for i in range(2, maxA+1):
    if isPrime[i] == False:
        continue
    for j in range(i*2, maxA+1, i):
        isPrime[j] = False
        exclude[i] = exclude[i] or exclude[j]
    if exclude[i]:
        donotUsePrime.append(i)

for p in donotUsePrime:
    for j in range(p*2, m+1, p):
        exclude[j] = exclude[j] or exclude[p]

ans = [1]
for i in range(2, m+1):
    if not exclude[i]:
        ans.append(i)

print(len(ans))
print(*ans, sep="\n")
