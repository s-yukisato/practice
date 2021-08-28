n, x = map(int, input().split())
a = list(map(int, input().split()))

sum_ = sum(a)
m = len(a)//2
print("Yes" if x-(sum_-m) >= 0 else "No")