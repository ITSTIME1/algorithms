from itertools import combinations_with_replacement
import sys

N, K = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, input().split()))


len_N = len(list(str(N)))


# 이게 중복 조합으로 안풀리는 이유가 뭐지?
# 같은 숫자를 중복해서 사용할 수 있다는건 똑같은데
# 대신 순서가 바뀌는건 고려하지 않는건데

while True: 
    ar = []
    for i in combinations_with_replacement(arr, repeat=len_N):
        # N보다 작거나 같은 경우들에서만 확인하고
        print(i)
        check = "".join(list(map(str, i)))
        if int(check) <= N:
            ar.append(i)
    # 해당 자릿수에서 없는거니까 ar len 을 줄여보는거지
    if len(ar) == 0:
        len_N -= 1
    else:
        break

print(int("".join(list(map(str, max(ar))))))


# 가장 큰 수를 찾으면 되니까 가장 큰 수부터 고려해보면 되지 않을까?
# 만약 가장 큰 자릿수에서 나오지 않는다면 그 다음 자릿수를 고려해볼 수 있지 않을까?


# 만약 이걸 중복조합으로 풀면?
# 중복순열과 중복조합 둘 중의 하나를 생각할 수 있었을때
# 예제에서는 577 한가지만 주어진 상황에서 수만 두개를 뽑을 수 있다고 했으니
# 내가 알 수 있는 범위는 현재 숫자를 중복해서 뽑을 수 있다는 경우의 수 뿐이다
# 만약 예제에서 중복해서 뽑았을 때 123 이나 132 숫자는 중복해서 뽑았지만
# 순서가 다른걸 고려하지 않았다면
# 즉 예제에 순서가 다른걸 고려하지 않아 그 숫자가 없다면
# 중복조합으로 풀었을 가능성이 있다.
# 100000000 1
# 1
