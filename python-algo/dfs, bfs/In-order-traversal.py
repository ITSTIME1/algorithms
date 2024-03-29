# insert() 함수 이해만 이틀이 걸렸다.
# in-order(중위순회 이해)

# 먼저 큐 자료형 방식을 사용할건데
# 큐를 사용하는 이유는 가장 앞에 있는것부터 뽑아내야 하기 때문이다.
# 가장 앞의것을 뽑는 이유는 왼쪽 요소부터 즉 먼저 put 하는 게 leftchild 기 때문에
# 가장 먼저 들어와져 있는 값또한 왼쪽 자식값이 먼저 들어와져 있어 그 왼쪽 값을 먼저 뽑기 위해선
# 선입선출 구조인 (fifo) 큐 자료구조가 필요로 되어 진다.


from queue import Queue

# 해당 코드는 educative in-order 순회 방식 코드이다.
# 재귀를 이용한 방식이며 이해하는데 이틀이나 걸렸다..

# 1. Node 클래스를 생성하여 자식 key 값을 담아줄 것이다.
# 2. 가장 왼쪽부터 하나씩 채워가면서 재귀적인 형식으로 담아줄것이다.
# 3. 왼쪽이 채워진다면 오른쪽으로 넘어가야 할 때는 다음 오른쪽 서브트리의 가장 왼쪽의 key가 대입되게 된다.

class Node:
	def __init__(self, val):
		self.leftChild = None
		self.rightChild = None
		self.data = val

	def insert(self, data):
		if data is None:
			return
		if self.leftChild is None:
			self.leftChild = Node(data)
			data = None
		elif self.rightChild is None:
			self.rightChild = None(data)
			data = None
		else:
			queue.put(self.leftChild)
			queue.put(self.rightChild)

		while queue.empty() is False:
			queue.get().insert(data)


	# 재귀의 이해만 가지고 있다면 충분히 보이는 함수.
	def inorderTraversal(self, root):
       ret = []
       if root:
           ret = self.inorderTraversal(root.leftChild)
           ret.append(root.data)
           ret = ret + self.inorderTraversal(root.rightChild)
       return ret
	# 해당 함수 코드를 이해하기 위해서 선행되어야 될 지식은
	# 재귀의 호출방식과 호출되었을때 어떻게 쌓이고 사라지는지의 대한 이미지가 그려져야 한다.
	# 그럼 먼저 설명을해보자면 이건 node를 수동적으로 입히는 코드기 때문에
	# 노드의 삽입 방식과 + 재귀의 순회 방식을 동시에 이해하면서 손으로 그려가며 풀어봐야 이해가 빠르게 된다.

	# 우선 root node를 처음에 설정해준다 이 예시에서는 27의 값이 루트노드가 되었고
	# 이 루트노드에서부터 시작을 하게 되는데
	# insert(14)의 값이 넣어지게 된다
	# 그렇게 된다면 if문의 조건의 이해서 기저조건은 피하게 되고
	# leftChild 값이 아직 None 값이기 때문에
	# 해당 위치에 14가 들어가게 된다.
	# python if elif else 문의 이해가 완벽히 되어 있다면
	# if문의 조건이 틀릴 수 elif 문의 조건이 실행되고 if문 elif 문 둘다 조건이 성립이 되지 않을시 else 문이 실행된다.
	# 그렇기 때문에 왼쪽값이 들어가져 있으므로 if문 조건절을 타게 되는거고
	# 아래 elif, else 문은 타지 않게 된다.
	# 하지만 마지막 else 아래 while문은 돌게 된다.
	# while문의조건은 큐에 값이 없을때 까지 큐에 값이 없다면 false 기 때문이다
	# 그럼 결국 큐의 값은 현재 false 기 때문에 while문을 타지 않고 함수가 종료되게 된다.
	# insert(5) 의 값이 넣어지게 된다.
	# 그렇다면 27이 루트노드이면서 왼쪽값은 14로 채워져 있고 나머지 오른쪽 값만이 남겨져 있게된다.
	# 그럼 그 자리가 바로 5의 자리가 되어진다.
	# 그럼 하나의 이진트리형태가 완성되어져 있는 것이다.

	# insert(10)이 들어오게 된다면 14, 5가 채워져 있기 때문에 != None 아니기 때문에 
	# else 문을 타게 되는데 else 문을 타게 되었기 때문에
	# queue에 14, 5를 추가하는게 아니라 '객체'인 Node(14) 와 Node(5) 값이 들어가게 되는것이다.
	# 처음에 queue.get()하게 되면 가장 앞의 값을 뽑아오게 되는데
	# int 형 타입의 어떻게 insert()함수를 붙였는지 이해가 되지 않았지만
	# 자세히 본다면 Node(14) 값이 들어온다는걸 알 수 있게 된다.
	# 이건 간단하게 알아볼 수 있는데 print(queue.get()) 했을시 정수라면 그 값 자체가 나오게 된다. int형타입인.
	# 하지만 해보면 알겠지만 정수형 타입이 아닌 주소값 형태로 들어오게 된다
	# 때문에 Node(14).insert(10)이라고 생각하면 된다.


	# 그럼 10이 들어오게 되면 14의 왼쪽 노드는 비었기 때문에 10이 그자리를 차지하게 되고
	# 이때 가장중요한건 data = None 으로 만드는 작업이다
	# 이걸 하지 않는다면 큐에 담겨져 있는 다른 객체의 값에도 똑같이 10이 들어가지기 때문에
	# 함수가 종료될 수가 없다.

	# 자 그렇다면 10이 대입됨과 동시에 data = None 으로 바뀌었기 때문에
	# 큐에서 node(5)를 똑같이 뽑아오게 된다면 node(5).insert(none) 의 값이 들어가지기 때문에
	# 재귀의 기저조건에 의해서 node(5).insert(none) = return 아무값도 반환하지 않는 상태라 종료되게 된다.
	# 따라서 큐에는 아무것도 없는 상태로 종료가 되는 것이다.

	# insert(6) 들어오게 된다면 이번에도 마찬가지로 node(14), node(5)가 큐에 넣어지게 되고
	# node(14)에서 오른쪽 값이 비었기 때문에 6을 넣어주고
	# node(5).insert(none) 값을 넣으면서 node(5)를 리턴해준다
	# 그럼 똑같이 값이 아무것도 남지 않게 되며

	# insert(31) 이 들어올때도 마찬가지로 14, 5 순서대로 삽입되면서
	# 이번엔 14가 루트시점이며 그 서브트리가 완성되었기 때문에
	# 31이 들어가질 공간이 없다 때문에
	# 5, 10, 6이 들어가지며
	# node(5).insert(31)이 들어가지게 된다
	# 이렇게 되면 5의 왼쪽 노드값은 존재하지 않기 때문에 5의 왼쪽값이 31이 되면서
	# 나머지 값들또한 while문에 의해서 뽑아지게 되고
	# 그 뽑아진 값들에 data = none 인 값들을 대입시켜준다면
	# 5에서도 큐에 아무것도 없는상태로 종료된다는걸 알 수 있다


	# insert(9) 또한 마찬가지로 14, 5, 10, 6
	# 5<-9가 대입되게 되면서 오른쪽 값이 넘겨지고
	# data = None 이되면서 뒤에 있는 10, 6 은 기저조건에 의해서 종료 되게 된다.


	# 그럼 여기까지 들어온 노드들로만 완전이진트리를 이루고 있다.
	# 좀더 쉽게 설명해보자면 data = None 이라는건 밑단 노드는 없다라는 것이다.
	# 그럼 밑단 노드가 없으면 다시 돌아게 되는것이다.

	# 이런식으로 함수가 완성이된다. 



	# 트리를 처음 공부해보며 느낀점 = 트리는 그리자..
	
