from itertools import product
def solution(users, emoticons):
    answer = []
        
    # 할인율
    sales_list = [10, 20, 30, 40]
    
    # 할인율에 대해서 이모티콘의 개수만큼 할인율들을 뽑아보자
    for i in product(sales_list, repeat=len(emoticons)):
        sales = i
        # 이러한 조건에 대해서 users를 데려오고
        total_money = 0
        emoticon_plus = 0
        for user in users:
            # 기준율, 기준 money
            stand_sales, stand_money = user[0], user[1]
            # 먼저 기준율 이상의 할인율을 보여주는 것이 있는지 확인
            # 만약 기쥰율 이상의 할인율이 없다면 즉 기준율보다 다 아래라면 이모티콘을 살 수 없으므로
            # 종료한다.
            user_money = 0
            for j in range(len(sales)):
                # 기준율 이상이라면
                if stand_sales <= sales[j]:
                    # 7000 * 40%
                    # 이게 할인율 돈이지
                    user_money += emoticons[j] * ((100 - sales[j]) / 100)
            # 총 금액이 stand_money보다 크다면        
            if user_money >= stand_money:
                emoticon_plus += 1
            else:
                # 기준 돈보다 작다면 이모티콘 플러스에 가입을 하지 않으므로
                # 총 금액에다가 더해준다.
                total_money += user_money
                continue
            
        answer.append((emoticon_plus, total_money))
    answer_list = sorted(answer, key=lambda x : (-x[0], -x[1]))
    return list(map(int, answer_list[0]))
    