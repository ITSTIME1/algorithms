n = int(input())
while True:
    flag = True
    for i in str(n):
        print(i)
        if i != '4' and i != '7':
            flag = False
            n -= 1
            print(n)
        print("오켕")
    print("오케")
    if flag:
        print(n)
        break

# 예를 들어 77 같은경우
# 초반에 flag = True로 바꿔주고
# if문의 들어가지 않기 때문에
# 처음 7일떄 오켕을 출력하고
# 다음 문자를 검사할때도 7이라면 
# if문을 타지 않기 때문에
# N 또한 더이상 줄어들지 않고
# 다음 7에서 오케를 출력하면
# 아래 if문을 만나는데
# if문을 타지 않았기 때문에
# 해당 flag 값은 처음에 while문이 돌아갈때 
# flag = True 값을 유지하고 있기 때문에
# if flag 문을 타고 가장 큰 금민 수 값을 찾을 수 있게 된다.

