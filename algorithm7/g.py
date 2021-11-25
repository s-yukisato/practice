N = int(input())
def f(x):
    if x == 0:
        return []
    ret = []
    if x%3 == 0:
        ret = [i*3 for i in f(x//3)]
    if x%3 == 1:
        ret = [i*3 for i in f((x-1)//3)]
        ret.append(1)
    elif x%3 == 2:
        ret = [i*3 for i in f((x+1)//3)]
        ret.append(-1)
    return ret
ans = f(N)
print(len(ans))
print(' '.join(map(str,ans)))