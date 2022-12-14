# append x 그 자체를 원소로 넣고
# extend x 그 요소를 원소를 넣어줍니다
# ex a = ["1", "2"]
# 이런식이면 arr.append(a) 한다면 그 자체[]를 넣어주고
# extend 라면 [] 를 제외한 나머지를 넣어줍니다.

# 문자열이라면 append 문자열 그 자체를 넣어줍니다
# extend 는 문자열을 하나씩 요소로 
a, b = map(int, input().split())

arr = []
for i in range(1, b+1):
	arr += [i] * i
print(sum(arr[a-1:b]))
