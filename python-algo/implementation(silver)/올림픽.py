# 1. 금을 많이 받은 나라 순으로 정렬을한다.
# 2. 정렬을 완료한 후 하나씩 비교한다
# 3. 금을 많이 받았다면 cnt+=0, 금을 더 적게 받았다면 cnt+=1
# 4. 금의 개수가 동일하다면 은을 비교해서 상대방 은이 더높다면 cnt+=1
# 5. 금 은 개수가 동일하고 동의 개수가 상대방이 더 높다면 cnt+=1
# 6. 금 은 동 개수가 다 같다면 나 자신이거나 혹은 상대방이거나 cnt+=1

# N, K = map(int, input().split())
# info_dic = {}
# cnt_dic = {}
# for i in range(N):
# 	grade, g, s, b = map(int, input().split())
# 	info_dic[grade] = (g, s, b)
# 	cnt_dic[i+1] = 0 
# # 금을 기준으로 정렬

# result = sorted(info_dic.items(), key = lambda x : x[1][0], reverse=True)



# # [(1, (3, 0, 0)), (3, (0, 0, 2)), (4, (0, 2, 0)), (2, (0, 2, 0))]
# for i in range(len(result)):
# 	# 0 1 2 3 
# 	cnt = 0
# 	for j in range(len(result)):
# 		# 금메달 순위 상대방이 더 크다면
# 		if result[i][1][0] < result[j][1][0]:
# 			cnt += 1
# 		# 금메달 순위가 같다면
# 		elif result[i][1][0] == result[j][1][0]:
# 			# 은메달을 확인하고
# 			if result[i][1][1] < result[j][1][1]:
# 			# 은 메달의 순위도 같다면
# 				cnt += 1
# 			elif result[i][1][1] == result[j][1][1]:
# 				# 동메달의 순위를 본다음에
# 				if result[i][1][2] < result[j][1][2]:
# 					# 동메달의 순위가 상대방이 더 크다면 
# 					cnt += 1
# 				# 금 은 동 다 같은거
# 				elif result[i][1][2] == result[j][1][2]:
# 					cnt+=1
# 	cnt_dic[result[i][0]] += cnt-1
# print(cnt[K]+1 if cnt_dic[K] == 0 else cnt_dic[K])


# 와..도대체 어떻게 이렇게 풀어야 되는거지..
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
s.sort(key=lambda x : (-x[1], -x[2], -x[3]))
for i in range(n):
    if s[i][0] == k:
        index = i
        

for i in range(n):
    if s[index][1:] == s[i][1:]:
        print(i + 1)
        break