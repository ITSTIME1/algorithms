string = input().rstrip()

string_arr2 = []
string_arr = []
flag = False
tag_1 = ""
tag_2 = ""
for i in string:
    if i == "<":
        flag = True
        string_arr.append(i)
    elif i == ">":
        if flag == True:
            string_arr.append(i)
            flag = False
            # 공백이나 문자 숫자가 들어왔다면
    else:
        # flag 값이 true인지 false 인지 판단해주고
        # flag 값이 true 라면 여는 태그가 진행중에 있기 떄문에
        # 문자를 string_arr에 넣어주고
        # flag 값이 false 상태라면 tag가 닫힌 거기 때문에 다른 배열에 넣어준다.
        if (flag == True):
            string_arr.append(i)
        else:
            string_arr2.append(i)

# 태그 완성
for j in range(len(string_arr) - 1):
    if (string_arr[j] == ">" and string_arr[j + 1] == "<"):
        tag_1 = "".join(string_arr[:j + 1])
        tag_2 = "".join(string_arr[j + 1:])

# 문자열 완성
# bsdfs +
# baekjoon online judge
change_new_list = "".join(string_arr2)
change_string = change_new_list.split(" ")

check_string_list = []
for m in range(len(change_string)):
    check_string = list(change_string[m])
    check_string.reverse()
    s_string = ""
    for n in range(len(check_string)):
        s_string += check_string[n]
    check_string_list.append(s_string)
    s_string = ""

ss_string = ""
for s in range(len(check_string_list)):
    mem_string = ""
    mem_string += check_string_list[s]
    if (s == len(check_string_list) - 1):
        ss_string += mem_string
    else:
        ss_string += mem_string + " "

print(tag_1 + ss_string + tag_2)


# 엣지 케이스가 안잡힘

# 남의 풀이
ans = ""
tag = False
stack = ""
for i in input():
    if i == "<":
        tag = True
        ans += stack[::-1]
        stack = ""
        ans += i
        continue
    elif i == ">":
        tag = False
        ans += i
        continue
    elif i == " ":
        ans += stack[::-1] + " "
        stack = ""
        continue
        
    if tag:
        ans += i
    else:
        stack += i
print(ans+stack[::-1])
