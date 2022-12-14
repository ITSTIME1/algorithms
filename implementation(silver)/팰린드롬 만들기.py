import collections
import sys

word = sys.stdin.readline().rstrip()
# counter 를 이용하면 dic 형태로 제공해주네
# word 의 개수랑 같이 dic 형태로 제공
check_word = collections.Counter(word)

cnt = 0
result = ''
mid = ''

for k, v in list(check_word.items()):
    if v % 2 == 1: #홀수라면
        cnt += 1
        mid = k #중간에 들어갈 값으로 저장
        # 홀수가 두개 이상이면 어떻게 만들어도 팰린드롬이 될 수 없음
        # 여기서 홀수란 각 문자가 홀수의 개수를 가진다면 그 알파벳의 개수들 중
        # 홀수가 두개 이상이라면 절대적으로 만들수 없다
        # ex) ABBAAC
        # ABCABA
        # 이건 어떻게 만들어도 팰린드롬이 될 수 없다
        # 때문에 팰린드롬이 만들어지는 즉 회문이 만들어지는 조건은
        # 알파벳이 문장에나온 횟수가 홀수이면서 그런 문자열이 두개 이상 존재한다면
        # 만들 수 없다
        # 만약 그렇지 모두 짝수개라면
        # 해당 알파벳이 나온 횟수 // 2 해서 정확히 앞에서부터
        # 문자열을 만들어준다면
        # AABB

        # 같은 경우 2//2 A 가 한번 B가 한번씩 만들어지게 되면
        # AB 가 만들어지게 되고
        # 짝수기 때문에
        # 문자열을 뒤집어서 더해준 결과가
        # ABBA 가 정답이 된다
        # 만약 홀수개 문자가 존재한다면 AAABB
        # 그렇다면 중간값을 하나 설정해서
        # 홀수개의 중간값을 사용한다 
        # 그렇게 된다면
        # mid 값은 정해졌기 때문에
        # AAABBCC
        # 이렇게 되면 a 만 홀수가 되고 나머지는 짝수가 되기 때문에
        # mid 값은 홀수값으로 정해지게 된다
        # 만약 AAABBBCC 이런 겨우라면
        # 홀수를 가진 문자열 두개 이상이오면 회문이 만들어질 수 없기 때문에
        # 이런건 불가능 하다
        # 이렇게해서 홀수의 문자열을 mid 값으로 잡아두고

        # 이제 사전순으로 정렬해달라는 조건에 따라
        # 문자열을 정렬해주고
        # 그 문자열이 몇번 나왔는지 
        # AAAAAABBBCC
        # AAABCBCBAAA
        # 오케이


        if cnt >= 2: #홀수가 2개이상이면 팰린드롬이 될 수 없다!!
            print("I'm Sorry Hansoo")
            exit()

for k, v in sorted(check_word.items()): #정렬을 통해 사전순으로 for문을 돌게함

    result += (k * (v // 2)) #정확히 절반으로 나뉜 문자열을 만들어야 하므로 현재 갯수를 2 나로눠줌

print(result + mid + result[::-1]) # 앞+중간+뒤 를 더해 문자열 출력


# 이 문제에서 새롭게 알게 된 내용은
# collections.Counter 함수이다
# 이 함수는 리스트를 -> 딕셔너리로 키와:횟수 로 변형해서 만들어지고
# for k, v in (list.items())
# items() 함수로 가져오게 되면
# items() 로 k, v 둘다 받을 수 있따
# 추가적으로 팰린드롬이 무엇인지 알게 되었고
# 이 회문을 만들기 위한 조건들 그리고 어떻게 하면 만들어질 수 있는지 알게 된 문제였다

# 알파벳 ord 를 사용해서 푸는 방법도 있던데 이건 나중에 해보자

# 홀수가 두개 이상이면 팰린드롬이 만들어질 수 없기 때문에
# 무조건 홀 수는 한개이어야 하고
# 그 한개가 mid 역할을 하게 된다
# 즉 중간값 역할을 하기 때문에
# AAAABBBCCCCBB
# 어떠한 경우에도 홀수가 하나만 나오면 그 홀수는 항상 중간값을 가지게 되어있다