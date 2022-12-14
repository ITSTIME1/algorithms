n = int(input())
card = list(map(int,input().split()))
student = []
for i in range(n) :
    if card[i] == 0 :
        student.insert(0,i+1)
    else :
        student.insert(card[i],i+1)
    print(student)
for i in reversed(student):
    print(i,end=' ')