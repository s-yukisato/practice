N = int(input())

save = 1
day = 1
while N >= save:
    save += day
    day += 1

print(day-1)