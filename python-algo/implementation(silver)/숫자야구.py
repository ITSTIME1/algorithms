# 이 문제는 
# 일단 1~9 까지 3자리 숫자를 조합해서
# 만든 숫자를 가지고
# 상대방 숫자를 맞추는 게임이다.

# 우선 9p3 정도의 경우의 수가 나오고 중복을 허락하지 않고 순서가 중요하니까
# 순서가 바뀌게 되면 결과에 영향을 미치므로 조합이 아닌 순열을 사용해야 되는데
# 완탐식으로 한번 풀어보겠다

# 먼저 모든 경우의 수를 만들어서 리스트를 만들어줄거고
# 모든 경우의 수를 안다는건
# 내가 미리 말해서 s,b 의 유무를 알고 있다는건
# 한마디로 모든 경우의 수 중에서 이 수들과 스트라이크와 볼의 개수가 전부다 일치하는 숫자가ㅣ
# 바로 답의 가장 가까운 수이다
# 그 이유는 해당 숫자가 내가 말했던 숫자와 다르다면 만약 하나만 틀리고 3개는 맞다면 이래도 틀리다
# 왜냐 마지막에 틀린다는건 결국 답에 근접하지 않은 숫자라고 볼 수 있다 만약
# 1s 1b, 1s 0b, 2s, 0b 이라고 했을때 스트라이크의 개수도 맞고 볼의 개수도 똑같아야
# 해당 숫자의 범위가 작아지기 때문이다
# 이 문제의 핵심은 경우의 수를 줄이는것이다
# 무엇으로? 이미 내가 말해두었던 경우의 수들을 사용해서 결과를 얻어냈으니
# 그 결과를 역으로 이용하면 그 경우의 수들을 다 만족하는 수를 찾으면
# 결국 답이 되는 것이다.

# O(N3) 으로 해도 최대 100만정도
import itertools
import sys
num = list(itertools.permutations([_ for _ in range(1, 10)], 3))

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

total = []
for i in num:
	# 모든 나열된 경우의 수와 같아야 한다
	check = list(i)
	check = list(map(str, check))
	cnt = 0
	for j in range(len(arr)):
		st = 0
		ba = 0
		ar_check = list(map(str, str(arr[j][0])))
		for k in range(len(ar_check)):
			# 자리가 같다면
			if ar_check[k] == check[k]:
				st += 1
				continue
			elif check[k] in ar_check:
				ba += 1
		# 스트라이크와 ball이 맞는지 확인
		if str(st) == str(arr[j][1]) and str(ba) == str(arr[j][2]):
			cnt += 1
	if cnt == N:
		total.append(check)

print(len(total))


	
