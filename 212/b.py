x = list(input())
x = [int(i) for i in x]

if x[0] == x[1] == x[2] == x[3]:
    print("Weak")
    exit()

if (x[0] % 10) == (x[1]-1) % 10 == (x[2]-2) % 10 == (x[3]-3) % 10:
    print("Weak")
    exit()

print("Strong")