arr = [1, 2, 3, 4, 5]
def rotate(arr, n):
    # 1.
    # arr 이 참이 아닌 거짓이라면
    if not arr:
        return arr
        # n 의 연산을 진행하고
        # 나머지 값이 나오니까
        # 만약 나머지 값이 not 이라면?
        # 배열의 길이를 넘은 만큼 배열을 회전 시켜도 같은 값이 나온다
        # 만약 길이가 5인데 10번 돌린다고 하면 처음 5번을 돌릴때 원배열이 나오게 된다
        # 그리고 또 한번더 5번을 돌리게 된다면 또 원배열이 나오게 된다
        # 그럼 5번을 총 2번 돌은거니까 5 * 2 = 10이 된다
        # 그럼 원배열 = 10 이랑 같은 값이 나오기 떄문에
        # 배열의 길이 이상의 값만큼은 돌릴 필요가 없다 

        # 즉 회전수를 배열로 나눠서 나머지가 나온 값 만큼만 돌려준다면 회전 하는 만큼의 값과 같은
        # 결과를 얻을 수 있다는 뜻이 된다.
    n %= len(arr)
    # 값이 없다면
    if not n:
        return arr

    # 2.
    left = arr[:-n]
    right = arr[-n:]  

    # 3.
    # 왼쪽 배열과 오른쪽 배열을 바꿔서 해주면 값이 된다.
    # 회전수를 배열의 길이로 나눈 나머지 만큼 슬라이싱을 사용해서
    # L,R을 나눠주게 되면
    # 그 상태로 이제 구해준 값을 반대로 더해주기만 하면 해당 횟수만큼 1차원 배열을 회전한 것과 같다

    return right + left
print(rotate(arr, 10))

# 0 False 로 인식하지


def rotate2(arr, n):
    # 마찬가지로 배열과 회전수의 인자가 참이 아니라면 그대로 반환해준다.
    if not arr:
        return arr
    N = len(arr)
    n %= N
    if not n:
        return arr
    # 새로운 리스트를 만들어주고
    new_arr = [None for _ in range(N)]
    # for문을 돌리면서 원배열의 i 번째 인덱스를
    # i+n 번째 % 배열의 길이 만큼 나눈 나머지의 넣어준다
    # 즉 원배열의 첫번째 값부터 배열의 끝 값은
    # 각각의 인덱스 + 회전수 를배열의 길이로 나눈 나머지의 저장하게 되면
    # 해당 회전한 만큼의 인덱스의 갑싱 들어가지게 된다
    for i in range(N):  
        new_arr[(i+n) % N] = arr[i]
    return new_arr



# 돌리는 함수
def reverse(arr):
    new_arr = []
    n = len(arr)
    for i in range(n):
        new_arr.append(arr[n-1-i])
    return new_arr


def rotate(arr, n):
    if not arr:
        return arr
    N = len(arr)
    n %= N
    if not n:
        return arr

    # 새로운 왼쪽과 오른쪽 배열을 만들어주고
    right, left = [], []

    # 2. left와 right 값의 각각의 값을 넣어주고
    # 만약 배열이 [1, 2, 3, 4, 5]
    # 배열의 길이-회전수 = 곧 left 의 길이가 나온다
    # 그리고 오른쪽은 배열의길이-회전수 부터 배열의 끝부분까지가 오른쪽 배열이 되기 때문에
    # 해당 반복문을 통해서 left 와 right로 나눠서 배열의 넣어준다.
    for i in range(N-n):
        left.append(arr[i])
    for i in range(N-n, N):
        right.append(arr[i])
    # 그리고 왼쪽과 오른쪽 둘다 한번씩 뒤집은 결과를
    # 합치고 그 결과를 또 한번더 뒤집으면
    # 내가 회전하고자 하는 만큼의 결과가 나오게 된다.
    left_rev = reverse(left)
    right_rev = reverse(right)

    # 3.
    return reverse(left_rev + right_rev)

# 저글링, 분할정복 도 알면 좋다