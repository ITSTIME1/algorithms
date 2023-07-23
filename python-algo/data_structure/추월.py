# 문제분석

# 추월을 못한다는건


# 대근이가 터널입구
# 대근이가 들어온 순서대로 적어둔 차량번호판

# 영식이가 터널출구
# 차량들이 지나가고 적은 번호판



# 들어간 순서의 인덱스와
# 나간 순서의 인덱스가 다르다

# 그 말인 즉슨
# 만약 해당 인덱스의 위치가 다르다면
# 만약 그 인덱스가 원래 들어간 인덱스보다 < 크다면
# 이건 초월을 한게 아니고 더 느리게간것
# 하지만 나간 순서가 > 들어온 순서 보다 빠르다면
# 이건 추월을 하게 된것이라고 볼 수 잇따

n = int(input())
arr = [input() for i in range(n * 2)]

first = [i for i in arr[:n]]
second = [i for i in arr[n:]]

first_dic = {}
for i in range(len(first)):
	first_dic[first[i]] = i

second_dic = {}
for i in range(len(second)):
	second_dic[second[i]] = i

cnt = 0
for i in second_dic:
	if second_dic[i] < first_dic[i]:
		cnt += 1
print(cnt)
# ZG431SN ZG5080K ST123D ZG206A

# ZG206A(추월) ZG431SN(추월x) ZG5080K(추월x) ST123D(추월x)

# 결국 second 문자열을 하나씩 가지고와서
# 해당 문자열이 first의 어디 인덱스에 해당하는지 구하고
# 그 인덱스가 만약 다르다면

# first에서 해당 문자열이 만약 4 second 에서 문자열이 1이라면
# 4번이상으로 통과해야하는 이 차가 1번째로 통과 했으니 적어도 3개의 차량을 추월한것
# first > second = 추월o 4 > 1
# first < second = 추월x 2 < 4

