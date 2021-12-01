N = int(input())

registered = set()

for i in range(1, N+1):
    s = input()
    if not s in registered:
        registered.add(s)
        print(i)
