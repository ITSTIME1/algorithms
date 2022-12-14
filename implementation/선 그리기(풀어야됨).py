dp=[0]*10001
for _ in range(int(input())):
    a,b=map(int,input().split())
    for i in range(a,b):
        dp[i]=1
        print(dp)
print(sum(dp))