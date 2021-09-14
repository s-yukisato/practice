nums = list(map(int, [x for x in input()]))

def calc(nums, operator):
    res = nums[0]
    for i, oper in enumerate(operator):
        if oper == "+":
            res += nums[i+1]
        else:
            res -= nums[i+1]
    return res

def create_operators(n):
    operator = [["-"] * n for _ in range(2**n)]

    for i in range(2**n):
        for j in range(n):
            if i >> j & 1:
                operator[i][j] = "+"

    return operator

operator = create_operators(3)
for i in range(8):
    ans = calc(nums, operator[i])
    if ans == 7:
        print(f"{nums[0]}{operator[i][0]}{nums[1]}{operator[i][1]}{nums[2]}{operator[i][2]}{nums[3]}=7")
        break