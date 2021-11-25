T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())
    ans = min(b//2, c)
    if ans != b//2:
        b -= ans * 2
        tmp = min(a//2, b//2)
        a -= tmp * 2
        ans += tmp
        if a >= 5:
            ans += a//5
    else:
        c -= ans
        tmp = min(a, c//2)
        ans += tmp
        if tmp != a:
            a -= tmp
            c -= tmp*2
            if c == 1 and a >= 3:
                ans += 1
                a -= 3
            if a >= 5:
                ans += a//5
    print(ans)