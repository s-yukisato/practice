import re

N = int(input())
S = input()

ans = re.sub(r"axa|ixi|uxu|exe|oxo", "...", S)

print(ans)