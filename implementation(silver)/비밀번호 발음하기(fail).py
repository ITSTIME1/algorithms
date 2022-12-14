#모음 받아오기 
lst = ['a','e','i','o','u']
#모음이 연속되면 안되지만 예외경우 처리 
accept = ['ee','oo']
while True :
    x=y=0
    password = input()
    #들어온 값이 end면 그대로 리턴 
    if password == 'end' :
        break
    #카운트 
    cnt = 0
    #모음개수세기 
    for i in lst :
        if i in password :
            cnt +=1 
    #모음이 없으면 부적합 
    if cnt <1 :
        print(f'<{password}> is not acceptable.')
        continue
    #모음만 연속 3개거나 자음만 연속 3개인 경우 체크 
    for i in range(len(password)-2) :
        if password[i] in lst and password[i+1] in lst and password[i+2] in lst :
            x = 1 
        elif not(password[i] in lst) and not(password[i+1]in lst) and not(password[i+2] in lst) :
            x = 1 
    if x == 1 :
        print(f'<{password}> is not acceptable.')
        continue
    #같은 글이 연속 두개인지 체크 하지만 'e'나 'o'면 컨티뉴 
    for i in range(len(password)-1) :
        if password[i]==password[i+1] :
            if password[i] == 'e' or password[i] == 'o' :
                continue
            else :
                y = 1 
    if y == 1 :
        print(f'<{password}> is not acceptable.')
        continue
    #예외 케이스를 통과하면 적합 
    print(f'<{password}> is acceptable.')