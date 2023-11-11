import sys
from collections import defaultdict, deque
input = sys.stdin.readline


N = int(input())

# 학생들 목록
dic = defaultdict(list)

for _ in range(N):
	# 학생번호
	number, a, b, c, d = list(map(int, input().split()))
	# 학생들의 성적을 국 영 수 과 순으로 넣어준다.
	dic[number].append(a)
	dic[number].append(b)
	dic[number].append(c)
	dic[number].append(d)
		
award= []
index = 0
award_len = 0
while award_len != 4:
	compare = []
	for key, value in dic.items():
		compare.append((key, value[index]))

	# sort를 이용해서 점수가 가장 높은 순 그리고 점수가 높다면, 번호가 가장 빠른순으로 정렬한다.
	compare_sort = deque(sorted(compare, key=lambda x : (-x[1], x[0])))
	
	while compare_sort:
		# 받은 사람이라면 제외하는거지
		if compare_sort[0][0] in award:
			compare_sort.popleft()
			continue
		else:
			award.append(compare_sort[0][0])
			award_len+=1
			index+=1
			break
print(" ".join(map(str, award)))

# swap해서 풀수도 있겠네
# 그러면 더 빠르겠다. 나처럼 딕셔너리 한번더 거치지 않더라도


