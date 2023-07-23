import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n = int(input())

	
heap = []
# O(N^2)
# 그냥 n^2이랑 다른점은
# 모든 숫자를heap 에 다 넣는게 아니고
# n개의 숫자만 필요하기 때문에 n*n개의 크기는 필요치 않다.
# 처음 메모리 초과가 났던 아이디어의 상위코드인거 같다.
# 왜냐하면 처음에 리스트의 크기가 n인 것으로 고정해놓고
# 가장 큰 값이 유지되도록 만든다음 그럼 n의 값이 넘어갈때 자동적으로 가장 작은 값을 빼게된다면
# 마지막에 남는 가장 작은 값이 n번째 큰 수 가 되기 때문이다.
# 하지만 빈번히...n^3되고...메모리 초과의 시간초과까지..


# 해서 해당방법을 찾아봤는데 저번에 구현해봤던 최소힙, 최대힙의 성질을 이용하는것이다.

# 최소힙은 루트노드가 가장 작은 값을 유지하는 이진트리의 구성인데.
# 항상 부모노드가 루트노드이며 루트노드는 항상 작은 값을 가지기 위해 어떠한 값이 들어왔을때 그게 가장 작은 값이라면 push를 하게 된다음
# minheap을 유지한다 즉 가장 작은 값이 가장 앞에 있게끔 유지한다는 뜻이되고.
# 그럼 가장 작은 값을뽑을때 본다면 heappop을 하게 된다면 heap에서 가장 작은 값이 뽑히게 되면서
# 그 다음 가장 작은 값을 유지하게 된다.

# heapush의 함수는 O(logn)의 시간복잡도를 가지고있으며
# 가장 작은 인덱스 k가 2k+1 에 위치한 자식 노드보다 작게된다면 최소힙의 성질을 만족함.
# 반대로한다면 최대힙이 만족되는 것이고

# 따라서 위 아이디어의 상위버전이라는 뜻은 값을 넣었을때 항상 작은 값을 유지해줌으로써
# heappush 시 최소힙의 성질을 만족한다고 볼 수 있다.

# 그리고 이렇게만 한다면 메모리 초과가 나기 때문에
# 앞서 리스트의 크기를 n으로 고정한다는 아이디어에서
# 만약 리스트의 크기가 넘어가게 된다면 가장작은 값을 빼면 되므로 heappop하게 된다면
# heap자료구조에서 가장 작은 값을 빼게 되고 다음 작은값이 index = 0 인 부모노드에 위치하게 된다.

# 때문에 아래와 같은 코드가 리스트의 크기는 유지하면서
# 작은 값은 배출되고, 모든 값들의 대한 비교를 진행할 수 있으므로 결과적으로 O(N^2)의 성능을 보이지만 메모리의 측면에서는 해당 문제가 요구하는 메모리를 넘어서진 않게된다.

for i in range(n):
	num = list(map(int, input().split()))

	for j in num:
		if len(heap) < n:
			heapq.heappush(heap, j)
		else:
			if heap[0] < j:
				heapq.heappop(heap)
				heapq.heappush(heap, j)

print(heap[0])
