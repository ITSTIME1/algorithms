n = int(input())

num = [input() for _ in range(n)]


for i in range(1, len(num[0])+1):
	
	arr = set()
	for j in num:
		arr.add(j[-i:])

	if len(arr) == n:
		print(i)
		break


# 맞았따...
# 음 아까는 왜 안된건지 아직도 모르겠지만
 
# set() 자료형의 특징은 중복을 제거한다는 것이다.

# 즉 한번들어간 값이 저장되어 있다고 가정했을때 다른 똑같은 답이 set()자료형에 추가가 되어지려고 한다면
# 중복문자가 들어가지는 것이기 때문에
# 하나로 취급하여 결국에 arr에 == n 처럼 다 남겨져 있다는 뜻은 중복의 걸리지 않고 전부다 다른 숫자라는 뜻이된다.
# 때문에 arr의 구분할 수 있는 각기 다른 숫자의 개수가 모든 학생들에게도 적용이 된다면
# 그게 최소의 k가 된다.