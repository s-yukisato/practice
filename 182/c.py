N = list(input())
lenN = len(N)
num = list(map(lambda x: int(x) % 3, N))
mod = sum(num) % 3
d = set(num)

if lenN == 1:
    if mod == 0:
        print(0)
    else:
        print(-1)
    exit()

if lenN == 2:
    if mod == 0:
        print(0)
    elif mod == 1 and 1 in d:
        print(1)
    elif mod == 2 and 2 in d:
        print(1)
    else:
        print(-1)
    exit()

if mod == 0:
    print(0)
elif mod == 1:
    if 1 in d:
        print(1)
    elif num.count(2) % 3 == 2:
        print(2)
elif mod == 2:
    if 2 in d:
        print(1)
    elif num.count(1) % 3 == 2:
        print(2)
else:
    print(-1)
