# import sys
# input = sys.stdin.readline

# a, b = map(int, input().split())
# n = int(input())
# go = [int(input()) for _ in range(n)]


# # 2 3
# # 1
# # 3


# def one(arr):
# 	# 1. 현재 채널 -> b
# 	# 2. 현재 채널 -> arr -> b
# 	# 두개중 어떤게 더빠른지 판단한다.
# 	root = 0
# 	if a > b:
# 		root = a-b
# 	else:
# 		root = b-a

# 	check = (max(arr[0], b) - min(arr[0], b)) + 1

# 	if check == root:
# 		return root

# 	if check < root:
# 		return check
# 	else:
# 		return root

# def notOne(arr):
# 	distance = []
# 	root = 0

# 	for i in range(len(arr)):
# 		distance.append([arr[i], (max(arr[i], b) - min(arr[i], b))])

# 	# 거리의 대한 정렬 = 횟수가 가장 작은걸 오름차순으로 정렬한다.
# 	sorted_distance = sorted(distance, key = lambda x: x[1])
	
# 	if a > b:
# 		root = a-b
# 	else:
# 		root = b-a

# 	if root < sorted_distance[0][1]:
# 		return root
# 	else:
# 		return [sorted_distance[0]]


# # 64 120
# # 1
# # 567

# # 64 566
# # 1
# # 567


# ans = 0
# if n == 1:
# 	ans = one(go)
# else:
# 	# 거리에 1이 반환되고
# 	dis = notOne(go)

# 	distance = dis[0][1]
# 	maxVal = max(b, dis[0][0])
# 	minVal = min(b, dis[0][0])
# 	ans = (maxVal - minVal) + distance
# print(ans)



import sys
input = sys.stdin.readline


a, b = map(int, input().split())
n = int(input())
zu = [int(input()) for _ in range(n)]

def one(arr):
	root_a, root_b = 0, 0

	if a < b and arr[0] > b:
		root_a = b-a
		root_b = (arr[0]-b)+1
		
	elif a < b and arr[0] < b:
		root_a = b-a
		root_b = (b-arr[0])+1

	elif a > b and arr[0] < b:
		root_a = a-b
		root_b = (b-arr[0])+1

	elif a > b and arr[0] > b:
		root_a = a-b
		root_b = (arr[0]-b)+1

	# root_a 가 현재루트에서 b까지
	# root_b 가 즐겨찾기 들렸다가 b까지
	if root_a < root_b:
		return root_a
	else:
		return root_b



	
def notOne(arr):
	min_root, root_a = [], 0 
	
	# 현재 루트에서 가는게 더 빠를 수도 있기 때문에
	if a > b:
		root_a = a - b
	else:
		root_a = b - a

	for i in range(len(arr)):
		maxVal = max(arr[i], b)
		minVal = min(arr[i], b)

		ans = maxVal - minVal
		min_root.append(ans)

	ar = min(min_root)
	if ar+1 < root_a:
		return ar+1
	else:
		return root_a

if n == 1:
	# 가고자하는 주파수가 즐겨찾기에 등록되어 있다면 바로 이동 1 == 이동횟수
	if b in zu:
		print(1)
	else:
		ans = one(zu)
		print(ans)
else:
	ans = notOne(zu)
	print(ans)