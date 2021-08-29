from functools import reduce
import math

N = int(input())
X = list(map(int, input().split()))

absX = list(map(abs, X))
print(sum(absX))

squareX = reduce(lambda acc, cur: math.sqrt(acc ** 2 + cur ** 2), absX)
print(squareX)

print(max(absX))