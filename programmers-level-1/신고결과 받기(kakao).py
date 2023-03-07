# 이문제를 내가 코드르 잘못짰다 ㅎㅎ 그렇게 안해도 되는데 이상했을때 눈치를 챘어야함.

def solution(id_list, report, k):
    stand = k
    answer = []
    # 유저의 아이디 리스트고
    user_profile = {i: [] for i in id_list}
    
    # print(user_profile)    
    reporter_list = {i: set() for i in id_list}
   
    for i in range(len(report)):
        # 신고한 사람 -> 신고당한 사람
        reporter, thief = report[i].split(" ")[0], report[i].split(" ")[1]
        reporter_list[thief].add(reporter)
        user_profile[reporter].append(thief)
        # 기준에 맞는 값을 가진 사람을 걸러야지
    th = [k for k, v in reporter_list.items() if len(v) >= stand]

    for k, v in user_profile.items():
        answer.append(len(list(set(v) & set(th))))
        # 걸른다음에 이제 내가 신고한 사람이 잘 신고되었는지만 알면되는데



    ans = answer[-len(id_list):]
    return ans

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
a = solution(id_list, report, k)
print(a)