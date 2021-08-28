n, a, x, y = map(int, input().split())
 
if n > a:
    print(a * x + (n-a)* y)
else:
    print(x * n)