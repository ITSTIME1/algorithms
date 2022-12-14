# 순열과조합을 연습해보자



# 순열 = 서로 다른 n 개에서 r개를 택하는 경우의 수
# 조합 = 서로 다른 n 개에서 r개를 택하는 경우의 수

# 둘의 차이점은 순서를 지키냐 안지키냐이다
# 조합 같은경우 순서를 고려하지 않고 무작위로 뽑고 중복을 허용하지 안흔ㄴ다
# 순열도 마찬가지로 중복을 허용하진 않지만
# 순서가 정해져 있다


# 예를 들면 한 숫자를 뽑고 그 다음 숫자를 뽑았을때
# 그 결과가 내가 찾고자 하는 결과의 영향을 미치면 그것은 조합이 아닌 순열이 된다
# 즉 반대로 내가 n개에서 r개를 택했을 때
# 내가 찾고자 하는 결과에 영향을 미치지 않는다면
# 조합이라고 생각할 수 있다.



input_list = [1,2,3,4,5]

# 해당 숫자를 뽑았는지 뽑지 않았는지 체크.
used = [0]*len(input_list)

def perm(arr, n):
    if n == len(input_list):
        return
    for i in range(len(input_list)):
        if not used[i]:
        	# 뽑았으니 1로 변경.
            used[i] = 1
            # 해당 숫자를 리스트에 넣어주고
            arr.append(input_list[i])
            # 재귀를 돌려준다
            # arr = 값을 뽑았다고 알려준 다음
            # 그 해당 값을 리스트에 넣어서 다시 재귀를 돌려준다
            # n = arr의 추가되는 횟수를 넣어준다
            perm(arr, n+1)
            print(used)
            arr.pop()
            used[i] = 0

perm([], 0)



nums = [1, 2, 3, 4, 5]
answer_list = []

def nCr(n, ans, r):
    if n == len(nums):
        if len(ans) == r:
            temp = [i for i in ans]
            answer_list.append(temp)
        return
    ans.append(nums[n])
    nCr(n + 1, ans, r)
    ans.pop()
    nCr(n + 1, ans, r)

nCr(0, [], 3)
print(answer_list)