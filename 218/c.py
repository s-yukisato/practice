N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]


def rotate(oldList, n):
    newList = [["."] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            newList[n-x-1][y] = oldList[y][x]
    return newList

def upper_left_corner(targetList, n):
    min_x = n
    min_y = n
    for y in range(n):
        for x in range(n):
            if targetList[y][x] == "#":
                min_x = min(min_x, x)
                min_y = min(min_y, y)
    return (min_x, min_y)
    

def is_same(list1, list2):
    min_x1, min_y1 = upper_left_corner(list1, N)
    min_x2, min_y2 = upper_left_corner(list2, N)

    place1 = []
    place2 = []

    for y in range(min_y1, N):
        for x in range(min_x1, N):
            if list1[y][x] == "#":
                place1.append((y-min_y1)+(x-min_x1))
    
    for y in range(min_y2, N):
        for x in range(min_x2, N):
            if list2[y][x] == "#":
                place2.append((y-min_y2)+(x-min_x2))
    
    if place1 == place2:
        return True
    return False

R = T
isSame = False
for _ in range(4):
    if is_same(S, R):
        isSame = True
    R = rotate(R, N)

print("Yes" if isSame else "No")
