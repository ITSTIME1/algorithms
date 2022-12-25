# 문제분석

# 초기 상태랑 도달 상태랑 다른 말이 잇다
# 그럼 그 말을 골라서

# 두개의 말을 비교해서
# 서로 교환이 되서 같아진다면 ok
# 만약 같아지지 않는다며ㅑㄴㅁ


T = int(input())
for _ in range(T):
	n = int(input())
	first = list(input())
	second = list(input())

	cnt = 0
	for j in range(len(first)-1):

		if first[j] != second[j]:
			change_word = first[j+1] + first[j]
			if change_word == second[j] + second[j+1]:
				cnt += 1
				first[j], first[j+1] = first[j+1], first[j]
				continue
			else:
				if first[j] == "W":
					first[j] = "B"
				else:
					first[j] = "W"
				cnt += 1

	print(cnt)

# 이렇게 푸는게 좀 더 현실적인 풀이방법 같다..
# 위에 풀이도 예제케이스는 맞지만 이상하게 안되는 이유를 모르겠다..
# 우선순위로 swap 이 가능하다면 swap 을 했는데
# swap 을 하고 나서 나머지 것들을 보고 또 결정을 할 수 있는 greedy 한 문제라고는 생각이 들었지만
# fail..
t = int(input())
arr=[]
ans=0
answer=[]
for i in range(t):
    n = int(input())
    first = input()
    second = input()

    for i in range(n):
        if first[i]!=second[i]:
            arr.append(first[i])
    if arr.count('B')>=arr.count('W'):
        ans=arr.count('B')
    else:
        ans = arr.count('W')
    answer.append(ans)
    arr=[]
for a in answer:
    print(a)
