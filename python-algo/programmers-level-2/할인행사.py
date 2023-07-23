def solution(want, number, discount):
    # error = False
    # for i in range(len(want)):
    #     # 같거나 큰 것 까지는 괜찮은데 적으면 discount에 그만큼의 수량이 없는거니까 어떻게 탐색해봐도 못구하지
    #     if discount.count(want[i]) < number[i]:
    #         error = True
    #         break

    # 탐색이 가능하다면 모든 개수들이 있는거니까 탐색이 가능하고
    
    total = 0
    for i in range((len(discount) - 10)+1):
        a = discount[i:i+10]
        cnt = 0
        for j in range(len(want)):
            if a.count(want[j]) == number[j]:
                cnt += 1
                    
        if cnt == len(want):
            total += 1

    if not total:
        return 0
    else:
        return total

    
# 테스트 1 〉	통과 (22.43ms, 10.5MB)
# 테스트 2 〉	통과 (215.23ms, 14.7MB)
# 테스트 3 〉	통과 (22.17ms, 11.1MB)
# 테스트 4 〉	통과 (57.22ms, 15.4MB)
# 테스트 5 〉	통과 (69.64ms, 12.8MB)
# 테스트 6 〉	통과 (14.08ms, 10.4MB)
# 테스트 7 〉	통과 (55.55ms, 11.2MB)
# 테스트 8 〉	통과 (106.05ms, 17.2MB)
# 테스트 9 〉	통과 (18.74ms, 11MB)
# 테스트 10 〉	통과 (66.51ms, 13.7MB)
# 테스트 11 〉	통과 (10.30ms, 10.5MB)
# 테스트 12 〉	통과 (0.00ms, 10.2MB)