import sys

string = sys.stdin.readline().rstrip().upper()
upper_stirng = list(string)
set_string = list(set(string))

# set_string 에서 i로 문자열을 받아주고
# 그 문자열이 upper_string에 얼마나 있는지 count 체크
check = []
ch_string = []
for i in set_string:
  c = upper_stirng.count(i)
  check.append(c)
  ch_string.append(i)

# check의 max 값이 1개 이상 있다면
# 여러 문자가 여러개 있다는 뜻이므로
# ?출력한다

# print(check)
# print(ch_string)
cnt = check.count(max(check))
if cnt > 1:
  print("?")
else:
  ch_index = check.index(max(check))
  print(ch_string[ch_index])