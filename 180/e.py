N=int(input())
city=[list(map(int,input().split())) for i in range(N)]
print(f"{city=}")
 
inf=10**10
 
cost=[[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        cost[j][i]=abs(city[i][0]-city[j][0])+abs(city[i][1]-city[j][1])+max(0,city[i][2]-city[j][2])
        cost[i][j]=abs(city[i][0]-city[j][0])+abs(city[i][1]-city[j][1])+max(0,city[j][2]-city[i][2])
print(f"{cost=}")
 
 
ALL=2**N
dp=[[inf]*N for i in range(ALL)]
dp[0][0]=0
 
for i in range(ALL):
    for now in range(N):
        if i&(1<<now)==1:
            continue
        for nxt in range(N):
            if nxt==now:
                continue
            dp[i|1<<nxt][nxt]=min(dp[i|1<<nxt][nxt],dp[i][now]+cost[now][nxt])
 
print(dp[ALL-1][0])