N = input()
nums = ["111", "222", "333", "444", "555", "666", "777", "888", "999"]
if N[0:3] in nums or N[1:4] in nums:
    print("Yes")
else:
    print("No")
