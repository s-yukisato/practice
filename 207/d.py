import math
 
N = int(input())
S = [tuple(map(float, input().split())) for i in range(N)]
T = [tuple(map(float, input().split())) for i in range(N)]
 
 
def trans(X, i):
    # 点集合Xを、X[i]が減点になるように平行移動した集合を返す
    return [(p[0] - X[i][0], p[1] - X[i][1]) for p in X]
 
 
def dist(p, q):
    # 2点p,qの距離の2乗
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
 
 
def rot(X, theta):
    # 点集合Xを、theta回転する
    ret = []
    for x, y in X:
        xx = x * math.cos(theta) + y * -math.sin(theta)
        yy = x * math.sin(theta) + y * math.cos(theta)
        ret.append((xx, yy))
    return ret
 
 
def is_ok(S, T):
    # 2つの点集合S,Tが一致しているか判定する
    for p in S:
        flag = False
        for q in T:
            if abs(p[0] - q[0]) < 0.01 and abs(p[1] - q[1]) < 0.01:
                flag = True
                break
        if not flag: return False
    return True
 
 
if N == 1:
    print("Yes")
    exit()
 
# S[0]が原点になるように先にずらしておく
transS = trans(S, 0)
r = dist(S[0], S[1])
thetaS = math.atan2(transS[1][1], transS[1][0])
 
# (i,j)の組を全探索
for i in range(N):
    for j in range(N):
        # S[0],S[1] 間の距離が T[i],T[j] 間の距離が異なるならダメNo
        if dist(T[i], T[j]) != r: continue
        # 平行移動
        transT = trans(T, i)
        thetaT = math.atan2(transT[j][1], transT[j][0])
        # 回転移動
        rotS = rot(transS, thetaT - thetaS)
        # チェック
        if is_ok(rotS, transT):
            print("Yes")
            exit()
 
print("No")