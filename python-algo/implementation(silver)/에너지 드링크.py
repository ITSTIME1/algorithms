
# 일단 조건 자체가 까다롭진 않은거 같은데
# 에너지 드링크 중에서 임의의 두개를 골라서
# 하나가 남을떄까지 합치면되는건데
# 그리디인데
# 합쳐진 드링크의 양을 최대로 만든다라는건
# 절반을 나누는 양이 작아야 함을 의미한다.
# 즉 6, 4, 2
# 이렇게 있을때
# 6,4를 골랐다면
# 6 + 4//2 = 8
# 4 + 6//2 = 7

# 그럼 1번이 더 양이 많이진다
# 그 이유는 큰거는 그대로 더해져가면서 작은 것들은 비교적 큰 수보다 절반으로 나누는 수가 작기 떄문에
# 더 많은 양을 채워질 수 있다는걸 의미한다. (큰 것을 선택한 것 보다)

# 그럼 결국
# 드링크의 양이 큰 순서대로 나열하고
# 절반으로 나누게 되는건 버릭 ㅔ되는거니까
# 결국 정렬을 수행했기 때문에
# 드링크의 양은 점점 줄어들게되고
# 두개씩 뽑은것들은 첫번쨰가 크고 두번째가 작다
# 결국 첫번쨰 값에 계속 갱신해주면되고 
#드링크가 하나남을떄까지 계속 진행한다면
# 된다 대신 나눗셈은 / 사용하고
# 더해준다
import sys
input = sys.stdin.readline

n = int(input())

d = list(map(int, input().split()))

d.sort(reverse=True)

while n > 1:
	d[0] += d[1] / 2
	del d[1]
	n -= 1

print(d[0])


