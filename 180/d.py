X, Y, A, B = map(int, input().split())

cnt = 0
while X * A <= X + B and X * A < Y:
    X *= A
    cnt += 1

print(cnt + (Y-1-X)//B)