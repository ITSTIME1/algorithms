# 3 10 10

# 그럼 일단 한번 나무를 자를때마다 c원이 드는거니까
# 가장 길이가 큰걸로 잡아보고 몇번잘라야하는지보자
# 103 = 1
# 59 = 1
# 그럼 한번 자르니까
# 1원 까이는거야

# 그리디핳게접근하자
# 매순간의선택이최선의선택
# 우선 길이가 줄어드는건 안돼
# 그건 최대한 돈을 벌게 되는 방향에서 멀어지기 떄문이야
# 그럼 길이를 최대한으로 유지하는거.
# 덜 적게 자르는거
# 길이가 길면 그 만큼 가격도 많이주고
# 적게 자른다면 그 만큼 전체금액에서 c원만큼을 덜 주니까
`