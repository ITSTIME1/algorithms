def solution(n):
    answer = 0
    
    # check = [i for i in range(1, n+1)]
    result = []
    
    for i in range(1, n+1):
        if not result:
            result.append(i)
            continue
        
        if (result[-1] + 1) % 3 == 0 or 3 in list(map(int, str(result[-1] + 1))):
            re = result[-1] + 1
                
                
            while re % 3 == 0 or 3 in list(map(int, str(re))):
                re += 1
                
            result.append(re)
                
        else:
            result.append(result[-1] + 1)
    
    
    return result[-1]
    

    
                
        
            
        