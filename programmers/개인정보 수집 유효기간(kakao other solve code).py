def solution(today, terms, privacies):
    answer = []
    terms_dic = {term.split(' ')[0] : int(term.split(' ')[1])*28 for term in terms}
    
    # 오늘날짜를 구분한거
    t_y, t_m, t_d = today.split('.')
    # 오늘날짜를 계산하네
    today = int(t_y)*12*28 + int(t_m)*28 + int(t_d)
    print(today)
    today2 = int(t_y)*365 + int(t_m)*28 + int(t_d)
    print(today2)
    for idx, p in enumerate(privacies):
        year,month,day = p.split('.')
        day,term = day.split(' ')
        check_day = int(year)*12*28 + int(month)*28 + int(day)

        if check_day+terms_dic[term] <= today:
            answer.append(idx+1)
    
    return answer
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]


a = solution(today, terms, privacies)


