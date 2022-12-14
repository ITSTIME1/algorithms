# 1번 연산은 배열을 상하 반전 시킨다.
# 2번 연산은 배열을 좌우 반전 시킨다.
# 3번 연산은 90도 회전시키는 것이고
# 4번 연산은 왼쪽으로 90도 회전시키는 것이고

# 5번 연산은 N/2 * M/2 나눈 배열을 이동시키는 문제
# 6 8 = 3 * 4 = 12 3 * 4의 하나의 배열이
# 1/4 을 차지하게 되고
# 그 배열을 1번 돌리면서 이동하게 되면
# 1->2->3->4-1 로 돌아가게 된다.

# 6번연산은 오른쪽이 아닌 왼쪽으로 돌린다.



# 첫번째 방법 for dp 를 활용한 방법
N, M, R = map(int, input().split())

# dp = [[0 for _ in range(M)] for _ in range(N)]
arr = [input().split() for _ in range(N)]
# # N = 6 이라면
# # 0~5
# for i in range(N):
# 	for j in range(M):
# 		# 6 - 0 - 1 = 5
# 		# 6 - 1 - 1 = 4
# 		# 6 - 2 - 1 = 3
# 		# 6 - 3 - 1 = 2
# 		# 6 - 4 - 1 = 1
# 		# 6 - 5 - 1 = 0 
# 		dp[i][j] = arr[N-i-1][j]
# 		print(dp)

# for j in dp:
# 	print(*j, end = "\n")


# 리스트 컴프리헨션을 사용해서 배열을 재배열 시키는 방법
# def op1(a):
#     n = len(a)
#     a = [a[i][:] for i in range(n-1, -1, -1)]
#     return a

# print(op1(arr))



# 두번째 방법 
for i in range(N):
	tmp = []
	for j in range(M-1, -1, -1):
		tmp.append(arr[i][j])
# 아래의 방법도 마찬가지 입니다.
# for j in range(m):
#     tmp.append(a[i][m-j-1])
	print(tmp)
	arr[i] = tmp


def op3(a):
    n = len(a)
    m = len(a[0])
    ans = []
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append((a[n-j-1][i]))
        ans.append(tmp)
    return ans

def op4(a):
    n = len(a)
    m = len(a[0])
    ans = []
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append((a[j][m-i-1]))
        ans.append(tmp)
    return ans


 # 3번 연산 같은경우
 # 0~ N 까지 줄마다 가장 뒤에서부터 읽으면서
 # d[i][j] 에다가 넣는 방식
def op6(a):
    n=len(a)
    m=len(a[0])
    block_n=n//2
    block_m=m//2
    ans=[[0]*m for _ in range(n)]
    for i in range(block_n):
      for  j in range(block_m):
        # 각 덩어리 블록의 왼쪽 위 모서리 좌표가 기준점 입니다.
        # 1번 덩어리 블록
        ans[i][j]=a[block_n+i][j]
        # 2번 덩어리 블록
        ans[i][block_m+j]=a[i][j]
        # 3번 덩어리 블록
        ans[block_n+i][block_m+j]=a[i][block_m+j]
        # 4번 덩어리 블록
        ans[block_n+i][j]=a[block_n+i][block_m+j]
    return ans




def op6(a):
    n=len(a)
    m=len(a[0])
    block_n=n//2
    block_m=m//2
    ans=[[0]*m for _ in range(n)]
    for i in range(block_n):
      for  j in range(block_m):
        # 각 덩어리 블록의 왼쪽 위 모서리 좌표가 기준점 입니다.
        # 1번 덩어리 블록
        ans[i][j]=a[i][block_m+j]
        # 2번 덩어리 블록
        ans[i][block_m+j]=a[block_n+i][block_m+j]
        # 3번 덩어리 블록
        ans[block_n+i][block_m+j]=a[block_n+i][j]
        # 4번 덩어리 블록
        ans[block_n+i][j]=a[i][j]
    return ans