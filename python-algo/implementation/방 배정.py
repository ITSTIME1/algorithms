n, k=map(int, input().split())
w=[0]*1000
m=[0]*1000
for i in range(n):
    s, g=map(int, input().split())
    if s==0:
        w[g]+=1
    elif s==1:
        m[g]+=1

print(w[1:7])
print(m[1:7])
for i in range(1,7):

    if(m[i]%k==0):
        m[i]=m[i]//k
    else:
        m[i]=m[i]//k+1

    if(w[i]%k==0):
        w[i]=w[i]//k
    else:
        w[i]=w[i]//k+1

result=sum(m)+sum(w)
print(result)