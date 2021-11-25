S = input()
T = input()

N = len(S)
M = len(T)


ans = 0
for i in range(N-M+1):
    tmp = 0
    for j in range(M):
        if S[i+j] == T[j]:
            tmp += 1
    ans = max(ans, tmp)

print(M-ans)