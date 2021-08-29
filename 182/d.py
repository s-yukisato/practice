N = int(input())
A = list(map(int, input().split()))
 
ans = 0
x = 0
acc = 0
mx = 0
for a in A:
    acc += a
    if acc > mx:
        mx = acc
    x2 = x+mx
    x += acc
    if max(x, x2) > ans:
        ans = max(x, x2)
 
print(ans)