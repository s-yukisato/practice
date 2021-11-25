S = input()
L, R  = map(int, input().split())


if len(S) != 1 and S[0] == "0":
    print("No")
    exit()

if L <= int(S) <= R:
    print("Yes")
else:
    print("No")