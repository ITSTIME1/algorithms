from collections import Counter
def solution(k, tangerine):
    answer= 0 
    dic = Counter(tangerine)
    li = [[k, v] for k, v in dic.items()]
    a = sorted(li, key=lambda x:x[1])
    
    while k > 0:
        answer += 1
        k -= a[len(a)-1][1]
        a.pop()
        
    return answer
            
            
# 어렵네.. 