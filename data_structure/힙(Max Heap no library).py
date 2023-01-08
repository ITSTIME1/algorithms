# 문제분석 

# priority queue = 우선 순위 큐
# 힙 자료구조를 이용해서 푸는 문제이다
# 완전 이진 트리를 기반으로 한 데이터 자료구조 이다
# 힙은 트리 기반의 데이터 자료 구조이고
# 힙에는 최대힙과 최소힙을 구하는 방법이 있고

# 힙은 우선순위 큐라고도 불리는데 종종 힙이라고 지칭된다

# 보통 우선순위 큐를 구한다고 한다.
# 거기에서 최대값을 구할지 최소값을 구할지가 다르다

import sys

# MaxHeap Implementation
# 1. heap insert
def insert(heap, num):
	# heap list 에 마지막 값을 넣어주고
	heap.append(num)
	# 마지막 값의 index 값을 변수에 담아주고
	# 첫번째 들어오는 값은 0, 1만 들어있기 때문에
	# len(heap) == 2 - 1 = 1 이기 때문에
	# while문을 돌지 않는다
	i = len(heap)-1
	while i > 1:
		# 마지막 인덱스 값이 더 크다면 부모노드를 찾아 올라갔을때
		if heap[i] > heap[i//2]:
			# 부모노드 가 더 작은 값이라면 바꿔주고
			# 계속 찾아 올라갈 i의 값은 인덱스의 값이기 때문에 계속 올라간다
			heap[i], heap[i//2] = heap[i//2], heap[i]
			i //= 2
		else:
			# 만약 부모 노드가 더 크다면 swap 하는걸 멈추고
			break
	

# 2. heap delete
# step by step
# 1). Replace root node with last-value
# 2). After change root node and last-value, Delete previous root node.
# 3). need to know left child and right child and then what is the larger than root node. 
# 4). if left child larger than root node, have to change position(index) each other.
# 5). if right child larger than root node, have to change position(index) each other.

def delete(heap):
	# root node
	# [0, 3, 2, 1]
	maxVal = heap[1]
	tmp = heap.pop()

	parent = 1
	child = 2

	while child <= len(heap)-1:
		
		if child < len(heap)-1 and heap[child] < heap[child+1]:
			child += 1
		# [0, 3, 1, 1]
		# maxVal = 3
		# tmp = 1
		# [0, 3, 1]
		# 1 <= 1
		# 교환할 필요가 없기 때문에
		if heap[child] <= tmp:
			break

		heap[parent] = heap[child]
		parent = child
		child *= 2
	# 부모 노드랑 바꾸는 거
	# [0, 3, 1]
	if len(heap) != 1:
		heap[parent] = tmp
	return maxVal

# x 가 자연수라면
# 추가하는 연산
# 0 이라는 값을 준다면 출력
# 음의 정수는 나오지 않는다
n = int(sys.stdin.readline().strip())
heap = [0]
for _ in range(n):
	x = int(sys.stdin.readline().strip())
	if x != 0:
		insert(heap, x)
	else:
		# 왜 0 이 아니고 1이지 == index 를 1로 맞추기 위해서 0이 들어가 있기 때문에
		# 사실 의미 없는 값을 넣어둔 것이나 마찬가지 그렇기 때문에
		# 그 값만은 끝까지 남아있기에 0을 출력한다
		# 만약 1을 맞추지 않고 인덱스 대로 했다라고 한다면 len(heap) == 0으로 체크했어야 했다.
		
		if len(heap) == 1: 
			print(0)
		else:
			print(delete(heap))

# maxHeap 알고리즘의 설명

heap = [0]
13
0 = 0 이 들어오면 출력 근데 리스트에 인덱스를 맞춰놓고자 하는 값 0을 제외하고 부모노드의 원소가 존재하지 않으므로
"0"을 출력한다.
1 = 0 이 아닌 자연수는 push 를 진행하고 heap[0, 1] 상태가 된다. 만약 지금과 같은 상태라면 1이 추가 되었을 때 heapy 를 할 정도의 원소가 존재하지 않으므로 해당 루트는 추가만 되어진다
2 = 2는 insert 를 해야 하기 때문에 우선 적으로 [0, 1, 2] 와 같은 상태가 된다
부모노드와 비교해서 자식노드가 > 부모노드 보다 더 크다면 바꾸어준다(swap).
그렇게 i 바꾸고자 하는 index 값을 부모노드의 index로 위치시키면서 > 1보다 클때까지만 동작하도록 한다 만약 i == 1 이라면
현재 root node에 와있는 것이다 [0, 2, 1] 상태가 된다
0 = 출력을 요구 하기 때문에 maxVal = 2 tmp = 1 상태로 두고 heap [0, 2] 상태가 된다
때문에 while문을 돌지 못하고 마지막 len(heap) != 1 인 조건에 만족하므로 마지막에 꺼냈던 tmp 값을 index= 1 값으로 변경해줌으로써
heap [0, 1] 상태가 됨과 동시에 return 값으로 2 를 내보내게 된다


0 = 출력을 요구 하기 때문에 maxVal = 1 tmp = 1 이 된다 heap 의 상태는 [0]
부모노드 또한 없기 때문에 [0]만 남은상태 그렇기 때문에 최대값은 maxVal의 저장되어 있는 상태가 최대값이기 때문에
바로 return 하게 된다.

### 현재까지 출력순서가[0, 2, 1] 순으로 출력되고 있다
3 = insert 를 요구 하게 된다 [0, 3] 이 되고
2 = insert 를 요구 하게 된다 [0, 3, 2] 그럼 여기서 자식 노드와 부모노드같의 크기 비교를 하게 되는데
부모 노드 보다 크지 않으므로 while 문을 break 함과 동시에 "swap이 이루어지지 않으면서" 현 heap 상태를 유지하게 된다 
1 = insert 를 요구 하게 된다 [0, 3, 2, 1] 부모노드보다 큰지 확인해보고 자식 노드가 부모노드보다 크지 않기 때문에
while 문을 종료한다

0 = 출력을 요구하므로 maxVal = 3 tmp = 1 그렇다면 [0, 3, 2] parent 의 이번에 그 다음 큰 값을 넣어주고 [0, 2, 2] tmp 값을 다음 값으로 넘겨준다 [0, 2, 1] return maxVal = 3
0 = maxVal = 2 tmp = 1 heap[0, 2] => hea[0, 1] return maxVal = 2
0 = maxVal = 1 tmp = 1 return maxVal 1
0 = 0
0 = 0 
