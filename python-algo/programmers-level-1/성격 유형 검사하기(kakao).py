def solution(survey, choices):
    answer = ''
    # 음 일단 그럼 최종적인 지표를 하나 만들어두고
    total = {1: {"R": 0, "T": 0},
        2: {"C": 0, "F": 0},
        3: {"J": 0, "M": 0},
        4: {"A": 0, "N": 0}}
    
    # 매우비동의 ~ 매우 동의 까지.
    score = {1: 3,
            2: 2,
            3: 1,
            4: 0,
            5: 1,
            6: 2,
            7: 3}
    
    disagree = [1, 2, 3]
    agree = [5, 6, 7]
    
    # "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"
    w = {"RT": 1, 
         "TR": 1,
         "FC": 2,
         "CF": 2,
         "MJ": 3,
         "JM": 3,
         "AN": 4,
         "NA": 4
        }   
    
    for i in range(len(survey)):
        # AN, 5
        # value 를 이용해서 key를 찾아야되나
        word = survey[i]
        s = choices[i]
        
        find = w[word]
        if s in agree:
            total[find][word[1]] += score[s]
            continue
        elif s in disagree:
            total[find][word[0]] += score[s]
            continue
        else:
            # 4 번일때
            continue
    # 그럼 이제 합산을 해야되는데
    answer = ""
    for k, v in total.items():
        c = v
        ans = []
        for j in c:
            ans.append((j, total[k][j]))
        ans_list = sorted(ans, key = lambda x: -x[1])
        answer += ans_list[0][0]
    
    return answer