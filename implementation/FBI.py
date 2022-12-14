N = 5
det = "FBI"
arr = [] 
for i in range(1, N+1): 
    string = input()
    # 이런 문자가 string 에 있다면
    # 해당 인덱스를 저장해준다
    # 없으면 그냥 통과 
    if det in string: 
        arr.append(i)
    else:
    	pass

# 그리고 만약 리스트 가 존잰한다는건ㄱ
# fbi 라는 값이 있는 문자의 인덱스가 있기 때문에
# 그 값을 unpacking 해서 end 옵션을 준다음
# 출력 해준다.

# 리스트에 fbi 값이 없다는건 아무것도 fbi 라는 문자를
# 가지고 있다는게 아니기 때문에
# 문자열을 출력해준다.
if arr: 
    print(*arr, end = " ") 
else: 
    print("HE GOT AWAY!")