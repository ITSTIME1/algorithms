s=input()
j=0
i=0
# 6
# 4
for k in range(len(s)-2):
    if s[k:k+3]=='JOI':j+=1
    if s[k:k+3]=='IOI':i+=1
print(j)
print(i)
