
# 아이디를 입력받는 부분.
str1 = input('아이디를 입력하세요: ')

# 로직 함수
def recommend_newId(new_id):

    # 답을 받을 변수
    answer = ''
    # 변경 변수
    temp_str = ""

    #1 입력받은 대문자를 소문자로 변경하는 함수 입력받은(new_id).lower()
    temp_str = new_id.lower()
    #2 소문자로 치환한 값을 temp_list 리스트 변수에다가 한글자씩 넣어줌.
    temp_list= list(temp_str)
    
    #3 temp_list 의 길이 만큼 반복문 실행
    for i in range(0, len(temp_list)):
        #4 만약 리스트에 문자가 소문자가 아니거나 또는 숫자가 아나거나 받아온 값이 - 이거나 받아온 값이 _ 이거나 받아온 값이 . 이라면
        #5 대문자 같은것들을 제거
        if(not temp_list[i].islower() and not temp_list[i].isdigit() and temp_list[i] != '-' and temp_list[i] != '_' and temp_list[i] != '.'):
            temp_list[i] = '@'
            temp_str = "".join(temp_list)
            temp_str = temp_str.replace('@', '')



    while(temp_str.find('..') != -1):
        temp_str = temp_str.replace('..', '.')
    print('3단계: ', temp_str)

    # 4단계 temp_str이 빈 문자열이라면 a를 대입
    if temp_str.find('.') == 0:
        temp_str = temp_str[1:]
    if temp_str.rfind('.') == len(temp_str)-1:
        temp_str = temp_str[:len(temp_str)-1]

    if temp_str == '':
        temp_str = 'a'

    
    if len(temp_str) >= 16:
        temp_str = temp_str[:15]
        if temp_str.rfind('.') == len(temp_str) -1:
            temp_str = temp_str[:len(temp_str)-1]

    if len(temp_str) <= 2:
        while(len(temp_str) < 3):
            temp_str = temp_str + temp_str[len(temp_str)-1]
    
    answer = temp_str
    return answer


result = recommend_newId(str1)
print("신규 아이디 : ", result)