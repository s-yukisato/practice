S = list(map(int, input()))

odd = sum(S[:-1:2])
even = sum(S[1:-1:2])


if (odd * 3 + even) % 10 == S[-1]:
    print("Yes")
else:
    print("No")