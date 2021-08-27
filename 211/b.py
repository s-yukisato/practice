s = [input() for _ in range(4)]
s.sort()

c = ["H", "2B", "3B", "HR"]
c.sort()

print("Yes" if s == c else "No")