N = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def dfs(n):
    mx = 0
    divisors = make_divisors(n)
    print(divisors)
    if divisors[1] == n:
        return mx
    for num in divisors[1:n-1]:
        mx = max(mx, dfs(n//num+1) + 1)
    return mx


ans = dfs(N)
print(ans)
