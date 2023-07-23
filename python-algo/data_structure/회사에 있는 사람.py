# 문제분석


# 로그가 주어졌을때, 출퇴근 시간은 일정하지 않고
# 출퇴근 시간이 일정하지 않기 때문에
# 현재 회사에 있는 사람의 인원수가 다르다
# 로그의 개수는 최대 100만개 까지만 주어질 수 있음.	

import sys

n = int(sys.stdin.readline().strip())


# enter 나 leave 가 주어진다고 했을때
# 동명이인은 없다
# 대소문자가 다른 경우 다른 이름으로 가정한다.

# enter, leave
# enter, enter
# leave, enter
# leave, leave


# 이런 경우들이 있는데

# 10^6승을 선회하기엔 너무 오랜 시간이 걸리고
# dic 에서 최선의 경우가 O(1)의 시간복잡도가 걸리는데
# 최악의 경우 in 자체가 O(n)이 걸리니
# 12개 = 1조의 시간이 걸려 시간안에 통과를 못해



stu = {}

for i in range(n):
	string, num = input().split()
	if string not in stu:
		stu[string] = [num]
	else:
		stu[string].append(num) 

ans = []
for k, v in stu.items():
	a = v.pop()
	if a == "enter":
		ans.append(k)

ans.sort(reverse = True)

for _ in ans:
	print(_)