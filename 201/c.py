S = list(input())

cnt = 0

for i in range(10000):
    flag = [False] * 10
    word = f'{i:04}'
    for w in word:
        flag[int(w)] = True
    
    correct = True
    for j in range(10):
        if S[j] == "o" and not flag[j]:
            correct = False
        if S[j] == "x" and flag[j]:
            correct = False
    if correct:
        cnt += 1

print(cnt)