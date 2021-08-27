# mod = 10 ** 9 + 7

# s = list(input())

# sample = list("chokudai")

# dp = [[0] * len(s) for _ in range(8)]

# for i in range(len(s)):
#     if i == 0:
#         if s[i] == "c":
#             dp[0][0] = 1
#             continue
#     if s[i] == sample[0]:
#         dp[0][i] += dp[0][i-1] + 1
#     else:
#         dp[0][i] += dp[0][i-1]

# for i in range(1, 8):
#     for j in range(i, len(s)):
#         if s[j] == sample[i]:
#             dp[i][j] += (dp[i-1][j-1] + dp[i][j-1]) % mod
#         else:
#             dp[i][j] += dp[i][j-1]

# print(dp[7][len(s)-1])


f = [1] + [0] * 8

for i in input():
	j = 'chokudai'.find(i)
	if j != -1:
		f[j + 1] = (f[j + 1] + f[j]) % 1000000007

print(f[-1])