# # 문제분

# # 스트리밍 문제


# # 일단 입장부터 퇴장까지 모두 확인된 학회원을 찾아야 하는 프로그램인데 

# # 1. 개강총회를 시작하기전 학회원의 입장여부를 확인
# # 학회원 입장여부 확인방법 = 개강총회가 시작하기 전에 대화를 한 적이 있는 회원의 닉네임
# # 개강총회를 시작하자마자 채팅기록을 남긴 학회원도 제 시간에 입장이 확인된 것으로 간주

# # 개강총회 시간 전에 대화 한 닉네임은 모두 출석
# # 개강총회 시간 정각에 있는 닉네임도 모두 출석


# # 2. 개강총회가 끝나고, 스트리밍을 끝낼때까지
# # 스트리밍이 끝날떄 까지 학회원의 닉네임을 보고 체크

# # 개강총회가 끝나자마자 채팅기록을 남긴사람 = 정상퇴장
# # 스트리밍이 끝나자마자 채팅기록을 남긴사람 = 정상퇴장

# # s = 개강총회를 시작한 시간
# # e = 개강총회를 끝낸 시간
# # Q = 스트리밍이 끝난 시간 

# # HH:MM
# # 시간 학회원네임
# # 00:00 ~ 23:59 분까지 단 하루 개강총회가 진행되는 하루동안의
# # 모든 시간의 닉네임이 다 들어있다

# 21:30 malkoring

# s, e, q
# 22:00 23:00 23:30
# 21:30 malkoring (True)
# 21:33 tolelom (True)
# 21:34 minjae705 (True)
# 21:35 hhan14 (True)
# 21:36 dicohy27 (True)
# 21:40 906bc (True)

# 23:00 906bc  (False)
# 23:01 tolelom (False)
# 23:10 minjae705 (False)
# 23:11 hhan14 (False)
# 23:20 dicohy27 (False)


# # 이 로그들 중에서 정상퇴장한 ( 입장 ~ 퇴장 까지 맞는 사람)

# # 출석한 사람들의 대한 dic 만들고 = 개강총회 이전 시간 + 개강총회 정각
# # 모두 입장한 사람들의 대한 로그가 남겨져 있을것이고

# # 그럼이제 정상 퇴장한 사람들의 목록을 비교하면 되기 때문에
# # 두 조건을 만족한다면 dic 의 value 값을 바꾸게 된다면
# # 그 해당 사람은 마지막까지 남겨져 있는 사람이 될 것이기에

# # 그 두 조건은 개강총회 끝난시간 ~ 스트리밍 종료전 + 스트리밍종료시간 정각
# # 값을 변경한다면 value 값은 최종적으로 입장~퇴장까지 모두 정상참작한 사람들이 된다


# # 1. 22시 전에 대화를 한 사람들을 출석시킨다
# [21:30 malkoring (True)
# 21:33 tolelom (True)
# 21:34 minjae705 (True)
# 21:35 hhan14 (True)
# 21:36 dicohy27 (True)]

# # 2. 개강총회를 끝낸 시각 + 끝날떄까지 채팅기록이 남긴 사람
# [21:30 malkoring (True)
# 21:33 tolelom (True)
# 21:34 minjae705 (True)
# 21:35 hhan14 (True)
# 21:36 dicohy27 (True)]
# # 총 5명의 사람들이 정상출석한 사람들이라고 볼 수 있다

# s, e, q
# 06:00 12:00 18:00



# 18:21 jinius36 (False)
# 18:40 jeongyun1206 (False)

# # 1. 개강총회전 + 개강총회 정각 = 정상출석한 사람들
# []

# # 2. 개강총회가 끝난정각시간 + 스티리밍 까지의 시간
# # 퇴장을 고려할때 더 큰 시간이 있으면
# # 더 큰 시간을 우선순위로 본다

# # 스트리밍 시간 전에 이미 정상출석이 되어있다면 그 이후 시간을
# # 넘어가도 영향을 주지 않는다

# [06:00 kimchist (True)
# 17:59 swoon (False)
# 18:00 kheee512 (False)]

# # 문제 이해 완료
# # 해쉬테이블을 이용하면 쉽게 풀리거 같은 느낌인데
# # 시간은 분으로 바꾸고 분 + 분 으로 보면 될거 같은데
import sys
start, end, qtream = sys.stdin.readline().split()

st_time = (int(start[:2]) * 60) + int(start[3:])
et_time = (int(end[:2]) * 60) + int(end[3:])
qt_time = (int(qtream[:2]) * 60) + int(qtream[3:])

# print("입력시간 : " + str(st_time) + ", " + str(et_time) + ", " + str(qt_time))


start_dic = {}
end_dic = {}
while True:
	try:
		input_time, name = input().split()
		check_time = (int(input_time[:2]) * 60) + int(input_time[3:])
		if check_time <= st_time:
			start_dic[name] = check_time
		elif et_time <= check_time <= qt_time:
			end_dic[name] = check_time
	except:
		break


cnt = 0
for i in start_dic.items():
	if i[0] in end_dic:
		cnt += 1
print(cnt)